# Technology Preferences Review

Assessment dated 2026-09-05. This is a review snapshot, not another source of
accepted guidance. The [README](../README.md) routes to the owning decisions.
Scope covered all active guidance, drafts, references, and repository scripts;
history was consulted where an intentional preference reversal mattered.

## Overall opinion

The strongest part of these preferences is the emphasis on ownership and
observable behavior. Pure cores, explicit errors, durable intent, real database
tests, and clean-consumer verification reinforce each other. The SvelteKit
modular monolith is consistent with that approach.

Some defaults extended those principles into requirements for additional
mechanisms: a separate specification for every integration, handwritten
repetitions of wire facts, a preference that could lead simple clients toward
native packaging, and a self-updater for every distributed CLI. Those choices
can make a system locally explicit while increasing the contracts maintainers
must coordinate.

My recommendation is to keep the strong boundaries and raise the threshold
for additional machinery. Build targets, upgrade coupling, and failure modes
remain long-term obligations even when initial development time is secondary.
The revisions apply that principle while retaining the preferred application
stack.

## Assessment by preference

| Area | Opinion and resulting guidance |
| --- | --- |
| SvelteKit, Svelte, PostgreSQL | Keep the conditional modular-monolith default. A second transport or service should have a real consumer or operating boundary. Nothing in this repository establishes a reason to switch frameworks. |
| Effect | Keep it for substantial asynchronous orchestration and resource lifetimes. Its value falls when most code merely wraps simple promises or pure transformations. Choose the runtime for the application, then its compatible CLI; parser preference should not force a runtime migration. |
| Rust | Strong for an already justified core and native artifact. Consumer-language adapters are the starting point for application-local HTTP. Count bindings, cancellation, platform builds, and release coupling as part of the design. |
| HTTP authority | Keep portable contracts for reusable SDKs. Drop the blanket ban on generation: generated wire facts can reduce drift, while handwritten boundaries retain project semantics. Small integrations need independent evidence, not necessarily another schema file. |
| Database authority | Keep one project-owned migration path, least privilege, and real-engine evidence. SQL-first tools are justified when the database owns meaningful behavior; they need not be mandatory for ordinary tables. Added coexistence and irreversible-migration constraints. |
| External effects | Keep admitted operations and transactional outboxes. Local durability cannot establish an unknown provider outcome. Added discoverable unfinished state, explicit uncertainty, and safe retry conditions. |
| Go and CLI parsers | Kong, clap, and Commander are reasonable scoped choices; no evidence here warrants replacing them for fashion. A new Go executable still needs a deployment or ownership reason beyond a generally attractive language. |
| CLI distribution and CI | Keep actual release-artifact testing. Make self-upgrade optional and installers audience-specific. Linux remains the routine CI default, with affected-platform tests when the change itself warrants them. |
| PDF ingestion | Keep paired source PDF and Markdown, selective OCR, and independent parser comparison. Xberg is an initial candidate, not a demonstrated universal quality winner. Corpus failures should decide escalation and switching. |
| Documentation | Keep one owner per decision and distinguish selected, proposed, observed, and delivered states. Improve routing and remove unsupported precision from research instead of adding more categories. |
| Rewrites | Replace structure when it prevents a required improvement. Own the preserved contracts, evidence, and cutover criteria locally; use external migration methods as supporting material. |

## Drafts worth retaining

These are unresolved scope decisions, not deficiencies that prevent completing
this review. None needs a universal answer before a project has the relevant
requirements.

- **Local JSON:** a strong fit for portable authored documents with one writer.
  Relational operational state should evaluate SQLite early. Atomic visibility
  and crash durability are separate guarantees.
- **Desktop authorization:** retain channel separation and credential handling,
  but evaluate a provider-supported standard flow before a custom protocol.
- **Local tool packages:** static validation and a supervised process do not
  enforce an execution sandbox. Resolve package trust and enforceable platform
  capabilities before making third-party execution a promise.
- **Desktop stack:** keep privileged operations outside the renderer. Select
  Electron against native integration, accessibility, resource, and delivery
  requirements independently of the renderer library.
- **Go tooling:** use an independently deployed role or concrete operational
  needs to justify another language boundary.
- **Node, Bun, pnpm:** distinguish runtime compatibility from installation and
  development commands. An extra tool earns its place through measured benefit;
  public consumers need validation in the runtime actually promised to them.

One well-understood project can justify a narrow preference. Project count
alone is neither promotion evidence nor a reason to keep a decision uncertain.

## Bucket I — Safe fixes applied

- The lifecycle query now exposes accepted documents incorrectly placed under
  `draft/`. It shares placement rules with validation, and regression tests
  exercise the public process behavior.
- Xberg examples now convert into unique candidates and publish without
  clobbering an existing destination. Source-backed flag verification is
  explicitly separated from execution and corpus-quality claims.
- Native-package guidance no longer promises recovery from aborting panics,
  and artifact verification no longer demands byte-identical regeneration of
  lossy projections.
- The README exposes every accepted topic and documents the actual lifecycle
  schema and tools. Research notes retain evidence and limitations rather than
  current-looking rankings, prices, or unsupported test precision.

## Bucket II — Needs decision

None required to complete this review. The substantive preference revisions in
the assessment table were applied under the requested free-rewrite scope.
The drafts remain non-authoritative choices for projects with the corresponding
requirements; they do not block these revisions.

## Validation and limits

The repository gate passed lifecycle validation, script regressions, Markdown,
and relative-link checks. Independent review found one retry-wording ambiguity;
it was corrected so confirmed provider success leads to local finalization
without another call. No other material findings remained. The revised shell
examples were exercised with a controlled Xberg stub for failed, empty, and
successful extraction and for publication
against new paths, existing files, symlinks, and directories.

Effect package organization was checked through Context7 and its upstream
migration guide. Xberg v1.0.14 flags and Korean model routing, installation
instructions, migration-kit scope, and Rust panic-containment limits were
checked against primary sources linked in the owning documents.

No Xberg engine or new OCR corpus benchmark ran in this review. No consuming
application was inspected, so initial-evidence project names remain provenance
rather than renewed implementation claims. Dated desktop observations were
condensed without inspecting a new app build. There is no configured repository
CI gate; validation remains locally invoked.
