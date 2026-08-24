# mytech

This repository records my current reusable technical preferences and design
decisions. They provide a consistent starting point, not a substitute for the
requirements and local instructions of the project applying them.

## Using the guidance

Search by topic and read only the documents relevant to the decision at hand.
Accepted guidance is the default starting point; project-specific requirements
take precedence. Link to the relevant document when applying it elsewhere.

Drafts are proposals awaiting review. Reference notes describe useful system
knowledge rather than preferences. History is outside the normal reading path
and matters only when the reason a preference changed is relevant.

Rewrite guidance: [Code rewrites](practices/code-rewrites.md).

CI guidance:
[Cost-aware CI platform coverage](practices/cost-aware-ci-platform-coverage.md).

CLI distribution guidance:
[Standalone CLI distribution](practices/standalone-cli-distribution.md).

Rust-backed native package guidance:
[Node.js](architecture/rust-cores-for-nodejs-packages.md) and
[Python](architecture/rust-cores-for-python-packages.md).

## Guidance document contract

Guidance documents declare one status:

```yaml
---
status: accepted
---
```

- `accepted` documents contain `Decision` and `Revisit when` sections.
- `draft` documents contain `Tentative preference`, `Why this is uncertain`,
  `Promotion questions`, and `If accepted` sections.

Each document should capture one coherent reusable preference and only the
rationale and stable constraints needed to apply it. Keep project-specific
procedures, implementation plans, verification catalogs, and change history in
their owning locations instead.

## Maintaining guidance

Update guidance in place as preferences change. When guidance is replaced,
update its consumers and remove the superseded document. Preserve only useful
change rationale in a brief dated history note; Git retains exact prior content.

After changing guidance, run:

```sh
./scripts/validate-guidance
```
