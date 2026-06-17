# Unified Routing — Overview & App Map

**What it is:** Unified Routing (UR) is Sprinklr's assignment engine that routes incoming work items (cases/messages/calls) to the right agent based on queues, skills, capacity, and priority. It supersedes the legacy Assignment Engine.

**Where it lives:** Launchpad → **Unified Routing** (ROUTE section) → opens the Unified Routing app at `/unified-routing-app/unified-routing/queues`.

## The app's 6 tabs (components)
The UR app has a left/top sub-nav with six tabs. Each is the entry point for one building block:

| Tab | URL slug | What it's for | Deep-dive KB |
|---|---|---|---|
| **Queues** (Work Queues) | `/unified-routing/queues` | Virtual holding areas that store work items before assignment; carry the routing type, sort order, assignees, stickiness, and routing-configuration relaxation. | [[routing-types]], [[routing-configuration]], [[stickiness-timeout]], [[wait-time-queue]], [[troubleshooting-assignment]] |
| **Skills** | (Skills tab) | Agent competencies used for skill-based routing; grouped under **Skill Categories**. Create via *Add Skill* (needs a category) / *Add Skill Category*. | [[agent-skills]] |
| **Agents** | (Agents tab) | Agents/user-groups eligible for assignment; per-agent **skills + proficiency** and **capacity** are set here (and via bulk edit / user groups). | [[agent-skills]], [[capacity-configuration]] |
| **Capacity Configuration** | (Capacity tab) | Capacity profiles = how many simultaneous interactions an agent can take (points out of ~100, per channel), with overflow, dynamic idle reduction, daily targets. | [[capacity-configuration]] |
| **Custom Channels** | (Custom Channels tab) | Configurable routing options for **client-specific interaction types beyond standard channels**; use filtering criteria to categorize/route specialized incoming work. | [[custom-channels]] |
| **Debug Console** | (Debug Console tab) | Shows the **specific reasons cases were waiting in a queue over time** (historical, case-level) to find assignment bottlenecks. | [[debug-console]], [[troubleshooting-assignment]] |

### Verified live (prod8, 2026-06-18) — URLs & gotchas
- **Queues:** `/unified-routing-app/unified-routing/queues` → *Add Work Queue*.
- **Skills:** Skills tab → *Add Skill* (needs a Skill Category) / *Add Skill Category*.
- **Agents:** `/unified-routing/agents` → **surfaces the User Groups list** (agents are managed via user groups for routing eligibility, skills & capacity; edit a group/user to assign skills + a capacity profile).
- **Capacity Configuration:** `/unified-routing/capacity-configurations` → *Add Capacity Profile* (name only mandatory; Default Capacity 100; +Capacity Group per channel; Simulate).
- **Custom Channels:** `/unified-routing/custom-channels` → *Add Custom Channel* (Name + ≥1 Property Filter mandatory).
- **Debug Console:** `/unified-routing/debug-console` → **permission-gated** ("Access Denied" even for Global Admin); sub-views *Debug Console* + *Reporting Dashboard*.
- **Sub-nav note:** the UR tab bar hydrates a moment after load and navigates via onClick (not plain hrefs) — drive it by clicking the tab refs, not by guessing URL slugs (several slugs 404 / redirect to User Groups).

## Routing types (set per queue)
- **No Skill Matching** — any eligible agent in the queue.
- **All Skill Matching** — only agents meeting *all* required skills (with **no skills defined, this is the simplest default** — it considers all assignees). *(Best practice #4.)*
- **Best Skill Matching** — proficiency-scored; routes to the best-suited agent.
- **Round Robin** — sequential distribution regardless of idle time.
See [[routing-types]].

## How a case flows (mental model)
Case enters → lands in a **Queue** → UR filters eligible **Agents** by routing type + **Skills** → respects **Capacity** → applies **priority/sort** → assigns. If no one is eligible, **Routing Configuration** progressively relaxes constraints (drop skill, lower proficiency, backup queue); **Stickiness** prefers the last-engaged agent for returning cases; **Debug Console** explains waits.

**Source:** Product Foundation Courses → Unified Routing (course series 023–030). **Help:** sprinklr.com/help → *Automation and Assignment > Unified Routing Overview* — "Components of Unified Routing" (`/articles/unified-routing-overview/components-of-unified-routing/6985c271243d9d29873a5255`), "What is Unified Routing?", "Journey of a Customer Message".
