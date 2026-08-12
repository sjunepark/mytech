# Korean OCR Options for Agent Ingestion

This is a descriptive research snapshot from 2026-08-12, not a technical
preference. The corresponding preference is
[PDF Ingestion for LLM Agents](../stacks/pdf-ingestion-for-llm-agents.md).

## Conclusion

The useful distinction is not old-fashioned “systematic programs” versus AI.
Modern OCR systems already use neural recognition, layout models, or document
vision-language models. The real choice is between a specialized transcription
pipeline and a general generative multimodal model.

For Korean documents, use native extraction for born-digital PDFs and
specialized OCR or document parsing for scans. A general model can be better at
reading order, charts, damaged pages, and clean Markdown, but it is less safe as
the only transcription authority because it can omit, normalize, or invent
content. Retaining the PDF makes occasional verification easy, but it does not
recover facts that disappeared from the Markdown and therefore from retrieval.

The practical defaults to test are:

1. **Local:** Xberg with its native PaddleOCR Korean path for scanned pages,
   emitting only clean Markdown.
2. **Hosted:** Upstage Document Parse for Korean-first agent-ready Markdown.
3. **Escalation:** a document VLM or general multimodal model only for pages
   that are low-confidence or visually complex.

No neutral current benchmark compares all serious providers on Korean
documents. These are informed candidates, not a declared accuracy winner.

## Local options

| Option | Korean and output | Strengths | Limits and best role |
| --- | --- | --- | --- |
| [Xberg](https://github.com/xberg-io/xberg) with PaddleOCR | Explicit Korean recognition, automatic per-page scan detection, and direct Markdown | Best ordinary local workflow: Rust-native PDF extraction and OCR without a separate Python runtime | Complex-layout Markdown requires deliberate layout configuration; young and maintainer-concentrated |
| [PaddleOCR PP-OCRv5](https://github.com/PaddlePaddle/PaddleOCR/blob/main/docs/version3.x/algorithm/PP-OCRv5/PP-OCRv5_multi_languages.en.md) | Dedicated Korean and English recognition model; structured OCR that can feed Markdown normalization | Best conventional Korean recognition baseline; Apache-2.0 code and relevant weights; active, large ecosystem | Recognition is not itself polished document Markdown; use through Xberg or another document normalizer |
| [PaddleOCR-VL 1.6](https://github.com/PaddlePaddle/PaddleOCR/blob/main/docs/version3.x/pipeline_usage/PaddleOCR-VL.en.md) | Korean among 109 languages; parses layout, tables, charts, formulas, handwriting, and historical documents | Strong local candidate for difficult pages; compact 0.9B document VLM with direct Markdown and JSON | Heavier and more generative than ordinary OCR; published quality claims are project-authored |
| [Docling](https://github.com/docling-project/docling/blob/main/docs/concepts/OCR.md) | Orchestrates native extraction, layout, Markdown, and several OCR backends | More established quality fallback when Xberg misses reading order, tables, or other structure | Heavier stack; its rich JSON is useful diagnostically but unnecessary to retain |
| [EasyOCR](https://github.com/JaidedAI/EasyOCR) | `ko` model supports Korean with English | Simple Apache-2.0 fallback and useful independent comparator | Less active and less document-structure-oriented than PaddleOCR |
| [Tesseract](https://github.com/tesseract-ocr/tesseract) | `kor+eng` language data; text or searchable PDF | Mature, deterministic, CPU-friendly baseline with no generative invention | Usually weaker on degraded scans, handwriting, dense layouts, and polished Markdown |
| Apple Vision through Docling OcrMac | macOS-native recognition; supported languages depend on the OS version | Convenient private on-device option on Apple hardware | Mac-only and less reproducible across OS versions; benchmark before relying on Korean quality |

Xberg's current PaddleOCR configuration defaults to the PP-OCRv6 generation
but routes Korean requests to the script-specific Korean recognizer. Select
Korean explicitly rather than relying on language detection, and pin the Xberg
version so this routing remains reproducible.

Docling currently exposes RapidOCR models for PP-OCRv4, v5, and v6. Its own OCR
guide notes that the `korean` alias exists for PP-OCRv6 but the underlying v6
model does not currently support Korean. When using Docling, pin PP-OCRv5 for
Korean instead of assuming the newest model name has the broadest coverage.

PaddleOCR reports large PP-OCRv5 improvements on its own Korean recognition
dataset. That evidence supports testing it, but it is not a neutral
whole-document comparison and should not replace a corpus test.

Other technically relevant local models are not as clean a default:

- [NVIDIA Nemotron OCR v2](https://huggingface.co/nvidia/nemotron-ocr-v2) is a
  promising compact Korean-aware alternative on Linux with recent NVIDIA CUDA,
  but does not fit a Mac-only or CPU-first deployment.
- [Surya 2](https://github.com/datalab-to/surya) offers multilingual full-page
  OCR and layout understanding, but its model-weight terms and relatively slow
  Apple or CPU path need explicit acceptance.
- olmOCR has permissive code and weights and respectable Korean benchmark
  results, but its 7B runtime and NVIDIA memory requirement are excessive for
  an ordinary Korean OCR fallback.
- [BizOnAI-OCR](https://github.com/ONTHEIT-AI/BizOnAI-OCR) is a new
  Korean-document specialist with promising
  project-authored benchmark results. Its tiny ecosystem, lack of releases,
  and model-license wording make it a benchmark or watch-list candidate rather
  than a foundation.
- docTR includes Korean vocabulary, but that alone is not evidence that its
  default recognizers are well trained for Korean documents.

### Modernness and maintenance snapshot

GitHub signals captured on 2026-08-12:

| Project | Stars | Latest observed activity | Assessment |
| --- | ---: | --- | --- |
| PaddleOCR | 87,509 | v3.7.0 on Jun 11; pushed Jul 22, 2026 | Large, modern, and active; the preferred Korean OCR ecosystem |
| Tesseract | 75,874 | v5.5.3 on Jul 24; pushed Aug 12, 2026 | Old but actively maintained, not abandoned or “ancient” in capability stewardship |
| Docling | 64,658 | v2.119.0 on Aug 10; pushed Aug 12, 2026 | Very current and rapidly maintained |
| EasyOCR | 29,897 | Last release Sep 2024; pushed Dec 5, 2025 | Popular but less current than PaddleOCR |
| Surya | 21,255 | v0.22.1 on Jul 20; pushed Jul 23, 2026 | Current and active; licensing is the larger concern |
| olmOCR | 19,297 | v0.4.27 on Mar 12; pushed Mar 25, 2026 | Current enough, but hardware-heavy and English-oriented |
| Xberg | 8,964 | v1.0.14 on Aug 4; pushed Aug 12, 2026 | Extremely active and modern, but young and predominantly maintained by one contributor |
| RapidOCR | 7,466 | Pushed Aug 12, 2026 | Active lightweight runtime for Paddle-family models |
| docTR | 6,206 | Pushed Jul 28, 2026 | Active, but not a Korean-first choice |

Stars describe ecosystem reach, not Korean accuracy. Tesseract demonstrates
why creation age alone is a poor “modernness” test: its architecture is mature,
but the project and current releases remain active.

### Available Korean benchmark evidence

The public
[KDoc-OCRBench-V2](https://huggingface.co/datasets/ONTHEIT/KDoc-OCRBench-V2)
contains 849 Korean public-sector pages and 56,197 reviewed tests, heavily
weighted toward tables. Its reported overall scores put BizOnAI-OCR at 82.3,
PaddleOCR-VL at 77.7, DeepSeek OCR at 76.7, olmOCR at 76.3, and GLM OCR at
61.7. The BizOnAI authors created the dataset, initial silver outputs used a
general model, and exact model versions matter, so this is useful evidence but
not an independent verdict.

The narrower [KORIE receipt benchmark](https://github.com/MahmoudSalah/KORIE)
contains 774 Korean receipts. It reports character error rates of 15.84 for
PaddleOCR, 17.36 for EasyOCR, and 25.43 for Tesseract. This supports PaddleOCR
for noisy receipt-like Korean, but it does not generalize to every document
type.

## Hosted Korean and multilingual options

| Option | Output and published price | Best role | Important boundary |
| --- | --- | --- | --- |
| [Upstage Document Parse](https://www.upstage.ai/ko/products/document-parse) | HTML or Markdown; Standard $0.01/page, Enhanced $0.03/page; separate OCR $0.0015/page | First hosted test for Korean-first agent-ready output, including scans, tables, charts, and handwriting | Synchronous API inputs and outputs are not stored or used for training under the [2026 terms](https://www.upstage.ai/terms-of-service/update-january-27-2026); async retention differs |
| [NAVER CLOVA OCR](https://www.ncloud.com/api-cms/service-product/static/ocr) | JSON text, confidence, line breaks, polygons, and optional tables; not Markdown | Korean print or handwriting when raw transcription and privacy matter more than direct Markdown | PDFs are limited to 10 pages per general request; [the API FAQ](https://guide.ncloud-docs.com/docs/en/clovaocr-faq) says originals and results are processed in memory and not used for model improvement |
| [Mistral OCR 4](https://docs.mistral.ai/studio-api/document-processing/basic_ocr) | Per-page Markdown and structured tables; $4/1,000 pages | Strong international purpose-built document parser with explicit [Korean support](https://docs.mistral.ai/resources/languages) | Proprietary; zero-data retention requires approval and applies only to eligible stateless paths |
| [Azure Document Intelligence Layout](https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/prebuilt/layout?view=doc-intel-4.0.0) | Markdown with HTML for complex tables; explicit Korean print and handwriting support | Mature enterprise-cloud alternative, especially in an existing Azure estate | Analysis data is retained for up to 24 hours unless deleted sooner; price varies by region and contract |
| [Google Gemini Layout Parser](https://docs.cloud.google.com/document-ai/docs/layout-parse-chunk) | Context-aware RAG chunks and structure; $10/1,000 pages; Enterprise OCR is $1.50/1,000 pages | Complex charts, tables, and retrieval-oriented chunking | Current Gemini layout versions include previews; some global endpoints do not meet data-residency requirements |

AWS Textract is not a Korean candidate: its official document-analysis limits
list English, French, German, Italian, Portuguese, and Spanish, but not Korean.

## General multimodal models

[OpenAI's PDF input](https://developers.openai.com/api/docs/guides/file-inputs)
gives a vision-capable model both extracted text and page images. That can make
a current OpenAI model useful for semantic reconstruction, table cleanup,
figure descriptions, and pages where the normal OCR path fails. Direct PDF
input is limited to 50 MB per file and 50 MB total per request, and page images
can consume substantial tokens.

It should not be assumed to be the best Korean OCR engine. OpenAI's
[vision guide](https://developers.openai.com/api/docs/guides/images-vision/)
explicitly warns that non-Latin text including Korean may perform poorly and
that small or rotated text can be misread. General models also optimize for a
helpful response rather than a conservative transcript unless constrained and
validated.

If a general model is used for transcription, require it to preserve wording,
numbers, and uncertainty; prohibit summarizing or silent correction; and mark
unreadable text. Prefer sending only failed pages at sufficient image detail.
For large retained corpora, ingest the normalized Markdown into retrieval
instead of resending whole PDFs to the model for every question.

The strongest hybrid is:

```text
born-digital page -> native text and layout extraction
Korean scanned page -> Xberg with native PaddleOCR Korean
low-confidence or complex page -> document VLM or general model fallback
all pages -> one normalized Markdown document
```

This uses generative models where their semantic understanding adds value
without making every character depend on unconstrained generation.

## Choosing with a Korean corpus

Use 50–100 representative pages rather than a synthetic English benchmark.
Include mixed Korean and English, small fonts, low-resolution scans,
handwriting, government forms, dense tables, charts, and pages containing
dates, currency, identifiers, and proper nouns.

Measure:

- Hangul character error rate plus omitted and inserted spans;
- exact numbers, dates, units, names, and punctuation;
- paragraph and column reading order;
- table cell content and Markdown usability;
- hallucinated or silently normalized content;
- retrieval-answer accuracy over the resulting Markdown; and
- latency, hardware, price, failure rate, and privacy constraints.

Select the cheapest and simplest default that clears the content threshold,
then route only failed pages to the stronger fallback. Quality gating by page
is usually more reliable and cheaper than choosing one maximum-capability model
for every document.
