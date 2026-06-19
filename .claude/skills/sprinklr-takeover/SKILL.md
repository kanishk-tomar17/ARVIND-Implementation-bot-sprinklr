---
name: sprinklr-takeover
description: Use when ARVIND should stop guiding and directly operate the browser to inspect or fix a Sprinklr configuration — triggered after the consultant has 3–4 failed attempts at the same step, or whenever they ask ARVIND to do it directly. Covers the accessibility-first interaction loop, the shared Supabase macro ledger (pull known paths, record new ones), choosing the browser path, confirming safely, and handing back.
---

# Sprinklr Takeover

When guidance isn't landing, take control and do it — safely, cheaply, and in a way that makes the *next* takeover faster for the whole team.

## When to trigger
- Consultant has **3–4 failed attempts** on the same step, OR
- They explicitly ask ARVIND to do it.

Announce the switch: "I'll take it from here — let me drive the browser." Don't take over silently.

---

> **Pair with [[sprinklr-explore]]:** when a takeover means driving an unfamiliar screen, apply the `sprinklr-explore` discipline — step through every tab/wizard step, read the (i) tooltips (they're in the a11y snapshot as field `description`s), flip toggles to reveal conditional fields, and open dropdowns for their full option lists. It's the same a11y-first technique set, and it stops you missing fields mid-takeover.

## A. Interaction loop — accessibility-first (do NOT scrape the DOM)

The browser is driven through the **`chrome-devtools` MCP**, which already gives you a semantic accessibility tree with ref ids. Use it. This is the default and it is what keeps takeover fast and cheap.

1. **See with `take_snapshot`.** It returns the a11y tree — each actionable node as `role` + `name` + `uid`. That `uid` is your handle.
2. **Act by `uid`.** Use `click(uid)`, `fill(uid)`, `hover(uid)`, `press_key`. Never act on coordinates.
3. **Re-snapshot after every navigation or state change.** `uid`s are **ephemeral** — they are regenerated on each snapshot (e.g. `14_52` one moment, `19_31` the next). A `uid` from a previous snapshot is invalid; resolve a fresh one each time.
4. **Scope, don't dump.** On a large screen (big grids/long lists), snapshot or reason over the relevant subtree — don't pull the whole page.

**Avoid by default (they burn tokens):**
- **`take_screenshot`** — only when the consultant explicitly wants to *see* something, or when the a11y tree genuinely can't disambiguate two controls. It is not how you navigate.
- **`evaluate_script` returning bulk DOM** — never dump HTML to context. `evaluate_script` is allowed only for a **targeted read** (one value) or the **React native-setter write trick** when a control can't be driven by `fill(uid)` (e.g. Monaco editors, custom React inputs):
  ```js
  const setter = Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype,'value').set;
  setter.call(inp, val);
  inp.dispatchEvent(new Event('input',{bubbles:true}));
  inp.dispatchEvent(new Event('change',{bubbles:true}));
  ```

**Decision rule (memorize this — don't drift either way):**
> **A11y by default** (`take_snapshot` → act by `uid`). **Drop to `evaluate_script`** only for React / unlabelled controls a `uid` can't drive (native-setter write, one-value read). **Screenshot only for visual verification** the a11y tree can't express (did the chart render? is the colour-coding right?) or when the consultant asks to see it — never to navigate.

These are **scoped exceptions, not bans** — when a control genuinely needs DOM or a screenshot, use it. Being dogmatic and getting stuck is worse than a justified fallback. (Lesson: in past takeovers `evaluate_script` + screenshots were *overused* as the default and caused both token bloat and avoidable errors — `uid` clicks were more reliable.)

### Multi-select / checkbox dropdowns and "Create new" options — drive by a11y, NOT DOM

Many Sprinklr fields (e.g. **Persona**, tag-style pickers) are dropdowns whose options are **checkboxes you must tick to apply the value** — clicking the row text alone may not commit it. Some also offer a **"Create &lt;your text&gt;"** checkbox to add a brand-new value inline. **`click(uid)` on these options is unreliable** (it frequently reports *"did not become interactive"* because the list is virtualized) — so **drive them by keyboard**, which is the reliable accessibility path (and still avoids `evaluate_script`).

**First decide: type, or just pick?** Open the dropdown and snapshot.
- **Short list whose options actually render in the snapshot** → don't waste a turn typing. Just **`ArrowDown`** to the target option, then **`Enter`** (or `click` its uid if it's exposed and interactive).
- **Options DON'T render in the a11y tree** (e.g. **Product Seat**) → you can't see the highlight, so **don't blind-count `ArrowDown`s — you'll overshoot** (this happened: 3 downs landed on the 4th option). **Type to filter** even though the list is short.
- **Long list, options truncated/not all visible, or adding a "Create &lt;value&gt;" entry** → **type to filter first**:
  1. **`fill`** (or click then type into) the combobox to filter (e.g. type `Sprinkl` → narrows to `Sprinklr Employee`; type the full new value for a "Create" entry).
  2. **`wait_for`** the option's label to confirm the filter landed.
  3. **`ArrowDown`** then **`Enter`** to tick/select.
- Either way, **`take_snapshot` to confirm** the combobox reads "Selected …", then **dismiss the dropdown** (click a neutral spot — best practice #2) before the next field.

> The **same keyboard pattern** handles **single-select listboxes whose options never render in the a11y tree** (e.g. **Product Seat**) — ArrowDown→Enter if it's a short known list, or type-to-filter for a long one. Only fall back to `click(uid)` when the option *is* exposed and interactive. **Never** drop to `evaluate_script` for these — earlier takeovers did, and it was avoidable. *(Best practice #9.)*

---

## B. Macro ledger — pull a known path, or record a new one

A shared **Supabase** table, `sprinklr_macros`, is the team's memory of *how to do things in Sprinklr*. Every consultant's ARVIND reads from and writes to the same table (via the Supabase MCP), so a path discovered once is instantly available to everyone. There is no live push — you **pull on takeover, upsert on success**.

Each macro stores **generalized** steps (never `uid`s, never client-specific literals):
```json
{
  "macro_key": "create_reporting_dashboard",
  "variables_required": ["dashboard_name", "folder_name"],
  "steps": [
    {"action": "navigate", "url": "https://{{space}}.sprinklr.com/care/insights/reporting"},
    {"action": "click", "role": "button", "name": "Create Dashboard"},
    {"action": "fill",  "role": "textbox", "name": "Dashboard Name", "value": "{{dashboard_name}}"},
    {"action": "click", "role": "treeitem", "name_contains": "{{folder_name}}"}
  ]
}
```

### The loop
1. **Resolve — two-phase, column-projected (never `SELECT *`).** Pull the *minimum* payload, in two phases, so candidate matching doesn't drag the heavy `steps` jsonb into context:
   - **Phase 1 — discovery (no `steps`):** project only the columns you need to choose a match.
     ```sql
     SELECT macro_key, description, tags, variables_required
     FROM sprinklr_macros
     WHERE status = 'active'
       AND (macro_key ILIKE '%<term>%' OR description ILIKE '%<term>%' OR '<term>' = ANY(tags));
     ```
     Pick the best-matching `macro_key`. The `steps` blob is **not** fetched for the candidate set.
   - **Phase 2 — hydrate the one chosen macro:**
     ```sql
     SELECT macro_key, variables_required, steps
     FROM sprinklr_macros
     WHERE macro_key = '<chosen_key>';
     ```
   - **Read-time projection rules:** never `SELECT *`; never select the telemetry/audit columns (`id`, `success_count`, `fail_count`, `created_by`, `updated_at`) when *reading* — they're only needed at upsert (step 5). When you show the consultant the resolved path, **summarize the steps in compact prose** — don't echo the full `steps` jsonb back into context.
2. **Variable prompting.** If the matched macro lists `variables_required` the consultant hasn't given (dashboard name, folder, account, etc.), **pause and ask for them before driving the browser.** Don't guess client-specific values.
3. **Execute.** For each step: take a fresh `take_snapshot` → resolve `role` + `name` / `name_contains` to a live `uid` → act, substituting `{{variables}}`.
4. **Fuzzy fallback — NEVER delete a macro.** If a step's target isn't found (a client's instance is customized, a folder is renamed/missing):
   - Pause the script. Take a fresh a11y snapshot.
   - Reason the closest matching node or an alternate route from the live tree. If the match is vague, **confirm with the consultant** before clicking.
   - If the path diverges hard or the target simply doesn't exist, **ask**: "I couldn't find the folder '{{folder_name}}'. Create a new one with that name, or use an existing one?"
   - On success, generalize the bridged step, set the macro's `status='needs_review'`, bump `fail_count`, and **upsert** — but never delete the original.
5. **Record on success.** When you complete a task by fresh exploration (no macro existed), or you repaired one, distill the exact action sequence and **upsert** into `sprinklr_macros` (`on conflict (macro_key) do update`), bumping `success_count`.

   **⚠️ Parameterization rule — MANDATORY, never hardcode client data.** Before saving, **scan every step's `name` / `name_contains` / `value` for strings that look client-specific** — custom folder names, unique dashboard/widget titles, account/brand names, user names, workspace/space names, IDs, anything the consultant typed or chose for *this* client. Replace each such literal with a `{{variable}}` and add it to `variables_required`. Only genuinely stable, product-level labels stay literal ("Create Dashboard", "Add Widget", "Save", standard metric names). Example: if exploration entered a folder `Client_X_Ad_Campaigns`, save `{"action":"click","role":"treeitem","name_contains":"{{folder_name}}"}` with `folder_name` in `variables_required` — **not** the literal string. **When unsure whether a string is client-specific, treat it as a variable.**

> **Ledger location:** Supabase project **`arvind-macros`**, ref **`qtghghiuyagxcebdglna`** (org "RaViAtOr's Org") — pass this `project_id` to the Supabase MCP (`execute_sql` for read/upsert). Table `public.sprinklr_macros`. Setup / how a consultant connects lives in `SETUP.md`. If the Supabase MCP isn't connected, skip the ledger and drive the task manually with the a11y loop — then offer to record it once the connector is up.

---

## C. Pick the browser path
- **chrome-devtools MCP** — the **primary engine**. The a11y loop and macro execution run here. Use it for inspection and for driving the UI by `uid`.
- **Claude for Chrome extension** — **manual fallback** for when the action must happen in the consultant's **own logged-in, SSO-authenticated** session (their real environment/permissions). The macro's `role`+`name` steps still tell you what to click; you (or the consultant) execute them there by hand, since ref-execution is MCP-side.

If unsure: inspect with the MCP browser, act with the extension. See `SETUP.md`.

---

## Act safely — non-negotiable
1. **State the change before making it.** "I'm going to add condition X to rule Y."
2. **Confirm before anything destructive or irreversible** — deletes, publishing, bulk edits, or any change to a live production rule. Wait for an explicit yes.
3. **Prefer sandbox.** If a sandbox exists, do it there first and verify before touching production.
4. **One change at a time** for risky steps; re-check state (re-snapshot) between steps.
5. **Dismiss open dropdowns/popovers before clicking.** An open dropdown can overlay buttons/fields — after selecting value(s), click a neutral spot to close it, then check for any newly-revealed fields and click the (previously covered) button. Applies to all dialogs. *(Best practice #2.)*
6. **In reporting, finish one column/metric fully before starting the next** — the per-column metric picker replaces, it doesn't accumulate. *(Best practice #3.)*
7. **Mandatory picklist you can't answer? Ask — don't guess.** If a required dropdown/picklist value wasn't specified and you don't know the concrete answer, **ask the consultant directly** (you may suggest a sensible default), but **never pick a picklist value on a whim** — these choices often grant permissions, set routing, or drive behaviour. Don't act as the consultant on a value only they can decide. *(Best practice #10, extends #5.)*
8. **Never** change credentials, permissions, or unrelated config without asking.

## Hand back
- Summarise exactly what changed (object, field, old → new value).
- State how the consultant can verify it.
- Return control and confirm they're unblocked.
- If you discovered or repaired a path, confirm it was recorded to the ledger (macro_key) so the team has it next time.
