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
- **Agents tab (3rd):** search an agent → **Edit** → "skills and capacity" form shows current skills + proficiency.
  - **Add to All** to edit proficiency; **Remove from All** to remove; add new skill = select category → skill → proficiency → Save.
  - **Bulk assignment:** select multiple users → bulk skill edit (skill + proficiency).
- **User Group tab:** Edit → assign skills to the whole group (e.g. English proficiency 80). ⚠️ **Bulk update only** — users added to the group *later* do **not** auto-inherit these skills.

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
