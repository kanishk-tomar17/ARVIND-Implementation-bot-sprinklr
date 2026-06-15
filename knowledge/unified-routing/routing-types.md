# Routing Types & Case Sorting (Unified Routing 029)
**Source:** Product Foundation Courses → Unified Routing / 029 Routing types (video transcript) · **Help:** search `site:sprinklr.com/help unified routing type no skill all skill best skill sort works by`

## Three routing types (how an agent is chosen)
- **No skill matching** — ignores skills/proficiency; assigns the next available agent. (Equivalent to **queue-based routing**.)
- **All skill matching** — assigns to an agent who has **all** the skills tagged on the case.
- **Best skill matching** — uses skills **and proficiency**; assigns the agent with the highest **combined** proficiency across the required skills.

## "Sort works by" (how pending cases are ordered)
- **Work creation time** — cases **created** earliest are assigned first.
- **Work queue assignment time** — cases **added to the queue** earliest are assigned first.
  - Prefer **assignment time** for **returning/on-hold** cases, so a reopened (old-creation-time) case doesn't jump ahead; ordering reflects queue wait.

## Assignment process
**No skill matching:** case enters queue → waits if backlog → pick next case by sorting → fetch available agents (by availability status) → pick the one with the **highest free capacity** (load balance) → ties → **most idle** (received last case earliest) → assign → **post-assignment rules** fire → capacity consumed.

**All skill matching:** tag skills (rule/IVR/bot) → case to skill-based queue → fetch available agents with **all required skills** → sort by capacity → most idle → assign → post-assignment rules.

**Best skill matching:** fetch available agents with required skills → **score = Σ (case skill required × agent proficiency)** across skills → sort → top agent → ties → most idle → assign → post-assignment rule.

## Sorting + priority (precedence)
- **Priority is always the first sort criterion.** Highest-priority case is picked first.
  - With all/best skill matching, a high-priority case **waits** if no skilled agent is available; otherwise it goes first.
- Then, among equal/no-priority cases, **"sort works by"** decides (creation time = oldest created; assignment time = longest waited in queue) → then the routing algorithm runs.
- ⚠️ **Priority is only considered within a single work queue.** If agents belong to multiple queues with different-priority cases, there's **no cross-queue ordering** — a lower-priority case can be assigned first.

## In the platform
Work queue → edit → select **Routing type** + **Sort works by** (help text explains each) + a **Post-assignment rule** to run after assignment.

## Notes / gaps
- This is the **master routing topic** — [[agent-skills]], [[routing-configuration]], [[smart-routing]] all build on these three types.
- "Highest free capacity, then most idle" is the universal tie-break — load-balances across agents.
- No cross-queue priority ordering is a real gotcha for agents staffed on multiple queues.
