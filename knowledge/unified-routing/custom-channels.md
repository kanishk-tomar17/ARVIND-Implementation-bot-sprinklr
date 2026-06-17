# Unified Routing — Custom Channels

**What it is:** Custom Channels are configurable routing options that let an org define and manage **client-specific interaction types beyond Sprinklr's standard channels** (Social, Email, Live Chat, Messaging, Voice). They use **filtering criteria** to categorize specialized incoming work so it can be routed appropriately through Unified Routing.

**When to use:** when a client has a work type that isn't one of the built-in channels (e.g., a bespoke integration, a partner feed, or a non-standard case source) and you need UR to recognize and route it like any other channel.

**Where:** Unified Routing app → **Custom Channels** tab (`/unified-routing-app/unified-routing/...`). Create/define a custom channel there, then reference it in queue routing/filters.

## Create flow (VERIFIED live, prod8, 2026-06-18)
**Unified Routing app → Custom Channels tab** (`/unified-routing-app/unified-routing/custom-channels`) → **Add Custom Channel**:
- **Custom Channel Name** * — mandatory.
- **Description** — optional.
- **Property Filters** — **at least one is mandatory** (saving with none errors *"Hold on! This field can't be blank."*). Each filter = **Select Attribute → Select Operator → Select Value**. VERIFIED options: **Attribute** = *Skill · Work Message Type · Work Social Network · Work Type*; **Operator** = *Containing · Not Containing · Exists* (operators vary by attribute); Value depends on the chosen attribute. **+ Add Filter** (more conditions) and **+ Add Filter Group** (grouped logic).
- **Save**.

Once defined, the custom channel behaves like a **channel dimension** for routing and capacity — e.g., capacity profiles list it like any channel (`Message Custom Channel (0)`, `Task Custom Channel (0)`). See [[capacity-configuration]].

Existing examples in prod8: *Message Custom Channel*, *Task Custom Channel*, *Goods Receipt Note channel*, *Gokul test social instagram*.

## Notes & gaps
- Niche/advanced — most implementations route on the standard channels.
- The Attribute/Operator/Value dropdowns are **portal-rendered** (need trusted clicks / fuzzy resolve) and the Value depends on a real case attribute. Macro: `create_custom_channel` (ledger).

**Source:** sprinklr.com/help → *Automation and Assignment > Unified Routing Overview* — "Components of Unified Routing" (`/articles/unified-routing-overview/components-of-unified-routing/6985c271243d9d29873a5255`). Related: [[overview]], [[capacity-configuration]].
