# Survey on Community (Community 188)
**Source:** Product Foundation Courses → Community / 188 Survey on Community (video transcript + demo) · **Help:** search `site:sprinklr.com/help community survey trigger`

## What it is
Triggering a **survey** on the community to collect feedback from community users.

## Steps
1. **Create the survey** in Sprinklr: Launchpad → search **Create Survey** → **Survey** tab → create a survey via the **Survey Builder**. (Each survey gets a **Survey ID**.)
2. **Configure the trigger UI** in **Community Builder → Content Settings → Survey section:** enable Survey, then set the **Headline, Message, Primary button, Secondary button** — these populate the **trigger-survey pop-up** the user sees (primary = go to survey, secondary = skip).
3. **Enable the survey via a support ticket** — the **Sprinklr engineering team** configures it from the back-end. The ticket must specify **4 conditions**:
   - **Survey ID** (of the created survey).
   - **Authenticated vs unauthenticated users** — trigger for logged-in or non-logged-in users.
   - **Time spent** on the community before the survey triggers (e.g. after 3 minutes).
   - **Re-trigger interval** — after the user skips/completes, after how many days/months to show it again.

Once these 4 conditions are in the support ticket, Sprinklr engineering enables the survey from the back-end.

## Notes / gaps
- Survey creation uses the standard **Survey Builder** (also see Case Management [[survey-rules]]); community triggering is a **back-end/support-ticket** step (not fully self-serve).
- Part of Community: [[community-builder]], [[global-workspace-roles]], [[message-level-rules]], [[live-chat-on-community]], [[guided-workflow-on-community]], [[spam-model]], [[case-management-for-community]], [[social-sso]], [[support-ticket]], [[community-reporting]].
