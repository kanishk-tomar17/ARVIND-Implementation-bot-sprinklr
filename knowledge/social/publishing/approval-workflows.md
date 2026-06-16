# Approval Workflows (Sprinklr Social — Publishing)
**Source:** sprinklr.com/help — Publishing sub-area (multiple articles; see links below)

## What it is
- Approval workflows force posts through a review/sign-off path before they publish, so no content goes live without the right people approving it.
- Reviewers can be a single account owner, or a structured **approval path** combining **tiered** (sequential) and **parallel** (simultaneous) approvers.
- Goal: prevent bottlenecks, add accountability, and keep brand/messaging/quality consistent across teams.
- Approval can be set manually per post at publish time, or applied automatically via the Rule Engine ([[rule-engine]]).
- After approval, what happens to the post depends on its scheduled time (publish now, hold to schedule, or pending reschedule).

## Key features & how to use

### Set the approval workflow while publishing
- Open the composer: **Publishing Options icon** (top-right of the Navigation Bar) > **Create Post**.
- Two composer modes: the default **Quick Publisher** window, or the **Maximized Create Post** window (click the Maximize icon).
- In the post, set the approval type. Three options:
  - **Not Required** — default; post publishes with no approval.
  - **Required By Account Owner** — the account owner is the sole approver.
  - **Follow an Approval Path** — uses a pre-built workflow combining tiered and parallel approvals.
- **Approval Note** — add a note to give approvers extra context; you can attach media files or documents.
- **View icon** in the approval section — shows the full approval chain (approver sequence and hierarchy levels) for the selected workflow.
- Click **Submit** after choosing the approval path. The post only publishes once approval is complete.

### Apply approval automatically via the Rule Engine
- Path: **Platform Modules > Collaborate > Rule Engine** (outbound rule).
- Action options:
  - **Set User Approval** — pick an individual approver from the dropdown.
  - **Set Approval Path** — pick a pre-created workflow from the dropdown.
  - **Set if absent** operator — applies the approval only when the post author hasn't already assigned one.
- See [[rule-engine]] for building the conditions that trigger these actions.

### Tiered approvals (overview)
- Tiered approvals define the **steps (sequence) in an approval workflow** — content moves through approvers in order before it can publish.
- Use them to enforce structured, multi-reviewer sign-off so the right people review in turn.
- Notable: approvers can update/edit the post content to fix an error even after publishing.
- Implementation steps live in the "Create a tiered approval" article (see Notes & gaps — the body of that article did not render for capture).

### Parallel approvals (overview)
- Parallel approvals let multiple approvers review at the **same time** rather than in sequence, and are combined with tiered steps inside an approval path.
- Detailed mechanics/conditions were not captured (see Notes & gaps).

### Approve / reject posts
- Approvers act on submitted posts from the approval queue and receive email confirmation when a message is approved and published.
- Users with approval-queue permissions can recall a post from the queue.
- Exact button names and queue UI steps were not captured (see Notes & gaps).

### Publishing scenarios after approval
What happens once a post is approved depends on its scheduled time:
- **No scheduled time** — the post publishes **instantly** on approval.
- **Approved before the scheduled time** — the post returns to **Scheduled Message** status and goes out at the scheduled time.
- **Approved after the scheduled time has passed** — the post moves to **Pending Reschedule** status in the Outbound column; you can then reschedule or recall it. (Requires specific configuration via your Success Manager.)
- Posts can be recalled after approval if not yet published, subject to user permissions.
- The full create-and-approve workflow can be automated (via [[rule-engine]]).
- See [[editorial-calendar]] for managing scheduled/pending posts.

## Common issues & fixes
- **Post not publishing at the scheduled time** — if approval lands after the scheduled time, the post will not auto-publish; it goes to **Pending Reschedule** and must be rescheduled or recalled manually.
- **Pending Reschedule not appearing** — this behavior needs specific configuration enabled through your Success Manager; raise it with them if missing.
- **Approval set twice (author + rule)** — use the **Set if absent** operator on the rule so it only applies when the author hasn't already assigned an approver, avoiding conflicting/duplicate paths.

## Notes & gaps
- **Prerequisites/permissions:** approval-queue permissions are needed to approve/reject and to recall posts from the queue; recall after approval depends on user permissions. The articles do not list the exact role/permission names.
- **Success Manager dependency:** the Pending Reschedule scenario requires backend configuration via Sprinklr's Success Manager.
- The body content of three source articles did not render for capture: **Approve/Reject posts**, **About Parallel Approvals**, and **Create a tiered approval**. Their step-by-step UI details (exact button names, navigation path to build a tiered/parallel path, number of tiers, approver-selection fields, and any limits) were therefore not captured here — consult those URLs directly before configuring.
- The "About tiered approvals" article does not specify tier levels, configuration fields, conditional logic, or technical limits; it points to the "Create a tiered approval" article for setup.
- Related ARVIND topics: [[approval-workflows]], [[rule-engine]], [[editorial-calendar]], [[ai-in-publishing]], [[asset-manager]], [[web-analytics]].

## Sources
- How to set the Approval Workflows while publishing — https://www.sprinklr.com/help/articles/approval-workflows/how-to-set-the-approval-workflows-while-publishing/6454897b0d27fc559bbeb45e
- Approve/Reject posts — https://www.sprinklr.com/help/articles/approval-workflows/approvereject-posts/64548de5f65d86626c82b8d3 (body did not render; title/URL only)
- About Parallel Approvals — https://www.sprinklr.com/help/articles/approval-workflows/about-parallel-approvals/64548d490d27fc559bbeb460 (body did not render; title/URL only)
- About Tiered Approvals — https://www.sprinklr.com/help/articles/approval-workflows/about-tiered-approvals/64548737f65d86626c82b8cb
- Create a Tiered approval — https://www.sprinklr.com/help/articles/approval-workflows/create-a-tiered-approval/64548a6a0d27fc559bbeb45f (body did not render; title/URL only)
- Publishing scenarios after approval — https://www.sprinklr.com/help/articles/approval-workflows/publishing-scenarios-after-approval/645489d0f65d86626c82b8cc
