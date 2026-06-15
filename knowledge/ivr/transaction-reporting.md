# IVR Transaction & Reporting (IVR 148)
**Source:** Product Foundation Courses → IVR / 148 IVR transaction and its reporting (video transcript + demo) · **Help:** search `site:sprinklr.com/help IVR transaction node level report flow reporting`

## What an IVR transaction is
A **transaction** = the **journey of a customer** once they reach the Sprinklr IVR. Sprinklr collects/analyses IVR data in various formats: **call volume, call duration, menu selections, call outcomes** — used to improve CX, find issues, and spot customer-behaviour trends.

## Node-level execution reports
Access: **IVR Flow Manager → ⋯ → View Reports** → a **node-level execution report** for the IVR flow. Set a **time range** and add **filters** (e.g. by case number).

### Important metrics
- **Total Calls** — sum of calls that landed on that IVR.
- **Number of Unique Users** — unique callers.
- **Average IVR Time** — avg time users spent on the IVR.
- **States per Call** — avg number of **steps** completed per call (each node = a step, first & last node counted).
- **IVR Contained** — calls completed **within the IVR** (not transferred to an agent).
- **Agent Transfers** — calls transferred to agents.
- **Incomplete Calls** — calls disconnected mid-IVR.
- **Per node:** number & **percentage of calls that reached that node successfully** → debug **up to which node** a call reached.

## Use cases of flow reporting
- Identify nodes causing issues (e.g. **high abandonment**) and nodes performing well (apply best practices elsewhere).
- Track a **particular call** — exactly what happened, at which node it abandoned.
- Understand caller behaviour.

## Notes / gaps
- "Enabling transactions" on critical paths also drives the [[disconnect-journey]] (detect drops between transactions). Node-level data is the IVR's analytics layer.
- Part of IVR: [[communication-nodes]], [[disconnect-journey]], [[api-integration]], [[system-nodes]], [[pci-input]].
