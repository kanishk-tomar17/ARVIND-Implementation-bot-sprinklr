---
name: sprinklr-explore
description: Use when exploring or learning a Sprinklr product/screen to build or update the knowledge base and macro ledger (or when driving an unfamiliar config screen). The exhaustive UI-discovery discipline — click every interactive element, step through ALL tabs, read every (i) tooltip, flip every toggle to reveal its conditions — plus the chrome-devtools techniques that make it reliable. Owner-mandated; apply automatically, don't wait to be told.
---

# Sprinklr Explore — exhaustive UI discovery

**Mandate (owner, Kanishk): don't skip anything clickable.** When learning a screen, be exhaustive — every button, tab, icon, toggle, and dropdown teaches you something. The goal is to learn the screen *completely* and record it so a consultant never has to rediscover it.

## The checklist — for every screen
1. **Click every interactive element.** Buttons, every **"Add / Create X"**, each row's **More Actions (⋮)** menu (Edit / Clone / Remove / Reset / View Activity / View Usages…), **Manage Columns**, **Add Filter / Quick Filter**, **Import / Export**.
2. **Step through ALL tabs / wizard steps — never document only step 1.** E.g. a queue = *General Settings → Routing Configuration → Assignees*; an agent edit = *Set Skills → Capacity → Voice Settings*; a capacity profile = *Capacity Profile → Share Settings*; a Voice Application = *Overview → Caller IDs → Audio and Voice Settings → Advanced Settings*; a Disposition Plan = *Disposition Plan Settings → Autowrap Up Settings → Share Settings*. Click each tab/step and capture it.
   - **If a later step is gated** behind validation, enter the **minimum valid throwaway data** to unlock it (then Cancel/delete) — *don't* stop at step 1 and call it done. Prefer **editing an existing, already-valid record** to walk later steps with zero risk (owner-preferred).
   - **In EVERY step, click into every clickable field** — open each dropdown for its options, flip every toggle ON to reveal conditional fields, expand each "Add …"/condition group, read each (i) tooltip. This applies to *Autowrap Up Settings, Share Settings*, and every other step, not just the first. **Owner standing rule — do this automatically on every explore, don't wait to be asked.**
3. **Open nested sub-sections / inner "+Add" groups.** `+ Capacity Group`, `+ Routing Group`, `+ Action Group`, `+ Add Filter Group` — these contain their own fields. Open and capture them.
4. **Read every (i) info icon tooltip.** They explain non-obvious fields (e.g. Agent Readiness = mic/WebRTC checks; Overflow = extra units for interrupting channels only). **Technique:** `take_snapshot` usually exposes the tooltip text as the field's `description` (or an adjacent StaticText) — so you rarely need to hover. If it's not there, `hover` the icon (trusted) and read the portal tooltip.
5. **Flip every toggle / checkbox ON — they reveal conditional fields.** A toggle off hides its config. E.g. *Add dynamic capacity* → reveals **Case Idle After + % Original Consumption**; *Use Voice* → voice config; *Dynamic Input Type* → variable-driven input. Switch on, capture the revealed fields, note the condition.
6. **Open every dropdown and capture the full option list** (routing types, "if not assigned" actions, operators, agent statuses, sort-by values). The exact option set is the gold.
7. **Record mandatory vs optional** — the `*` markers and the validation errors that appear on Save ("this field can't be blank") tell you what a consultant must provide.

## Capture & record (the output) — reconcile ALL RAG layers, automatically
Per create-flow capture: **path, mandatory fields, all options, toggle-reveals, (i) tooltip meanings**, gotchas.

**Then keep all RAG layers in sync in the SAME turn — proactively, without being asked (best practice #7 / R4). This includes edits and deletes, not just adds:**
1. **Knowledge base** — create/edit/delete the distilled `knowledge/<area>/<topic>.md`; cite source; stamp **verified date**.
2. **Map** — set/update/clear its `local_kb` in `sprinklr-map.json` (so JIT lookups land on local KB) — link the relevant help articles.
3. **Macro ledger** — upsert/update (or deactivate) the macro in Supabase `sprinklr_macros`.
4. **`INDEX.md`** — add/rename/remove the row + update the count.
If something is removed, remove it from **all** layers so they never drift. Don't make the owner ask.

- Use generic **"Kanishk Agent Test …"** names for any sample you create; don't persist throwaway entries unless asked; **Cancel** out of forms you opened only to read.

## chrome-devtools techniques that make this reliable
- **Trusted clicks for "Add/Create" buttons and portal dropdowns** — they often ignore a synthetic DOM `.click()`. Use the MCP `click` tool by `uid` (snapshot → ref → click).
- **App sub-navs hydrate a moment after load and navigate via onClick (not href)** — `wait_for` the tab text, then click its ref; don't guess URL slugs (several 404 or redirect).
- **Re-snapshot after each navigation** — `uid`s are ephemeral.
- **Big list pages:** don't dump the whole snapshot — `evaluate_script` to extract just buttons/headers/options, or grep the saved snapshot file.
- **Portal listboxes** (routing type, status, channel, attribute/operator) render outside the form — read options from the open `[role="listbox"]`; if a synthetic click won't open it, click the combobox by `uid` (trusted).
- **Exhaustively inspecting a long *list* of items (e.g. a widget/template library with ~100 entries):** don't snapshot per item — that's huge on a busy page (a case feed alone is ~250 a11y lines). Instead drive it entirely inside `evaluate_script` with a **trusted-ish synthetic pointer sequence**: dispatch `['pointerover','pointerdown','mousedown','pointerup','mouseup','click']` on the target element (a bare `.click()` often won't fire the framework handler, but the full sequence usually does). Loop in **batches of ~10** (one `evaluate_script` per batch to stay under the call timeout), and for each item: open the picker → type into its search box (via the native `value` setter + `input` event) to filter → fire the matching item → read the config form text → **identify the just-added node by diffing** the set of action buttons (e.g. "Delete Widget") before vs. after → fire its delete + confirm. Capture `{name, config[], render}` per item. **Cleanup:** if some deletes don't take, just **reload the page** at the end (never Save) — unsaved builder edits are discarded. This turned ~97 widgets into ~10 cheap calls instead of ~100 giant snapshots.

## Safety
Sandbox first; this is read-to-learn — **cancel forms you opened just to inspect**, never modify existing client config, and confirm before anything destructive. (Same rules as `sprinklr-takeover`.)
