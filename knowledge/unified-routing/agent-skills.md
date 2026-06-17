# Agent Skills & Skill-Based Routing (Unified Routing 023)
**Source:** Product Foundation Courses → Unified Routing / 023 Agent Skills and skill groups (video transcript) · **Help:** search `site:sprinklr.com/help unified routing skills proficiency skill based routing`

## What skills are
**Skills** represent agent talents (e.g. languages, products). Cases are routed to the **best-suited agent**.
- A skill is assigned to an agent with a **proficiency score 0–100** (per skill).
- Skills are grouped into **categories** for organisation.
- **Benefits:** customers reach the right agent; agents work to their strengths; reduces handling time and contact-centre cost.
- **Examples:** *Language* category → English/Spanish/French; banking *Product* category → credit cards/debit cards/bank accounts. Also channel, issue, category, brand, region/country.

## Setup flow
1. **Identify** the skills the contact centre needs.
2. **Document** each agent against those skills.
3. **Create** skills/categories in the **Unified Routing** module.
4. **Assign** skills to agents / user groups.

## Configuration (Unified Routing module)
- **Skills tab (2nd):** add a **skill category** (e.g. Language) and **multiple skills** within it (English, …); add a skill to an existing category via its button.
- **Agents tab (`/unified-routing/agents`):** VERIFIED live 2026-06-18 — this tab **shows the User Groups list** (agents are managed via user groups). Each row's **More Actions** menu = **Edit · View Activity · Remove · Reset · View Usages**.
- **Edit → a 3-tab wizard** (right panel shows the group + type Static/Dynamic):
  1. **Set Skills** — *User Skills* → **Add Skill** (pick skill + proficiency 0–100).
  2. **Capacity** — **Capacity Profile** (assign one) + **Daily Reset Configuration** (Country + Timezone — when the daily assignment target resets).
  3. **Voice Settings** (each field has an (i) tooltip):
     - **Call Handling** — *"when enabled, you can handle incoming and outgoing calls."*
     - **Auto Answer** — enable/disable auto-answering.
     - **Agent Readiness** — *system runs Microphone & WebRTC checks; on failure the agent is set to "System Not Ready" and can't go available until fixed.*
     - **Nailed Up Call** — *"nailed up connection will only be preferred if there is only one voice account shared."* (Prefer / Do Not Prefer.)
     - **VOIP Calling** — *VoIP allows voice calls over the internet* (enable/disable).
     - **Configure Provider Settings → Twilio Provider Config** (*"Twilio VoIP call parameters for the agent's leg"*): **WebRTC Logs**, **Codec Preference** (in priority order), **Maximum Average Bitrate** (6000–510000 hz).
  - **Bulk:** select multiple users/groups → bulk edit. ⚠️ User-group skill/capacity assignment is **bulk-only** — members added *later* don't auto-inherit (re-run on onboarding).

## How skill-based routing works
1. **Tag skills on the case** (driven by IVR flow, chatbot flow, region, or account).
2. Case enters a **queue**. A queue has **3 routing methods**:
   - **All Skill Matching** — uses case skills, ignores proficiency.
   - **Best Skill Matching** — uses case skills **and** proficiency.
   - **No Skill Matching** — ignores the case's skills.
3. The queue finds agents who have **all required skills**, filtered by **availability**.
4. **Best Skill Matching:** computes a proficiency score (**sum-product** across required skills), sorts agents, assigns the **best**. **All Skill Matching / ties:** picks the **most idle agent** (most capacity available, or idle longest).
5. If **no agent** has the required skill, the case **waits in the queue** until one is available — check the queue's **assignment failure logs**.

## How skills get tagged onto a case
- **Rule Engine** (digital/social) — use the **"Universal Case → Manage required skill"** action in **inbound** or **case update** rules. **Set** (replace existing) or **Merge** (add to existing). E.g. billing skill, proficiency > 50. Then add the case to the work queue.
- **IVR** — a **Set Skill node** after a decision/other node: define skills + proficiency, **Merge** or **Set**.
- **Conversational AI bot** (chat/voice) — a **Set Skill node**; when the case enters a queue via the **Assign Agent node**, those skills are **mandatory** for assignment.

## Notes / gaps
- **Set vs Merge** is the key gotcha: Set wipes prior skills; Merge accumulates. Pick deliberately across IVR/bot/rule stages.
- User-group skill assignment is a one-time bulk action — onboarding new agents needs a re-run.
- This is the agent side of [[routing-configuration]]/[[routing-types]]; capacity is in [[capacity-configuration]].
