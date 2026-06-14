# Skill-Based Assignment in Voice Campaigns (Outbound Voice 168)
**Source:** Product Foundation Courses → Outbound Voice / 168 Skill based assignment in Voice Campaigns (video transcript) · **Help:** search `site:sprinklr.com/help voice campaign required skills queue skill based`

## What it is
Allocate outbound calls to agents by **skill/expertise** rather than randomly — routes each call to the **most suitable agent**. (Demo: a plan-upgrade call routed to a **pricing-plans specialist** → tailored advice → upgrade + satisfaction.)
- **Benefits:** better CX, higher **first-call resolution** (fewer transfers/escalations), agent productivity, **reduces AHT ~5–10%**, optimises resource allocation.
- **Use cases:** customer/technical support, sales by product/segment/geography, **language support** (e.g. dial a region with preferred-language agents), healthcare, legal/financial, travel/hospitality.

## How it works in Sprinklr (end-to-end)
1. **Assign skills to agents/user groups** in **Unified Routing**.
2. **Create a queue** (a group of agents with skill sets).
3. **Add the queue to a dialer.**
4. **Assign required skills in the campaign** (and optionally **overwrite per segment**).

## Platform walkthrough
- **Skills:** Sprinklr Service → Route → **Unified Routing → Skills** → add a **skill name + skill category** (e.g. *French* under *Language*) → Create.
- **Assign to agent:** edit agent → **Add new skill** → category + skill + **proficiency** (e.g. 100) → Save. (Or assign to a **user group**.)
- **Create queue:** **Add work queue** → name → **Routing type = All skill matching** (only agents meeting *all* the case's skill criteria) → Next → select **users / user group** → agent status = **Available** → Save → View details (capacity, status, skills).
- **Dialer:** **Voice Care → Dialer Profiles** → edit a dialer → set its **queue** to the skill-based queue.
- **Campaign:** edit → **Required Skills** (e.g. *French* → only French-skilled agents get the calls; add multiple like *French/German/English/Spanish* → any agent with **one** of them is eligible) → set the **dialer** → Save.
- **Per-segment overwrite:** in **Activate Segment**, overwrite the initial config so a specific contact list routes to a **different skill** than the campaign default.

## Notes / gaps
- Skills are defined once in [[../unified-routing/agent-skills]]; this topic is how they flow into **voice campaigns** (queue → dialer → campaign required-skills).
- Campaign-level required skills vs **segment-level overwrite** is the key flexibility — different lists to different agent pools within one campaign.
- "All skill matching" routing type is the usual choice; see [[../unified-routing/routing-types]] for best-skill alternatives.
