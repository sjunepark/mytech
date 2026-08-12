---
status: accepted
---

# PDF Ingestion for LLM Agents

**Initial evidence:**
[PDF-to-Agent Parsing Landscape](../reference/pdf-to-agent-parsing-landscape.md),
[Korean OCR Options for Agent Ingestion](../reference/korean-ocr-options-for-agent-ingestion.md)

## Decision

Use [Xberg](https://github.com/xberg-io/xberg) as the default local PDF
normalizer for LLM and agent ingestion. Its Rust-native extraction, direct
Markdown output, selective OCR, and relatively low operational weight fit the
ordinary goal of keeping an agent-readable copy beside the source PDF.

For the ordinary case, retain only the original PDF and a clean normalized
Markdown file with the same basename:

```text
report.pdf
report.md
```

The PDF remains the visual authority. The Markdown is the agent-friendly
reading and search copy. Prefer this simple pair unless a concrete product
requirement needs more structure.

Use Xberg's native PDF path first. Enable its layout-informed Markdown with an
automatic page-selection strategy when a corpus contains multicolumn pages,
tables, forms, or other structure that the fast path may miss.

Keep [Docling](https://github.com/docling-project/docling) as the independent,
quality-first local fallback. Its layout and table models are more central to
its standard PDF pipeline, its ecosystem is substantially larger, and its rich
document model is useful while diagnosing conversion failures. Those benefits
come with a heavier Python and model stack and do not require retaining its
JSON output.

## Retaining the source PDF

Normalize headings, paragraphs, lists, code, links, and ordinary tables into
one readable Markdown document. Avoid exposing parser-internal objects,
per-token geometry, or duplicated representations to agents by default; they
increase storage and retrieval noise without improving ordinary content
questions.

Record only enough provenance to reproduce or audit the conversion. Small
Markdown frontmatter is normally sufficient:

```yaml
---
source: report.pdf
source_sha256: <digest>
generated_by: <parser and pinned version>
---
```

The exact fields are project choices. Keep the source path, source hash,
conversion version, and material warnings somewhere durable. Embeddings and
vector-store records remain disposable indexes derived from the Markdown.

Page-break comments such as `<!-- source-page: 12 -->` are a cheap optional aid
when page citations are common. Do not retain bounding boxes merely because a
parser can produce them. If an agent needs stronger verification, it can search
or open the paired PDF.

This authority split follows
[Canonical Sources and Derived Artifacts](../architecture/canonical-sources-and-derived-artifacts.md):
the PDF owns source evidence, while Markdown, chunks, and embeddings are
rebuildable projections.

## Escalating to exact structure

Retain structured JSON, stable element identifiers, bounding boxes, extracted
assets, or evidence crops only when a concrete feature depends on them. Typical
examples are legal or audit evidence, exact quotation workflows, table-cell
lineage, document viewers that highlight a cited region, and automated
cross-checking that must locate an extraction on the page.

Exact geometry is not a general retrieval requirement. Adding it later may
require re-parsing retained PDFs, which is usually a better trade than making
every document package and agent context permanently complex.

## Text-only ingestion

When the original PDF has no continuing evidentiary, legal, or product value,
retain the complete normalized Markdown plus minimal provenance. Markdown may
become the canonical ingested content only after conversion has been validated.
Store the complete document outside the vector index so it can be re-chunked
and re-embedded without re-parsing.

Prefer Markdown over plain text because headings, lists, code blocks, links,
and ordinary tables improve navigation and chunking. Use embedded HTML only
where a complex table would otherwise lose important merged-cell semantics.
Describe important figures and charts before deleting the PDF; otherwise their
information is intentionally discarded.

Before deleting the source, verify that every page produced plausible content,
OCR ran where needed, representative reading order and tables survived, and
the result has no suspicious repetition, omissions, invented text, or abrupt
density changes. For valuable material, retain the PDF through a review window
or compare another parser. Deleting the only source makes silent conversion
errors permanent.

## Korean OCR

Do not OCR a born-digital PDF whose embedded Korean text extracts correctly.
For scanned pages, use specialized OCR or document parsing as the transcription
authority and reserve a general multimodal model for difficult pages or
semantic repair.

The preferred local Korean OCR baseline is Xberg's native PaddleOCR integration
with Korean selected explicitly. Its current model routing uses the
script-specific Korean recognizer where needed. Test Xberg's PaddleOCR-VL path
when handwriting, dense forms, tables, charts, or damaged scans defeat the
ordinary pipeline. These paths can still emit only the final Markdown; their
richer intermediate output does not need to be retained.

When hosted processing is acceptable, test Upstage Document Parse first for
Korean-first, agent-ready Markdown. Test NAVER CLOVA OCR when Korean raw
transcription and in-memory API processing matter more than direct Markdown,
and add a deterministic Markdown normalization step. Mistral OCR and Azure
Document Intelligence are strong international alternatives.

A general vision model such as a current OpenAI multimodal model can improve
reading order, repair awkward tables, describe figures, and produce cleaner
Markdown. It can also omit text, normalize wording, or invent characters and
numbers. That risk remains important even when exact coordinates do not. Use
such models on low-confidence or visually complex pages, or as a verifier,
rather than rewriting every Korean page by default.

No current neutral benchmark establishes a universal Korean OCR winner. Choose
the production fallback with a representative corpus test that measures Hangul
character errors, omissions and insertions, numbers and dates, reading order,
table fidelity, Markdown cleanliness, latency, cost, and privacy.

## Parser roles

| Need | Preferred parser | Reason |
| --- | --- | --- |
| One general local default | Xberg | Fast Rust-native extraction, direct Markdown, selective OCR, broad formats, and low operational weight |
| Korean scan default | Xberg with PaddleOCR | Native local Korean and English recognition without a separate Python OCR runtime |
| Complex Korean pages locally | Xberg with PaddleOCR-VL | Korean-aware document VLM for layout, tables, charts, formulas, and handwriting |
| Independent quality fallback | Docling | More established layout- and table-centered PDF pipeline with a larger ecosystem |
| Korean hosted Markdown | Upstage Document Parse | Korean-first document parsing with direct HTML or Markdown output |
| Korean hosted raw OCR | NAVER CLOVA OCR | Explicit Korean print and handwriting support with confidence and table data |
| General hosted fallback | Mistral OCR | Purpose-built multilingual page Markdown at low published per-page cost |
| Scholarly citation metadata | GROBID | Purpose-built authorship, affiliation, bibliography, and citation structure |
| Scan cleanup and archival PDF | OCRmyPDF | Deskew, rotation, OCR layer, and PDF/A workflow; not a Markdown parser |

Do not choose MarkItDown as the primary PDF parser merely because it has the
largest GitHub audience. Its built-in PDF path lacks OCR and is not a full
layout-understanding pipeline.

Do not make Marker, MinerU, or PyMuPDF4LLM an unconditional organization-wide
default without accepting their model or code licensing constraints. Their
technical capability does not erase the deployment terms.

## Validation and operation

Probe pages before escalating them. Use Xberg's native text extraction for
ordinary born-digital pages, enable its layout-informed Markdown selectively,
use specialized OCR for scanned pages, and reserve expensive vision processing
for difficult pages when recombination can preserve reading order.

Do not silently convert parser failures into empty text. At minimum distinguish
a successful extraction, an empty source page, a page requiring OCR, a partial
result, and a parser failure.

Qualify cloud fallbacks under
[External Provider Qualification](../practices/external-provider-qualification.md).
Sensitive documents require an explicit retention, training-use, region, and
zero-data-retention decision.

## Revisit when

Switch the default to Docling when representative corpus tests show recurring
Xberg omissions or reading-order, heading, table, or formula errors that
Docling materially fixes, especially when doing so is simpler than maintaining
extensive Xberg layout configuration or fallbacks.

Otherwise re-evaluate when another parser materially improves content
accuracy, retrieval answers, Korean OCR, throughput, or operating simplicity.
Revisit immediately when a selected project's code or model license changes,
or when PDF plus Markdown no longer supports the product's citation and
reprocessing needs.
