---
name: sprinklr-implement
description: Use when a consultant needs to BUILD or configure a new Sprinklr use case from scratch — set up assignment rules, design a guided workflow, configure a bot, stand up a Care Console, enable a channel, build a listening dashboard, etc. Runs the requirements → config-mapping → ordered-steps → verify playbook. Do NOT use for fixing something already broken (use sprinklr-diagnose).
---

# Sprinklr Implement

Playbook for implementing a new Sprinklr use case cleanly and the optimised way.

## 1. Gather requirements
- What is the business outcome the client wants? (Not the feature — the outcome.)
- Which product/module, which channels, what volume/scale.
- Environment: sandbox available? Production access? Any change-control constraints.
- Existing config that this must fit into (don't build in a vacuum).

## 2. Map to Sprinklr config
- Translate the requirement into specific Sprinklr objects (rules, queues, workflows, dashboards, custom fields, macros, bots…).
- Check `knowledge/INDEX.md` and `site:sprinklr.com/help` for the canonical way to build it. Prefer the documented/native approach over a workaround.
- Note dependencies and ordering (e.g. custom fields before rules that reference them).
- Flag the **optimised** choice when there are multiple ways — and why.

## 3. Ordered build steps
- Lay out a numbered sequence with the exact navigation path for each step.
- Confirm the plan with the consultant before they start.
- Recommend building in **sandbox first**, then promoting (see ALM / sandbox KB).

## 4. Guide / build
- Walk through step by step. Offer to take over (`sprinklr-takeover`) for the fiddly parts or if asked.

## 5. Verify
- Define the test: what input proves it works end to end (e.g. send a test message → confirm it routes to the right queue/agent).
- Confirm the client's actual use case is satisfied, not just that the config saved.

## Always
- Cite sources. Don't invent steps. Recommend sandbox before production.
- Keep the output as a clean numbered runbook the consultant can follow.
