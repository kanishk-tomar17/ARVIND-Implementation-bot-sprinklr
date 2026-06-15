# Sandbox Refresh (Sandbox 192)
**Source:** Product Foundation Courses → Sandbox - Sandbox Refresh (192, video transcript) · **Help:** search `site:sprinklr.com/help sandbox refresh manager`

## What it is
**Sandbox refresh = the act of cloning the production configuration into the sandbox environment** (with limitations).

- **Limitation — account data is NOT cloned.** A brand's production **account data cannot be moved to sandbox** for **compliance reasons**. Only configuration is cloned.
- On refresh, **all existing config in the sandbox is wiped** and the **latest production config is imported** fresh.
- **Irreversible** — exercise extreme caution; a refresh removes all existing sandbox config.
- **Unidirectional** — you can only refresh a **sandbox from production**, never production from sandbox.

## When to use
- Whenever the brand needs the **latest production configuration** reflected in sandbox.
- Periodic refresh keeps the sandbox **up to date and aligned** with production's latest configs, software version, and system updates → accurate, reproducible testing/development.
- **Best practice: refresh at the start of a sprint / new project** to maintain integrity between the two environments.

## Configuration steps (how to refresh)
1. Go to the **production environment** (refresh can only be triggered from production).
2. **All Settings** (top menu, or **Platform Modules → All Settings**).
3. With the correct permissions, open **Sandbox Manager**.
4. Open **Connected Environments** — lists all sandboxes connected to this production environment.
5. On the sandbox you want to refresh, click the **three dots (⋯) → Refresh Sandbox**.
6. A **confirmation** prompt warns it will **wipe all data/config** in that sandbox.
7. Click **Yes** → the sandbox refresh starts.

## Notes / gaps
- Because refresh **wipes** the sandbox, migrate any sandbox-only work back to production (via outbound change set) **before** refreshing, or it's lost. See [[outbound-changesets]].
- Account data exclusion means workflows needing real accounts use **Account Mapping** / test accounts instead (see [[features]]).
- Additional resources: Sprinklr **Help** articles on sandbox refresh + the **Sandbox Learn course** (recommended before working in a sandbox).
- Part of the Sandbox module: [[features]], [[inbound-changesets]], [[outbound-changesets]], [[alm-best-practices]].
