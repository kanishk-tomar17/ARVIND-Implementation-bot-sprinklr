# Record Manager — Bulk Actions & Bulk Delete (Custom + Standard Entities)

**Question this answers:** "Can I bulk delete records of an entity?" — asked for custom entities, but the rule is the same for standard ones.

**Sources:**
- [Record Manager Types, Views, and Density](https://www.sprinklr.com/help/articles/record-manager-types-views-and-definitions/record-manager-types-views-and-density/693bab53f0afa271d1b9fb1b)
- [Record Manager — An Overview](https://www.sprinklr.com/help/articles/record-manager-an-overview/record-manager-an-overview/693bab341db8130c76ee0064)
- [Configure Actions Section for Record Manager](https://www.sprinklr.com/help/articles/configure-action-section-for-record-manager/configure-actions-section-for-record-manager/693bab70f0afa271d1ba2f54)

## Short answer
Yes — **but only from a Standard Record Manager.** Bulk delete is a property of the *Record Manager type*, not of the entity. A custom entity with no Standard Record Manager built over it has no bulk-delete surface in the UI.

## The rule: Record Manager type decides it
| Type | What it's for | Bulk actions? |
|---|---|---|
| **Standard Record Manager** | Default tabular view to manage records (Leads, Opportunities, Accounts, Customers, or any custom entity) | ✅ **"Supports bulk actions like updating, assigning, or deleting records."** |
| **Reporting Record Manager** | Metrics, charts, graphs; export reports | ❌ read/analyse only |
| **Pivot Reporting Record Manager** | Pivot-table multi-dimensional analysis | ❌ read/analyse only |

Views available on any type: **Table / Grid (cards) / List**. Density: **Spacious / Compact / Comfortable**.

## Where delete lives
Two distinct surfaces — don't confuse them:
- **Row-level actions** — hover a row → menu → **edit, delete, view details**. Per-record. Documented in the Record Manager overview.
- **Bulk actions** — multi-select in the grid, then act on the selection. Only on Standard. The overview says the grid "presents a list of records with capabilities to take bulk or row-level actions directly from the table."

## Trap: the configurable Actions section is NOT where bulk delete comes from
When you build a Record Manager, the **Actions** config section only exposes:
- **Global CTAs** — Open Form (create record), Run Data Connector, Initiate Guided Workflow
- **Header actions** — Refresh, Search Bar, Sort, Export, Column Manager, Freeze
- **Upfront filters**

There is **no "add bulk delete action"** toggle. Bulk delete is inherent to the Standard type, not something you configure in. If a consultant is hunting the Actions config for it, they're in the wrong place.

## Not documented (verify in the tenant before promising it)
The help center does **not** state:
- selection limits (how many records can be selected at once, whether "select all across pages" exists)
- whether bulk delete respects **View Policy** / permissions per user
- whether deletes are soft or hard, and whether they're recoverable
- whether **Triggers** or **Validation Rules** fire on bulk delete

Treat all four as unknown. Confirm in the client tenant on a throwaway record set before running a bulk delete on real data.

## If bulk delete isn't there
Fallbacks, in order of preference:
1. Build/switch to a **Standard** Record Manager over the entity (a Reporting one won't ever give you delete).
2. Export → clean → re-import via **Data Connector** (upsert/overwrite rather than delete).
3. API-driven delete.

## Safety
Bulk deleting entity records is irreversible in effect (recoverability undocumented). **Always confirm with the consultant, always filter down to the exact set first, and always test on a small selection.** Never run one during a takeover without explicit sign-off.
