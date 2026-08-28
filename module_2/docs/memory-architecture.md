Memory Architecture
What this workflow needs to remember

This agent maintains a small Python project by updating code, documentation, and tests. It should remember current tasks, important decisions, and project rules. Code, test files, secrets, and completed-task details should not be stored in memory.

Layer 1: Project memory directory
Belongs: Current tasks, decisions, and open issues.
Does not belong: Code, tests, or secrets.
Scope: Project.
Write: Agent can update.
Pruning: Remove old information.
Layer 2: Knowledge files
Belongs: Stable coding and testing rules.
Does not belong: Temporary task information.
Scope: Project.
Write: Human-controlled.
Pruning: Update when rules change.
Layer 3: Indexed reference documents
Belongs: Detailed project and technical documentation.
Does not belong: Current task notes.
Scope: Project.
Write: Human-controlled.
Pruning: Remove outdated documents.
Allocation decision table
Current work → Layer 1
Stable rules → Layer 2
Detailed references → Layer 3
Code/tests → Repository
Secrets → Never stored
Alternatives considered

A single memory layer was rejected because it could become cluttered. The three-layer approach keeps current work, stable rules, and reference material separate.

## Data Classification

Before writing anything to a memory file, classify it:

- **Public** — Safe to commit to the repo and share
  broadly. Most project decisions and coding standards
  fall here.

- **Internal** — Safe within the team but not for
  public repos. Store in a non-committed volume or
  .gitignore the containing folder.

- **Confidential** — Sensitive business data. Do not
  store in agent memory. Retrieve from secure systems
  on demand.

- **Secret** — Credentials, tokens, API keys, PII.
  Must never appear in any memory file. If the agent
  encounters a secret during a run, use it for the
  immediate task only and explicitly do not write it
  to any memory layer. Reference the environment
  variable name instead.

### Guardrails

A pre-commit hook at .git/hooks/pre-commit scans
.memory/ for common credential patterns before each
commit. If a pattern is found, the commit is blocked.

