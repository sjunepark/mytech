# CLI Installation Guides History

## 2026-09-09

Added an accepted preference for writing consumer installation guides, informed
by the KASB and krx-cli READMEs. Their different installer and package-manager
paths motivate explicit prerequisites, executable discovery, verification,
upgrade ownership, and released-feature accuracy. Distribution policy remains
owned by Standalone CLI Distribution; the new guidance owns how authors make
that policy usable in a README.

Extended verification to require independence across the relevant filesystem
or launch boundary after the Windows MSIX incident recorded in
[issue #4](https://github.com/sjunepark/mytech/issues/4). Installers launched by
the packaged Codex app and their child shells saw redirected AppData binaries
that ordinary user terminals could not see despite correct PATH. Destination
overrides passed local checks for Darty, KASB, and YTM; the user independently
confirmed only Darty's help command in the previously failing tab. This
motivates separate visibility and discovery checks, explicit validation limits,
and recovery that preserves installation ownership without generalizing one
launcher configuration or destination to all installations.
