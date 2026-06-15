# Outbound Voice — Campaign Management (Reporting 080)
**Source:** Product Foundation Courses → Reporting / 080 Outbound Voice Use Cases - Campaign Management (video transcript + Campaign Management Dashboard screenshot) · **Help:** search `site:sprinklr.com/help outbound campaign management dashboard hit rate connected abandoned`

## What it is
A key report for **dialer admins / unit heads** to monitor campaign performance — calls per campaign/segment, connect rates, hit rate, abandon rate.

## Dashboard columns (example)
Campaign, Segment Name, **Dialer Type** (Predictive/Preview/Manual), **Total Records**, **Records Called**, **Customer Answered**, **Agent Connected**, **Connected %**, **Dialed**, **Answered**, **Agent Connects**, **Hit Rate**, **No Answer / Busy / Abandoned**.
- **Dialed** = total attempts made in the campaign.
- **Hit Rate** = Answered Calls ÷ Dialed Calls.
- **Abandoned calls** = customer connected but **no agent connected**; track **Abandoned %**.

## Build it — which report + metrics
Use the **Voice Report** (not Voice Agent Performance) — you want overall call counts including calls where no agent connected.

**Standard dimensions/metrics:**
- **Campaign**, **Segment ID**, **Dialer Type** (mode of calling).
- **Total Profiles** (uploaded) → "Total Records".
- **Unique Profiles** (attempted) → "Records Called".
- **Call States** — used as filters to isolate agent-connected / customer-connected calls.
- **Call Count** — total attempts → "Dialed".
- **Call Exchange Completion Status** — system disposition (Complete / No Answer / etc.).

**Custom metrics (built on Unique Profiles with Call State filters):**
- **Customer Answered** — Unique Profiles, filter Call State **containing "Customer Connected"**.
- **Records Connected (agent)** — Unique Profiles, filter Call State containing **Customer Connected AND Agent Connected** (separate-line filters = **AND**; same-line = **OR**).
- **% Connected** — Agent Connected ÷ Total Records.
- **Total Dialed** — Call Count.

> Filter reminder: filters on the **same line** are combined with **OR**; filters on **separate lines** are combined with **AND**.

## Notes / gaps
- Uses [[voice-backend-structure]] (Voice Report) + [[custom-metrics]] with [[filtering]]. Campaign/segment/dialer config is in the Outbound Voice module.
- Part of Reporting (Voice/Outbound): [[outbound-voice-overall]], [[outbound-voice-agent-performance]], [[outbound-voice-schedule-callback]], [[outbound-voice-ingestion-report]].
