---
status: accepted
---

# External HTTP Contracts and Handwritten Clients

**Initial evidence:** OpenDART, DartDB, Seoro

## Decision

Give each external HTTP integration one reviewed description of its supported
wire behavior. Prefer OpenAPI for a reusable SDK, multiple independent
implementations, or a contract that needs language-neutral review and tooling.
For a small application-local adapter, executable schemas and independent
provider examples may be sufficient; a second specification must earn the
obligation to keep it synchronized.

The provider owns the external protocol. A repository-owned contract records
the subset the project supports and its evidence, including deviations from
an incomplete or inaccurate official specification. Preserve unknown facts
instead of inventing a cleaner protocol.

Prefer a maintained provider SDK when it meets the required transport, error,
and resource contract. Otherwise handwrite a narrow client in the consuming
application's language. Neither adopting an SDK nor writing a client removes
the need to qualify provider behavior.

## Ownership and generation

The wire authority owns operation identity, serialization, authentication
shape, schemas, statuses, media types, and provider failure envelopes. The
application boundary owns credentials, timeouts, retries, resource bounds,
domain translation, and sanitized project-facing failures.

Keep orchestration and the project-facing API handwritten. Allow generated
wire types, validators, or private client code when the generator faithfully
implements the supported contract and removes synchronized duplication.
Generation is a tool choice, not a second authority: pin its inputs and verify
freshness. Reject or replace it when its output leaks awkward contracts or
requires permanent patches to generated facts.

A handwritten implementation is appropriate when it is clearer or when the
protocol exceeds the generator's supported semantics. Wire changes begin in
the chosen authority and finish only when the affected implementation and
independent evidence agree.

Do not translate library types merely to rename them. Translate where the
project promises a different semantic or compatibility contract, following
[Boundary-Owned Contracts and Pure Cores](../boundary-owned-contracts-and-pure-cores.md).

## Shared implementations

A binding that delegates wire behavior to an existing core is not another
protocol implementation. The core keeps semantic and resource ownership; the
binding owns translation and consumer-language ergonomics. Use the
[Node.js](../rust-cores-for-nodejs-packages.md) or
[Python](../rust-cores-for-python-packages.md) guidance when that core is
already justified in Rust.

Independent language implementations may remain idiomatic. Share fictional
wire fixtures and independently justified expected outcomes when this reduces
real conformance risk. Compare supported request, response, and failure
semantics; do not force identical internal models or introduce a differential
harness for one implementation.

## Verification

Validate the chosen authority and test the real transport boundary, including
serialization, provider failures, timeouts, retry safety, and redaction where
applicable. Generated code cannot certify the specification that produced it;
use provider documentation, sanitized observations, and independently authored
expectations.

Apply [Verification from Source to Consumer](../../practices/verification-from-source-to-consumer.md).
Evidence and production enablement follow
[External Provider Qualification](../../practices/external-provider-qualification.md);
authority and freshness follow
[Canonical Sources and Derived Artifacts](../canonical-sources-and-derived-artifacts.md).

## Revisit when

Introduce a portable contract when a local integration acquires independent
consumers or its supported behavior becomes hard to review. Replace an SDK or
generator when concrete transport gaps or repair work outweigh the behavior it
reliably supplies. Keep one authority and independent evidence through either
change.
