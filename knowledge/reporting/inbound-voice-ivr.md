# Inbound Voice Use Cases — IVR Reporting (Reporting 076)
**Source:** Product Foundation Courses → Reporting / 076 Inbound Voice Use Cases - IVR (video transcript + IVR Tree Journey report screenshot) · **Help:** search `site:sprinklr.com/help IVR reporting tree journey funnel call abandoned within IVR`

## What it is
Four ways to report on IVR: **Tree Journey, Funnel, custom (B2B) reporting, Leg reporting.**

## 1. IVR Tree Journey reporting
Traces the call's path through the IVR — which nodes calls went into and where they dropped.
- **Access:** Admin screen → **Voice IVR** → pick an IVR → **View Reports**.
- **Top numbers:** Total Calls, No. of Unique Users, Avg IVR Time, Steps Per Call (avg nodes covered), **IVR Contained**, **Agent Transfers**, Incomplete/Complete Calls.
- **Node tree:** each node shows the **% of calls that reached it** and where calls **dropped** (e.g. 25% dropped at a node) — use to analyse the flow.

## 2. IVR Funnel reporting
A **standard dashboard** (IVR Journey Report). Key metrics (apply **Direction = Inbound** at section level, since every inbound call hits IVR first):
- **Total IVR Calls** — Call Count.
- **Calls Completed within IVR** — started in IVR, never requested an agent.
- **Short Calls in IVR** — below a threshold (default **10 seconds**, **not editable in the UI** — configurable only via a Sprinklr support ticket). Distinct from queue-level **Short Abandoned** (default 5s, editable per work queue — see [[queue-standard-metrics]]).
- **% Calls Abandoned within IVR** — calls that entered IVR and didn't request an agent.
- **Average IVR Time** — metric **IVR Time**.
- **Configure "abandoned/completed within IVR"** as a **custom metric**: filter **Call State NOT containing "Requested for an Agent"** (Call State is the key metric to slice agent-connected vs not).
- For **multiple IVRs**, use the **IVR** dimension to break down call count / abandon / agent-requested / avg IVR time per IVR.
- **Language Call** dimension — calls per language (NA appears when the customer didn't select a language initially).

## 3. Custom / B2B reporting
Business-specific reporting, e.g. by **product selected in IVR**, **customer tier**, or **location** (calls per tier/location).

## 4. IVR Leg reporting
For leg-based journeys (point A → B): how many journeys triggered, customers who entered a leg, left it incomplete, or completed it.
- **Wrong input** reporting → use **Process Execution Analytics** (Guided Workflow IVR runs through process engines).

## Notes / gaps
- Uses the voice reports from [[voice-backend-structure]]; IVR config in the IVR module ([[ivr]], [[communication-nodes]], [[system-nodes]]). Custom metrics built per [[custom-metrics]].
- Part of Reporting (Voice): [[voice-backend-structure]], [[live-reporting-voice]], [[inbound-voice-agent-performance]], [[inbound-voice-queue-report]].
