# Inbound Voice Use Cases — Queue Report (Reporting 078)
**Source:** Product Foundation Courses → Reporting / 078 Inbound Voice Use Cases - Queue Report (video transcript + per-conversation queue metrics glossary slide) · **Help:** search `site:sprinklr.com/help queue reporting assignment engine per conversation per assignment SLA preset`

## What it is
Queue / assignment-engine reporting covers: queue reporting from the **Voice report** (call-level work-queue path), the **Assignment Engine report** (per-conversation + per-assignment), and **SLA metrics** + SLA presets.

## Per-conversation vs per-assignment
- **Per conversation** — reports on **one unique call** and its status in a work queue.
- **Per assignment** — counts each time the call is **rerouted/assigned** to a queue.
- *Example:* call lands on Queue A → transferred to Queue B. **Total Calls per Assignment = 2**; **Total Calls per Conversation = 1**.

## Per-conversation metric glossary
- **Conversation Creation Date** — when the call was created.
- **Work Queue** — name of the queue the call landed in.
- **Total Calls (per conversation)** — calls that entered the work queue.
- **Total Calls Taken** — calls answered in the queue.
- **Total Abandoned Calls** — calls not answered. *(Calls Taken + Abandoned = Total Calls.)*
- **Originated in Queue** — calls whose first landing queue was this queue.
- **Flew In Count** — calls that came into this queue **from another** queue.
- **Flew Out Count** — times a call was transferred **out** of this queue (by agent or routing config).
- **Number of Calls Answered within SLA** — answered within SLA (requires **SLA preset** applied at widget level).
- **Number of Calls Abandoned within SLA** — abandoned during the SLA period (SLA preset required).
- **% Calls Answered within SLA** = Answered within SLA ÷ (Total Calls − Abandoned within SLA) — the queue's SLA %. (SLA preset required.)
- **Answered (per conversation)** — total **wait time** of an answered call before connecting to an agent.
- **Call Abandoned SLA** — time the call spent in the queue before being abandoned.

## Per-assignment wait metric (verbatim, in-product hover, confirmed June 2026)
- **Total Wait Time (Per Assignment)** — "Measures the total time a call had to wait before the call was assigned to an agent. **It includes both Queue time and ring/agent inbox time** for the agent over total calls that entered the queue based on each assignment." So: **Queue time + Ring time**, measured **per assignment leg** (each queue entry = its own record), and aggregated as an **average over calls that entered the queue** (not a raw sum).
  - **vs. per-call queue metrics** ([[voice-backend-structure]]): *Total Queue Time* = sum of all queue legs, **queue-only**; *First Queue Time* = first leg, **queue-only**. Total Wait Time (Per Assignment) is the only one of the three that **includes ring**.
  - **First-segment-only use case:** to get "wait until the **first** agent connect, transfers excluded, incl. ring" → use **Total Wait Time (Per Assignment) filtered to the first leg via `Originated in Queue`** (or earliest assignment per Conversation ID). Without that filter, transfer legs are also counted.

## SLA preset
SLA metrics need an **SLA preset** (the threshold defining "within SLA") applied at the widget level — logic is set at the work-queue level. Create an SLA preset in the system and apply it to the SLA metrics.

## Notes / gaps
- Uses the **ACD report** + Voice report from [[voice-backend-structure]]; complements [[inbound-voice-agent-performance]] and [[inbound-voice-ivr]]; live queue view in [[live-reporting-voice]].
- Part of Reporting (Voice): [[voice-backend-structure]], [[live-reporting-voice]], [[inbound-voice-ivr]], [[inbound-voice-agent-performance]].
