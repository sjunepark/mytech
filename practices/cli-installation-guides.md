---
status: accepted
---

# CLI Installation Guides

**Initial evidence:** KASB and krx-cli READMEs

## Decision

For projects distributing prebuilt CLIs, make the README installation section
a complete path from a supported machine to a verified executable. Lead with
the project's recommended, currently available consumer installation method.
Readers should not need to reconstruct that path from development commands,
package internals, or a maintainer release runbook.

Follow [Standalone CLI Distribution](standalone-cli-distribution.md) for
artifact channels and installation ownership. This guidance explains how to
document the chosen method; it does not require a different installer, runtime,
package manager, or self-updater.

For an agent skill, route to installation only when setup is needed, following
[CLI Consumer Skills](cli-consumer-skills.md). Keep the complete installation
path available without loading it during routine CLI use.

## Reader path

Keep the common installation path in the README, in this order:

1. **Prerequisites and compatibility.** State supported operating systems and
   architectures, relevant OS or libc floors, required shell and download
   utilities, and any runtime or package-manager requirements. Distinguish
   installation requirements from build tools. A prebuilt native executable
   does not establish that its packaged launcher needs no language runtime.
2. **Obtain and install.** Link to the actual release channel and give commands
   for each supported shell whose syntax differs. Explain automatic target
   selection or show how platform names map to downloadable assets. Make any
   version, target, or local-filename substitutions explicit next to the block.
   State whether an installer verifies checksums; for a manual path, show or
   directly link the verification steps before the installation command.
3. **Make the command available.** Explain the default installation location,
   any supported override, and required PATH setup. Distinguish changes for the
   current shell from persistence in new terminals. If the package manager
   manages executable discovery, document or link its necessary setup.
4. **Verify installation.** End with the actual executable's version and help
   commands and explain that its identity should match the selected release.
   These checks should work without provider credentials. Put authentication
   and the first service request in a separate, linked usage section.
5. **Upgrade.** Show the supported upgrade or reinstall path for that
   installation method. When self-upgrade exists, explain its ownership
   requirements, any receipt users must preserve, and platform behavior that
   affects completion. Distinguish checking for an update from applying it;
   link [version-check behavior](cli-version-checking.md) through the project's
   own CLI documentation when applicable.

Write ordered, copyable command blocks for the declared shell. Include the
steps readers need on a clean machine; do not rely on a maintainer's checkout,
global configuration, or previously installed executable. Keep required
prerequisites and substitutions visible before readers run the commands.

## Scope and accuracy

Separate CLI installation, SDK dependency installation, and contributor setup
when the project offers all three. Give each audience its own prerequisites
and commands. An npm-format release archive does not imply npm registry
publication; a built SDK package does not establish a supported install path.

Describe what consumers can obtain from the documented channel. Mark
checkout-only or unreleased features explicitly and keep them out of the
ordinary released installation sequence. Apply
[Repository Documentation States](repository-documentation-states.md) across
the README and the linked installation and release documents.

Keep less common configuration, manual alternatives, ownership recovery, and
troubleshooting in a focused consumer guide when they would obscure the common
path. Link to their canonical explanation instead of copying release machinery
or maintaining competing installation instructions. Show platform support
limits honestly; building an archive and verifying its installed consumer
behavior are different claims.

For known redirected installation environments, document a supported recovery
path, such as reinstalling from the ordinary user context or using a supported
destination override visible to that consumer. Respect custom destinations and
preserve applicable receipts and
[upgrade ownership](standalone-cli-distribution.md#upgrade-ownership).
Do not prescribe one global directory or silently edit shell profiles as a
workaround for file visibility failures.

## Verification

Treat the documented command sequence as part of the supported installation
boundary. Exercise it with the exact release artifacts in clean consumers,
covering the claimed platforms under the
[distribution verification requirements](standalone-cli-distribution.md#verification).
Check prerequisite assumptions, asset selection, checksum verification,
version identity, help, and the documented upgrade path where applicable.

Check physical file visibility at the intended installation path separately
from command-name discovery and invocation. Exercise command discovery and
invocation in both current and newly launched consumer shells or applications,
distinguishing persistent PATH registration from their inherited environment
state. Correct PATH alone does not prove that the consumer can see the
executable; a working full path alone does not prove command discovery.

Verify in the intended user's ordinary shell or application context, crossing
the filesystem or launch boundary that can affect the installation claim. A
fresh subprocess under the same packaged launcher, container, or redirected
environment may share its private filesystem view and does not by itself
establish independence. Automation is sufficient when it crosses the relevant
boundary. When that consumer context is unavailable, record the tested context
and the remaining verification gap instead of reporting installer-local smoke
checks as proof of consumer usability. Separate observed results from inferred
causes, and limit success claims to the commands and contexts actually verified.

When packaging, prerequisites, installer behavior, or delivery status changes,
update the affected reader paths together. A Markdown or link check alone does
not demonstrate that installation works.

## Revisit when

Revisit the guide's entry point and depth when the intended audience,
installation owner, supported platforms, or distribution channel changes.
Preserve one clear recommended path while documenting alternatives that serve
actual users.
