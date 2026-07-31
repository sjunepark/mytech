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

Effect is not the default representation for pure domain transformations,
framework presentation state, serialized data, or public library APIs.

## Runtime boundary

Compose one runtime for each application or process boundary. Provide shared
resources such as database pools, browser managers, configuration, and provider
clients through that composition root.

Run Effect programs at established edges:

- a server request adapter;
- a desktop main-process handler;
- a command-line entry point;
- a worker entry point; or
- a public Promise-returning adapter.

Do not scatter `runPromise` or `runSync` through service and domain code. That
creates hidden runtimes, loses shared resource ownership, and breaks
interruption and logging context.

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

## Keep Effect internal

Do not expose Effect types merely because the implementation uses Effect.
Translate at:

- SvelteKit load, action, hook, endpoint, and serialization boundaries;
- public React or library entry points;
- browser-evaluated code that must remain self-contained;
- JSON Schema or other published configuration contracts; and
- process output and exit-status contracts.

This keeps the application model consistent without forcing every consumer,
framework, or persisted format to adopt the same runtime.

## Version policy

Pin prerelease runtime-family packages to a compatible exact tuple. Upgrade
them deliberately and rerun integration, lifecycle, interruption, and
clean-consumer gates. Keep unstable APIs behind narrow infrastructure adapters.

Once the selected release line is stable, exact pins may be relaxed only when
the project's compatibility and lockfile policy still makes upgrades explicit.

## When not to use

Prefer ordinary TypeScript for pure calculations, immutable transformations,
small synchronous modules, and framework-local UI state. A small script with no
meaningful resource or error model does not need an Effect runtime.

Use Effect because it removes durable lifecycle and orchestration complexity,
not to make every function share one return type.

## Revisit when

Reconsider Effect when the application no longer owns meaningful asynchronous
lifecycles or typed operational failures, or when its boundary translations and
runtime model cost more than the complexity they remove. Do not retain it only
for consistency with another project.
