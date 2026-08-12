# PDF-to-Agent Parsing Landscape

This is a descriptive research snapshot, not a technical preference. GitHub
popularity and repository activity were refreshed on 2026-08-12. Capabilities,
licenses, benchmarks, and hosted-service details were inspected during a
multi-agent research pass on 2026-08-05 and rechecked where they affected the
recommendation.

The corresponding preference is
[PDF Ingestion for LLM Agents](../stacks/pdf-ingestion-for-llm-agents.md).
Korean-specific OCR and multimodal-model choices are compared separately in
[Korean OCR Options for Agent Ingestion](korean-ocr-options-for-agent-ingestion.md).

## Research question

The goal was to identify one or two dependable ways to turn PDFs into material
that LLM agents can query, retrieve, quote, and cite. The comparison considered:

- semantic and visual fidelity, including reading order, headings, tables,
  formulas, figures, and OCR;
- output suitability for agents, including Markdown, structured document
  models, chunks, page provenance, and bounding boxes;
- modernness, separating old-but-current infrastructure from abandoned code;
- GitHub adoption and contributor signals;
- current releases and default-branch activity;
- code and model licensing;
- local runtime, accelerator, privacy, and hosted-service requirements; and
- independent versus project-authored evaluation evidence.

Stars are evidence of ecosystem size, not a quality score. They favor visible,
broad, and newer LLM-era projects and understate mature infrastructure and
narrow specialists.

## Primary local candidates

| Project | GitHub snapshot | Activity | License | Main focus | Assessment |
| --- | ---: | --- | --- | --- | --- |
| [Xberg](https://github.com/xberg-io/xberg) | 8,964 stars; created 2025 | Pushed Aug 12, 2026; v1.0.14 on Aug 4 | MIT | Rust-native extraction across more than 100 formats, GFM Markdown, structured trees, bounding boxes, native PaddleOCR, layout, CLI, API, and MCP | Preferred ordinary default for paired PDF and clean Markdown. Light, fast, polyglot, and unusually convenient for Korean; still young, fast-changing, and maintainer-concentrated. Complex layout is opt-in. |
| [Docling](https://github.com/docling-project/docling) | 64,658 stars; created 2024 | Pushed Aug 12, 2026; v2.119.0 on Aug 10 | MIT | Layout, reading order, OCR, tables, formulas, figures, Markdown, lossless document JSON, and native chunks | Preferred independent quality fallback and plausible future default. Its layout- and table-centered pipeline is more established, but heavier than Xberg's native path. |
| [OpenDataLoader PDF](https://github.com/opendataloader-project/opendataloader-pdf) | 28,361 stars; created 2025 | Pushed Aug 10, 2026; v2.5.0 on Jul 14 | Apache-2.0 | Fast PDF-specific Markdown and JSON with bboxes, headings, tables, images, tagged PDF, and prompt-injection filters | Strong PDF-only fast path. Requires Java 11 and benefits from batching. Its hybrid mode delegates difficult pages to Docling, so it is not an independent fallback. |
| [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) | 87,509 stars; created 2020 | Pushed Jul 22, 2026; v3.7.0 on Jun 11 | Apache-2.0 code and relevant weights | Multilingual OCR, layout, tables, formulas, charts, seals, structured Markdown and JSON | Best multilingual OCR specialist. Broad language and hardware coverage; production VLM serving adds complexity. |
| [MinerU](https://github.com/opendatalab/MinerU) | 77,436 stars; created 2024 | Pushed Aug 11, 2026; v3.4.4 on Jul 10 and v4 alpha in July | Custom license reported as `NOASSERTION` by GitHub | OCR, layout, tables, formulas, figures, Markdown and structured `content_list` JSON | Technically top-tier and very active. Rapid schema evolution and scale or service conditions in its custom license require explicit acceptance. |
| [Marker](https://github.com/datalab-to/marker) | 38,692 stars; created 2023 | Pushed Aug 7, 2026; v2 rewrite in July | Apache-2.0 code; restricted model weights | Visually strong Markdown, LaTeX, tables, images, and GPU, CPU, or Apple Silicon execution | Capable but not a clean unconditional default. Weight terms include commercial thresholds, competitive-service restrictions, and output conditions. |
| [olmOCR](https://github.com/allenai/olmocr) | 19,297 stars; created 2024 | Last push Mar 25, 2026; v0.4.27 on Mar 12 | Apache-2.0 code and weights | English-heavy scans, equations, tables, handwriting, multicolumn reading order, and clean linearized Markdown | Best clean-license local VLM fallback. Requires an NVIDIA-class runtime, roughly 12 GB or more VRAM, and substantial model storage. |
| [MarkItDown](https://github.com/microsoft/markitdown) | 173,318 stars; created 2024 | Last push Jul 29, 2026; v0.1.7 on Jul 29 | MIT | Convenient conversion from many file formats to Markdown | Excellent convenience converter, not the strongest PDF parser. Its built-in pdfplumber/pdfminer path has no OCR; its tests expect a scanned PDF to produce empty text. |
| [Unstructured](https://github.com/Unstructured-IO/unstructured) | 15,304 stars; created 2022 | Pushed Aug 11, 2026; v0.25.2 on Aug 3 | Apache-2.0 | Typed elements, metadata, chunking, connectors, and fast, OCR, or high-resolution PDF strategies | Better treated as an ingestion framework. Operationally heavy; element JSON is usually more valuable than its lossy Markdown projection. |
| [LiteParse](https://github.com/run-llama/liteparse) | 12,062 stars; created Feb 2026 | Pushed Aug 11, 2026; v2.11.0 on Aug 3 | Apache-2.0 | Rust/PDFium Markdown, JSON, text, bboxes, screenshots, Tesseract, and complexity detection | Promising fast local route, but only six months old. Its own guidance routes difficult visual documents to commercial LlamaParse. |
| [PDF Inspector](https://github.com/firecrawl/pdf-inspector) | 14,904 stars; created Feb 2026 | Pushed Aug 12, 2026; no formal releases | MIT | Pure-Rust, position-aware Markdown and page classification for OCR routing | Interesting native front end, but extremely young, nearly single-author, and not itself an OCR engine. |
| [PyMuPDF4LLM](https://github.com/pymupdf/pymupdf4llm) | 2,092 stars; created 2024 | Pushed Aug 12, 2026; package v1.28.0 in June | AGPL-3.0 or commercial; current layout plugin has separate terms | Fast local Markdown, JSON and text with reading order, tables, image references and selective OCR | Technically the strongest lightweight LLM-specific extractor. Licensing is the reason not to make it an unqualified default. |

## Mature tools and specialists

An old creation date does not make a project ancient in the pejorative sense.
Release cadence and continuing compatibility matter more.

| Project | GitHub snapshot | Role and conclusion |
| --- | ---: | --- |
| [OCRmyPDF](https://github.com/ocrmypdf/OCRmyPDF) | 34,424 stars; created 2013; pushed Aug 6, 2026 | Actively maintained scan cleanup, rotation, deskew, searchable PDF, and PDF/A workflow. Its sidecar is plain text, not semantic Markdown. MPL-2.0 core; Ghostscript paths can introduce AGPL considerations. |
| [GROBID](https://github.com/grobidOrg/grobid) | 5,064 stars; repository since 2012; pushed Aug 10, 2026 | Best scholarly-paper specialist for authors, affiliations, citations, references, identifiers, and TEI XML. No OCR; Markdown is a lossy downstream conversion. |
| [Apache Tika](https://github.com/apache/tika) | 3,967 stars; repository since 2009; pushed Aug 11, 2026 | Excellent long-tail metadata and extraction coverage across more than 1,000 formats. Current Markdown output does not provide modern ML layout or table reconstruction. |
| [pdfplumber](https://github.com/jsvine/pdfplumber) | 10,000-plus stars; active in 2026 | Best permissively licensed geometry and table-diagnosis workbench. No OCR or native semantic Markdown. |
| [pypdf](https://github.com/py-pdf/pypdf) | 10,000-plus stars; active in 2026 | Strong PDF manipulation and basic text extraction. It is not a document-understanding or Markdown system. |
| [Poppler](https://gitlab.freedesktop.org/poppler/poppler) `pdftotext` | Official upstream is GitLab; monthly releases in 2026 | Dependable independent plain-text fallback with reading-order and layout modes. No OCR or semantic Markdown; GPL. |
| [Camelot](https://github.com/camelot-dev/camelot) | About 3,800 stars; active in 2026 | Table specialist, not a whole-document parser. |
| [Surya](https://github.com/datalab-to/surya) | About 21,000 stars; active in 2026 | Strong OCR and layout geometry in JSON or HTML, not direct Markdown. Apache code with restricted weights. |
| [Chandra](https://github.com/datalab-to/chandra) | About 12,000 stars; active in 2026 | Heavy 4B specialist for difficult forms, handwriting, tables, diagrams and multilingual content. Restricted weights and substantial GPU expectations. |

[Citra](https://github.com/SylphxAI/pdf-reader-mcp), with 889 stars and
activity in August 2026, is noteworthy for agent-facing PDF search, page-level
citations, structured tables, OCR routing, and visual evidence crops over MCP.
Its recent Rust-native rewrite and maintainer concentration make it better as
an interaction layer than the durable parsing authority.

## Declining or unsuitable new defaults

- [Nougat](https://github.com/facebookresearch/nougat) has about 10,000 stars,
  but its last substantive release was in 2023. It remains relevant to legacy
  academic and Mathpix-Markdown workflows, not as a new universal parser.
- PDF-Extract-Kit is a lower-level toolbox whose own documentation directs end
  users to MinerU. Its default branch was dormant after January 2025 during the
  research pass.
- Zerox is a clean page-to-VLM baseline, but was inactive after May 2025 and
  carries the usual API cost, privacy, and hallucination risks.
- MegaParse was inactive after February 2025.
- OpenParse offers useful visual chunking and bounding-box nodes, but is not a
  leading full-fidelity Markdown parser and reports weak table performance.

## Hosted services

For these products, GitHub contains an SDK, CLI, or examples rather than the
parsing engine. SDK stars must not be compared with open-source parser stars.

| Service | Current GitHub signal | Best role | Important boundary |
| --- | ---: | --- | --- |
| Mistral OCR 4 | [Python SDK](https://github.com/mistralai/client-python): 761 stars, pushed Aug 11, 2026 | Best general hosted fallback: multilingual page Markdown, typed blocks, bboxes, confidence, images, and tables | Proprietary service. Published pricing was $4 per 1,000 pages or $2 through batch. Ordinary API retention and ZDR availability must be qualified per integration path. |
| LlamaParse v2 | [Current Python SDK](https://github.com/run-llama/llama-parse-py): 57 stars, pushed Aug 11, 2026 | Configurable cost-effective and agentic parsing, broad formats, and LlamaIndex integration | Proprietary parser. The old 4,000-plus-star SDK is deprecated, so historical stars are misleading. Pin a parser version and explicitly disable caching for sensitive documents. |
| LandingAI ADE | [Python SDK](https://github.com/landing-ai/ade-python): 1,026 stars, pushed Aug 11, 2026 | Strong block, cell, character-range, bbox, and schema-extraction grounding | Proprietary parser. Sensitive use requires the paid zero-retention or negotiated deployment path. |
| Reducto | [Python SDK](https://github.com/reductoai/reducto-python-sdk): 26 stars, pushed Aug 12, 2026 | Complex forms, tables, semantic chunks, and downstream document workflows | Proprietary and relatively expensive. Its standard zero-data-retention wording meant automatic expiry within 24 hours, not literal no-persistence processing. |
| Mathpix | [Python client](https://github.com/Mathpix/mpxpy): 41 stars, pushed Jul 24, 2026 | Printed or handwritten mathematics, tables, chemistry, and STEM conversion | Specialist proprietary service. Mathpix Markdown may need normalization, and retention must be configured deliberately. |

Mistral OCR 4 was the strongest hosted general fallback in this comparison.
LlamaParse and Reducto deserve corpus tests when their agentic parsing and
document-workflow features justify higher cost. LandingAI ADE is particularly
interesting when extraction must be grounded back to exact source ranges.

## Benchmark evidence and limits

There is no current neutral leaderboard covering all serious candidates with
like-for-like versions and outputs.

- [OmniDocBench](https://github.com/opendatalab/OmniDocBench) contains 1,651
  pages across document, layout, and language categories. It comes from the
  OpenDataLab ecosystem, uses a noncommercial dataset, and does not compare all
  current parser versions consistently.
- `olmOCR-bench` contains 1,403 English single-page PDFs and 7,010
  deterministic tests. It avoids an LLM judge but was authored by the olmOCR
  team and does not measure every aspect of whole-document output.
- [ParseBench](https://github.com/run-llama/ParseBench) contains 2,078 pages,
  1,211 documents, and 169,011 deterministic agent-oriented rules. It was
  authored by LlamaIndex and mixes APIs, pipelines, and raw vision models.
- [OpenDataLoader Bench](https://github.com/opendataloader-project/opendataloader-bench)
  is reproducible but project-authored. Its hybrid score includes Docling as a
  backend rather than measuring a wholly independent parser.
- An independent 2026 study covering 1,706 pages of Portuguese administrative
  PDFs reported 97.1% downstream QA accuracy from manually prepared Markdown,
  86.9% from naive PDF loading, and 94.1% from its best automated Docling
  pipeline. Its important finding is that hierarchical splitting, metadata,
  and image descriptions mattered in addition to parser choice. See the
  [paper](https://doi.org/10.3390/app16105069) and
  [reproduction repository](https://github.com/sousaalexandre/loss-j).

A bounded smoke test on four repository fixture PDFs compared MarkItDown and
OpenDataLoader local mode. OpenDataLoader produced better headings and reflow
on the academic fixture; MarkItDown handled two simple form or borderless-table
fixtures better; both returned empty output for the scanned fixture without
OCR. This is diagnostic evidence, not a general speed or quality ranking.

## Licensing and privacy findings

- Xberg is MIT. Its low operational weight and native OCR integration make it
  the best fit for the ordinary local default, but its rapid evolution makes
  version pinning and corpus regression tests important.
- Docling is MIT, supports local and offline operation, and had no telemetry
  during source inspection. It retains the strongest quality-fallback
  position; optional OCR engines and models still need exact-version license
  checks.
- PaddleOCR provides the cleanest broad multilingual OCR option among the
  inspected systems.
- olmOCR provides Apache-licensed code and weights, making it a cleaner VLM
  fallback than Marker, MinerU, Surya, or Chandra when its English and NVIDIA
  constraints are acceptable.
- Marker and the related Datalab model projects pair permissive code with model
  licenses containing commercial thresholds, competitive-use restrictions,
  or output conditions.
- MinerU uses a custom Apache-derived license with scale and online-service
  conditions.
- PyMuPDF and PyMuPDF4LLM require AGPL compliance or a commercial license. The
  current PyMuPDF4LLM installation path also pulls a layout component with
  separate noncommercial or commercial terms.
- No telemetry was found in the inspected Docling, Marker, MinerU,
  PyMuPDF4LLM, or olmOCR source paths. First-run model downloads still contact
  external model registries unless artifacts are pre-provisioned.
- Every hosted service needs separate qualification for retention, training
  use, region, encryption, caching, deletion, and actual zero-data-retention
  semantics. Open-source client licensing says nothing about the hosted
  parser's privacy contract.

## Research method

The research used GitHub repository and topic searches, exact GitHub API
metrics, release histories, source inspection at pinned local refs, official
project documentation, published licenses and model cards, benchmark source
repositories, and a small local fixture probe. Searches covered PDF-to-Markdown,
PDF parser, document parsing, document AI, intelligent document processing,
OCR, layout, table extraction, and agent or MCP terms.

Maintenance judgments considered releases, default-branch commits,
contributor concentration, issue and pull-request stewardship, and whether
activity reflected substantive development rather than an isolated dependency
update. GitHub's generic `updated_at` field was not treated as maintenance
evidence.
