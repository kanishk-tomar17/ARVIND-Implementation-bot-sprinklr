# Unified Routing — Debug Console

**What it is:** The Debug Console shows the **specific reasons cases were waiting within a queue over time** — historical, case-level insight into *why* assignment didn't happen. Use it to spot bottlenecks (no eligible agent, capacity full, skill mismatch, outside business hours, etc.) and improve routing.

**When to use:** a case sat in a queue too long / wasn't assigned, and you need the recorded reason rather than a live guess. This is the historical companion to live troubleshooting (agent availability, capacity, skills) — see [[troubleshooting-assignment]].

**Where:** Unified Routing app → **Debug Console** tab (`/unified-routing-app/unified-routing/debug-console`). It has two sub-views: **Debug Console** and **Reporting Dashboard**.

> ⚠️ **Permission-gated (VERIFIED live 2026-06-18):** opening Debug Console returned **"Access Denied — you don't have permission to access this page"** even for a **Global Admin**. So access needs a specific Unified Routing debug permission/feature enablement (grant the relevant permission in the role, or have the Sprinklr product team enable it) — being Global Admin is not sufficient. Flag this to the consultant if they can't open it.

## How to use (high level)
- Open Debug Console, scope to the queue / case / time window.
- Read the **assignment wait reasons** logged per case over time (this is the same data surfaced by the help center's "Historical Assignment Wait Reasons").
- Cross-reference with [[troubleshooting-assignment]] (live checks: View Details → Messages/Assignees, Assignment Failures tab) and [[routing-configuration]] (relaxation/backup) to fix the root cause.

## Notes & gaps
- Exact filters/columns not yet captured from the live UI (UR sub-nav was flaky during exploration). When a consultant uses it, read the screen and enrich this file.

**Source:** sprinklr.com/help → "Components of Unified Routing" (`/articles/unified-routing-overview/components-of-unified-routing/6985c271243d9d29873a5255`) + *Inbound Voice > Setting up Unified Routing > Assignment Failures & Troubleshooting* — "Historical Assignment Wait Reasons" (`/articles/assignment-failures-troubleshooting/historical-assignment-wait-reasons/68ca6de6c8792738a66aa935`). Related: [[overview]], [[troubleshooting-assignment]].
