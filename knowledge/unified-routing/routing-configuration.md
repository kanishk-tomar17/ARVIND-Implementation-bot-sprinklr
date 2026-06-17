# Routing Configuration (Unified Routing 025)
**Source:** Product Foundation Courses → Unified Routing / 025 Routing configuration (video transcript) · **Help:** search `site:sprinklr.com/help unified routing configuration routing group backup queue drop skill`

## What it is & why
When skill-based routing leaves a case **waiting** (no agent with the required skills available, agent imbalance, competing channel priorities), **routing configuration** progressively **expands the pool** of eligible agents — after configurable **wait times** — to protect **SLA**.
- It relaxes criteria over time: **drop a skill**, **drop proficiency**, or **change priority**.
- *Example:* a case needs skills A–E (only agents 1–3 qualify); if they're unavailable, **drop skill A** → agents 4–6 also become eligible (pool of 6); drop further to widen more.

## How it works (sequence)
Case enters queue → match agents by skill/proficiency → if none available, **wait** → at the configured time an **action fires** (drop skill / change proficiency / change priority) → a larger pool is eligible → if an agent is found, assign; else keep waiting and repeat. You chain **multiple actions**, each after a wait time.

## Creating a routing configuration
**Unified Routing → Queue tab → edit a queue → Routing configuration.**
- Add a **routing group** with a **filter** at the top (e.g. applies only to Facebook, or Facebook+Twitter cases). Different groups per filter (e.g. WhatsApp cases follow a separate group); cases not matching any group follow none.
- Define a **wait time** before actions fire (e.g. 2 min, or **based on estimated wait time** → can act immediately). ("Wait for assignment" toggle.)
- **Actions:**
  - **Drop skill** / **drop skill category**.
  - **Change proficiency** (e.g. reduce English requirement by 10).
  - **Change priority** (e.g. +20 so a channel can compete).
  - **Send to another queue** — last resort; the case is **removed** from this queue (e.g. out of business hours, location down).
  - **Backup queue** — the case **stays** in this queue, but **idle agents in the backup queue also become eligible**. Two variants: **Backup queues** (applies the skill drops already done) vs **Backup queue – retain original skills** (search backup with the case's *original* entry skills).

## Examples
- **Live chat + email queue (2 routing groups):**
  - *Live chat:* after 5 min drop **product type** category, after 2 more min drop **language**; add a **backup queue** after 30s.
  - *Email:* wait **4 hours** (don't skip when agents offline — business hours change), **+20 priority** (compete with live chat), then drop **product type**.
- **Voice queue:** estimated wait > 5 min → drop **city** skill (route to other cities); +2 min → drop **voice** skill (non-voice agents get the call); +30s → **backup queue**; +10s → **escalation queue** (removed from this queue, better-staffed).

## Notes / gaps
- Each relaxation **degrades match quality to protect wait time** — sequence them so the customer is answered before they drop off, not so aggressively that quality collapses.
- Per-channel routing groups let one queue serve sync (chat/voice — short waits) and async (email — hours) very differently.
- Builds directly on [[agent-skills]] (skills/proficiency) and feeds [[routing-types]]/[[smart-routing]].

## Live UI verified (prod8, 2026-06-18)
Queue builder → **Routing Configuration** step. Structure = **Routing Group(s)** → each has a **Filter** + one or more **Action Group(s)**:
- **Filter** (per Routing Group): `Select Attribute` → `Select Operator` → `Select Value` (+ Add Filter). Determines which cases this group applies to.
- **Action Group:** a wait condition — radio **Wait for assignment** vs **Estimated wait time**; checkbox **"Skip wait time if no users are available"** (default on); **Wait to assign for:** time + unit (with a **Dynamic Input Type** toggle to drive the wait from a variable); then **If not assigned then → Select Action**.
- **Select Action options (verified exact list):** **Change Priority · Change Proficiency by Skill · Change Proficiency by Skill Category · Drop Skill · Drop Skill Category · Send To Another Queue · Backup Queues (Retain original skills) · Backup Queues.**
- Buttons: **+ Add Action** (chain actions in a group), **+ Add Action Group**, **+ Add Routing Group**.
- (To reach this step in the wizard you must first fill Queue Name + Routing Type on General Settings.)
