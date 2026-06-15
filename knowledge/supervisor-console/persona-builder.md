# Persona Builder (Supervisor Console 050)
**Source:** Product Foundation Courses → Supervisor Console / 050 Persona Builder (video transcript + Persona App Manager builder screenshot) · **Help:** search `site:sprinklr.com/help persona app manager build persona tabs components`

## What it is
The **Persona App Manager** lets you create/edit **persona apps** and configure them to a client's custom use case — add/remove tabs, set default dashboards, define statuses that trigger the snackbar (agent available/unavailable), define universal-search components, and add most enterprise modules.

## Where it lives
**All Settings → Manage Customer → Persona App Manager.** Lists personas per product suite — e.g. **Sprinklr Service** care personas: standard **Agent, Supervisor, Quality Manager, Agent Assist** (plus Conversational AI / Conversational Analytics).

## Persona construct (3 components)
A persona app has three menu-item groups:
- **Primary** — top (e.g. Search / universal search).
- **Secondary** — the main tabs (Home, Agents, Queues Monitoring, Campaign Monitoring, Callbacks, Quality Manager, Alerts, Announcement, Reports, Console).
- **Footer** — bottom (e.g. notification/profile icon, Open Teams Chat, Call). Each item has a **Label** + **Icon**.

## Editing a persona
Open a persona in the App Manager → it shows **Primary / Secondary / Footer**.
- **Rename:** click the **share** icon → change the name; define **who** sees it in the **Hyperspace view** (the persona cards) by adding user groups (controls which cards each person sees).
- **Clone** (⋮ → Clone) — duplicate an existing persona without changing the original; name it, pick the **suite**, choose an **icon**.
- **Add / remove components** — e.g. delete the **Call** icon from a group, add tabs, etc.
- **Update Draft** → **Preview** (see the draft without affecting end users). Changes go live **only when you Publish**. **Reset to Live** reverts the draft.

## Notes / gaps
- The persona built here is what's shared to users (see [[best-practices]] for bulk persona assignment + dashboard sharing); tabs surface the monitoring screens ([[agent-monitoring]], [[queue-monitoring]], [[campaign-monitoring]], [[callback-monitoring]], [[announcement]]). Persona/voice concept also in [[persona]] (Inbound Voice).
- Part of Supervisor Console: [[home-page-features]], [[agent-monitoring]], [[queue-monitoring]], [[callback-monitoring]], [[campaign-monitoring]], [[announcement]], [[peer-to-peer-chat]], [[best-practices]].
