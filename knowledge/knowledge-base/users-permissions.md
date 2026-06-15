# Users, User Groups, Roles & Permissions (KB 122)
**Source:** Product Foundation Courses → Knowledge Base - Users, User Groups, Permissions, Personas, Roles → **"KB Microskills - Users, Roles and Permissions" PDF** (slide deck; no course video) · **Help:** search `site:sprinklr.com/help knowledge base roles permissions`

## What it is
How access to Knowledge Base is controlled — by attaching **roles/personas** (which carry **permissions**) to **users and user groups**.

## The model (logins → roles → permissions)
- **Logins:** **User(s)** and **User Group(s)** — who signs in.
- **Roles / Personas:** the role attached to a login determines what it can do in KB.
- **Permissions (KB-relevant):** what the role is actually allowed to do.

## KB roles → permissions

| Role / Persona | KB permissions granted |
|---|---|
| **Knowledge Base Administrator** | **ALL permissions** |
| **Content Manager – Approver** | **Approve** (articles) |
| **Content Creator** | **Create / Edit / Upload / Delete** articles |
| **Agent** | **View** only |

- Permissions are **cumulative by responsibility**: Admin = everything; Approver adds approval rights; Creator can author/edit/upload/delete but not approve; Agent can only consume (view).

## Notes / gaps
- Source is a short "microskill" slide deck (the deck then shows a **Permissions Demo** in-platform, not captured as text). Confirm exact permission-key names and how to attach roles in **All Settings → Users / User Groups / Roles** against `sprinklr.com/help` or the live platform.
- The approve/create split maps directly onto the [[tiered-approval]] workflow (Creator submits → Approver approves).
- Related: [[enablement]], [[tiered-approval]], [[change-management]].
