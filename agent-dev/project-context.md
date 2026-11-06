# Project Context

> **Humans write the four Fundamentals sections once, at the start (~5 minutes).**
> **Everything under "Grows with the project" is maintained by agents** at the sidecar step of each feature. Humans can edit it, but don't need to pre-fill it.
> Agents read this file first for every feature.

---

# Fundamentals (human-written)

## Problem
<!-- The organization, what they do, the problem we're solving. 3–5 sentences. -->

## Users
<!-- Each user type and what they need. e.g. "Volunteer: finds and signs up for shifts." -->

## Demo goals
<!-- What must work in the demo, in priority order. Agents use this to judge tradeoffs. -->
1.
2.
3.

## Tech stack
<!-- One line per layer. e.g. "Frontend: React (Vite)", "Backend: FastAPI", "Database: SQLite via SQLModel". -->
- Frontend:
- Backend:
- Database:

---

# Grows with the project (agent-maintained)

<!-- Agents: add or update these sections at the sidecar step. Only record facts that exist in the code.
     Create a section the first time something belongs in it. Keep entries short. -->

## Architecture
<!-- One-line request flow, plus extras (LLM calls, uploads, external APIs). -->

## Folder layout
<!-- Where each kind of code lives. -->

## Data model
<!-- | Table | Fields | Notes | -->

## API
<!-- | Method | Path | What it does | Feature | -->

## Commands
<!-- run-checks reads this. | Name | Command |
     Names: Run (backend), Run (frontend), Test (backend), Test (frontend), Lint, Build, Smoke, Reset dev DB -->

## Conventions
<!-- Env vars, branch names, date format, naming. -->

## Stack conventions
<!-- The framework-specific "how" behind each law: patterns, test setup, gotchas. One subsection per area
     (Backend, Frontend, Database, Testing) as they come up. -->

## Decisions log
<!-- Date — decision — why (feature NNN). -->
