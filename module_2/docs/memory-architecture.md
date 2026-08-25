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

