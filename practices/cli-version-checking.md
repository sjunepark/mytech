---
status: accepted
---

# CLI Version Checking

**Initial evidence:** sjskills (agent-scripts)

## Decision

Prefer automatic, cached version advisories after successful CLI operations,
including agent, CI, and other noninteractive use. Those callers are often the
tool's primary users and should receive useful update evidence. Bound refresh
work within a documented latency budget, provide an explicit opt-out, preserve
primary command success and structured output, and never install automatically.

Provide an explicit status or version-check operation for callers that want a
report even when no update is available. Keep help, exact version output, and
other contract-only discovery local and free of status checks. Skip incidental
checks after invalid or failed invocations and cancellation.

## Release comparison

Compare the running executable's embedded version with the highest published
stable version for that tool in its authoritative release channel. Use the
tool's version ordering, not lexical sorting, publication order, or branch
freshness. Exclude drafts, prereleases, and unrelated product tags from the
stable comparison. Report uncomparable development identities explicitly.

Version equality establishes neither source-commit freshness nor executable
integrity. Keep version identity consistent across the executable, release tag,
and artifacts. The release and installation contract belongs to
[Standalone CLI Distribution](standalone-cli-distribution.md).

Before presenting an update as installable, check that the selected release has
the assets required by the current platform and supported installation method.
Report incomplete distribution explicitly rather than silently falling back to
an older release. Metadata availability does not verify archive bytes;
installation still performs its own verification. Link to the exact release
and recommend the owning installation method, including the package manager
when it owns the installation.

## Evidence and refresh cost

Cache remote release evidence and its observation time, then compare it with
the currently running version on each check. Replacing an executable
should immediately change the comparison without waiting for cache expiry.
Reuse evidence across working directories when the tool, release channel, and
target match; keep the cache disposable and separate from installation state.

Represent comparison and freshness separately. Distinguish newer, equal, and
ahead versions, confirmed absence of a stable release, uncomparable identity,
incomplete distribution, and unavailable evidence. On refresh failure, retain
usable prior evidence with a visible stale label and observation age. Without
usable evidence, report uncertainty rather than claiming the tool is current.

Use a documented refresh interval and failure retry cooldown. Bound requests,
response sizes, pagination, and lock waits within one cancellable refresh
budget shared by any concurrent ancillary checks. Incomplete lookups and cache
failures remain advisory. Public release checks should not require credentials,
a source checkout, or development tools.

Choose timings for the tool's invocation frequency and latency needs; no fixed
duration is a universal default. A foreground refresh may extend process
completion, including delivery of a complete JSON response. Make that cost
explicit. The opt-out skips ancillary inspection, fetching, and cache work;
it does not disable verification required by the primary operation.

## Output and authority

Explicit reports show the comparison and freshness even when there is no
update. Incidental notices stay quiet for fresh equal, ahead, or no-release
results; updates, stale evidence, and inspection problems remain visible.
Human incidental notices belong on stderr. Machine-readable advisories belong
in the command's single structured response, separate from its primary result,
under the [automation contract](automation-facing-cli-contracts.md).

An advisory failure must not change primary command success. Version evidence
does not grant installation or other mutation authority.

## Revisit when

Revisit automatic refresh behavior when command frequency, latency targets,
offline operation, or network restrictions make its cost inappropriate.
Revisit release selection when the tool deliberately supports prerelease
channels or maintained version lines. Document those project-specific choices
without treating an update notice as a requirement to add self-upgrade.
