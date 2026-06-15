# Accounts & Account Groups (Governance 004)
**Source:** Product Foundation Courses → Sprinklr Services - Governance / 004 Accounts & Account Groups (video transcript + demo) · **Help:** search `site:sprinklr.com/help add social account account permissions`

## What it is
Brands add their **accounts** (social accounts, voice accounts) into Sprinklr to manage operations, interact with customers, and for benchmarking/listening/reporting. Sprinklr supports **30+ social channels**.

## Accessing accounts
- **Launchpad → search "Accounts"** (Social Accounts) → the accounts page for that workspace lists already-added accounts.
- **Search** by account name; **filter** by channel; **quick filters** (e.g. Active/Inactive) — and create custom quick filters.

## Account details & ID
- **⋯ → Details** shows: properties, **permissions** (which users have which access), and **activity** (when added, by whom, changes since).
- **Share** an account: copy the link and share with another user.
- **Account ID:** copy the account's URL; the **numeric value between `%2F … %2F`** (the last segment) is the account ID — use it when raising support tickets for account issues.

## Editing & per-account permissions
- **Edit** to change name, owner, sharing, subscribers, or properties after adding.
- Grant **granular permissions per account** to users/user groups:
  - **Publish** (publish from this account)
  - **View Reporting**
  - **Channel-level actions** (e.g. on Facebook: hide a comment, like a comment, etc.)
  - **All permissions**
  - **View in Global Planner**
- **Subscriber:** subscribe to an account so that if it gets **deactivated** (e.g. due to low volume) you receive an **alert** (triggered once per 24h) — prevents silently losing an account and mistaking it for "no new queries".

## Adding / deactivating / deleting accounts
- **Add:** you must be an **admin (or have admin rights) of the account**. Pick the channel, fill the details in the UI, add.
- **Deactivate:** if no longer needed — and you can **reactivate** later.
- **Delete:** possible from the UI for most; some accounts need a **support ticket**. **Deleting removes all associated data** → **prefer deactivating** so reporting data is retained.

## Why manage accounts from Sprinklr (vs natively)
- Sprinklr's **AI capabilities** — e.g. **Intuition moderation** on incoming messages — and the scale problem: high-volume brands (Google, Facebook) can't natively reply to every comment, so Sprinklr's automation/routing manages it.

## Notes / gaps
- The "**Account Groups**" portion (grouping accounts) wasn't detailed in the captured transcript beyond the accounts management above — confirm account-group creation on `sprinklr.com/help` / live.
- Per-account permissions tie into [[roles-permissions]]; accounts are assigned to users as **default handles** in [[users-user-groups]].
- Part of Governance: [[users-user-groups]], [[roles-permissions]], [[customer-vs-workspace]], [[custom-fields]], [[macros]], [[queues]].
