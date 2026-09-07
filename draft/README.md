# Draft Guidance

Documents in this directory are plausible interpretations of the owner's
preferences that need explicit review.

They are not defaults, must not be cited as accepted guidance, and should not
constrain another project. Each draft records why the interpretation is
uncertain and the questions that decide whether it should be promoted, revised,
or removed.

One well-understood use can justify a narrow preference. Promotion depends on
clear applicability, tradeoffs, and evidence, not a minimum project count.
These drafts remain proposals because their role or operating guarantees need
resolution; the repository-wide review does not make them universal defaults.

## Drafts

### Architecture

- [Desktop Device Authorization](architecture/desktop-device-authorization.md)
- [Safe Local Tool Packages](architecture/safe-local-tool-packages.md)

### Practices

- [JSON-First Local Application State](practices/json-first-local-state.md)

### Stacks

- [Electron, Svelte, and Effect for Desktop Applications](stacks/electron-svelte-effect.md)
- [Go for Operational Services and Repository Tooling](stacks/go-operational-services-and-tooling.md)
- [TypeScript Runtime and Package Management](stacks/typescript-runtime-and-package-management.md)

When a draft is accepted, move the distilled decision into the appropriate
active area and remove the review questions. Record meaningful preference-change
rationale under `history/`; Git retains the exact draft text.
