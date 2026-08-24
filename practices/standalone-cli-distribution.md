---
status: accepted
---

# Standalone CLI Distribution

**Initial evidence:** YTM

## Decision

For a standalone CLI intended for use across machines, use public GitHub
Releases as the canonical distribution channel. The owner's machines and
outside users use the same release installation path. A source checkout remains
a development path, not the normal installation path.

Each tool owns its supported operating-system and architecture matrix. Publish
only the prebuilt targets that the tool claims and verifies; this preference
does not impose a common platform matrix across tools.

## Release and installation

Build immutable, versioned release assets in CI from the tagged source. Publish
a prebuilt archive for each supported target, SHA-256 checksums, and generated
shell and PowerShell installers. Generate asset names and both installers from
the same tool-owned target definition so platform selection cannot drift across
the release paths.

The installers select a compatible release asset, verify its checksum, and
install the executable without requiring a language toolchain, repository
clone, Homebrew or another platform package manager, or GitHub CLI. Do not
embed or invoke `gh`. Keep published tags and assets immutable; corrections use
a new version.

Package-manager and language-registry releases may be added for demonstrated
consumer demand, but they must consume or faithfully project the same versioned
release rather than create an independent CLI release line.

## Managed upgrades

The installer writes a receipt identifying the installed version, target,
executable, release source, and installed artifact digest. The CLI manages an
installation only when the current executable matches that receipt; otherwise
it leaves the executable unchanged and directs the user to the installation
method that owns it.

Provide `upgrade --check` to report whether a newer compatible release exists
without installing it. Provide `upgrade` to download the selected asset,
verify its checksum and executable identity, stage and validate the candidate,
and publish the replacement executable and updated receipt as one recoverable
sequence. Report success only after both are durable. Unsupported targets,
missing assets, interrupted downloads, checksum mismatches, replacement
failures, and receipt-write failures leave or restore the previous executable
and receipt. If restoration cannot complete, preserve recovery evidence and
report the exact installed state rather than claiming success.

A tool may also perform a cached update check during interactive use, at most
once per day. Normal commands must never wait for that network check or fail
because of it. Do not check in CI or other noninteractive runs. A cached update
notice recommends `upgrade` on stderr only; it never changes structured stdout,
the command's exit status, or the installed executable, and updates are never
installed automatically.

## Verification

Exercise the exact published installers, archives, and upgrade path in clean
consumers for every target the tool claims. Verify artifact identity and
checksums, receipt ownership, recoverable replacement failure, and the absence
of update-check network traffic or output changes in CI and noninteractive
execution. Follow
[Verification from Source to Consumer](verification-from-source-to-consumer.md)
and [Canonical Sources and Derived Artifacts](../architecture/canonical-sources-and-derived-artifacts.md).

## Revisit when

Reconsider this default when a CLI must remain private, a concrete audience
requires native package-manager lifecycle management, GitHub Releases can no
longer serve as the canonical public artifact source, or the threat model
requires signatures or provenance beyond immutable assets and checksums.
