# Sandbox Features (Sandbox 191)
**Source:** Product Foundation Courses → Sandbox - Sandbox Features (191, video transcript) · **Help:** search `site:sprinklr.com/help sandbox manager environment`

## What it is
A **Sandbox** is a standalone environment that is a **replica of a brand's production environment**, used for **development, testing, and training** without touching production live data.

- Sandbox and production sit on the **same server** (e.g. AWS or Azure).
- Brands **move entities** (configs) between environments — build in sandbox, test, then migrate to production.
- Every migration has a **detailed audit trail**.

## Why it matters (4 risks Sandbox safeguards against)
1. **Human error** — e.g. a team unintentionally updates/deletes a custom field, breaking workflows. Fix is slow (must correct every impacted entity). With sandbox, make/test the change there first, then migrate.
2. **Critical system downtime** — direct production changes are risky and can interrupt live components across departments → hours of correction. Avoided by using sandbox.
3. **Limited innovation** — hard to adopt/test new features safely in live; sandbox is a **playground** to test without hampering production.
4. **Insufficient training** — new users need practice before going live; sandbox acts as a **training environment**.

## Unique capabilities (covered in detail across this module)
1. **Refresh** — cloning the production environment into the sandbox. → [[refresh]]
2. **Change set** — migrate entities/configs between environments. → [[inbound-changesets]], [[outbound-changesets]]
3. **Rollback** — any unwanted migrated change can be instantly rolled back.
4. **Audit trail** — full version history of actions taken while migrating entities.
5. **Account Mapping** — test real workflows with **test accounts**.
6. **Granular Permissions** — access to Sandbox and its features is governed per user via permissions.

## How to get a sandbox set up
- Setup is a **back-end process** done by the **Sprinklr support team** — raise a support ticket (e.g. to the Sprinklr support email / ticket address).
- Ticket body should include: **reason** for the sandbox, **production partner name**, **production partner ID**, **sandbox name/description**, whether it should be **premium or not**, the **environments** to connect, and a **user suffix**.
- Support then enables the sandbox for the brand.

## Accessing the sandbox (demo)
1. In your **production** environment, go to **All Settings → Sandbox Manager** (requires the correct permissions to view).
2. Sandbox Manager shows **connected environments** plus the **inbound** and **outbound change sets**.
3. Open **connected environments** — e.g. production may have several sandboxes connected.
4. Log into a sandbox using your **email + the user suffix** appended to your email ID, then your password.
5. Distinct visual cue: once logged into a sandbox, the **top bar is blue**. The environment is a replica of production — train/test/build freely there.

## Notes / gaps
- Additional resources: Sprinklr **Help** articles for Sandbox, plus a **Learn course** — recommended before anyone starts working in a sandbox.
- "Premium" sandbox is a ticket option but the tier difference isn't detailed in this video.
- This is the module overview; the listed capabilities are detailed in [[refresh]], [[inbound-changesets]], [[outbound-changesets]], [[alm-best-practices]].
