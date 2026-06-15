# Roles & Permissions (Governance 003)
**Source:** Product Foundation Courses → Sprinklr Services - Governance / 003 Roles and permissions (video transcript + demo) · **Help:** search `site:sprinklr.com/help roles permissions workspace global`

## What they are
- **Permission** = the right to access a specific tool/part of Sprinklr (each product, and each settings area — accounts, custom fields, macros, queues, users, user groups — has multiple permission levels).
- **Role** = a **named collection of permissions** granted to relevant **users and user groups**. You don't assign permissions one-by-one; you club them into a role and assign the role.

## Creating / managing roles
- **Settings (in the managed workspace) → Roles.** Lists existing roles; search or **create new**.
- Create: give the role a **name**, then **select permissions** — all permissions of a module (e.g. all of Engagement Dashboard) or selected ones, **across multiple modules**.
- Assign the role to **individual users** or to a **user group** (all users in the group inherit it).
- **Why assign to a user group:** for 1000s of users / new joiners you don't assign manually — create a **dynamic user group** (users auto-added by criteria) and assign the role to that group, so membership (and thus permissions) updates automatically.
- **Details** of a role: which users/user groups are added, which permissions are granted, and the **activity log** (what changed, when).
- **Edit** (⋯ → Edit): add/remove permissions, add users/user groups. View **activity**; **Delete** if no longer relevant.
- A user can be assigned **multiple roles**.

## Role types & precedence
- **Workspace roles** (granted at workspace level) and **Global roles** (granted at global level; also "customer roles").
- **Precedence: Workspace role takes precedence over Global role.** If a global role grants all permissions but a workspace role grants only a few, the **workspace role's set wins** for that user (this is by configuration).
- Within **global roles**, scope can be **Global-Global** or **Global-Local** → **Global-Local takes precedence over Global-Global**.
- Workspace-level roles are **not applied across workspaces**; global roles **can** apply across workspaces.

## Troubleshooting access ("user A can do X, user B can't")
- Open the affected user's **Details → Permissions** and check whether they have the relevant permission.
- Compare the two users' permissions (Settings → Users → user details) — the one who can access has the permission; the one who can't, doesn't.

## Dashboard visibility (config admin)
- Engagement/Reporting **dashboards** are normally visible only to the **creator** and users it's **shared with**.
- Granting **Config Admin** permissions to a user/group lets them **view all dashboards** (listening, reporting, monitoring, production rule, profile list) **regardless of sharing**.

## Notes / gaps
- This is the engine behind the KB role model in [[users-permissions]] and is attached to users per [[users-user-groups]].
- Part of Governance: [[users-user-groups]], [[accounts-account-groups]], [[customer-vs-workspace]], [[custom-fields]], [[macros]], [[queues]].
