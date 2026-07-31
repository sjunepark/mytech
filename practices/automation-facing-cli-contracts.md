# Automation-Facing CLI Contracts

**Status:** Accepted  
**Initial evidence:** OpenDART, Seoro, Unslide

## Decision

Treat a command-line interface used by agents or automation as a versioned
process API. Its arguments, stdout, stderr, artifacts, and exit statuses are
one compatibility surface.

Human-readable help remains important, but automation must not scrape
presentation text to understand success, failure, or available operations.

## Process contract

Each explicitly machine-readable invocation should produce at most one complete
structured stdout document, terminated by a newline. Plain-text help and
version output may remain separate human-facing surfaces.

The machine contract defines how compatibility relates to the executable
version. Its result envelope includes, as applicable:

- a contract version or another unambiguous version relationship;
- a stable success or failure discriminant;
- operation or command identity;
- typed result or structured error data;
- warnings and bounded diagnostics where applicable; and
- direct artifact paths, hashes, or byte facts when files are produced.

JSON is the default interoperable choice. Alternate encodings may share one
semantic result model, but each enlarges the wire compatibility surface and
requires a concrete consumer benefit.

Logs and progress belong on stderr and are disabled or explicitly selected when
quiet machine operation is the default. A library logger must never contaminate
structured stdout.

Define a small stable exit-status taxonomy for success, valid execution
failure, and invalid invocation. More statuses are warranted only when callers
need distinct shell-level control flow.

## Discovery and preparation

Provide keyless, side-effect-free commands for:

- top-level orientation and version information;
- operation or capability listing;
- detailed parameter and output discovery; and
- validating configuration or a proposed invocation.

Discovery should use the same canonical model as execution rather than a
handwritten inventory.

Perform lexical parsing, structural validation, path checks, operation lookup,
and policy preflight before acquiring credentials, starting runtimes, opening
files for replacement, or making network requests.

A command that only describes a contract should not possess network,
credential, filesystem-write, or subprocess capabilities.

## Errors and diagnostics

Errors expose stable project-owned categories and safe structured context.
Human messages help diagnosis but are not identifiers.

Bound:

- diagnostic entries and message sizes;
- captured stdout and stderr from child processes;
- response and artifact bytes;
- timeouts and attempts; and
- lists returned by discovery.

Never echo credentials, authenticated URLs, unrestricted external payloads, or
rejected secret-bearing values. Full diagnostics should require an explicit,
documented option and remain subject to redaction.

## Artifacts

Binary or large output should use an explicit destination instead of sharing a
structured stdout channel. Default to no-clobber behavior and publish through
staging plus atomic replacement when replacement is allowed.

Return the resolved path and integrity facts directly. Do not make callers
reconstruct paths by parsing configuration or combining unrelated fields.

If a composed command publishes several artifacts independently, report which
steps completed and which prior artifacts remain valid. Do not claim a global
transaction that the implementation cannot provide.

## Ownership

Reuse public application or SDK types when they already own operation semantics.
The CLI should add process evidence and presentation, not mirror every request,
response, validation rule, or error in a second model.

Generated command breadth is appropriate when it follows a canonical contract.
Keep orchestration and stable process envelopes handwritten.

## Verification

Test the CLI as an external process:

- exact stdout document count and newline behavior;
- empty or explicitly structured stderr;
- exit statuses;
- discovery without credentials or side effects;
- malformed and oversized input;
- secret redaction;
- no-clobber and partial-publication behavior; and
- installation from the actual packaged artifact.

## Revisit when

Add interactive modes, alternate encodings, field selection, or streaming only
for a concrete consumer. Each changes the process contract and should not be
introduced as speculative agent ergonomics.
