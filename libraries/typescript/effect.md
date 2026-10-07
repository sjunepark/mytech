---
status: accepted
---

# Effect for TypeScript Application Runtimes

**Initial evidence:** implemented in Creo and Unslide; accepted target in Seoro

## Decision

Use Effect as the default internal runtime model for TypeScript applications
whose owned behavior includes asynchronous orchestration, typed expected
failures, resource lifetimes, cancellation, dependency provisioning, and
structured operational evidence.

Use ordinary TypeScript representations for pure domain transformations, small
synchronous modules, framework presentation state, serialized data, and public
API surfaces. A small script without a meaningful resource or error model does
not need an Effect runtime.

## Runtime and public boundary

Compose one runtime for each application or process boundary. Provide shared
resources such as database pools, browser managers, configuration, and provider
clients through that composition root. Generate environment configuration from
the [Varlock contract](../../practices/varlock-environment-contracts.md) rather
than declaring it again in `Config`.

Run Effect programs at established application edges, such as request, desktop,
command-line, worker, or Promise-returning adapters. Do not scatter `runPromise`
or `runSync` through service and domain code; hidden runtimes lose shared
resource ownership, interruption, and logging context.

Keep Effect types internal. Translate them into project-owned framework,
serialization, process, and public API contracts at the relevant edge. Follow
[Boundary-Owned Contracts and Pure Cores](../../architecture/boundary-owned-contracts-and-pure-cores.md)
for the general boundary rules.

## Services and layers

Service values should expose Effect-returning operations with their expected
error types. Acquire implementation dependencies while constructing the live
service and provide layers at the owning runtime boundary.

Create services for genuine capabilities, shared resources, or proven alternate
implementations. A dependency with one simple use does not automatically need
a service and layer.

Use scopes for resources whose cleanup must survive failure or interruption.
Preserve the primary failure when cleanup also fails, while retaining cleanup
diagnostics or recovery evidence.

## Errors, schemas, and logging

Model expected failures as small tagged project-owned types. Wrap unknown
dependency failures at their adapter boundary and reserve defects for violated
invariants.

Use Effect Schema, or an already authoritative external schema, when data
crosses persistence, IPC, HTTP, configuration, or another trust boundary.
Do not create a parallel validation authority merely to express the same rules
inside Effect.

Use Effect logging, annotations, and spans inside the runtime so context and
redaction policy compose. Translate logs at the process boundary. Structured
stdout, public result envelopes, and serialized protocols remain separate
contracts.

Pin prerelease runtime-family packages to a compatible exact tuple. Upgrade
deliberately and renew integration, lifecycle, interruption, and clean-consumer
evidence. Relax exact pins for stable releases only when compatibility and
lockfile policy keep upgrades explicit. Keep unstable Effect APIs behind narrow
infrastructure adapters.

## Revisit when

Reconsider Effect when the application no longer owns meaningful asynchronous
lifecycles or typed operational failures, or when its boundary translations and
runtime model cost more than the complexity they remove. Use Effect to remove
durable lifecycle and orchestration complexity, not to make every function share
one return type or to preserve consistency with another project.
