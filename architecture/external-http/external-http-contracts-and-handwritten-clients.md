---
status: accepted
---

# External HTTP Contracts and Handwritten Clients

**Initial evidence:** OpenDART, DartDB, Seoro

## Decision

For every external HTTP provider integration, keep or create an OpenAPI
contract as the sole repository authority for the supported wire behavior,
even when only one language implements it.

Handwrite each language implementation as a conformer to OpenAPI. Do not
generate client code, wire types, validators, request builders, or response
decoders from the contract. The implementation may repeat wire facts in types
and code as necessary, but a wire change begins in OpenAPI and is complete only
when every applicable conformer agrees.

The provider owns the external protocol. The repository-owned OpenAPI contract
is the reviewed representation of the subset the project supports. Official
specifications and bounded observations are evidence for that representation,
not competing repository contracts.

## Ownership

OpenAPI owns supported operations, parameter and body serialization,
authentication shape, wire schemas, statuses, media types, provider failure
envelopes, and the supported dialect and extensions.

Handwritten code owns its project-facing interface, private conforming types
and validators, pure request preparation and response decoding, credentials,
transport policy, safety bounds, domain translation, and presentation. It does
not need to parse OpenAPI at runtime.

Give each rule one semantic owner. Do not add a language-owned manifest,
fixture set, or model that becomes a parallel authority for OpenAPI-owned
facts. Keep provider-native wire types and dependency failures behind the
project-owned protocol boundary described in
[Boundary-Owned Contracts and Pure Cores](../boundary-owned-contracts-and-pure-cores.md).

A language binding or facade that delegates all wire behavior to an existing
conformer is not another language implementation. The conformer continues to
own request preparation, authentication, transport policy, safety bounds,
retries, response decoding, domain translation, and sanitized failure
semantics; the binding and facade own boundary translation and
consumer-language ergonomics, not wire behavior.
For the preferred Node.js or Python binding shape over a Rust conformer, follow
[Rust Cores for Node.js Packages](../rust-cores-for-nodejs-packages.md) or
[Rust Cores for Python Packages](../rust-cores-for-python-packages.md).

## Verification

Every project validates the OpenAPI source and supported profile, checks its
handwritten implementation against independent provider evidence, and tests
the real language transport at an appropriate boundary.

A single-language project uses proportionate project-native tests; it does not
need a cross-language fixture or projection harness. When multiple languages
implement the same contract, use one fictional shared fixture corpus and
independent expected results. Each conformer emits a minimal, deterministic,
credential-free projection of prepared requests, decoded outcomes, and stable
failure categories. Verify each projection against the independent expectation
and compare conformers exactly. Public APIs and internal structures may remain
idiomatic to their languages.

Apply the broader verification portfolio in
[Verification from Source to Consumer](../../practices/verification-from-source-to-consumer.md).
Provider evidence and production enablement follow
[External Provider Qualification](../../practices/external-provider-qualification.md),
and general source ownership follows
[Canonical Sources and Derived Artifacts](../canonical-sources-and-derived-artifacts.md).

## Revisit when

Reconsider the mechanism when OpenAPI cannot represent the supported protocol
truthfully or handwritten conformers cannot be maintained reliably. Preserve a
language-neutral wire authority, independent evidence, and language-specific
transport verification while evaluating an alternative.
