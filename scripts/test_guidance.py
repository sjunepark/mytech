"""Exercise guidance discovery through its public process contract."""

from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


class GuidanceQueryTests(unittest.TestCase):
    def setUp(self) -> None:
        self.fixture = tempfile.TemporaryDirectory()
        self.addCleanup(self.fixture.cleanup)
        self.root = Path(self.fixture.name)
        scripts = self.root / "scripts"
        scripts.mkdir()
        for name in ("guidance_contract.py", "query-unsettled-guidance", "validate-guidance"):
            shutil.copyfile(Path(__file__).parent / name, scripts / name)

    def document(self, path: str, status: str) -> None:
        destination = self.root / path
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(
            f"---\nstatus: {status}\n---\n\n# Example\n\n"
            "## Decision\n\nAn accepted choice.\n\n## Revisit when\n\nNeeds change.\n",
            encoding="utf-8",
        )

    def run_script(self, name: str, *arguments: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(self.root / "scripts" / name), *arguments],
            capture_output=True,
            text=True,
            check=False,
        )

    def test_discovery_reports_drafts_and_omits_settled_documents(self) -> None:
        self.document("architecture/accepted.md", "accepted")
        self.document("draft/proposal.md", "draft")
        result = self.run_script("query-unsettled-guidance")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stderr, "")
        self.assertTrue(result.stdout.endswith("\n"))
        payload = json.loads(result.stdout)
        self.assertTrue(payload["ok"])
        self.assertEqual([item["path"] for item in payload["documents"]], ["draft/proposal.md"])
        self.assertEqual(payload["documents"][0]["issues"], [])

    def test_misplaced_accepted_document_is_visible_and_rejected(self) -> None:
        self.document("draft/misplaced.md", "accepted")
        query = self.run_script("query-unsettled-guidance")
        self.assertEqual(query.returncode, 0, query.stderr)
        documents = json.loads(query.stdout)["documents"]
        self.assertEqual(len(documents), 1)
        self.assertEqual(documents[0]["path"], "draft/misplaced.md")
        self.assertIn("invalid at this path", documents[0]["issues"][0])
        validation = self.run_script("validate-guidance")
        self.assertEqual(validation.returncode, 1)
        self.assertIn(documents[0]["issues"][0], validation.stderr)

    def test_unknown_status_remains_visible(self) -> None:
        self.document("architecture/unknown.md", "pending")
        result = self.run_script("query-unsettled-guidance")
        self.assertEqual(result.returncode, 0, result.stderr)
        documents = json.loads(result.stdout)["documents"]
        self.assertEqual(documents[0]["status"], "pending")
        self.assertEqual(documents[0]["issues"], ["unknown status 'pending'"])

    def test_invalid_invocation_has_a_structured_failure(self) -> None:
        result = self.run_script("query-unsettled-guidance", "unexpected")
        self.assertEqual(result.returncode, 2)
        payload = json.loads(result.stdout)
        self.assertFalse(payload["ok"])
        self.assertEqual(payload["error"]["category"], "invalid_invocation")


if __name__ == "__main__":
    unittest.main()
