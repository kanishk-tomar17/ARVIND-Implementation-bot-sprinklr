---
name: sprinklr-diagnose
description: Use when a consultant reports a Sprinklr issue or sends a screenshot of something not working — a rule not firing, a case not routing, a workflow erroring, a config that won't save. Runs the structured triage → clarify → plan → guide → escalate loop. Do NOT use for building something new from scratch (use sprinklr-implement) or for purely informational "how does X work" questions.
---

# Sprinklr Diagnose

Structured flow for diagnosing and fixing a broken/misbehaving Sprinklr configuration.

## 1. Read the evidence
- If there's a screenshot, identify: which module (Service/Care, Social, Insights, Platform), which exact screen, and the actual configured values shown. Read the values, not just the layout.
- Name what's wrong in one line before going further.

## 2. Locate the likely cause
- Map the symptom to the most probable config area. Check `knowledge/INDEX.md` for the relevant topic file; if not covered, search `site:sprinklr.com/help <topic>`.
- Common symptom → cause map (extend as the KB grows):
  - Case not assigned → assignment rule conditions / queue membership / agent availability / Unified Routing config.
  - Bot not triggering → bot rule checks & conditions, application state, trigger order.
  - Rule not firing → rule order, scope/filters, enabled state, conflicting higher-priority rule.
  - Workflow erroring → variable/resource manager, Groovy script, node config.
  - Can't save config → required field, permission, validation error in a collapsed section.

## 3. Clarify (before acting)
- Ask only the questions that change the diagnosis.
- If you know roughly where the problem is, ask for a **specific** clarification screenshot (e.g. "show the condition block of the rule", "show the queue's agent list").
- Ask what they've already tried and where exactly it broke — don't assume they started from zero.

## 4. Plan & confirm
- Present a numbered fix plan. State the expected outcome.
- Confirm: "Does this match what you're trying to achieve, or have you already done part of this?"

## 5. Guide
- Walk through the fix step by step in their environment. One step at a time for anything fiddly.
- After the change, state how to verify it worked.

## 6. Escalate to takeover
- If the consultant has **3–4 failed attempts** on the same step, or asks you to do it: switch to the `sprinklr-takeover` skill.

## Always
- Cite the source for any config claim (KB path or `sprinklr.com/help` URL).
- Never invent steps. If the KB and help docs don't cover it, say so and propose how to find out (test in sandbox, raise Sprinklr support ticket).
