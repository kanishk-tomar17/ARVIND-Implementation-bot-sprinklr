# Customer vs Workspace (Governance 005)
**Source:** Product Foundation Courses → Sprinklr Services - Governance / 005 Customer Vs Workspace (video transcript) · **Help:** search `site:sprinklr.com/help customer partner workspace`

## The two levels
- **Customer = Partner.** A customer is a brand's dedicated **instance of Sprinklr** (its own slice of Sprinklr's code) where all that brand's configuration lives. E.g. a partner is created for Google, another for Nike. (Example partner in the demo: "Sprinklr QA Prod0".)
- **Workspace.** A customer contains **multiple workspaces** — think of each workspace as **one team** within a big customer (e.g. Google has YouTube, Google Ads, Google Cloud… 40+ teams).

## Why multiple workspaces under one customer
- Different teams have different requirements and **must not see each other's data/config**. Each workspace isolates that team's **users, accounts, custom fields**, and other onboarding entities.

## Customer level vs Workspace level (settings)
- Access via **Launchpad → settings → All Settings**. Two scopes: **Manage Workspace** and **Manage Customer**.
- **Customer level:** anything configured here is **accessible across all workspaces** (visible to any user in any workspace who has the role/permission to view it).
- **Workspace level:** only the things meant for that specific workspace.
- Maps to the 4 user types ([[users-user-groups]]): **Workspace admin/user** → only workspace-level things; **Global admin/user** → both global (customer) and workspace level.

## Why create a new workspace in an existing partner
- A **new team is onboarding**.
- A team's config is **old/obsolete** (5–10 yrs) — instead of retrofitting, spin up a **fresh workspace**, migrate only the necessary data (accounts + associated data), and configure cleanly.

## Deleting
- **Delete a workspace** (team leaving / merging) → **all that team's data is deleted**.
- **Delete a customer/partner** → **all associated data is deleted**.
- Account for this before deleting.

## Notes / gaps
- This is the structural container for everything else in Governance — roles/users/accounts exist at customer (global) or workspace scope. See [[users-user-groups]], [[roles-permissions]], [[accounts-account-groups]].
- Part of Governance: [[custom-fields]], [[macros]], [[queues]].
