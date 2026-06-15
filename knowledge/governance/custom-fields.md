# Custom Fields (Governance 006)
**Source:** Product Foundation Courses → Sprinklr Services - Governance / 006 Custom Fields (video transcript + demo) · **Help:** search `site:sprinklr.com/help custom fields create visibility`

## What they are
**Custom fields** are variables/tags defined against Sprinklr entities, indicating properties that entity holds — usable downstream in **reporting** and **custom workflows**.

## Entities a custom field can be defined on
- **Message** (inbound or outbound)
- **Account**
- **Case** (a bundle of messages)
- **Audience** (audience profiles)

A **single custom field can apply to multiple entities at once** (e.g. a "Country" field on Case + Message + Profile). It then holds **separate instances/values** per entity — the value on a case is independent of the value on a message or profile.

## Where to create
**Launchpad → Sprinklr Service → Custom Fields → Create custom field** → pick the asset(s) (case, message, audience profile, account).

## Custom field types (data types)
- **Single Select List** — list of values (e.g. India, USA, UK); pick **one**.
- **Multi Select List** — list; pick **multiple** values.
- **Text** — open text box; can set a **default value** (e.g. default Country = India; user can override).
- **Number**
- **Date** / **Date-Time**
- **Text Area**
- **Text Multi** — multiple text snippets in one field.

## Visibility control
By default a custom field is **visible across the platform / all workspaces**. You can scope it:
- **Workspace** / **Workspace group** (multiple workspaces grouped) / **all workspaces**.
- **Users** / **User groups** — only they can see it.
- **Advanced visibility filters** — show the field only when **another custom field holds a specific value** (e.g. show only when Campaign = X), so its values appear against the entity only under that condition.
- **Layout / reporting visibility** — control whether it appears in **reporting widgets** (exclude it so filtering can't happen on it) or expose it in **monitoring dashboards**.

## Notes / gaps
- Custom fields feed reporting and rules; they're a core entity migrated via changesets ([[change-management]]) and a common human-error target that Sandbox guards ([[features]]).
- Part of Governance: [[users-user-groups]], [[roles-permissions]], [[accounts-account-groups]], [[customer-vs-workspace]], [[macros]], [[queues]].
