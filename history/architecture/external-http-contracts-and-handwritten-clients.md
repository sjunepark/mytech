# External HTTP Contracts and Handwritten Clients History

## 2026-08-02

Consolidated the overlapping language-neutral and Rust-specific guidance into
one policy. OpenAPI remains the canonical wire contract even with one language
because implementation types and runtime behavior do not state the complete,
portable HTTP contract clearly enough. Each language implementation is now
individually handwritten; client generation, including repository-owned custom
emitters, is deliberately excluded.

Rust is the default when no consumer ecosystem, platform, runtime, deployment,
or organizational constraint favors another language. The preference is based
on type-enforced protocol and capability states, explicit transport behavior,
and typed sanitized failures. It does not prescribe Rust for OpenAPI tooling or
all consumers. Multiple implementations share fixtures, independent expected
projections, and differential checks while retaining idiomatic public APIs and
language-specific transport verification.

Earlier the same day, the guidance reversed a conditional Rust-authority
preference and made OpenAPI canonical for every external provider integration.
It replaced generated clients with conforming implementations verified through
shared fictional evidence, versioned projections, independent expectations,
differential comparison, deterministic mutations, and per-language transport
tests.

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
