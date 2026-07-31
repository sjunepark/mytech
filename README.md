# Design Decisions

This collection is the canonical home for reusable technical design decisions,
reference architectures, and preferred technology profiles. It records the
target state independently of any one project's current implementation.

Adopting repositories should:

- adopt a decision explicitly;
- keep migration plans and current-state notes locally;
- record a local exception when project constraints require one; and
- link here instead of copying normative text.

## Decision types

- **Principles** describe durable design preferences.
- **Architectures** define reusable system shapes, interfaces, and invariants.
- **Stacks** define preferred technologies and the roles they should play.

Create a directory for a type when its first document is added. Avoid empty
categories and placeholder documents.

## Status

- **Proposed** — under discussion and not yet normative.
- **Accepted** — the default for projects that adopt the decision.
- **Superseded** — retained for history and linked to its replacement.

## Accepted architectures

- [External HTTP Contracts and Rust SDKs][external-contracts] — a shared target
  architecture for [OpenDART], [Seoro], and future Rust clients of external
  HTTP providers.

[external-contracts]: decisions/external-http-contracts-and-rust-sdks.md
[OpenDART]: https://github.com/cpaikr/opendart
[Seoro]: https://github.com/cpaikr/seoro

## Writing decisions

Each decision should state:

- its status and intended adopters;
- what it governs and what remains project-specific;
- the normative target design and enforceable invariants;
- preferred technology roles, including what must stay replaceable; and
- migration principles without embedding a project's temporary task list.

Prefer one clear decision over parallel recommendations. When experience
invalidates a decision, supersede it rather than silently rewriting its intent.
