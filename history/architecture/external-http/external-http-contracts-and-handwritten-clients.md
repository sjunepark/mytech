# External HTTP Contracts and Handwritten Clients History

## 2026-08-02

Separated Rust language selection into
[Rust for External HTTP Protocol Implementations](../../../architecture/external-http/rust-for-external-http-protocols.md)
because it can be reconsidered independently. Distilled this guidance around
OpenAPI authority, handwritten conformance, ownership, and verification without
changing those preferences.

Earlier the same day, made OpenAPI canonical for every external provider
integration, reversing a conditional Rust-authority preference. Replaced
generated clients with individually handwritten conformers. Multiple
implementations share fictional evidence, independent expectations, canonical
projections, and differential checks while retaining language-specific
transport verification.

OpenDART informed the Rust rationale and language-neutral conformance design,
but its repository-owned custom generation was intentionally not adopted as
the handwritten-client policy.

## 2026-08-01

The prior guidance had made direct Rust the authority for Rust-only
integrations and required OpenAPI to have a current independent consumer. That
decision was later reversed because language-specific code was not considered
a sufficiently clear and portable wire authority.

## 2026-07-31

Made the OpenAPI dialect project-selected rather than prescribing OpenAPI 3.1.
Added an explicit transport-policy boundary and links to the reusable command-
line and provider-qualification guidance.
