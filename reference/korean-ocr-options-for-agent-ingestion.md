# Korean OCR Options for Agent Ingestion

A research snapshot from 2026-08-12, edited for scope on 2026-09-05. It records
candidates and evaluation limits, not a current accuracy ranking. The owning
preference is [PDF Ingestion for LLM Agents](../stacks/pdf-ingestion-for-llm-agents.md).

## The useful distinction

Modern OCR already uses learned recognition and layout models. Compare a
specialized transcription pipeline with a general generative multimodal model,
rather than treating OCR as the non-AI alternative.

Native text extraction, character recognition, reading order, and semantic
reconstruction solve different problems. Good-looking Markdown can still omit
numbers or silently normalize wording. Retaining the PDF permits verification,
but facts lost during extraction will also be absent from ordinary retrieval.

## Local candidates

| Candidate | Evidence to inspect | What a corpus test must resolve |
| --- | --- | --- |
| [Xberg](https://github.com/xberg-io/xberg) with PaddleOCR | CLI, build features, and language/model routing | Mixed native/scanned pages, Korean recognition, and final Markdown fidelity |
| [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) recognition models | The exact model's language coverage and model card | Characters, small text, numbers, handwriting, and the separate layout/normalization path |
| [PaddleOCR-VL](https://github.com/PaddlePaddle/PaddleOCR/blob/main/docs/version3.x/pipeline_usage/PaddleOCR-VL.en.md) | Document-model capabilities and deployment requirements | Structural gains versus omissions, invented text, and runtime cost |
| [Docling](https://github.com/docling-project/docling/blob/main/docs/concepts/OCR.md) | Selected OCR backend, model, and language configuration | Whether layout and table handling improve the complete document |
| [EasyOCR](https://github.com/JaidedAI/EasyOCR), [Tesseract](https://github.com/tesseract-ocr/tesseract) | Korean models and preprocessing choices | Independent recognition baselines on the actual scans |
| [OcrMac](https://github.com/straussmaximilian/ocrmac) | Installed macOS recognition capabilities | Korean accuracy and reproducibility across supported OS versions |

A newer general model does not necessarily preserve a script-specific model's
coverage. Xberg v1.0.14 accepts `ko`, `kor`, and `korean` and routes Korean to
its dedicated recognizer; the
[language mapping](https://github.com/xberg-io/xberg/blob/v1.0.14/crates/xberg/src/paddle_ocr/mod.rs)
and [routing implementation](https://github.com/xberg-io/xberg/blob/v1.0.14/crates/xberg/src/paddle_ocr/model_manager.rs)
were checked on 2026-09-05. Revalidate the selected release and model rather
than carrying that routing claim forward indefinitely.

Other candidates in the original investigation included Nemotron OCR, Surya,
olmOCR, BizOnAI-OCR, and docTR. Vocabulary coverage, project benchmarks, and
model size alone did not establish their suitability as a general Korean
pipeline. Hardware, licensing, and actual trained language coverage remain
selection inputs.

## Korean benchmark evidence

[KDoc-OCRBench-V2](https://huggingface.co/datasets/ONTHEIT/KDoc-OCRBench-V2)
provides Korean public-sector document tests with substantial table coverage.
Its authors also develop an OCR candidate. Inspect annotation methods,
model versions, and task weighting before using its scores to select a parser.

[KORIE](https://github.com/MahmoudSalah/KORIE) provides Korean receipt evidence.
Receipt results help evaluate that class of noisy input; they do not establish
quality on accounting reports, government forms, or long mixed-layout PDFs.

The original investigation did not establish an independent, like-for-like
ranking across all serious Korean pipelines. The September review did not add
new corpus measurements.

## Hosted and general-model candidates

Upstage Document Parse, NAVER CLOVA OCR, Mistral OCR, Azure Document Intelligence,
and Google Document AI were relevant candidates in the original investigation.
Compare the specific API's Korean support, output form, limits, cost, and privacy
contract. Raw OCR JSON and agent-ready Markdown require different downstream
work; a product name alone does not establish either capability.

General multimodal models are candidates for difficult layouts, figures, and
uncertain pages. When testing transcription, require preserved wording and
numbers, visible uncertainty, and no summarization or silent correction. Compare
the result with the source rather than asking another unconstrained generation
to certify it. Measure whether model assistance improves retrieval as well as
visual neatness.

Provider terms, retention, regional processing, and model availability change.
Use [External Provider Qualification](../practices/external-provider-qualification.md)
for the exact selected endpoint; this snapshot grants no production or data-use
authority.

## Representative evaluation

Use material that reflects the intended corpus: mixed Korean and English,
small fonts, low-resolution scans, handwriting, forms, dense tables, charts,
and pages with dates, currency, identifiers, and proper nouns. Keep source
identities, reviewed expected content, selected versions, and configuration.

Measure omissions and inserted spans, exact numeric and named values, reading
order, table semantics, retrieval answers, latency, resource requirements, and
privacy. Check difficult pages separately so a high average cannot hide a
failure on the documents that matter most.
