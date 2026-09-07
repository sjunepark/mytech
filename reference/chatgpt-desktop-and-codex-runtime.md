# How ChatGPT Desktop Uses the Codex Runtime

A descriptive record of public documentation and a local macOS observation on
2026-08-12. The September documentation review condensed the record; it did not
inspect a new app build. Product names, bundle paths, and internal packaging are
version-specific evidence, not current product guarantees.

## Client and runtime boundary

In the inspected build, ChatGPT desktop bundled a platform-specific `codex`
binary and launched it in `app-server` mode. It did not run the separately
installed CLI on the user's `PATH` or embed the terminal UI.

```text
Desktop UI
    | launches bundled process; exchanges protocol messages
    v
Codex App Server
    | hosts agent runtime and exposes threads, turns, and events
    v
Codex core
    | executes tools in the selected environment
    v
Files, shell, Git, MCP, and other integrations
```

OpenAI's [App Server architecture account](https://openai.com/index/unlocking-the-codex-harness/)
describes rich clients sharing the Codex harness and bundling or fetching a
platform-specific runtime. The
[App Server documentation](https://learn.chatgpt.com/docs/app-server)
describes its bidirectional protocol. The
[open-source implementation](https://github.com/openai/codex/tree/main/codex-rs/app-server)
is separate from the desktop UI.

These sources concern Codex execution. They do not establish that every
ordinary Chat or Work request uses the same local process path.

## Recorded local evidence

The inspection concerned ChatGPT desktop `26.803.61601`, build `6396`, on Apple
Silicon. Its observed bundle was `/Applications/ChatGPT.app`, with identifier
`com.openai.codex`.

| Observation | What it established for that build |
| --- | --- |
| `Contents/Resources/app.asar` and Electron/Chromium frameworks | The inspected UI used an Electron shell |
| `Contents/Resources/codex`, a native arm64 executable | The app carried its own platform runtime |
| Bundled runtime launched with `app-server` | The local desktop client drove the App Server entry point |
| Bundled `codex-cli 0.147.0-alpha.6.5`; separate CLI `0.146.1` | Desktop and terminal installations could use different versions |
| Different executable hashes and bundle-path process launch | The desktop did not select the separately installed binary |
| Code Mode, browser, native, and Node.js helpers | Some desktop tool capabilities involved additional processes |

The recorded launch shape was:

```text
/Applications/ChatGPT.app/Contents/Resources/codex \
  -c features.code_mode_host=true \
  app-server \
  --analytics-default-enabled
```

This record is a summarized observation, not a retained process trace or a
reproducible package attestation. Re-inspect the installed build when exact
paths, versions, or topology affect a decision.

## Implications

Runtime concepts can transfer between surfaces without identical UI, version,
configuration discovery, or tool availability. When behavior differs, identify
the actual executable and client before assuming the same runtime is failing.

For integration work, distinguish a one-shot command or SDK operation from the
larger App Server lifecycle and event contract. Match generated protocol
schemas to the runtime the client actually launches. The
[Codex repository](https://github.com/openai/codex) owns runtime source, while
current product documentation owns supported integration behavior.

For diagnosis, locate the failing boundary: desktop UI, client/server protocol,
core runtime, model provider, execution environment, or a tool/helper. A
standalone CLI reproduction is useful evidence of shared runtime behavior, but
matching versions alone does not establish surface parity.

Local tool execution does not establish offline model inference. Likewise,
open-source runtime code does not establish that the complete desktop UI is
open source, and a shared harness does not imply identical local and hosted
execution environments.
