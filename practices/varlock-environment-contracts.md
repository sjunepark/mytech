---
status: accepted
---

# Varlock Environment Contracts

**Initial evidence:** darty (eval-only key); accepted target in Seoro

## Decision

Use [Varlock](https://varlock.dev) as the default environment contract in any
repository whose code reads environment variables, regardless of language. A
committed `.env.schema` declares every variable with its type, whether it is
required, and whether it is sensitive. Misconfiguration then fails at startup
with a clear error instead of at first use.

Prefer this over reading the environment directly, even in small repositories.
The extra schema, CLI, and generated code are an accepted cost for one
declared, validated, and redaction-aware contract that people, CI, and agents
can read without seeing secret values.

Do not add Varlock to a repository that reads no environment variables. Add it
when the first variable appears.

## Shape

- Launch every entry point through `varlock run` or a framework integration.
  This covers package scripts, task runners, IDE run configurations, tests, and
  CI.
- Read typed values through the generated module for the language, such as
  `@generateTsTypes`, `@generatePythonEnv`, `@generateRustEnv`, or
  `@generateGoEnv`. These loaders fail closed when the program was not started
  by Varlock. Keep that behavior.
- Resolve secrets from 1Password through the Varlock plugin rather than storing
  them in `.env.local`. Commit no secret values.
- In Effect applications, let Varlock own validation and generate the Effect
  `Config` module from the schema (`@generateEffectConfig`). Do not validate the
  same variables twice. See [Effect](../libraries/typescript/effect.md).

## Distributed binaries

Released CLIs and libraries must not require Varlock on the end user's machine.
Use Varlock for the repository's own development, test, and CI environment.
The shipped program reads its runtime configuration through its own validated
contract, such as plain environment variables or a configuration file, and
never calls a generated Varlock loader.

## Revisit when

Revisit when a Windows-native install path for non-JavaScript repositories
proves impractical, when the 1Password plugin cannot work within the
`op-agent` access boundaries, or when Varlock upgrades repeatedly break
consumers. Also revisit if a project's deployment platform cannot run
`varlock run` or a supported integration.
