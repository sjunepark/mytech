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

## Verification

Treat the documented command sequence as part of the supported installation
boundary. Exercise it with the exact release artifacts in clean consumers,
covering the claimed platforms under the
[distribution verification requirements](standalone-cli-distribution.md#verification).
Check prerequisite assumptions, asset selection, verification, executable
discovery in the current and a new shell, version identity, help, and the
documented upgrade path where applicable.

When packaging, prerequisites, installer behavior, or delivery status changes,
update the affected reader paths together. A Markdown or link check alone does
not demonstrate that installation works.

## Revisit when

Revisit the guide's entry point and depth when the intended audience,
installation owner, supported platforms, or distribution channel changes.
Preserve one clear recommended path while documenting alternatives that serve
actual users.
