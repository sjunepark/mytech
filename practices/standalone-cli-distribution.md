---
status: accepted
---

# Standalone CLI Distribution

**Initial evidence:** YTM

## Decision

For a public standalone CLI used across machines, prefer immutable GitHub
Releases as the canonical artifact source. The owner's machines and outside
users should exercise the same supported installation path. A source checkout
is a development path rather than the ordinary installation contract.

Each tool owns its operating-system and architecture matrix. Publish only
prebuilt targets that it claims and verifies. A private tool should use a
suitable private artifact channel without making its source or binaries public.

## Release and installation

Assign one owner to each transition through version preparation, tagging,
certification, and publication as one coherent release process, even when
different tools perform them. Gate publication on successful verification of
the exact release artifacts for every claimed target; historical evidence does
not certify a new release. Apply the [verification requirements](#verification)
at the artifact and supported installation boundaries.

A release is complete only when consumers can retrieve durable versioned
archives and SHA-256 checksums through the supported public or private channel
and install the exact verified artifacts for every claimed target. Temporary
CI artifacts alone do not establish delivery. Failed or partial publication
must have an explicit recovery owner and report the remaining state; recovery
preserves published tags and assets, with corrections using a new version.

Build versioned archives in CI from tagged source and publish SHA-256 checksums.
Choose installers for the supported audience: a shell installer for Unix-like
targets, PowerShell for Windows, or a package-manager path when that is the
consumer's expected lifecycle owner. Generate target selection and asset names
from one tool-owned definition.

A direct installer downloads the compatible archive and verifies it without
requiring a language toolchain, source checkout, or GitHub CLI. Published tags
and assets remain immutable; corrections use a new version. Package-manager
and language-registry distributions consume or faithfully project that same
release instead of creating an independent release line.

Checksums detect corruption against the supplied manifest; they do not prove
publisher identity when an attacker can replace both. Add independently
verifiable signatures or provenance when the distribution threat model
requires them.

## Upgrade ownership

Begin with reinstalling through the supported installation path. Add built-in
self-upgrade when recurring user needs justify maintaining executable
replacement and recovery across the supported platforms. Package-manager-owned
installations should continue to use that package manager.

When the CLI owns upgrades, an installation receipt identifies its version,
target, executable, source, and artifact digest. Manage only an executable that
matches the receipt. `upgrade --check` inspects availability without installing;
`upgrade` downloads and verifies a candidate, then replaces the executable and
receipt as a recoverable sequence.

Report success only after both are durable. Interrupted downloads, missing
assets, incompatible targets, checksum failures, and replacement or receipt
failures leave or restore the previous installation. If recovery cannot
complete, report the exact remaining state and preserve recovery evidence.

Follow [CLI Version Checking](cli-version-checking.md) for automatic cached
advisories, including agent and CI use, bounded refresh cost, and an explicit
opt-out. Update detection recommends the owning installation method;
installation remains an explicit operation.

## Verification

Exercise the exact published archives and supported installation paths in clean
consumers for each claimed target. Verify identity, checksums, platform
selection, and failure behavior. If self-upgrade exists, also verify receipt
ownership, interruption, recoverable replacement, and quiet noninteractive
execution. Follow
[Verification from Source to Consumer](verification-from-source-to-consumer.md)
and [Canonical Sources and Derived Artifacts](../architecture/canonical-sources-and-derived-artifacts.md).

## Revisit when

Change distribution or upgrade ownership when the audience's installation
requirements, privacy, platform restrictions, or authenticity guarantees change.
A small tool should not acquire an updater merely for consistency with a larger
one.
