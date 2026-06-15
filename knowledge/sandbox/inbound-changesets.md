# Inbound Change Sets (Sandbox 193)
**Source:** Product Foundation Courses → Sandbox - Inbound Change sets (193, video transcript + demo) · **Help:** search `site:sprinklr.com/help sandbox inbound change set deploy rollback`

## What it is
An **inbound change set** is the **opposite entity of an outbound change set** ([[outbound-changesets]]). When an outbound change set is created in the **source** environment, its corresponding **inbound** change set is created in the **destination** environment. To make pushed entities **reflect** in the destination, you **deploy** the inbound change set.
- **On-demand, not auto-deployed** — deployment is triggered manually, giving **full control over timing** in the destination.

## Why it matters
- **Review / plan / deploy** changes in appropriate time slots after aligning with stakeholders — full **access control with granular permissions**.
- **Preview** before deploying — see the entities being transferred and **what will happen post-deployment** (expected outcome without actually deploying).
- **Rollback** — after deployment, if the migrated config has errors, **revert to the previous state with one click** → maintains integrity, minimizes downtime.

## Deploy an inbound change set (demo)
1. In the destination/production env: **All Settings → Sandbox Manager → Inbound Change Sets**.
2. A change set in **New** status shows a **Deploy** option. First click **Preview** → a pop-up generates (takes a few seconds); **download** the preview.
3. The **preview** lists: **Object type, Object ID, Object name, Action type**, and the key field **Operation Executed** — showing whether each entity will be **updated & altered**, **updated & unaltered**, or **created** once deployed.
4. If the preview matches expectations → **⋯ → Deploy**.
5. If, after deploy, the migration isn't as expected → **⋯ → Rollback**.

## Inbound change set statuses
- **New** — ready to be exported/deployed/deleted in the child environment.
- **Processing** — being deployed in the child environment.
- **Queued** — waiting for current change sets to finish.
- **Deployed** — final, deployed in the child environment.
- **Rolled back** — change set was reverted.
- **Error / Failed** — didn't deploy due to an error.

## Notes / gaps
- Inbound (deploy side) is the counterpart to [[outbound-changesets]] (create/send side); together they are the migration mechanism (also framed in KB [[change-management]]).
- Additional resources: Sprinklr **Help** articles + the **mandatory Sandbox Learn course**.
- Part of Sandbox: [[features]], [[refresh]], [[outbound-changesets]], [[alm-best-practices]].
