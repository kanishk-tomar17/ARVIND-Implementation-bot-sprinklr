# Case Management — Bot Rule

**Source:** Product Foundation Courses → `Sprinklr Services - Case Management / 018_… Bot Rule` (video transcript) · **Cross-check:** `site:sprinklr.com/help bot rule`

The rule that decides, per inbound message, whether to **trigger the bot** or **route to an agent**.

## Purpose
- After the **Case Maker rule** associates/creates a case, private messages on the **bot account** are sent into the **Bot Rule** via **scheduler actions**.
- The Bot Rule then decides: **trigger the conversational-AI bot** on the message, or **send the case to agents**.

## Setup pattern
- Usually **one bot rule per channel** (e.g. a Facebook rule) so any auto-response triggered is channel-specific.

## Checks & conditions (in order, from the blueprint example)
1. **Trigger + partner-queue check** — the rule runs via a **scheduler queue**, but the message is also put in a **bot trigger queue** so it can **retry** if the bot didn't trigger first time.
2. **Fan-post check** — double-check (also done in Case Maker).
3. **Load the case** — condition "does the message have an associated case" loads that case into the rule's memory.
4. **"Case created" custom field** (tagged in Case Maker) = **Yes** → this is the **first message** of the case → **reset the conversational-AI context** and **trigger the bot** (new cases go to the bot first; escalate to agent only if unresolved).
5. **Regex check (internal testing)** — e.g. typing **"reset bot"** in the conversation re-tags the case so the bot runs on the next message, removes it from assignment queues, puts it back in the bot queue, and sends an auto-response that the case was reset (lets testers reuse a case instead of deleting/recreating).
6. **"Case currently with" custom field** (the key router):
   - Value = **agent** → message goes **straight to the agent** (bot not triggered). This field is tagged "agent" wherever a case is routed to an agent.
   - Value = **empty** → bot path. Empty happens on the first message (which actually flows via the create-path above), or for **pre-existing cases** that predate the bot setup (already with agents, field untagged → routed to agent queue, then tagged "case currently with agent").

## Bot application states & actions
- The video's third segment covers bot application **states and their corresponding actions** (trigger/reset/route). Core mechanic: the **"case currently with"** field gates bot vs agent on every subsequent message.

## Notes / gaps
- From the course video transcript (blueprint environment walkthrough). Exact fields/regex vary per client. Related: `case-management/case-creation-logic.md` (Case Maker rule — pending), `conversational-ai/*` (bot building), `case-management/assignment-rules.md`.
