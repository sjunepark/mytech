---
status: accepted
---

# Rust Cores for Node.js Packages

## Decision

When a Node.js or TypeScript package needs a capability already implemented and
owned in Rust, keep Rust as the sole semantic implementation of that capability
and expose it through a narrow Node-API binding, normally using
[napi-rs](https://napi.rs/). Put an idiomatic TypeScript facade over that
binding when it improves the consumer API. Do not reimplement the Rust-owned
behavior in TypeScript merely to make the native core convenient to call.

Keep ownership explicit across the boundary. The Rust implementation owns the
capability's domain rules, state transitions, resource policy, safety bounds,
domain translation, and sanitized failure semantics. The binding translates
project-owned inputs, outputs, and failures across Node-API. The TypeScript
facade owns naming, ordinary JavaScript ergonomics, and genuinely
consumer-specific orchestration, but it does not become a second owner of
Rust-owned rules.

## Binding contract

Expose a small project-owned API rather than Rust internals or dependency
types. Expose potentially blocking or asynchronous operations as promises
without blocking the Node.js event loop. Make cancellation, client lifetime,
and cleanup explicit where an operation owns resources or may outlive its
caller.

Translate expected Rust failures into stable project-owned categories with
bounded safe context. Do not expose credentials, unrestricted external
payloads, dependency errors, or panic details. Treat a Rust panic as a defect
that must be contained at the native boundary rather than allowed to unwind
through Node.js.

Generated TypeScript declarations and platform package metadata are derived
binding artifacts. They may be packaged or committed when useful, but the Rust
binding surface is their canonical input and freshness must be verified. Apply
[Canonical Sources and Derived Artifacts](canonical-sources-and-derived-artifacts.md)
and keep dependency types behind the boundary described in
[Boundary-Owned Contracts and Pure Cores](boundary-owned-contracts-and-pure-cores.md).

## Packaging and verification

Node-API provides compatibility across supported Node.js versions, not one
binary for every operating system, CPU architecture, or C library. Build and
publish an explicit native target matrix, or restrict an internal package to
the targets it actually supports. Keep the TypeScript facade, generated
declarations, native binary, and Rust core version-compatible as one released
package surface.

Keep core behavior, invariants, and resource-lifecycle tests in Rust. Also test
the packaged module from a clean Node.js consumer. Cover loading every
supported native target, synchronous or promise behavior as applicable, stable
error translation, cancellation, cleanup, panic containment, and declaration
compatibility.

## Revisit when

Use another boundary when a concrete consumer requires a browser, edge runtime,
Bun, Deno, or another environment that cannot use the chosen Node-API package;
when native binary distribution is unacceptable; or when cross-boundary
callbacks and shared state dominate the interface. If consumers genuinely need
an independent TypeScript implementation, give it explicit ownership and
verification rather than silently maintaining two implementations of the same
rules.
