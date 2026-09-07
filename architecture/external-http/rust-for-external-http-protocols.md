---
status: accepted
---

# Rust for External HTTP Protocol Implementations

**Initial evidence:** OpenDART, Seoro

## Decision

Start an application-specific HTTP adapter in the consuming application's
language. Network I/O alone does not justify a second runtime, native bindings,
or a new distribution matrix.

Prefer Rust for an independently owned protocol core when concrete consumers
benefit from sharing that implementation, when a standalone native artifact is
required, or when demonstrated parsing, resource-control, or performance needs
justify it. Rust remains a strong choice for such a core: explicit ownership
and types help express protocol states and constrain credential-bearing data.
Those benefits must survive the consumer and packaging boundary.

Consider the whole lifecycle: cancellation, diagnostics, build targets,
installation, releases, and maintainer ownership. Prefer one implementation
when it reduces total obligations; two thin idiomatic adapters may be simpler
than maintaining a native bridge for a trivial protocol.

Choose language separately from contract authority. Follow
[External HTTP Contracts and Handwritten Clients](external-http-contracts-and-handwritten-clients.md)
for the wire contract and verification, and the
[Node.js](../rust-cores-for-nodejs-packages.md) or
[Python](../rust-cores-for-python-packages.md) binding guidance for an already
justified Rust core.

## Revisit when

Extract a shared core when duplicated behavior or measured resource needs make
the native boundary worthwhile. Reconsider it when platform support, callback
coordination, release work, or consumer friction exceeds the complexity it
removes. Language preference alone is not a migration reason.
