# mytech

This repository is my personal reference for reusable technical preferences and
design decisions. It gives me and the agents I work with a consistent baseline
when different projects face similar requirements.

The guidance describes my current preference. It is a starting point for
project-specific discussion, not a substitute for considering that project's
requirements and local instructions.

## How to use this repository

1. Use this README to find the relevant area.
2. Read only the document needed for the decision at hand.
3. Treat its guidance as the default starting point.
4. Discuss whether project constraints justify a different choice.

Link to the relevant document when using it from another project. A project's
requirements and local instructions take precedence over this repository.

Brief "Initial evidence" annotations record extraction context only. They are
not dependencies or current-state inventories; each decision must stand on its
own.

## Areas

- [`architecture/`](architecture/) contains reusable system shapes, boundaries,
  interfaces, and architectural decisions.
- [`libraries/`](libraries/) contains preferred libraries and the roles for
  which they are a default.
- [`stacks/`](stacks/) contains preferred combinations of technologies.
- [`practices/`](practices/) contains reusable engineering, tooling, and
  workflow guidance.
- [`reference/`](reference/) contains descriptive technical knowledge that is
  useful across projects but is not a preference or policy.

The areas are intentionally broad and shallow. Add another area only when
concrete guidance does not fit an existing one.

## Current guidance

### Architecture

- [Boundary-Owned Contracts and Pure Cores](architecture/boundary-owned-contracts-and-pure-cores.md)
- [Canonical Sources and Derived Artifacts](architecture/canonical-sources-and-derived-artifacts.md)
- [Database Schema Authority](architecture/database-schema-authority.md)
- [Persist Before External Effects](architecture/persist-before-external-effects.md)
- [External HTTP Contracts and Handwritten Clients](architecture/external-http-contracts-and-handwritten-clients.md)
- [Rust for External HTTP Protocol Implementations](architecture/rust-for-external-http-protocols.md)

### Libraries

- [Kong for Go Command-Line Interfaces](libraries/go/cli.md)
- [Clap for Rust Command-Line Interfaces](libraries/rust/cli.md)
- [Effect CLI for TypeScript Command-Line Interfaces](libraries/typescript/cli.md)
- [Effect for TypeScript Application Runtimes](libraries/typescript/effect.md)

### Stacks

- [PDF Ingestion for LLM Agents](stacks/pdf-ingestion-for-llm-agents.md)
- [SvelteKit, Effect, and PostgreSQL](stacks/typescript/sveltekit-effect-postgresql.md)

### Practices

- [Automation-Facing CLI Contracts](practices/automation-facing-cli-contracts.md)
- [External Provider Qualification](practices/external-provider-qualification.md)
- [Repository Documentation States](practices/repository-documentation-states.md)
- [Verification from Source to Consumer](practices/verification-from-source-to-consumer.md)

## Reference knowledge

Reference notes preserve useful system understanding and observed behavior.
They are evidence-backed descriptions, not guidance to apply by default.

- [How ChatGPT Desktop Uses the Codex Runtime](reference/chatgpt-desktop-and-codex-runtime.md)
- [Korean OCR Options for Agent Ingestion](reference/korean-ocr-options-for-agent-ingestion.md)
- [PDF-to-Agent Parsing Landscape](reference/pdf-to-agent-parsing-landscape.md)
- [Xberg PDF Ingestion Usage](reference/xberg-pdf-ingestion-usage.md)

## Draft guidance

[`draft/`](draft/) contains plausible preferences that need owner review before
they become defaults. Drafts are not active guidance and must not be applied to
another project as policy.

## Guidance document contract

Guidance documents use one minimal frontmatter field:

```yaml
---
status: accepted
---
```

Allowed statuses and required sections are:

- `accepted`: `Decision` and `Revisit when`;
- `draft`: `Tentative preference`, `Why this is uncertain`, `Promotion
  questions`, and `If accepted`.

An accepted document records one coherent reusable preference. Keep only the
rationale and stable constraints needed to decide whether and how to apply it.
Use additional sections when they materially clarify ownership, invariants, or
safe application.

Active guidance is not a project implementation guide, migration plan,
exhaustive verification catalog, or change log. Link shared rules to their
owning guidance instead of restating them, keep project-specific procedures in
the consuming project, and keep useful change rationale under `history/`.

When consolidating documents, re-distill them around the surviving preference.
Do not preserve sections merely because they appeared in the source documents.

Accepted guidance belongs under an active area. Draft guidance belongs under
`draft/`. Routing READMEs and history notes are not guidance and do not use
this frontmatter.

Do not duplicate titles, areas, technology versions, evidence inventories, or
review dates in frontmatter. Paths and document content own that information.

Run the repository-owned validation after changing guidance. It checks the
guidance document contract and Markdown style:

```sh
./scripts/validate-guidance
```

Query all non-settled guidance as one JSON document with:

```sh
./scripts/query-unsettled-guidance
```

Accepted guidance is settled. Draft guidance, and guidance with a malformed,
missing, or unknown status, is included in the query result for owner review.
Success and execution failures use a versioned JSON envelope; exit status `2`
identifies an invalid invocation.

The validation uses `uvx` to run the repository-pinned `rumdl` version. To
apply safe Markdown formatting fixes directly, run:

```sh
./scripts/rumdl fmt .
```

## Maintaining guidance

Active documents describe current preferences. Update them in place when a
preference changes.

When guidance is replaced, update its consumers and delete the superseded
document. Do not keep redirect or tombstone guidance in active areas. Preserve
useful change rationale under `history/`; Git retains exact prior content.

When the reason for a meaningful change will remain useful, add a brief dated
note under [`history/`](history/) at the same relative path as the active
document. For example, the history for `architecture/example.md` belongs at
`history/architecture/example.md`. Create history files only when they have
something useful to record; Git retains the exact textual changes.

History is not part of the normal reading path. Consult it only when the
evolution of a preference matters.
