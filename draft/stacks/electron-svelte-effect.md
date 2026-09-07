---
status: draft
---

# Electron, Svelte, and Effect for Desktop Applications

**Initial evidence:** Creo

## Tentative preference

For a local-first cross-platform desktop product, use:

- Electron for the operating-system and application shell;
- Svelte for renderer presentation and interaction;
- a pure TypeScript core for portable documents and deterministic domain logic;
- Effect in the main process for I/O, lifetimes, typed failures, and runtime
  composition; and
- a narrow schema-validated preload and IPC bridge for renderer capabilities.

The main process owns filesystem, subprocess, storage, credential, and other
privileged capabilities. The renderer owns presentation and interaction state
and cannot import Node or Electron implementations.

Portable authored state remains separate from run state, renderer state, and
machine-local state.

## Why this is uncertain

The process and capability boundaries are reusable. The complete stack still
depends on the product's native integration, accessibility, startup and memory
budgets, supported platforms, and distribution constraints. Those requirements
should select the shell independently of renderer preference.

## Promotion questions

- Is Electron the preferred desktop shell for future local-first products?
- Is Svelte the default renderer independently of Electron?
- Should Effect be the default main-process runtime, or only when resource and
  orchestration complexity justifies it?
- Is a schema-backed preload bridge a mandatory invariant for every Electron
  application?
- Which product requirements would instead favor a native shell or a web-only
  application?

## If accepted

Promote the process and capability ownership rules with a conditional stack
profile. Keep packaging target, managed runtimes, UI libraries, and distribution
store project-specific.
