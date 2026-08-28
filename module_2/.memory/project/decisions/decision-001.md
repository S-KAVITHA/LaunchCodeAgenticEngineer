# Decision 001 - Test File Organization

**Date:**
2026-08-25  
**Review by:**
2026-11-25  
**Status:**
Active

## Decision

Test files are organized in a separate `/tests` directory, rather than being placed alongside the source files they test.

## Rationale

This keeps test code separate from production source code and provides a consistent project-wide test structure. Tests can mirror the source structure under `/tests` as needed.

## Alternatives rejected

Placing tests alongside the source files was rejected to keep production code and test code clearly separated.

## How to apply

When creating or moving test files in this project, place them under `/tests` (mirroring source structure as needed) rather than next to the corresponding source file.