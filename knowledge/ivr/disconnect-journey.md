# IVR Disconnect Journey (IVR 147)
**Source:** Product Foundation Courses → IVR / 147 IVR disconnect journey (video transcript + demo) · **Help:** search `site:sprinklr.com/help IVR disconnect journey callback journey facilitator`

## What it is
A **Disconnect Journey** is a workflow **triggered after a call ends on the IVR** (including when the customer drops on a critical path or while waiting in queue). It lets you run business logic post-call or **reconnect** with the customer on their channel of choice.

## Top use cases
1. **Callback for queue-abandoned customers** — at rush hours, high wait time → abandoned calls rise. If a customer **requested an agent but dropped before connecting**, schedule a **callback** (via Scheduled Callback node) at a less-busy time. Can **filter** customers (e.g. offer this only to **premium** customers).
2. **Callback on critical-path drops** — define **critical paths** by **enabling transactions** on them (e.g. payment confirmation, fraud reporting). If the customer drops **between transactions**, the disconnect journey checks this and schedules a callback so the brand doesn't lose the critical interaction. (See [[transaction-reporting]].)
3. **Other-channel communication** — after the call, reach the customer via **SMS / Email / WhatsApp**.

## Configure a disconnect journey
1. **Create the journey:** Launchpad → **Journey Facilitator** → Journey Facilitator Manager → create a **trigger-based journey** → define the business logic → Save. (See the Journey Facilitator module.)
2. **Connect it to the IVR:** **IVR Flow Manager** → select the IVR → **⋯ → IVR Settings** → locate the **Disconnect Journey** field → select the configured **JF** from the dropdown → Save.

## Real implementations (HDFC Bank examples)
- **Premium callback:** identify if the caller requested an agent and didn't connect → check if **premium** → **Callback node** to reconnect with an agent (premium treatment).
- **Upsell via SMS:** if a customer opts to hear eligible products and **drops before applying**, trigger an **SMS** with a link to those product details (upsell by the path they took).
- **CRM activity record:** create a **CRM activity** for every IVR call — record who called, options selected, and time → holistic interaction history.

## Notes / gaps
- Built on **Journey Facilitator** (trigger-based journey) + IVR settings; uses **Scheduled Callback** and **transactions** ([[transaction-reporting]]). Related: [[communication-nodes]], [[system-nodes]].
- Part of IVR: [[communication-nodes]], [[transaction-reporting]], [[api-integration]], [[system-nodes]], [[pci-input]].
