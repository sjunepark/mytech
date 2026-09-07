# Xberg PDF Ingestion Usage

Usage for [PDF Ingestion for LLM Agents](../stacks/pdf-ingestion-for-llm-agents.md).
Flags were checked against the
[v1.0.14 CLI source](https://github.com/xberg-io/xberg/blob/v1.0.14/crates/xberg-cli/src/commands/overrides.rs)
on 2026-09-05. This review did not execute Xberg or qualify conversion quality.
Record the installed version and recheck flags when upgrading.

## Install

The [official installation guide](https://docs.xberg.io/getting-started/installation/)
documents this macOS path:

```bash
brew trust xberg-io/tap
brew install xberg-io/tap/xberg
xberg --version
```

Homebrew selects the formula's version, not necessarily the version inspected
here. OCR and layout need the corresponding build features, libraries, and
model files. Models may download on first use; prepare them beforehand for an
offline environment.

## Select extraction options

In Bash, start each conversion with these options. Disabling automatic config
discovery makes this example independent of nearby Xberg configuration files.

```bash
xberg_options=(
  --no-config-discovery
  --content-format markdown
  --page-markers true
)
```

For scanned Korean pages, add:

```bash
xberg_options+=(
  --ocr true
  --ocr-backend paddle-ocr
  --ocr-language ko
  --ocr-scanned-pages
)
```

This requests Korean OCR for pages classified as scans. Do not force OCR over a
correct native text layer. In v1.0.14, Korean routes to its script-specific
recognizer; confirm model routing when upgrading rather than assuming the
newest general model supports the same languages.

If reading order, headings, or tables remain poor, add layout handling to the
options appropriate for the document:

```bash
xberg_options+=(--layout --layout-strategy auto --use-layout-for-markdown)
```

The [CLI reference](https://docs.xberg.io/cli/usage/) describes these modes.
JSON, geometry, and chunks are separate product choices, not required output.

## Convert into a review candidate

Use a unique candidate beside the PDF. A failed or empty extraction must not
truncate a previous `report.md`.

```bash
candidate=$(mktemp ./report.md.XXXXXX) || exit 1
if xberg extract report.pdf "${xberg_options[@]}" > "$candidate" && test -s "$candidate"; then
  printf 'Review candidate: %s\n' "$candidate"
else
  rm -f -- "$candidate"
  unset candidate
  printf 'Conversion failed or produced empty output.\n' >&2
  false
fi
```

Nonempty output is only a preliminary check. Review page coverage, Korean text,
numbers, reading order, and tables against the source PDF. Preserve the source
and material warnings. If the candidate fails that review, choose another mode
or compare Docling before publishing it.

## Publish a new Markdown file

After the successful candidate passes review, this Python 3 command publishes
it without replacing an existing destination, including a symlink or directory.
The hard link requires a supporting local filesystem; the candidate is on the
same filesystem as the destination.

```bash
python3 - "${candidate:?No successful candidate}" ./report.md <<'PYTHON'
import os
import sys

source, destination = sys.argv[1:]
os.link(source, destination, follow_symlinks=False)
os.unlink(source)
PYTHON
```

If `report.md` already exists, publication fails and keeps the candidate and
prior output. Use the adopting project's explicit, recoverable replacement
procedure for an update. This snippet provides no-clobber publication, not a
power-loss durability guarantee. Keep provenance with the final artifact as
specified by the owning ingestion guidance.
