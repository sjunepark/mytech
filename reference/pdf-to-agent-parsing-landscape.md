# PDF-to-Agent Parsing Landscape

A research snapshot from August 2026, edited for scope on 2026-09-05. This is
an evidence map, not a live leaderboard or the authority for parser selection.
Current preferences belong in
[PDF Ingestion for LLM Agents](../stacks/pdf-ingestion-for-llm-agents.md).
Korean-specific evaluation belongs in the
[Korean OCR comparison](korean-ocr-options-for-agent-ingestion.md).

## What the comparison establishes

Extraction, OCR, layout reconstruction, and document understanding are distinct
capabilities. A convenient Markdown output mode does not establish accurate
reading order or tables; recognition quality does not establish a useful
whole-document representation.

The useful comparison is the complete pipeline on the intended corpus:
source fidelity, provenance, retrieval usefulness, operating requirements,
licensing, and reproducibility. Repository popularity helps assess ecosystem
reach, but cannot rank these outcomes.

## Candidate roles

These roles summarize the original investigation. Check the linked source for
the exact release, models, build features, and license before adoption.

| Candidate | Role worth evaluating | Main comparison boundary |
| --- | --- | --- |
| [Xberg](https://github.com/xberg-io/xberg) | Local extraction with Markdown, optional OCR and layout, CLI and language bindings | Qualify the selected build and models; native code alone does not establish a small deployment or accurate output |
| [Docling](https://github.com/docling-project/docling) | Document structure, layout, tables, OCR orchestration, and structured output | Compare fidelity gains against model/runtime requirements; retaining its full document model is optional |
| [OpenDataLoader PDF](https://github.com/opendataloader-project/opendataloader-pdf) | PDF-specific extraction with structured output and optional hybrid processing | Identify delegated backends so a fallback is actually independent |
| [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) | Recognition and document-parsing models | Separate recognition, layout, normalization, and serving requirements |
| [MinerU](https://github.com/opendatalab/MinerU), [Marker](https://github.com/datalab-to/marker), [olmOCR](https://github.com/allenai/olmocr) | Model-centered extraction for visually difficult documents | Check corpus language, accelerator needs, and exact code and weight terms independently |
| [PyMuPDF4LLM](https://github.com/pymupdf/pymupdf4llm) | Local extraction with document structure | Review licensing for the complete installed stack alongside extraction quality |
| [MarkItDown](https://github.com/microsoft/markitdown) | Convenient multi-format normalization | Establish what the selected PDF path does on scans and complex layouts rather than inferring it from Markdown support |
| [Unstructured](https://github.com/Unstructured-IO/unstructured) | Element-oriented ingestion and connectors | Compare as an ingestion framework, not just a PDF parser |
| [LiteParse](https://github.com/run-llama/liteparse), [PDF Inspector](https://github.com/firecrawl/pdf-inspector) | Local extraction and page inspection | Distinguish built-in capability from escalation to another engine or hosted service |

[OCRmyPDF](https://github.com/ocrmypdf/OCRmyPDF) addresses scan cleanup and
searchable PDF workflows. [GROBID](https://github.com/grobidOrg/grobid) addresses
scholarly metadata and citation structure. They solve different parts of the
pipeline and should be compared against those needs.

## Benchmark evidence

- [OmniDocBench](https://github.com/opendatalab/OmniDocBench) provides varied
  document and layout categories. Check dataset terms and model/version coverage.
- [olmOCR](https://github.com/allenai/olmocr) includes a benchmark built around
  observable document properties; its authors also develop a candidate engine.
- [ParseBench](https://github.com/run-llama/ParseBench) evaluates agent-oriented
  document properties, but its project ecosystem also supplies parsing products.
- [OpenDataLoader Bench](https://github.com/opendataloader-project/opendataloader-bench)
  exposes a reproducible comparison; distinguish local and hybrid backends.
- A [Portuguese administrative-document study](https://doi.org/10.3390/app16105069)
  and its [reproduction repository](https://github.com/sousaalexandre/loss-j)
  investigate downstream retrieval and QA. Its language and document scope
  limit generalization to Korean scans or unrelated corpora.

Project-authored benchmarks are useful evidence when inputs, versions, and
scoring are inspectable. They do not establish a universal winner. Compare
like-for-like output requirements and disclose delegated engines, preprocessing,
and model assistance.

The earlier note mentioned a four-document smoke test and telemetry inspections
without retaining fixture identities, commands, or inspected commits. Those
claims cannot support a reproducible recommendation and are not treated as
validation here. No new corpus benchmark was run in the September review.

## Hosted services and deployment

Hosted candidates from the investigation include Mistral OCR, LlamaParse,
LandingAI ADE, Reducto, and Mathpix. Their useful differentiation is output
structure, source grounding, specialist content, and operational integration;
current price and retention must be checked on the actual service path.

Separate the license of code, model weights, optional dependencies, and hosted
services. An open-source SDK says nothing about the remote parser's retention
or training-use terms. Local processing may still download models or contact
registries during setup.

Keep the selected release, configuration, model identities, source corpus, and
comparison method with any new evaluation. Follow
[External Provider Qualification](../practices/external-provider-qualification.md)
for cloud decisions rather than carrying old price or privacy summaries forward.
