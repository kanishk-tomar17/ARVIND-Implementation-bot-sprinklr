# Capacity Configuration (Unified Routing 024)
**Source:** Product Foundation Courses → Unified Routing / 024 Capacity configuration (video transcript) · **Help:** search `site:sprinklr.com/help unified routing capacity profile dynamic capacity overflow`

## What capacity is
**Capacity** = how many **simultaneous interactions** an agent can handle.
- **Synchronous** (voice/video) → **1 at a time**.
- **Chat** → a few (semi-sync).
- **Email** → many (async — customer takes time to reply).

## Capacity units
Each agent has **100 capacity points** by default. Define how many units **each channel consumes**:
- e.g. chat = 25 → up to **4 chats**; or voice 100% / chat 50% / email 25% (so an agent could run 4 emails, or 2 chats, or 1 voice, or a mix).

## Create a capacity profile
**Unified Routing → Capacity Configuration tab (4th) → Add → name it.** Per-channel fields:
- **Capacity group (per channel):** channel + **% consumed per case** + **"can be interrupted by"** (e.g. chat interrupted by voice → a voice call is assigned even when chats already fill 100%).
- **Allowed capacity overflow** — the max % capacity may reach (e.g. 100% overflow → one extra voice call on top of 2 chats; agent can run at 150–200%).
- **Maximum allowed capacity** — cap one channel's share (e.g. email 25%/case, max 50 → only **2 emails**, leaving room for chat/voice).
- **Dynamic capacity** — when a case goes **idle** (customer not replying) after N minutes, it consumes **less** capacity (e.g. 50% → 10%), freeing the agent for more cases.
- **Daily assignment capacity** — tick *"ignore this group for daily assignment capacity"* to exclude a channel; set a daily **target** (e.g. 120 cases/day) → stop routing to an agent past it → **balances load** so long-logged-in agents aren't over-assigned.
- **Target** — a per-agent case target used in **reporting** (target vs actual).

## Assigning a profile
- **Agents tab (3rd):** search agent → the **skills & capacity** section shows the assigned profile → change → Save.
- **Bulk:** select multiple agents → bulk capacity edit.
- **User group:** select a group → replace → applies to the group's **current** members.

## Checking capacity utilisation
- **Work queue → Assignees tab** — shows capacity consumed per agent (can exceed 100% with overflow; usually <100%).
- **Engagement dashboard** — cases/messages/tasks filtered by *assigned to* an agent.
- **Supervisor Console → Agent tab → add the "consumed capacity" dimension** — capacity consumed across the team.

## Notes / gaps
- **Dynamic capacity** is the productivity lever — frees agents from idle chats; pair with idle-timeout thinking from [[stickiness-timeout]].
- **Daily assignment target** balances workload across shift lengths; the plain **Target** field is reporting-only.
- Capacity feeds the "most idle / most capacity available" tie-break in [[agent-skills]] routing.
