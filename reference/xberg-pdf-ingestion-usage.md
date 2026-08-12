# Xberg PDF Ingestion Usage

This is the executable setup for the default in
[PDF Ingestion for LLM Agents](../stacks/pdf-ingestion-for-llm-agents.md).
The commands were verified against Xberg v1.0.14. Xberg changes quickly, so
record `xberg --version` with generated artifacts and recheck flags when
upgrading.

## Install the CLI

On macOS, use Xberg's Homebrew distribution:

```bash
brew trust xberg-io/tap
brew install xberg-io/tap/xberg
xberg --version
```

Use the CLI for interactive work, shell scripts, and agent tool calls. Use an
SDK when extraction is part of application code; the SDKs embed the same Rust
engine rather than requiring a separate Xberg service.

```bash
pip install xberg
npm install @xberg-io/xberg
```

## Ordinary PDF-to-Markdown conversion

Keep the source PDF and write Xberg's Markdown stdout to the matching file:

```bash
xberg extract report.pdf \
  --content-format markdown \
  --page-markers true \
  > report.md
```

`--page-markers true` adds inexpensive source-page comments. Omit it when page
references have no value. Do not request JSON, extracted geometry, or chunks
unless a concrete consumer needs them.

## Korean scans

For PDFs containing scanned Korean pages, use PaddleOCR and select Korean
explicitly:

```bash
xberg extract report.pdf \
  --content-format markdown \
  --page-markers true \
  --ocr true \
  --ocr-backend paddle-ocr \
  --ocr-language ko \
  --ocr-scanned-pages \
  > report.md
```

This preserves native text on ordinary pages and OCRs pages classified as
scans. PaddleOCR models download automatically on first use and remain in the
local model cache. Do not use `--force-ocr true` by default; reserve it for an
image-only document or a demonstrably broken text layer.

## Layout escalation

If the ordinary result loses reading order, headings, tables, lists, or figure
placement, rerun with layout-informed Markdown and adaptive page selection:

```bash
xberg extract report.pdf \
  --content-format markdown \
  --page-markers true \
  --layout \
  --layout-strategy auto \
  --use-layout-for-markdown \
  > report.md
```

If representative documents remain unreliable after this escalation, compare
Docling and apply the switch criteria in the owning guidance.
