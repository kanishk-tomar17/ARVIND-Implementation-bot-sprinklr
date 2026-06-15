# Outbound Change Sets (Sandbox 194)
**Source:** Product Foundation Courses → Sandbox - Outbound Change sets (194, video transcript + demo) · **Help:** search `site:sprinklr.com/help sandbox outbound change set deploy`

## What it is
An **outbound change set** sends **configuration from one environment to another**. E.g. you create/update a rule in sandbox and want to push it to production — do it via an outbound change set.

- The user **selects the entities** to transfer.
- **Dependent entities** — objects the user didn't pick but that the selected objects depend on (e.g. a rule's **custom fields** or **triggers**). The system **automatically adds** these alongside the selected objects during creation. Sandbox has provisions to **control the movement of dependent entities** (see Action type below).
- **Direction is versatile:** outbound change sets can be pushed **sandbox→sandbox, sandbox→production, and production→sandbox**.

## Why it matters
- Enables **controlled release management** — select exactly what to transfer, so only **thoroughly tested/validated** entities reach production.
- Mitigates risk and **prevents introducing bugs** into production.

## Configuration steps (create an outbound change set)
1. In the **production environment** (or source env), go to **All Settings → Sandbox Manager → Outbound Change Set**.
2. The list shows outbound change sets already created from this environment. Click **Create New**.
3. Fill the form:
   - **Name** + **Description** (mandatory). **Tags** is optional — can skip.
   - **Action type** (important — controls how the change set behaves):
     - **Update if exists** — the normal sandbox functionality: new objects are created, existing objects (and **dependent objects** travelling along) are **updated** in the destination.
     - **Skip if exists** — only **new** objects are created; any existing object with the **same ID** in the destination is **skipped** during deployment.
     - **User selected updates only** (newer option) — new objects get created and **only the user-selected objects get updated**; any **dependent entity** in the change set is **skipped** in the destination.
   - **Destination** — pick the target environment (e.g. a QA sandbox).
   - **Entities** — choose entity type (e.g. **Rule**), then filter by conditions or search; select the specific items (e.g. 1 rule out of thousands).
4. Click **Save**.
5. The change set appears in the list, first in **Processing**, then moves to **Sent** state.
6. **Sent** means it's ready — it gets **deployed when the user deploys it in the destination environment** (see [[inbound-changesets]]).

## Export (governance)
- For a **Sent** change set: hover the **options (⋯) → Export** → generates an **Excel file** listing the objects moving between environments. Good for **governance / audit** of what's being migrated.

## Notes / gaps
- An outbound change set on the source side becomes an **inbound change set** to deploy on the destination side → [[inbound-changesets]].
- The three **action types** are the key control for how existing objects and dependents are treated — choose deliberately to avoid overwriting production config.
- Part of the Sandbox module: [[features]], [[refresh]], [[inbound-changesets]], [[alm-best-practices]].
