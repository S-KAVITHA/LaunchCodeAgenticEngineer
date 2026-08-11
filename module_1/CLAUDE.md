# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This is a Docker-based development environment for LaunchCode's **Agentic Programming** course. It provides a pre-configured Python 3.12 environment with AI/ML libraries, Anthropic Claude integration, and the Claude Code CLI.

## Running Streamlit Apps

From inside the container:
```bash
streamlit run app.py
```

Access at `http://localhost:8501`.

## Key Dependencies (requirements.txt)

- `anthropic` — Claude API client
- `streamlit` — web UI framework
- `python-dotenv` — environment variable management
- `slack_sdk` — Slack integration
- `google-api-python-client`, `google-auth-oauthlib` — Gmail/Google API access
- `fastapi`, `flask`, `uvicorn` — web frameworks
- `pydantic`, `httpx` — HTTP and data validation

## Environment & Tools in the Container

- Python 3.12 (aliased as `python` and `pip`)
- Claude Code CLI (`claude`) installed globally via npm
- OpenCode (`opencode-ai`) installed globally via npm
- ngrok for tunneling
- Workspace mounted at `/workspace`

## Gmail API Setup

Place `credentials.json` (from Google Cloud Console) in your workspace directory. On first run it triggers OAuth and saves `token.json`. Both files should be in `.gitignore`.

# Agent Context Boundary Policy

## Purpose
This file defines how context boundaries are managed in this project.
At the start of each new phase of work, the agent must follow the
procedure below before taking any action.

## Context Boundary Procedure
At the start of each new phase, before doing any editing or analysis:

1. Restate the current task goal in one sentence.
2. List the rules currently in effect (verbatim, not paraphrased).
3. State explicitly which prior rules are no longer in effect, if any.
4. Identify the specific artifact being worked on in this phase.
5. Then proceed with the requested work.

## Why This Matters
Rules and requirements change during long sessions. This procedure ensures the agent is always operating from the current version of the rules, not a prior version buried in conversation history.

## Compaction Policy

Compaction is a last resort. Proactive summarization (see .claude/skills/summarize-session/SKILL.md) should be triggered before the context window exceeds 60% capacity to avoid relying on compaction.

Observations from testing (update this based on your own runs):
- Compaction reliably preserves: [fill in based on your probe results]
- Compaction may lose or distort: [fill in based on your probe results]
- Manual compaction should be triggered at: [fill in your threshold]
Fill in the bracketed sections based on your actual probe results. 

