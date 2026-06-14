# Implementation Bot — Sprinklr (GROOT)

GROOT is an all-in-one **Sprinklr implementation assistant** for RaptorCX's product consultants — built as a Claude Code agent. It diagnoses issues, implements use cases, and can drive the browser to fix configurations in a consultant's live Sprinklr environment.

## What's here
- **`CLAUDE.md`** — GROOT's operating brain: persona, knowledge-lookup order, the diagnose→guide→takeover workflow.
- **`knowledge/`** — distilled Sprinklr knowledge base, built from RaptorCX's Product Foundation Course videos (auto-transcribed via Microsoft Stream, then distilled). See [`knowledge/INDEX.md`](knowledge/INDEX.md) for the full map and status.
- **`.claude/skills/`** — reusable playbooks: `sprinklr-diagnose`, `sprinklr-implement`, `sprinklr-takeover`.
- **`SETUP.md`** — browser access setup (chrome-devtools MCP + Claude for Chrome).
- **`LEARNING.md`** — how GROOT learns from the Lyearn/Stream course videos.
- **`.mcp.json`** — browser MCP config.

## Knowledge base coverage (so far)
- ✅ **Care Console** (11 topics) — overview, manager, third pane, case stream/SLA, case-control buttons, shortcuts (canned responses/macros), agent-assist AI, layouts by channel, collaboration notes, widgets, iframe.
- ✅ **Case Management** (6 topics) — case creation/case-maker, sub-cases (ticketing), bot rule, assignment rules, survey rules, checking case activity.
- 🔄 **Guided Workflow** (2/9) — overview, screen creation (in progress).
- ⬜ Conversational AI, Community, Email Care, Live Chat, Unified Routing, Outbound Voice, Sandbox/ALM, Governance (mapped, pending ingestion).

## How the knowledge was built
Each KB file is distilled from a course video: Microsoft Stream generates the transcript, GROOT reads it (plus on-screen frames where the UI path matters) and writes a concise, consultant-ready reference. Every file cites its source course + the matching `sprinklr.com/help` topic.

---
*Internal RaptorCX tool. Content derived from RaptorCX Sprinklr training material — keep this repository private.*
