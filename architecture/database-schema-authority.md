---
status: accepted
---

# Database Schema Authority

**Initial evidence:** implemented in Creo; accepted target in Seoro

## Decision

Use one database-change system as the authority for every project-owned database object.
Typed query mappings, generated snapshots, and language-specific clients are
consumers of that authority, not alternate schema definitions.

For PostgreSQL projects with meaningful database-owned behavior, prefer an
explicit SQL migration system such as Sqitch. It should own tables, constraints,
indexes, extensions, roles, grants, functions, triggers, and data migrations.

## Roles

Keep these roles distinct:

- **Schema history** expresses ordered changes and dependencies.
- **Deploy and verification SQL** applies and proves each change.
- **Revert SQL** supports development and recovery where reversal is safe.
- **Generated schema snapshots** provide review and inspection output.
- **Runtime mappings** expose only the objects and types an application needs.
- **Generated query clients** provide typed access for another language or
  process.

Do not edit generated snapshots by hand. Do not let an ORM migration generator,
runtime startup hook, or introspected mapping become a second database-change
path.

## Runtime mappings

An ORM or query layer is a typed access mechanism. Curate its mapping to the
runtime's needs rather than pretending it completely represents database
semantics.

Database features such as roles, grants, triggers, specialized constraints,
extensions, and functions often exceed an ORM's model. Verify them at the
database boundary. If introspection is useful, run it against a fresh database
created from the complete migration plan and treat its output as audit evidence.

Polyglot consumers may use different mappings, such as an Effect-aware
TypeScript query layer and generated Go queries. They share database contracts
and identities, not a migration implementation.

## Privileges and lifecycle

Schema-owner and migration credentials belong to controlled operator or
deployment paths. Application runtimes receive only the operations they need.
Prefer narrow function execution or relation privileges over broad ownership.

Do not migrate automatically during ordinary application startup. Deployment
should apply and verify schema changes before a runtime depends on them.

When old and new runtimes coexist, expand the schema compatibly, migrate or
backfill data, move consumers, and only then remove the old contract. Deployment
ordering alone does not make a destructive migration safe. Define the supported
rollback window; prefer a forward repair when reverting would discard data or
break a still-supported consumer. Provider-managed objects remain under their
provider's ownership.

Direct client access changes the security boundary. If a browser, mobile
client, PostgREST-style interface, or other untrusted caller gains table access,
database authorization such as tested row-level security becomes a prerequisite.
Server-only access does not remove the need for application authorization or
least-privilege runtime roles.

## Verification

Test database-dependent behavior against the real engine and required
extensions. Mocks cannot establish transaction behavior, locking, error
classification, role grants, spatial behavior, or database constraints.

A complete database gate should cover the applicable parts of:

- deploy and verify from an empty database;
- supported revert and redeploy paths;
- least-privilege runtime access;
- runtime mapping and codec compatibility;
- functions, triggers, and specialized constraints;
- interruption and transaction behavior; and
- backup and restore for systems that rely on them.

Use isolated, disposable databases for tests and preserve ordinary development
data by default.

## Revisit when

A simpler migration tool is sufficient when the database contains only
portable tables and ordinary constraints. Reconsider the chosen authority when
it cannot express or independently verify the database behavior the project
actually relies on—not merely because another framework offers a convenient
second migration path.
