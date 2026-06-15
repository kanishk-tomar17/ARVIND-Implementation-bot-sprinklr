# Engagement Actions, Macros & Search (Sprinklr Social — Engagement)
**Source:** sprinklr.com/help — Engagement sub-area (multiple articles; see links below)

## What it is
- How consultants act on dashboards and messages inside Sprinklr Social > Engage > [[engagement-dashboards]].
- Covers three things: dashboard-level actions (create/clone/share/lock/delete), applying [[macros]] to messages, and searching/filtering within engagement columns.
- Macros = one-click execution of multiple message actions saved as a reusable config.
- Search & filter let an agent find and narrow messages or cases within a column.

## Key features & how to use

### Actions in Engagement Dashboards (dashboard-level)
Access: Sprinklr Social → Engagement Dashboards (within Engage). Most actions live under the dashboard's **Options** icon (hover to reveal).
- **Create Dashboard:** Click "Create Dashboard" → fill required details → "Add".
- **Clone Dashboard:** Hover Options icon → "Clone Dashboard" → enter new Name + optional Tags → "Clone".
- **Edit Name & Tags:** Hover Options → "Settings" → "Dashboard Manager" → hover dashboard's Options → "Edit Dashboard" → set Name, Folder, Tags → "Save".
- **Share Dashboard:** Hover Options → "Share Dashboard" → choose visibility (All Workspaces / Workspace(s) / User(s) or User Group(s)) → "Share". Recipients open it via Dashboard Menu icon → "Shared Dashboard".
- **Lock Dashboard:** Hover Options → "Lock Dashboard". A lock icon appears to the right of the dashboard name. While locked you can still sort, share, clone, or unlock.
- **Delete Dashboard:** Hover Options → "Delete Dashboard" → "Delete". Permanently removes the dashboard.

### Apply a Macro on Engagement Dashboard Messages
- A macro is a saved configuration of multiple actions that applies more than one change to a message, an asset, or other Sprinklr entities all at once ("execute complex actions with a single click").
- Steps:
  1. Click the New Tab icon under Sprinklr Social → select Engagement Dashboards (within Engage).
  2. Search and navigate to the desired Engagement Dashboard.
  3. Hover over a message in the column → click the **Macro icon**. A list of available macros appears.
  4. Search and select the desired macro from the dropdown.
  5. On selection, the macro is applied and all associated actions execute on that message.
- Two source articles describe this identically; one names the asset as a "SAM asset", the other as a "DAM asset" (digital asset). See [[rule-engine]] for how macro actions are configured.

### Search & Filter in Engagement Columns
Access: Sprinklr Social > Engagement Dashboards (within Engage) → open dashboard from Engagement Home.
- **Basic search:** Hover over the top of a column → click the **Search icon** → type query → press Enter.
- **Advanced search:** Click the Search dropdown icon at the left of the search bar, then:
  - **Include Words / Include Keywords:** search terms, @mentions, #hashtags.
  - **Exclude Keywords:** checkbox to exclude specific terms.
  - **Tags:** select from dropdown.
  - **Sender:** enter account name.
  - **Case Number:** for case columns.
  - **Date Range:** filter by time period.
  - **Last Note Added Date Range:** case columns only.
  - Enable the **Query Search** toggle to use Boolean operators; click **Search** to apply.
- **Boolean operators (must be capitalized):**
  - `OR` — returns messages containing any keyword.
  - `AND` — returns messages containing all keywords.
  - Use brackets for complex queries, e.g. `(word1 AND word2) OR (word3 OR word4)`.
- **Custom Quick Filters:**
  1. Hover over column → click the **Filter icon**.
  2. Click "Add Filter".
  3. Browse standard filters or open the **Custom Fields** tab.
  4. Select a filter → apply via the button at bottom-right.
  5. Click the **Favorite icon** to pin a filter upfront.
- **Filter retention:** Filters persist across browser refresh, logout, and tab close (requires the relevant dynamic property to be enabled).

## Common issues & fixes
- **Filters not persisting across sessions:** retention requires a dynamic property to be enabled — raise with Sprinklr support if it is not honoring saved filters.
- **Boolean search returns nothing / treats AND/OR as text:** operators must be UPPERCASE and the Query Search toggle must be on.
- **Macro not in the list:** only macros available to the workspace/user appear; if missing, the macro likely is not shared or not created for that context (creation is out of scope of these articles).

## Notes & gaps
- **Macros:** the articles only cover *applying* an existing macro. They do NOT specify required permissions/roles, limits on macro count or action quantity, the types of actions a macro can contain, or how to create/manage macros. Source on macro creation needed before advising config — see [[rule-engine]].
- **Dashboard actions:** the "Actions in Engagement Dashboards" article documents dashboard-level operations, not per-conversation/column actions, despite the title.
- **Search/filter:** "dynamic property" for filter retention is named but not specified (no property key given). Custom Fields source list depends on tenant config — see [[data-engine]].
- No metric definitions, export troubleshooting, or SLA-related actions are covered here — see [[reporting]], [[sla-monitoring]], [[care-console]] for those.

## Sources
- Actions in Engagement Dashboards — https://www.sprinklr.com/help/articles/message-actions-automation/actions-in-engagement-dashboards/6450f6ac516411445be3ff72
- Apply a Macro on Engagement Dashboards Messages — https://www.sprinklr.com/help/articles/message-actions-automation/apply-a-macro-on-engagement-dashboards-messages/6450f70c516411445be3ff73
- Apply Multiple Message Actions at Once with Macros (Apply a Macro on Engagement Dashboards Messages) — https://www.sprinklr.com/help/articles/apply-multiple-message-actions-at-once-with-macros/apply-a-macro-on-engagement-dashboards-messages/6454bc1cf65d86626c82b942
- Search and Filter in Engagement Columns — https://www.sprinklr.com/help/articles/search-filtering/search-and-filter-in-engagement-columns/641beae255c4c33ae8b81421
