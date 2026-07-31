# External HTTP Contracts and Rust SDKs History

## 2026-08-01

The original guidance required project-owned OpenAPI, compilation, and
generated Rust for every external provider integration. Applying that shape to
Seoro showed that a Rust-only integration could gain extra representations and
tooling without an independent consumer for them.

The guidance now defaults to a canonical Rust protocol module for Rust-only
integrations. OpenAPI requires a current independent purpose, and generation,
custom compilation, and shared compilation are earned separately. The protocol
module, evidence, safety, and verification principles remain unchanged.

## 2026-07-31

Made the OpenAPI dialect project-selected rather than prescribing OpenAPI 3.1;
the initial adopters use different supported dialects. Added an explicit
transport-policy boundary and links to the distilled CLI and provider
qualification guidance after the broader repository scan. Generalized contract
ownership and compiler extraction, and removed adopter-specific profiles so
source repositories remain non-normative evidence.
