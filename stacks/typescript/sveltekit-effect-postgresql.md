# SvelteKit, Effect, and PostgreSQL

**Status:** Accepted  
**Initial evidence:** implemented in Creo; accepted target in Seoro

## Decision

For a server-rendered TypeScript product with one primary web client and
substantial application-owned policy, prefer:

- SvelteKit for HTTP, routing, server rendering, forms, sessions, and web
  delivery;
- Svelte for presentation and interaction state;
- Effect for server-side application orchestration and resources; and
- PostgreSQL for durable domain state and transactional policy.

Keep this as a modular monolith until an independent client, deployment,
security boundary, or scaling requirement earns a separate transport or
service.

## Integration shape

```text
SvelteKit routes, hooks, actions, endpoints
                    |
              thin adapters
                    |
                    v
       Effect application modules
       policy, orchestration, errors
                    |
          narrow persistence ports
                    |
                    v
              PostgreSQL
```

SvelteKit owns web semantics. Effect values never cross its serialization
boundary, and presentation state remains idiomatic Svelte.

Application modules own domain policy and call each other through in-process
interfaces. One process-scoped Effect runtime owns shared resources, while
request context and cancellation enter per invocation. PostgreSQL access stays
behind narrow application-owned persistence operations.

PostGIS, `pg_trgm`, and other extensions are conditional capabilities, not
baseline requirements. Add them only when spatial or search requirements make
the database the simplest authoritative home for that behavior.

## Transport boundary

Do not add an internal HTTP API between the only web client and its application
modules. Add a versioned client-independent transport when a concrete feature
or second client needs it.

A separately deployable worker may share PostgreSQL contracts and canonical
identities without sharing implementation code or calling the web process.
Do not create an internal service solely because the worker uses another
language.

## Deployment choices

Hosting provider, region, object storage, authentication provider, email
provider, and package-manager choice remain project decisions. They should not
be baked into the application core.

## Related guidance

- [Boundary-Owned Contracts and Pure Cores](../../architecture/boundary-owned-contracts-and-pure-cores.md)
  defines the framework and application seam.
- [Effect for TypeScript Application Runtimes](../../libraries/typescript/effect.md)
  defines runtime, service, resource, and error ownership.
- [Database Schema Authority](../../architecture/database-schema-authority.md)
  defines schema and runtime-mapping ownership.
- [Verification from Source to Consumer](../../practices/verification-from-source-to-consumer.md)
  defines the real-browser and real-database testing portfolio.

## Revisit when

Split the monolith when independently deployable ownership produces a concrete
benefit that outweighs the network, consistency, authorization, and operational
boundary it introduces. A possible future native client is not sufficient on
its own; define the transport when that client or a feature-specific contract
is committed.
