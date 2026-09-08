# mytech

This repository records reusable technical preferences. They are starting
points for decisions, not requirements imposed on every consuming project.
Project requirements and local instructions take precedence.

## Decision posture

Prefer clear ownership, explicit failure and recovery, and verification through
real consumer boundaries. Start with the existing language and platform when
they satisfy the need. Add a runtime, service, schema, binding, or release
mechanism when it removes more durable complexity than it creates.

Judge a choice by correctness, maintainability, operating behavior, and consumer
fit. Initial implementation speed is secondary, but additional build targets,
upgrade coupling, concepts, and failure modes are long-term costs. A preference
breaks a tie; it does not substitute for evidence or justify a rewrite by itself.

## Find guidance

| Decision | Accepted guidance |
| --- | --- |
| Application shape | [Boundaries and pure cores](architecture/boundary-owned-contracts-and-pure-cores.md); [SvelteKit, Effect, PostgreSQL](stacks/typescript/sveltekit-effect-postgresql.md) |
| TypeScript orchestration | [Effect](libraries/typescript/effect.md) |
| HTTP integrations | [Contracts and clients](architecture/external-http/external-http-contracts-and-handwritten-clients.md); [when Rust earns a core](architecture/external-http/rust-for-external-http-protocols.md); [provider qualification](practices/external-provider-qualification.md) |
| Durable state | [Database authority](architecture/database-schema-authority.md); [persist before external effects](architecture/persist-before-external-effects.md) |
| Generated and ingested artifacts | [Canonical sources](architecture/canonical-sources-and-derived-artifacts.md); [PDF ingestion](stacks/pdf-ingestion-for-llm-agents.md) |
| Native packages | Rust cores for [Node.js](architecture/rust-cores-for-nodejs-packages.md) and [Python](architecture/rust-cores-for-python-packages.md) |
| CLI parsers | [TypeScript](libraries/typescript/cli.md); [Rust](libraries/rust/cli.md); [Go](libraries/go/cli.md) |
| CLI delivery | [Automation contracts](practices/automation-facing-cli-contracts.md); [standalone distribution](practices/standalone-cli-distribution.md); [version checking](practices/cli-version-checking.md) |
| Verification and CI | [Source to consumer](practices/verification-from-source-to-consumer.md); [platform coverage](practices/cost-aware-ci-platform-coverage.md) |
| Changing a project | [Rewrites](practices/code-rewrites.md); [documentation states](practices/repository-documentation-states.md) |

Read only what the decision needs and link to its owner when applying it.
[Drafts](draft/README.md) are proposals, not defaults. Reference notes preserve
dated evidence or usage instructions; history explains meaningful preference
changes and stays outside the normal reading path.

For descriptive system knowledge, see the dated
[desktop/Codex runtime observation](reference/chatgpt-desktop-and-codex-runtime.md).

The [2026-09-05 review](reference/technology-preferences-review.md) gives a
candid assessment of the choices and the revisions made during the review.

## Guidance document contract

Guidance starts with exactly this restricted frontmatter form:

```yaml
---
status: accepted
---
```

Use `status: draft` for proposals. No other frontmatter fields are supported.
The body starts with a level-one title; required sections are level two.

- `accepted` belongs in `architecture/`, `libraries/`, `practices/`, or `stacks/`
  and requires `Decision` and `Revisit when` sections.
- `draft` belongs under `draft/` and requires `Tentative preference`,
  `Why this is uncertain`, `Promotion questions`, and `If accepted` sections.
- Routing READMEs, references, and history are outside this lifecycle schema.

Each guidance document owns one coherent preference with its rationale,
applicability, and stable constraints. Project procedures, delivery plans, and
historical evidence belong elsewhere. Initial-evidence project names record
provenance; they do not prove those projects currently implement the guidance.

## Maintenance and checks

Update guidance in place. Re-distill overlapping preferences rather than
concatenating them, update consumers, and preserve meaningful change rationale
in a brief dated `history/` file mirroring the guidance path. Git retains exact
diffs. Promote a draft when its scope and tradeoffs are resolved, not merely
because it appeared in more repositories.

Use Python 3.10 or newer and `uv` (providing `uvx`). The lint wrapper selects its
pinned rumdl version and may download it on first use. Run:

```sh
./scripts/validate-guidance
./scripts/query-unsettled-guidance
```

Validation checks guidance placement and headings, runs script regression
tests, and lints Markdown including relative links. The query emits one JSON
document listing drafts and invalid lifecycle metadata or placement; it does
not replace full validation. Neither command verifies external links or the
truth of technology claims. Checks currently run locally; this repository has
no configured CI gate.
