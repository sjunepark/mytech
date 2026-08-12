# PDF Ingestion for LLM Agents History

## 2026-08-12

Promoted Xberg from the independent fast path to the ordinary local default.
Its native PDF-to-Markdown flow and Korean PaddleOCR integration better fit the
chosen minimal PDF-plus-Markdown artifact contract. Docling remains the
quality-first independent fallback and should replace Xberg if representative
documents show recurring structural errors that Docling materially fixes.

Simplified the ordinary retained representation from PDF, structured JSON,
Markdown, manifest, and assets to a paired source PDF and clean Markdown file
with minimal provenance. Parser structure and coordinates are now temporary by
default and become durable only for a concrete exact-grounding feature.

Added Korean-first OCR routing. Specialized Korean OCR or document parsing is
the transcription authority; general multimodal models are selective fallbacks
for difficult visual or semantic content rather than automatic whole-document
rewriters.
