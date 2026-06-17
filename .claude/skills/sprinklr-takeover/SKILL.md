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
1. **Resolve.** At takeover start, query `sprinklr_macros` (trigram/ilike on `macro_key` + `description` + `tags`) for the task. If a good match exists, use it.
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
7. **Never** change credentials, permissions, or unrelated config without asking.

## Hand back
- Summarise exactly what changed (object, field, old → new value).
- State how the consultant can verify it.
- Return control and confirm they're unblocked.
- If you discovered or repaired a path, confirm it was recorded to the ledger (macro_key) so the team has it next time.
