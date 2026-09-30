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
| HTTP integrations | [Contracts and clients](architecture/external-http/external-http-contracts-and-handwritten-clients.md); [when Rust earns a core](architecture/external-http/rust-for-external-http-protocols.md); [provider qualification](practices/external-provider-qualification.md); [request pacing](practices/external-request-pacing.md) |
| Durable state | [Database authority](architecture/database-schema-authority.md); [persist before external effects](architecture/persist-before-external-effects.md) |
| Generated and ingested artifacts | [Canonical sources](architecture/canonical-sources-and-derived-artifacts.md); [PDF ingestion](stacks/pdf-ingestion-for-llm-agents.md) |
| Native packages | Rust cores for [Node.js](architecture/rust-cores-for-nodejs-packages.md) and [Python](architecture/rust-cores-for-python-packages.md) |
| CLI parsers | [TypeScript](libraries/typescript/cli.md); [Rust](libraries/rust/cli.md); [Go](libraries/go/cli.md) |
| CLI behavior | [Automation contracts](practices/automation-facing-cli-contracts.md); [version checking](practices/cli-version-checking.md) |
| CLI delivery | [Standalone distribution](practices/standalone-cli-distribution.md); [installation guides](practices/cli-installation-guides.md) |
| CLI agent skills | [Consumer skills and progressive loading](practices/cli-consumer-skills.md) |
| Verification and CI | [Source to consumer](practices/verification-from-source-to-consumer.md); [platform coverage](practices/cost-aware-ci-platform-coverage.md); [owner-gated PR CI](practices/owner-gated-pull-request-ci.md) |
| Repository files | [LF line endings](practices/lf-line-endings.md) |
| Changing a project | [Rewrites](practices/code-rewrites.md); [documentation states](practices/repository-documentation-states.md) |

Read only what the decision needs and link to its owner when applying it.
[Drafts](draft/README.md) are proposals, not defaults.
[Reference notes](reference/README.md) provide research, usage instructions, and
dated observations. History explains meaningful preference changes and stays
outside the normal reading path.

## Use from another project

Use [consult-mytech](skills/consult-mytech/SKILL.md) to read relevant preferences
and assess a coding task or project's alignment. Its source package is
`skills/consult-mytech/`; installation is separate from explicit invocation.

## Contribute

See [Contributing](CONTRIBUTING.md) for document placement, the guidance schema,
maintenance rules, skill ownership, and validation commands.
