---
status: accepted
---

# Automation-Facing CLI Contracts

**Initial evidence:** OpenDART, Seoro, Unslide

## Decision

Treat a command-line interface used by agents or automation as a versioned
process API. Its arguments, stdout, stderr, artifacts, and exit statuses are
one compatibility surface.

Human-readable help remains important, but automation must not scrape
presentation text to understand success, failure, or available operations.

## Process contract

Each explicitly machine-readable invocation should emit at most one complete,
newline-terminated structured stdout document. JSON is the default
interoperable encoding; plain-text help and version output may remain separate
human-facing surfaces.

Define how the machine contract relates to the executable version. As
applicable, its result envelope carries a stable success or failure
discriminant, operation identity, typed result or structured error, bounded
warnings or diagnostics, and direct artifact evidence.

Logs and progress belong on stderr and are disabled or explicitly selected for
quiet machine operation; follow [CLI Progress Reporting](cli-progress-reporting.md)
for human progress. Library logging must never contaminate structured stdout.
An alternate encoding requires a concrete consumer because it enlarges the
compatibility surface.

Define a small stable exit-status taxonomy for success, valid execution
failure, and invalid invocation. More statuses are warranted only when callers
need distinct shell-level control flow.

## Discovery and preparation

Provide keyless, side-effect-free help and version output. Add machine-readable
operation discovery and proposed-invocation validation when automation needs
them. Derive descriptions from the execution model when command breadth makes
a handwritten inventory drift-prone; a small CLI does not need a discovery
framework simply because an agent may invoke it.

Perform lexical parsing, structural validation, path checks, operation lookup,
and policy preflight before acquiring credentials, starting runtimes, opening
files for replacement, or making network requests.

A command that only describes a contract must not resolve credentials, mutate
files, or contact a service. Keep initialization outside this path; capability
isolation is useful when the application's trust model requires it.

## Safety and artifacts

Errors expose stable project-owned categories and safe structured context.
Human messages help diagnosis but are not identifiers.

Bound diagnostic count and size, captured child output, response and artifact
bytes, time and attempts, and discovery result sizes.

Never echo credentials, authenticated URLs, unrestricted external payloads, or
rejected secret-bearing values. Full diagnostics should require an explicit,
documented option and remain subject to redaction.

Binary or large output uses an explicit destination rather than structured
stdout. Default to no-clobber behavior unless replacement is explicitly
allowed. Return the resolved path and integrity facts directly, and report
partial publication truthfully. Follow
[Canonical Sources and Derived Artifacts](../architecture/canonical-sources-and-derived-artifacts.md)
for candidate validation, recoverable replacement, and recovery.

## Ownership

Follow
[Boundary-Owned Contracts and Pure Cores](../architecture/boundary-owned-contracts-and-pure-cores.md)
for application and dependency ownership. The CLI adds process evidence and
presentation rather than mirroring the application model.

Generated command breadth is appropriate when it follows a canonical contract.
Keep orchestration and stable process envelopes handwritten.

## Verification

Apply [Verification from Source to Consumer](verification-from-source-to-consumer.md)
and test the packaged executable as an external process. Assert stdout document
and newline behavior, stderr policy, exit statuses, side-effect-free discovery,
malformed and oversized input, redaction, and artifact publication.

## Revisit when

Add interactive modes, alternate encodings, field selection, or streaming only
for a concrete consumer. Each changes the process contract and should not be
introduced as speculative agent ergonomics.
