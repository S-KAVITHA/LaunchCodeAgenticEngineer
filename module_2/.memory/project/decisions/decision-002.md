# Decision 002 - Test File Organization (Reaffirmed)

**Date:**
2026-08-25  
**Review by:**
2026-11-23  
**Status:**
Active

## Decision

Test files are organized in a separate `/tests` directory, rather than being placed alongside the source files they test.

## Rationale

This reaffirms the decision recorded in [Decision 001](decision-001.md), per direct request from the project owner on 2026-08-25. It maintains a consistent test organization across the project.

## Alternatives rejected

Placing tests alongside source files was rejected to keep production code and test code clearly separated.

## How to apply

When creating or moving test files in this project, place them under `/tests` (mirroring source structure as needed) rather than next to the corresponding source file. See also Decision 001 for the original rationale.