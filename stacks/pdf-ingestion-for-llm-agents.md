---
status: accepted
---

# PDF Ingestion for LLM Agents

## Decision

Prefer [Xberg](https://github.com/xberg-io/xberg) as the initial local converter
for ordinary PDF-to-Markdown ingestion, subject to a representative corpus
check. Keep [Docling](https://github.com/docling-project/docling) as an
independent candidate when reading order, tables, or other document structure
remain unreliable. A parser's implementation language, feature list, or
popularity does not establish extraction quality.

Normally retain a simple pair:

```text
report.pdf
report.md
```

The PDF owns source evidence; Markdown is the reading and search projection.
Chunks and embeddings are rebuildable indexes. Follow
[Canonical Sources and Derived Artifacts](../architecture/canonical-sources-and-derived-artifacts.md).

## Extraction and escalation

Use native extraction when embedded text is correct. Escalate layout handling
when representative pages lose structure, and use specialized OCR for scans or
broken text layers. The initial Korean scan candidate is Xberg's PaddleOCR
integration with Korean selected explicitly; pin and qualify the actual engine
and model versions on the target machine.

Use document vision models or general multimodal models for difficult pages
when they improve measured fidelity. They may omit, normalize, or invent text;
keep source wording, numbers, and unresolved uncertainty visible. A model
should not silently rewrite the authoritative transcript to make it smoother.

Use [Xberg PDF Ingestion Usage](../reference/xberg-pdf-ingestion-usage.md) for
commands. The dated
[parser landscape](../reference/pdf-to-agent-parsing-landscape.md) and
[Korean OCR comparison](../reference/korean-ocr-options-for-agent-ingestion.md)
record candidates and evidence limits, not current quality rankings.

When hosted processing is acceptable, include Upstage Document Parse in a
Korean Markdown evaluation and CLOVA OCR when raw transcription is the need.
Select any cloud fallback through
[External Provider Qualification](../practices/external-provider-qualification.md)
using the actual service path's retention, training-use, region, and cost terms.
A local engine may still require first-run model downloads and native libraries;
pre-provision them when offline operation is required.

## Provenance and quality

Keep the source path or identity, source digest, conversion version, relevant
configuration and model identity, and material warnings somewhere durable.
Markdown frontmatter or a small sidecar is sufficient. Page markers are useful
when citations or debugging need page-level navigation.

Do not treat nonempty output as successful extraction. Check page coverage,
reading order, tables, important figures, and exact numbers and names against
the PDF. Distinguish an empty source page, OCR-required page, partial result,
and parser failure. A lossy or model-assisted conversion needs source-based
quality checks rather than byte-identical regeneration.

Use representative Korean and English material, scans, forms, tables, and
known difficult pages. Judge omissions and insertions, numeric accuracy,
structure, retrieval answers, latency, resource needs, and privacy together.
Retain difficult examples as upgrade regressions. Choose the simplest pipeline
that clears the required quality threshold and escalate failed pages when
recombination preserves whole-document order.

## When more structure is necessary

Retain structured elements, geometry, assets, or evidence crops when a feature
needs precise quotation, table-cell lineage, source highlighting, or automated
cross-checking. Do not retain them merely because a parser emits them. Keeping
the PDF preserves the option to re-parse later.

Markdown may become canonical ingested content only when the PDF has no
continuing evidentiary or product value and conversion has been validated.
Preserve important figures and complex table semantics before removing the
source. Keep the complete document outside the vector index, and follow the
adopting project's source-retention and deletion authority.

## Revisit when

Change the default when corpus regressions show omissions or structural errors
that another parser materially fixes, or when maintaining escalation becomes
more complex than switching. Recheck engine and model licenses, platform
support, model availability, and provider terms for the selected versions.
Revisit the PDF/Markdown pair when a concrete citation or reprocessing contract
requires stronger retained evidence.
