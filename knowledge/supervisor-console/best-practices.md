# Supervisor Console Best Practices (Supervisor Console 049)
**Source:** Product Foundation Courses → Supervisor Console / 049 Supervisor Console Best Practices (video transcript) · **Help:** search `site:sprinklr.com/help supervisor console best practices my team my reportees share persona`

## Defining team members (My Team / My Reportees)
The agent screen offers **My Team**, **My Reportees**, and **All Agents**.
- **All Agents** governance: a **global admin** sees all agents across workspaces; a **workspace user** sees only their workspace's users; a **workspace admin** sees that workspace's admins + users; **global users** see workspace users + the workspace admin of their workspace.
- **To populate My Team / My Reportees, set the agent's Manager field** (asked during discovery — get the client's team structure). When creating an agent, fill the **Manager** field.
  - **My Reportees** = the **immediate** people reporting to me.
  - **My Team** = the **entire hierarchy** below me. (e.g. A reports to B, B reports to C → C's "My Team" = A+B; C's "My Reportees" = B.)
- This is a **permission-controlled field** ("all users accessible") under Supervisor Console.

## Refresh interval
Screens (agent/queue monitoring) refresh every **15 seconds** by default. Can be reduced to a **minimum of 5 seconds** — but only via a **support ticket** after checking the servers.

## Sharing Reporting & Engagement dashboards to the persona
To control which dashboards appear in the persona's Reporting section:
1. **Care Reporting** → select the dashboard → top-right **⋮ → Share**.
2. Select the **User / User Group** AND the **Persona**. These act as an **AND** — the dashboard shows only to users who are in that user group **and** have that persona assigned.
3. Same structure for **Engagement Dashboards** (share with persona + user, AND operator).

## Bulk-assign personas to agents
1. **All Settings → Configuration Tools** → search **Users** → **Export** the configuration file.
2. In the file, set two fields per user: **Persona App** (the persona name) and **Supervisor View Enabled** = **true/false** (true enables the persona view). (Analogous to the two fields set when creating a user: persona name + enable flag.)
3. **Import** the edited file (Configuration Tools → Import) → personas updated in bulk.

## Quick filters
On the Agent Monitoring screen → **Show Filters** → create filters (e.g. by states, by user groups) for reuse.

## Notes / gaps
- Underpins all the monitoring screens ([[agent-monitoring]], [[queue-monitoring]], [[campaign-monitoring]]); dashboard sharing ties to [[organising-creating-dashboards]]; persona config in [[persona-builder]]. Manager field + permissions relate to [[users-user-groups]] / [[roles-permissions]].
- Part of Supervisor Console: [[home-page-features]], [[agent-monitoring]], [[queue-monitoring]], [[callback-monitoring]], [[campaign-monitoring]], [[announcement]], [[peer-to-peer-chat]], [[persona-builder]].
