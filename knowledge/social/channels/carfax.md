# Carfax (Sprinklr Social — Channel)
**Source:** sprinklr.com/help — Carfax channel (multiple articles; see links below)

## What it is
- Carfax is a Sprinklr Social channel for managing **vehicle dealer reviews and replies** from Carfax inside Sprinklr.
- Core use is **engagement**: view reviews and the replies on them, and reply to or edit replies on reviews.
- **Reporting is limited** to SLA and inbound reporting for Carfax conversations only.
- **Not self-serve**: the Carfax integration must be set up manually for the client by a Sprinklr Success Manager — consultants cannot add Carfax accounts themselves like other channels.

## Key features & how to use

### Capabilities & limitations (engagement scope)
- **Engagement supported:** view reviews and their replies; edit an existing reply.
- **Reporting supported:** SLA reporting and inbound reporting — only for Carfax conversations. See [[reporting]].
- **One reply per review:** a review can have only **one** reply. Once a reply is given, the reply icon for that review is disabled.
- **Re-editing allowed:** you can re-edit a reply you already edited.
- **Cannot delete** reviews or replies.
- **No emoji replies** — emoji are not supported in Carfax replies.
- **Manual onboarding:** Carfax accounts are added only via the Sprinklr Success Manager (custom integration), not through normal channel-add self-service.

### Create a Carfax column (engagement setup)
Builds a column in an Engagement Dashboard to surface Carfax messages. See [[engagement-dashboards]].
1. Click the **New Tab** ("+") icon, then go to **Engagement Dashboards** under the **Sprinklr Social** tab within **Engage**.
2. From **Engagement Home**, search and select the engagement dashboard you want.
3. Click **Add Column** (top-right of the dashboard).
4. In the **Add New Column** window, search for and select **Carfax** as the source.
5. In the **Add New Carfax Column** window (titled "Select the type of column you'd like me to make"), choose a column type:
   - **Inbox**
   - **Reviews**
   - **Replies**
   - A live **Column Preview** renders on the right as you configure.
6. Configure basic settings: **Name**, **Description**, **Accounts** (as needed), and other basic info.
7. Set **workflow properties** — message workflow status, user assignment, priority, spam designation, and sentiment.
8. Add **custom properties** to include or exclude messages based on the applied properties.
9. Click **Create Column** (bottom-right). Use **Back | Select Sources** to change the source, or **Cancel** to discard.

## Common issues & fixes
- **Reply icon greyed out / disabled** — expected behaviour: the review already has its one allowed reply. Edit the existing reply instead of adding a new one.
- **Can't add emoji to a reply** — not supported on Carfax; use plain text.
- **Can't delete a review or reply** — not supported; deletion is unavailable on this channel.
- **Can't add a Carfax account in channel setup** — requires manual integration via the Sprinklr Success Manager.

## Notes & gaps
- **Prerequisites:** Carfax integration provisioned by the Sprinklr Success Manager before any account/column setup; access to **Engage > Engagement Dashboards** with permission to add columns.
- **Publishing:** not documented for Carfax — these sources cover only engagement (reviews/replies) and limited reporting. No outbound publishing workflow described. See [[publishing]].
- **Reporting:** only SLA and inbound reporting are confirmed; broader review-analytics dashboards are not specified in these articles.
- **Unspecified:** exact workflow/custom-property field options, account-mapping detail, and any rate/volume limits are not detailed in the sources. See [[rule-engine]].

## Sources
- Carfax — Capabilities and Limitations: https://www.sprinklr.com/help/articles/carfax/carfax-capabilities-and-limitations/64557f190104980882a55591
- Create a Column for Carfax: https://www.sprinklr.com/help/articles/carfax/create-a-column-for-carfax/64557f19e66f2e36b45135bf
