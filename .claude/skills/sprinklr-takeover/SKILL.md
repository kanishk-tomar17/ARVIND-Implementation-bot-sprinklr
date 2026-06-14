---
name: sprinklr-takeover
description: Use when GROOT should stop guiding and directly operate the browser to inspect or fix a Sprinklr configuration — triggered after the consultant has 3–4 failed attempts at the same step, or whenever they ask GROOT to do it directly. Covers choosing the browser path, confirming safely, acting, and handing back.
---

# Sprinklr Takeover

When guidance isn't landing, take control and do it — safely.

## When to trigger
- Consultant has **3–4 failed attempts** on the same step, OR
- They explicitly ask GROOT to do it.

Announce the switch: "I'll take it from here — let me drive the browser." Don't take over silently.

## Pick the path
- **Browser MCP** (Playwright / chrome-devtools in this CLI) — for **inspection** and automated steps: navigate, read DOM/config state, confirm what's actually set. Use this first to diagnose, and for actions where a CLI-driven browser session is enough.
- **Claude for Chrome extension** — when the action must happen in the consultant's **own logged-in, SSO-authenticated Sprinklr session** (their real environment, their permissions). Use for the actual fix in production/sandbox where login matters.

If unsure: inspect with the MCP browser, act with the extension. See `SETUP.md`.

## Act safely — non-negotiable
1. **State the change before making it.** "I'm going to add condition X to rule Y."
2. **Confirm before anything destructive or irreversible** — deletes, publishing, bulk edits, or any change to a live production rule. Wait for an explicit yes.
3. **Prefer sandbox.** If a sandbox exists, do it there first and verify before touching production.
4. **One change at a time** for risky steps; re-check state between steps.
5. **Never** change credentials, permissions, or unrelated config without asking.

## Hand back
- Summarise exactly what changed (object, field, old → new value).
- State how the consultant can verify it.
- Return control and confirm they're unblocked.
