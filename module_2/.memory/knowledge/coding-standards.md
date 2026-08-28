# Coding Standards

Last reviewed: 2026-08-25
Maintained by: the team

These standards apply to all code in this project. The
agent should consult this file before writing or reviewing
any code. These rules are set by humans and the agent
should never modify this file.

## Type Hints Required
All function and method signatures should include type hints for parameters and return values. This makes intent explicit and lets tooling catch mismatches before runtime.

## No Bare Excepts
Never use a bare `except:` clause; catch specific exception types instead. Swallowing all exceptions hides real bugs and makes failures harder to diagnose.

## Secrets Stay Out of Source Control
API keys, tokens, and credentials must be loaded from environment variables or `.env` files, never hardcoded. Anything containing secrets (e.g. `credentials.json`, `token.json`) belongs in `.gitignore`.

## Consistent Formatting
Code should be formatted with a standard tool (e.g. Black for Python) rather than by hand. Consistent formatting keeps diffs focused on logic changes, not style churn.

## Docstrings for Public Functions
Public functions and classes should have a short docstring describing purpose, parameters, and return value. Internal/private helpers can rely on clear naming instead.

## Explicit Dependency Versions
Dependencies in `requirements.txt` should be pinned or version-bounded rather than left unconstrained. This keeps builds reproducible across environments.

## Validate at System Boundaries
Input validation belongs at the edges of the system (user input, API requests, external responses), not scattered through internal logic. Trust internal code paths once data has been validated on entry.
