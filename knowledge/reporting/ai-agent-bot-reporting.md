# AI Agent (Agentic Bot) Reporting — Care Reporting Widget Builder
**Source:** Verified live (prod3, Qatar Railways "Qrail Agentic bot - V2", 2026-08-13) — no course video/help article covers this at field level; distilled from live widget-builder exploration.

## What it is
How to build Care Reporting dashboard widgets for a Sprinklr **AI Agent** (Task/Tool-based agentic bot, not the classic dialogue-tree Conversational AI bot). The AI Agent has **no dialogue tree**, so node-level drop-off reporting ([[dialogue-tree-reporting]]) does not apply — this is the key reason "drop-off points" is a real gap for this bot type.

## Data source — use "Service Analytics", not "Social Analytics"
The widget builder's **Data Source** dropdown defaults to **Service Analytics** — that's the correct one for AI Agent bot reporting on this instance. It has a category sidebar (click the **Metrics/Dimensions picker → any field → category list on the left**) with a dedicated **AI Agent** category → **SmartFAQ Report** sub-report, plus bot-specific fields spread across the generic **Interaction Summary → Omnichannel Case Summary Report**.

(The generic help article "Sessions Reporting for Conversational AI on Digital Channels" names **Social Analytics** with fields Account/Session Count/Session Handled By — that's for the *classic* dialogue-tree bot, not the AI Agent. Fields with matching names (e.g. "Session Count") exist in both data sources but are **different underlying entities** and are NOT interchangeable — verify compatibility live, don't assume by name.)

## Confirmed fields — Service Analytics → Interaction Summary → Omnichannel Case Summary Report
All of these are mutually compatible (same case-level entity) and were verified with real Qrail data (Last 30 Days):
- **Channel** (Dimension) — "the name of the channel associated on the case" → per-channel breakdown.
- **Case Count** (Measurement) — total cases across all channels → **Total Sessions**.
- **Case Handled By (Current Value)** (Dimension) — bot / agent / both — but ⚠️ **incompatible** with the custom `Cases Handled by...` measurements below (different sub-grain); use it alone or with plain Case Count only.
- **Cases handled by bot count** (Measurement) — cases resolved by bot alone → **Resolutions**.
- **Cases Handled by Bot + Agent** (Measurement) — cases that started with bot, escalated to agent → **Escalations**. ⚠️ Not compatible with **Channel** — these two custom measurements are pre-aggregated and can only be plotted standalone (no dimension breakdown). Escalation rate = `Bot+Agent / (bot count + Bot+Agent)`; no native % metric exists — compute manually.
- **Average Handling Time of Bot** (Measurement) — "average time customer spent with Bots across cases where bot responded" → **Session Duration**.
- **Time Of Day** (Dimension, hourly) — pairs with Case Count → **Peak Usage Times**. Also available at 15-min/30-min granularity.
- **Unique Customer Participated Count** (Measurement, in Case Message Details Report) → **Unique Users**.

## Confirmed fields — Service Analytics → AI Agent → SmartFAQ Report
Message/query-level RAG telemetry for the AI Agent's knowledge retrieval pipeline. On Qrail (2026-08-13) **this entity returned 0 data** for Last 30 Days with no filters — the fields are real and valid, but either this report isn't what V2 logs to, or it needs an Account/Workspace filter scoped to the specific bot application. Flag this when building — don't assume 0 means broken config.
- Latency breakdown (all Measurements, use **Average** not Sum): `Create Embedding User Query Time Ms`, `Fetch Custom Answers Time Ms`, `Fetch Similar Documents Time Ms`, `Input Guardrail Time Ms`, `ML Time Taken Ms`, `Output Guardrail Time Ms`, `Qdrant Search Plugin Time Ms` → **Response Time**.
- `KB Articles` (Dimension) → proxy for **"most frequently asked questions"** (paired with a latency Measurement as the plottable metric — there's no direct "retrieval count").
- `Error Message`, `Error StackTrace` (Dimensions) → best available proxy for **System Performance / error rate**; there is **no native Uptime/Downtime metric** in Sprinklr — don't invent one.
- `Response Grounded` (Dimension) — RAG groundedness/hallucination flag.
- `Application Id`, `Message Id`, `User Message`, `Answer`, `Reworded Question` — message-level identifiers.

## Confirmed gaps (don't build a widget pretending these exist)
- **Escalation triggers by verbiage/type** — no field counts "how many times a specific failover message fired." Needs a custom field stamped by the bot flow at each exit point; doesn't exist yet.
- **New vs returning users** — no first-seen/returning flag field found. Needs a profile-level custom field.
- **User location** — no direct geo field surfaced in these two reports; would need Universal Profile country or phone-code derivation (not yet explored live).
- **Uptime/Downtime** — not a Sprinklr metric anywhere; Error Message/Count is the closest proxy.
- **Drop-off points mid-conversation** — genuinely not available for AI Agent (Task-based, no dialogue tree); only case-level abandonment concepts apply to classic bots.

## Widget-builder mechanics learned
- The **metric/dimension picker enforces compatibility by entity grain** — clicking an incompatible field shows a tooltip naming which existing selection conflicts. When blocked, pick the **dimension first**, then search metrics — the picker still lets incompatible ones through the search list, so you must click-test, but the error message tells you exactly what to remove.
- Search results are duplicated across data sources/entities with **identical display names but different grains** (e.g. 3 different "Session Count" fields, "Case Count" appears under both "Omnichannel Case Summary" and generic categories). Always check which **category/report** a result groups under, and re-verify compatibility rather than trusting the name.
- Custom pre-aggregated measurements (anything client-specific, e.g. `Cases handled by bot count`) generally **cannot combine with a breakdown dimension** — build them as standalone KPI numbers, not per-channel tables.
- Time-based Measurements (handling time, latency) default to **Sum** aggregation — switch to **Average** for anything that's already a per-case/per-message average, or Sum will silently show inflated/zero-looking totals.

## Notes / gaps
- This is Service Analytics on **space-prod3** for Qatar Railways specifically — category/report names (SmartFAQ Report, Omnichannel Case Summary Report) may be client-provisioned, not universal OOTB names. Re-verify live on other clients rather than assuming these exact report names exist.
- Related: [[standard-reporting]] (classic dialogue-tree bot dashboard), [[ai-agents]] (AI Agent Builder config, not reporting).
