---
status: accepted
---

# Rust Cores for Node.js HTTP SDKs

## Decision

When a Node.js or TypeScript project needs an external HTTP protocol
implementation already owned in Rust, keep Rust as the sole HTTP conformer and
expose it through a narrow asynchronous Node-API binding, normally using
[napi-rs](https://napi.rs/). Put an idiomatic TypeScript facade over that
binding when it improves the consumer API. Do not create a second TypeScript
HTTP implementation merely to make the Rust client convenient to call.

The OpenAPI contract remains the wire authority, and the Rust implementation
continues to own request preparation, authentication, transport policy, safety
bounds, retries, response decoding, domain translation, and sanitized failure
semantics. The binding translates project-owned inputs, outputs, and failures
across Node-API. The TypeScript facade owns naming and ordinary JavaScript
ergonomics, but no URL, header, serialization, authentication,
transport, retry, or decoding rules.

Follow
[External HTTP Contracts and Handwritten Clients](external-http-contracts-and-handwritten-clients.md)
for wire ownership and conformer verification. A Node binding and facade over
the same Rust implementation are another public boundary, not another language
conformer.

## Binding contract

Expose a small project-owned API rather than Rust internals or HTTP-library
types. Export asynchronous operations as promises without blocking the Node.js
event loop. Make cancellation, client lifetime, and cleanup explicit where the
underlying operation owns resources or may outlive its caller.

Translate expected Rust failures into stable project-owned categories with
bounded safe context. Do not expose credentials, unrestricted provider
payloads, dependency errors, or panic details. Treat a Rust panic as a defect
that must be contained at the native boundary rather than allowed to unwind
through Node.js.

Generated TypeScript declarations and platform package metadata are derived
binding artifacts. They may be packaged or committed when useful, but the Rust
binding surface is their canonical input and freshness must be verified. Apply
[Canonical Sources and Derived Artifacts](../canonical-sources-and-derived-artifacts.md)
and keep dependency types behind the boundary described in
[Boundary-Owned Contracts and Pure Cores](../boundary-owned-contracts-and-pure-cores.md).

## Packaging and verification

Node-API provides compatibility across supported Node.js versions, not one
binary for every operating system, CPU architecture, or C library. Build and
publish an explicit native target matrix, or restrict an internal package to
the targets it actually supports. Keep the TypeScript facade, generated
declarations, native binary, and Rust core version-compatible as one released
SDK surface.

Keep protocol conformance, transport, and provider-evidence tests in Rust. Also
test the packaged SDK from a clean Node.js consumer. Cover loading every
supported native target, promise behavior, stable error translation,
cancellation, cleanup, panic containment, and declaration compatibility.

## Revisit when

Use another boundary when a concrete consumer requires a browser, edge runtime,
Bun, Deno, or another environment that cannot use the chosen Node-API package;
when native binary distribution is unacceptable; or when cross-boundary
callbacks and shared state dominate the interface. If the consumer ecosystem
genuinely warrants a separate TypeScript HTTP implementation, make it an
independent handwritten conformer to the same OpenAPI contract and apply the
multi-language verification rules.
