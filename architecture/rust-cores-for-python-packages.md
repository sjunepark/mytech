---
status: accepted
---

# Rust Cores for Python Packages

## Decision

When a Python package needs a capability already implemented and owned in Rust,
keep Rust as the sole semantic implementation of that capability and expose it
through a narrow native extension, normally using
[PyO3](https://pyo3.rs/). Package the extension and an idiomatic typed Python
facade together, normally using [maturin](https://www.maturin.rs/). Do not
reimplement the Rust-owned behavior in Python merely to make the native core
convenient to call.

Keep the native module private to the package when a facade improves the public
API. The Rust implementation owns the capability's domain rules, state
transitions, resource policy, safety bounds, domain translation, and sanitized
failure semantics. The facade owns Python naming, type annotations, exception
classes, ordinary conveniences such as context managers, and genuinely
consumer-specific orchestration, but it does not become a second owner of
Rust-owned rules.

## Binding contract

Expose a small project-owned API rather than Rust internals or dependency
types. Expose Rust asynchronous operations as `asyncio` awaitables without
blocking the event loop. Use a maintained bridge for the chosen Rust runtime,
normally
[pyo3-async-runtimes](https://github.com/PyO3/pyo3-async-runtimes), after checking
compatibility with the selected PyO3 release. A synchronous blocking or CPU-bound
operation may remain synchronous when that fits Python consumer expectations,
but detach it from the interpreter while Rust performs the work. Make
cancellation propagation, client lifetime, and cleanup explicit where an
operation owns resources or may outlive its caller. Do not retain
interpreter-bound references across asynchronous work without an owned
lifetime.

Translate expected Rust failures into a stable project-owned Python exception
hierarchy with bounded safe context. Do not expose credentials, unrestricted
external payloads, dependency errors, or panic details. Treat a Rust panic as a
defect. Contain unwinding panics at the binding boundary and verify the behavior
under the release build's panic strategy. An abort cannot be translated into a
Python exception; use process isolation if surviving native crashes is a
required consumer guarantee. See Rust's
[panic containment limits](https://doc.rust-lang.org/std/panic/fn.catch_unwind.html).

Keep dependency types behind the boundary described in
[Boundary-Owned Contracts and Pure Cores](boundary-owned-contracts-and-pure-cores.md).
Native-module type stubs and platform package metadata are derived binding
artifacts. They may be packaged or committed when useful, but their freshness
must be verified against the Rust binding surface. Inline annotations in the
Python facade remain part of that facade's source. Apply
[Canonical Sources and Derived Artifacts](canonical-sources-and-derived-artifacts.md)
without treating all Python typing as generated output.

## Packaging and verification

Use a mixed Rust and Python package so one wheel contains the native extension,
typed facade, type information, and package metadata. Prefer prebuilt wheels
for supported targets; an sdist that requires an end user to install Rust is a
fallback, not a substitute for those wheels.

Use PyO3's stable ABI support when the binding and its dependencies are
compatible and reducing Python-version-specific builds is worth its API and
performance constraints. Stable ABI support does not produce one universal
binary. Build and publish an explicit matrix for the supported Python runtime,
operating system, CPU architecture, and Linux C library, or restrict an
internal package to the targets it actually supports. Keep the Python facade,
type information, native extension, and Rust core version-compatible as one
released package surface.

Keep core behavior, invariants, and resource-lifecycle tests in Rust. Also test
each packaged wheel from a clean Python environment. Cover imports on every
supported native target, synchronous or awaitable behavior as applicable,
cancellation, stable exception translation, context-manager cleanup, panic
containment, type compatibility, and installation without a local Rust
toolchain.

## Revisit when

Use another boundary when a concrete consumer requires a pure-Python package,
an unsupported interpreter or deployment platform, or an environment that
cannot load native extensions; when native wheel distribution is unacceptable;
or when cross-boundary callbacks and shared Python state dominate the
interface. If consumers genuinely need an independent Python implementation,
give it explicit ownership and verification rather than silently maintaining
two implementations of the same rules.
