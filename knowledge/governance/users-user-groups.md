# Users & User Groups (Governance 002)
**Source:** Product Foundation Courses → Sprinklr Services - Governance / 002 User and User Groups basics (video transcript + demo) · **Help:** search `site:sprinklr.com/help user types workspace global admin`

## What it is
**Users** are the most fundamental entity in Sprinklr — required to access the platform. Find them via **Launchpad → search "Users"** → the Users page lists everyone who can access that partner.

## The 4 user types (hierarchy, highest → lowest)
1. **Global Admin** — highest level; all access across the system, at the **partner** level (top of the hierarchy within that partner).
2. **Global User** — can navigate/work **across workspaces** but has **no admin rights**.
3. **Workspace Admin** — admin rights **only within their workspace** (not in other workspaces). *(A partner — e.g. "Sprinklr QA prod0" — contains multiple workspaces.)*
4. **Workspace User** — lowest; can only work/access within **one specific workspace**.

## Creating a user (fields)
- **First name, Last name, Email ID** (the email the user belongs to).
- **Language** — set by user locale; the platform UI loads in that language at login.
- **Persona** — optionally enable **persona-based experience**; define which persona the user works in (e.g. agent persona, supervisor persona). Covered in its own segment.
- **Custom properties** — tag user-level custom properties per use case.
- **User Group** — optionally add the user to a user group (see below).
- **Default handles** — per channel (Facebook, LinkedIn, YouTube, Twitter…), which of the shared handles is **preselected** for that user.
- **Assignment capacity** — how many cases the user can be assigned (used by the **older** assignment engine).
- **Skills** — for **skill-based assignment** (cases with a detected skill go only to users with that skill).
- **Roles & Permissions** — assign **global roles** (global level) and/or **workspace roles** (workspace level); same global/workspace hierarchy. Covered in [[roles-permissions]].

On **Save**, the user is created and receives an **email** with a login link for the environment (e.g. prod0).

## After creation — managing a user
- **Details** view: properties set, the **dynamic/static user groups** the user is in, and the **roles** assigned.
- **Edit** reopens the creation page to update properties any time.
- **Permissions** view: which permissions the user has (none if not added to any global/workspace role).
- **Default signature** — auto-appended when the user replies on a channel (agent name/signature shown to the customer), so the agent needn't type it each time.

## Notes / gaps
- This is the foundation of the [[users-permissions]] (KB) model; **roles & permissions** detail is in [[roles-permissions]], **personas** in the persona segment.
- **User Groups** (static/dynamic) are referenced here and assigned at creation; the deeper user-group mechanics were to be covered later in the same module.
- Part of Governance: [[roles-permissions]], [[accounts-account-groups]], [[customer-vs-workspace]], [[custom-fields]], [[macros]], [[queues]].
