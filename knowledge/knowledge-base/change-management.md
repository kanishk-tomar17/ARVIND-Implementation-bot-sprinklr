# Change Management — Inbound/Outbound Changesets (KB 131)
**Source:** Product Foundation Courses → Knowledge Base - Change Management → **"KB Microskills - Change Management" PDF** (slide deck; no course video) · **Help:** search `site:sprinklr.com/help change management changeset entities environments`

## What it is
Moving **entities** (configuration building blocks) **between environments** via changesets — the KB/Sprinklr-Services view of the same mechanism covered in [[inbound-changesets]] / [[outbound-changesets]] (Sandbox module).

## Entities
- **Entities = fundamental assets / building blocks**, aggregated and used together across different products.
- Entities are **moved across environments** (mainly **dev, staging, prod**) to: **test new features**, **simulate bugs and fixes**, and **reflect updates on the LIVE instance**.
- KB-relevant entities that get moved: **Users/User Groups, Roles, Permissions; Community Project; Knowledge Base; Tiered Approvals; Reporting Dashboards** (plus "other entities").

## How change management works when moving entities
A staged promotion path:
1. **dev** — *changes NOT visible to real-time users.* Where specific elements (e.g. new features) are **added / tested / fixed first for sanity**.
2. **staging** *(optional)* — *changes NOT visible to real-time users.* Where **general functioning is tested robustly** to simulate real scenarios.
3. **prod** — *changes ARE live and visible real-time.* Where the product is **made accessible in its entirety** to all users; any/all changes are **reflected real-time**.

→ Promote dev → (staging) → prod; only thoroughly tested entities reach prod.

## Notes / gaps
- This is the **conceptual** view; the actual **inbound/outbound changeset** mechanics (create, action types, deploy, export) are the same as the Sandbox module — see [[outbound-changesets]] and [[inbound-changesets]] for the step-by-step.
- The **Change Management Demo** is shown in-platform (not captured as text).
- Related: [[features]] (Sandbox), [[refresh]], [[users-permissions]], [[tiered-approval]].
