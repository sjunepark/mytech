# External HTTP Contracts and Rust SDKs History

## 2026-08-02

Reversed the conditional Rust-authority preference. Every external HTTP
provider integration now keeps a canonical OpenAPI wire contract, including
Rust-only integrations. Language clients are handwritten conformers rather
than generated derivatives. A shared fictional, evidence-backed fixture corpus,
versioned canonical projections, exact expectations, cross-language
differential checks, and deterministic mutations constrain their behavior.
Each language separately proves transport safety. Handwritten project policy
remains explicit without duplicating OpenAPI-owned wire facts.

## 2026-08-01

The original guidance required project-owned OpenAPI, compilation, and
generated Rust for every external provider integration. Applying that shape to
Seoro showed that a Rust-only integration could gain extra representations and
tooling without an independent consumer for them.

The guidance now defaults to a canonical Rust protocol module for Rust-only
integrations. OpenAPI requires a current independent purpose. Once selected,
the canonical dialect must serve the named provider and tool consumers;
OpenAPI 3.2 is the default for project-authored contracts only when they support
it. A repository-owned compiler boundary, deterministic generation, and
source-to-consumer verification are required. A separate normalized model is
earned by multiple semantic generators or a demonstrated generator gap rather
than by OpenAPI alone. Custom implementation and cross-project sharing remain
separate decisions. The protocol module, evidence, safety, and verification
principles remain unchanged.

## 2026-07-31

Made the OpenAPI dialect project-selected rather than prescribing OpenAPI 3.1;
the initial adopters use different supported dialects. Added an explicit
transport-policy boundary and links to the distilled CLI and provider
qualification guidance after the broader repository scan. Generalized contract
ownership and compiler extraction, and removed adopter-specific profiles so
source repositories remain non-normative evidence.
