# Application Lifecycle Management & Best Practices (Sandbox 195)
**Source:** Product Foundation Courses → Sandbox - Application Lifecycle Management and best practices (195, video transcript) · **Help:** search `site:sprinklr.com/help sandbox ALM best practices change set`

## What it is
**ALM** = how to use **multiple sandboxes** across a project and the steps for each action when working in sandbox.

## Recommended setup — 2 sandboxes (dev + staging)
Ideal: a **dev** sandbox (build configs) + a **staging/QA** sandbox (test configs). (Names are just conventions.) Flow:
1. **Refresh dev** → latest prod config in dev.
2. **Build new configs** in dev.
3. **Test thoroughly** in dev (can take days–weeks).
4. **Refresh staging** → so it has latest prod config before you move work into it.
5. **Enact a prod freeze** (no other production changes during testing).
6. **Move configs dev → staging** via change sets and **deploy**.
7. **Full UAT** on new configs in staging **+ sanity** of older workflows.
8. **Move configs → production** via change sets, **deploy in prod**, then **final sign-off**.

## Variations
- **One sandbox only:** build + test in that sandbox, then move directly to production (no separate test env) — **risky**; two sandboxes is recommended to mitigate risk.
- **More than two sandboxes:** multiple teams develop in **silos** (team 1 → dev1, team 2 → dev2, …); all changes converge into **one staging/UAT** sandbox for combined testing, then to production.
- **Rollback** can be used any time after deployment if changes don't behave as expected.

## Best practices — implementation
- **Account Mapping is your best friend** — map **test accounts** (added in sandbox) to production accounts; inbound/outbound messages on the test account then run the **same workflow** as the prod account. (And **Rollback** as a fallback.)
- **Always make a new copy of an object before changing it**, so you can fall back to the original entity.
- **Clear ownership:** ideally **one person** (max two, closely coordinated) should push change sets and do refreshes.
- **Always check dependencies** when deploying a change set (detail in [[outbound-changesets]]).

## Best practices — creating change sets
- **Create change sets at entity level** — one change set per entity type (e.g. one for custom fields, one for macros, one for rules) so any discrepancy can be **rolled back individually**.
- **Rollback in reverse order** — if deployed A → B → C, roll back C → B → A.
- Use **created/modified time filters** to push **only** the required entities (nothing missed, nothing extra).
- **Deploy one change set at a time** — deploy, test, then deploy the next.

## Notes / gaps
- Ties together the whole Sandbox module: [[refresh]] (step 1/4), [[outbound-changesets]] (create/send), [[inbound-changesets]] (deploy/rollback/preview), [[features]] (account mapping, rollback, granular permissions).
- Additional resources: Sprinklr **Help** + the **mandatory Sandbox Learn course**.
