---
status: accepted
---

# Rust for External HTTP Protocol Implementations

**Initial evidence:** OpenDART, Seoro

## Decision

Prefer Rust for a new external HTTP protocol implementation or SDK when no
consumer ecosystem, target platform, runtime, deployment, or organizational
constraint favors another language.

Rust is a useful default because its types can distinguish protocol and
capability states, constrain credential-bearing values, and express sanitized
failures while keeping transport behavior explicit. These advantages favor
correctness, reviewability, and maintainability; they do not make Rust
universally appropriate.

Choose the language separately for each role. This preference applies to the
protocol implementation, not to OpenAPI maintenance tools, documentation
pipelines, applications, or every consumer of the protocol. Contract authority
and client conformance follow
[External HTTP Contracts and Handwritten Clients](external-http-contracts-and-handwritten-clients.md).

When a Node.js or Python project consumes the Rust implementation, follow the
corresponding binding guidance:

- [Rust Cores for Node.js Packages](../rust-cores-for-nodejs-packages.md)
- [Rust Cores for Python Packages](../rust-cores-for-python-packages.md)

## Revisit when

Prefer another language when its ecosystem, platform support, runtime
integration, deployment model, or team ownership materially improves the
protocol's use and maintenance.
