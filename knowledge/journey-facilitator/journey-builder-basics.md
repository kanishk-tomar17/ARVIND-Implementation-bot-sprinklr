# Basics of Journey Builder (Journey Facilitator 142)
**Source:** Product Foundation Courses → Journey Facilitator / 142 Basics of Journey Builder (video transcript + demo; Create Journey details screen screenshot) · **Help:** search `site:sprinklr.com/help journey facilitator create journey trigger conditions`

## What it is
**Journey Facilitator** lets marketers create unified, **omni-channel customer journeys** via a visual flow builder. It maps the entire customer journey and communicates across channels — enabling targeted, personalised campaigns at each stage (builds awareness, loyalty, conversions; surfaces pain points).

## Configuration steps — Journey Details (demo)
1. **Open Journey Facilitator.** New tab icon → **Sprinklr Marketing** tab → **Journey Facilitator** (within **Publish**) → **Journey home page**.
2. Click **Add Journey** (top-right) → **Journey Details / Create Journey** page.
3. Fill the **basic details** (some mandatory):
   - **Journey Name** — clearly defines its purpose (e.g. "Product Launch").
   - **Add to Campaign** — assign to a campaign for reporting. **Compulsory.** (See [[campaigns]].)
   - **Conversion** — optional conversion goal.
   - **Start Journey From** — timestamp the journey begins triggering for the audience.
   - **Run Journey Until** — timestamp after which it stops triggering. *Keep a decent gap between start and end for optimal performance.*
4. **Trigger conditions** — three options:
   - **Segment Based** — select an audience **segment** (see [[segment-manager]]).
   - **Profile List Based** — select a **profile list** instead of a segment.
   - **Trigger Based** — two types:
     - **Audience update rules** — trigger when a profile meets specified criteria (changes in audience profiles).
     - **API calls** — trigger on external events (form submissions, on-help purchases, brand integrations).
5. **Share Settings** — visibility across all workspaces or specific ones; control which users / user groups can access.
6. **Message Delivery Settings** — rate limit and business hours per use case.
7. **Save** (or **Save as Draft**) bottom-right → settings saved, you're taken to the **Journey Builder canvas**. *If you don't Save here, all changes are lost.*

## Journey Builder canvas
On the canvas you add **actions and conditions** — automated messages, triggers, content personalised on customer preferences. (Node detail covered in [[journey-nodes]].)

## Notes / gaps
- Sits downstream of [[segment-manager]] / [[audience-profile-import]] and ties to [[campaigns]]; the canvas itself is [[journey-nodes]]; performance feeds [[journey-reporting]].
- Part of Journey Facilitator: [[audience-profile-import]], [[segment-manager]], [[campaigns]], [[journey-nodes]], [[channels-supported]], [[journey-reporting]].
