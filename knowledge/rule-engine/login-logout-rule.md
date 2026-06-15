# Login / Logout Rules (Rule Engine 015)
**Source:** Product Foundation Courses → Sprinklr Services - Rule Engine / 015 LoginLogout rule (video transcript + demo) · **Help:** search `site:sprinklr.com/help login logout rule unassign cases agent availability`

## What they are
- **Login rules** — triggered when a user **logs into** Sprinklr. Used to set the user's state on login (e.g. set **user status = Available**, change **user skills**).
- **Logout rules** — triggered when a user **logs out** (or **changes their status** themselves). **More commonly used** — they **unassign** the logging-out agent's cases and send them back into the assignment logic so the next available agent picks them up → protects customer response times.

**Why logout rules matter:** if an agent with 5 assigned cases logs out / goes unavailable, those cases would stay stuck on them until they return. Logout rules immediately unassign and re-route them.

## Login rule (demo)
- CONDITION: user group = e.g. "Customer Care Agents" → ACTION: change **user skills** and set **user status = Available** by default for agents in that group on login.

## Logout rule (demo) — the key one
On logout for the user group:
1. Set **user status = Unavailable**.
2. **Unassign cases** action block:
   - **Unassign cases** from the **Assigned** queue (specify which queue to unassign from).
   - **Add** the cases back to the **Awaiting Assignment / processing queue** so the **assignment engine / Unified Routing** re-picks them.
   - **Remove** them from the **Assigned** queue (the case is unassigned and may sit in awaiting-assignment before the next agent gets it).
   - Set **case status = Awaiting Assignment**.

## Two variants set up in practice
1. **Unassign on logout** — the base rule (no status-check condition).
2. **Unassign on status change** — add a condition **"Logout action via status change = Yes"** and specify the status (e.g. **Unavailable**); the action fires only when the user **changes status** (not a normal logout).

Live environments typically run **both** rules.

## Notes / gaps
- Feeds the assignment/routing loop — unassigned cases return to [[queues]] for the assignment engine / Unified Routing ([[routing-configuration]], [[troubleshooting-assignment]]). See the KB article for the full action/condition list.
- Completes Rule Engine: [[inbound-rules]], [[batches-triggers]], [[queue-rules]], [[case-update-creation]], [[on-demand-rules]], [[scheduler-engine]].
