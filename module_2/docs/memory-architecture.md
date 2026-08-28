# Memory Architecture

## Overview
This agent maintains a small Python project by updating code, documentation, and tests. It should remember current tasks, important decisions, and project rules. Code, test files, secrets, and completed-task details should not be stored in memory.

---

## Memory Layers

### Layer 1: Project Memory Directory
* **Belongs:** Current tasks, decisions, and open issues.
* **Does Not Belong:** Code, tests, or secrets.
* **Scope:** Project.
* **Write Access:** Agent can update.
* **Pruning:** Remove old information.

> `SCOPE.md` identifies the repository that owns the memory directory. The agent must verify this scope before reading other project memory.

### Layer 2: Knowledge Files
* **Belongs:** Stable coding and testing rules.
* **Does Not Belong:** Temporary task information.
* **Scope:** Project.
* **Write Access:** Human-controlled.
* **Pruning:** Update when rules change.

### Layer 3: Indexed Reference Documents
* **Belongs:** Detailed project and technical documentation.
* **Does Not Belong:** Current task notes.
* **Scope:** Project.
* **Write Access:** Human-controlled.
* **Pruning:** Remove outdated documents.

---

## Allocation Decision Table

| Information Type | Layer | Reason |
| :--- | :--- | :--- |
| **Current work** | Project memory | Tracks active tasks and open issues |
| **Stable rules** | Knowledge files | Provides reusable project guidance |
| **Detailed references** | Indexed reference documents | Keeps larger reference material separate |
| **Memory scope declaration (`SCOPE.md`)** | Project memory | Identifies which repository owns the memory directory |
| **Credential location** | Project memory | Records how a credential is accessed without storing its value |
| **Code and tests** | Repository | These are source artifacts, not memory |
| **Secrets** | Never stored | Credential values must never be persisted |

---

## Safeguards & Policies

### Stale Memory
Project-memory entries may contain review dates. Before using an entry, the agent must check its review date. If the review date has passed, the agent must:

1. Flag the entry as stale.
2. Request human confirmation.
3. Wait for confirmation before relying on the entry.

*This prevents outdated project decisions from being treated as current information.*

### Scope Verification
Each project memory directory contains a `SCOPE.md` declaring its owning repository.

Scope verification is the **first memory operation** of a session. The agent reads `SCOPE.md` and compares the declared project identity with the current repository before reading any other memory files.

If the identities do not match, the agent must stop and report:

> **SCOPE MISMATCH:** Memory directory belongs to `[name in SCOPE.md]` but current project is `[current project]`. Do not proceed until the correct memory directory is mounted.

*This safeguard prevents memory from another project from being incorrectly treated as valid context.*

### Data Classification
Before writing anything to a memory file, classify it:

* **Public:** Safe to commit to the repo and share broadly. Most project decisions and coding standards fall here.
* **Internal:** Safe within the team but not for public repos. Store in a non-committed volume or `.gitignore` the containing folder.
* **Confidential:** Sensitive business data. Do not store in agent memory. Retrieve from secure systems on demand.
* **Secret:** Credentials, tokens, API keys, and PII. **Never store these values in any memory file.** Use them only for the immediate task and reference the environment variable name instead.

### Credential Handling
Credential values must never be stored in memory. The system may record the name of an environment variable (e.g., `ANTHROPIC_API_KEY`), but must never record the value stored inside that variable.

*The corrected `decision-003.md` demonstrates this approach by referencing `ANTHROPIC_API_KEY` without storing its credential value.*

---

## Enforcement

The memory system uses two types of protection:

* **Soft guards:** Policies in `CLAUDE.md` instruct the agent how to verify scope, handle stale entries, classify data, and protect credentials.
* **Hard stops:** The Git pre-commit hook automatically blocks a commit when its credential scan detects a matching pattern.

### Pre-Commit Hard Stop
A pre-commit hook at `.git/hooks/pre-commit` scans staged files under `.memory/` for common credential patterns, including:
* `sk-`
* `password=`
* `secret=`
* `token=`
* `api_key=`
* `apikey=`

If a matching pattern is detected, the commit is blocked. Testing with a staged `api_key=abc123` value confirmed that the hook correctly stopped the commit.

> **Note:** The hook is stored locally in `.git/hooks/`. It is not tracked by Git and therefore does not automatically travel with the repository or become available to collaborators.

---

## Design Rationales

* **Architecture:** A single memory layer was rejected because it could become cluttered. The three-layer approach keeps current work, stable rules, and reference material separate.
* **Scope verification:** Added after testing a container with memory mounted from another project. The agent incorrectly treated the other project's memory as valid context. The startup check now requires the memory scope to match the current repository before other memory is read.
* **Credential handling:** Strengthened after a decision entry contained a hardcoded API key. The entry was corrected and renamed to `decision-003.md`, replacing the credential value with an `ANTHROPIC_API_KEY` environment-variable reference.
* **Pre-commit protection:** Added as an additional protection against accidentally committing credentials. Testing demonstrated that credential-like content under `.memory/` is blocked automatically.
* **Stale memory:** Review-date enforcement prevents old project decisions from silently being treated as current. Expired entries require human confirmation before they can be used.