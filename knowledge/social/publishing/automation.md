# Automation in Publishing (Sprinklr Social — Publishing)
**Source:** sprinklr.com/help — Publishing sub-area (multiple articles; see links below)

## What it is
- A set of [[rule-engine]] use cases that automate governance and response on outbound/inbound social content.
- Covers crisis controls (stop publishing, block expiring assets), compliance (highlight non-compliant keywords), source-based tagging/approvals (request source), auto-translation, and after-hours auto-replies.
- Almost everything here is built in the **Rule Engine** (Manage Rules within Triage, or Rule Engine within Collaborate). Most rules can be **saved without being enabled**, so you stage them and switch on when needed.
- Rule scope: **Customer** rules apply globally across all workspaces/environments; **Workspace** rules apply only in the current workspace.

## Key features & how to use

### Configure Rules to Stop Publishing
- Purpose: halt publishing of outbound content from some or all social accounts — a crisis-management lever. Can be saved disabled and enabled only when needed.
- Three rule contexts, each fires at a different point:
  - **Outbound** rule — applies to messages at the time of publishing. Does **not** apply to scheduled messages.
  - **Pre-Publishing** rule — applies at the time of message creation; stops both scheduled and non-scheduled messages. Offers more governance actions (including reschedule to publish later).
  - **Autofill** rule — stops team members from even accessing the Publisher, showing a notification that publishing is paused (saves wasted drafting time).
- Steps: Sprinklr Social tab > **Manage Rules** > Rule Engine > pick **Workspace** or **Customer**.
- Example outbound rule (stop all publishing):
  - **Condition:** Channel condition `Account is All Accounts` (use Account and/or Channel to scope to specific channels/brand accounts).
  - **Action (governance):** `Stop publishing of Message`.
- Example pre-publishing rule (stop only Facebook):
  - **Condition:** `Account is All Accounts`
  - **Condition:** `Message Type is Facebook Post`
  - **Action:** `Stop Publishing`
- Related: [[editorial-calendar]] (scheduled content this can block), [[approval-workflows]].

### Restrict Users from Publishing an Asset That Is Going to Expire
- Purpose: prevent publishing/scheduling of assets that expire within a set timeframe — content control for crisis management.
- Steps:
  1. New Tab icon > **Manage Rules** within Triage (Sprinklr Social).
  2. **Create New Rule** (top right).
  3. Enter name + optional description; set **Context = Outbound**; set **Activation Date**.
  4. Next > Rule Builder > Add icon > **Add Condition**.
  5. Under *Conditions Applies To*, set **Condition = `Asset Expires In`** and choose the values (timeframe) accordingly.
  6. Add icon > **Add Action** to configure the resulting action; **Save**.
- This is an **Outbound Message** rule. Related: [[asset-manager]].

### Configure Rules to Auto-Respond to Messages
- Purpose: auto-reply to inbound messages from a given account — e.g. an after-hours response on every message received outside working hours.
- Configured as **Inbound** (or Queue) rules. Requires a saved reply template first.
- Step 1 — create the response template:
  1. New Tab > Sprinklr Social > **Assets within Engage**.
  2. **Create Asset > Text** (top right).
  3. Pick the **Channel** for a channel-specific template, enter the response text, set details, **Save**.
- Step 2 — build the rule:
  1. New Tab > Platform Modules > **Rule Engine within Collaborate** > **Create New Rule**.
  2. Name + optional description; **Rule Scope = Workspace or Customer**; **context = Inbound**; Next.
  3. Rule Builder > ➕ > **Add Condition**. Under *Conditions Applies To "The source of the Message"*: set **`Account Is`** = the account you'll reply from.
  4. In the **Yes** branch add a condition: *The source of the Message* > **`Message Type Is`** = the content type to respond to.
  5. (After-hours pattern) add condition *The Source of Message* > **Condition = `Business Hours`**, **Operator = Is**, **Value = your defined Business Hours**.
  6. On the **No** branch of the final condition (so it fires outside business hours): **Add Action** > *Actions To "Auto Respond to a message"* > **`Send Auto Response To`** > pick the channel.
  7. **Add Required Details** to enter the auto-response details; **Save**.
- **Auto Respond field descriptions:**
  - **Choose Account to Reply From** — the account set in your first condition (the social account you reply from).
  - **Choose Campaign** — campaign to stamp on outbound auto-responses.
  - **Choose Preferred Reply Type** — options depend on the selected account.
  - **Choose Reply Template** — the post asset created in Asset Manager.
  - **Time Duration of Last Auto Message** — interval between auto-responses; set at least a few minutes to avoid unintended/too-rapid triggering.
- **Supported channels / message types** (auto-respond): LinkedIn Company DM; Bazaarvoice Review Comment; Trustpilot Reviews; X (Twitter) DM, Reply, Reply All; Facebook Messenger, Facebook Comment; Line Message; WeChat Message; Lithium Message, Lithium Private Note; Email Reply; Viber Message; GooglePlus Business Reviews Reply; VK Business Messages; Weibo Replies/DM/Comments; Google Play Store Reply; Discourse Comments; Telegram Messages; Instagram Comment, Reply, and DM.
- **Instagram gate:** auto-response for Instagram is controlled by the [[dynamic-properties|dynamic property]] **`<AUTO_RESPONSE_ENABLED_ACCOUNT_TYPES>`** — enable via Success Manager or a request to tickets@sprinklr.com.

### Highlight Non-Compliant Keywords
- Purpose: flag prohibited words during post creation and **block publishing until they are removed** (compliance guardrail).
- Step 1 — create the keyword list:
  1. New Tab > Platform Modules > **Keyword Lists within Unify**.
  2. **Add Keyword List** (top right).
  3. Enter **Name**, **Tags**, and **Query Words** (the prohibited keywords); **Save**.
- Step 2 — build the rule:
  1. New Tab > Sprinklr Social > **Manage Rules within Triage** > **Create New Rule**.
  2. Name + optional description; **Rule Scope = Workspace**; **Rule context = Autofill**.
  3. **Add Condition**, name it; *Conditions Applies to "The properties of the outbound Message"* > **`Message Keywords`** > under **Select Keyword List** choose your list.
  4. On the **Y node** > **Add Action** > set all to **Yes**: **`Highlight Search Items`**, **`Highlight Link Search Terms`**, **`Highlight Image Search Terms`**, **`Highlight Video Search Terms`**.
  5. **Save**, then **enable the rule** via the Options icon.
- With **Autofill** context the rule will not let users continue publishing until the non-compliant words are removed. Other usable contexts: **Pre-publishing** and **Outbound**.
- Related: [[ai-in-publishing]], [[approval-workflows]].

### Request Source in Outbound Message Conditions
- Purpose: in **outbound** rules, branch on where a message originated — to set custom fields, tags, or campaigns by source, or to force a mandatory approval path for messages from widgets.
- "Request Source" is simply a **condition** in the rule engine for outbound messages.
- Steps:
  1. New Tab > Platform Modules > **Rule Engine within Collaborate** > **Create New Rule**.
  2. Name + optional description; **Rule Scope = Workspace or Customer**; **context = Outbound**; Next.
  3. ➕ > **Add Condition**; choose **`Request Source`**.
  4. Select the source value(s) for the rule; **Save**.
- **Request Source values:**
  - **Apps** — published through Social Apps.
  - **API** — published through Sprinklr APIs (access via Mashery).
  - **Mobile** — published through Sprinklr Mobile Apps.
  - **Commerce** — published through Sprinklr Commerce.
  - **UI** — published through the Sprinklr Web UI.
  - **Widgets** — published through widgets.
  - **Auto Poster** — published through the Auto Poster on accounts where RSS Feed auto-posting is enabled.
- Example: **Condition** `Request Source is Widget` > **Action** `Tag with Widget` (Message Property action that tags matching messages with a pre-configured tag).
- Related: [[approval-workflows]], [[rule-engine]].

### Integrate Custom Translators in Sprinklr
- Purpose: auto-translate inbound/outbound customer messages so agents read conversations in their own language while replying in the customer's language, inside Engagement Dashboards.
- Built as a **Customer** rule on **Case Creation/Case Update**.
- Steps:
  1. Sprinklr Social > New Tab > **Manage Rules within Triage** > **Create New Rule**.
  2. Enter Name + Description; **Rule Scope = Customer**; **Context = Case Creation/Case Update**.
  3. Adjust **Activation Date** and **Rule Execution Batch** (or accept defaults); Next.
  4. Rule Builder > Add icon > **Add Condition** > under *Universal Case* set **`Added Queue`** = the desired queue.
  5. On the **Yes** branch > Add icon > **Add Action** > under *Universal Case* set **`Mark case for Language translation` = Yes**.
  6. **Save**.
- **Supported translation models:** DeepL, Azure, Google. Brands can integrate their own custom-trained models by contacting their Success Manager.

## Common issues & fixes
- **Stop-publishing rule didn't catch scheduled posts:** Outbound-context stop rules do **not** apply to scheduled messages. Use a **Pre-Publishing** rule to also stop scheduled/non-scheduled content.
- **Non-compliant keyword rule lets users publish anyway:** the hard block (cannot continue until words removed) applies under the **Autofill** context. Pre-publishing/Outbound contexts behave differently.
- **Auto-response firing too often:** set **Time Duration of Last Auto Message** to at least a few minutes to throttle replies and avoid unintended triggers.
- **Instagram auto-response not available:** it is gated by dynamic property `<AUTO_RESPONSE_ENABLED_ACCOUNT_TYPES>` — request enablement via Success Manager or tickets@sprinklr.com.

## Notes & gaps
- **Two entry points to the same Rule Engine:** "Manage Rules within Triage" (Sprinklr Social tab) and "Rule Engine within Collaborate" (Platform Modules) are used interchangeably across these articles.
- **Permissions:** the articles do not specify user-permission/role names required to create or enable these rules. Confirm rule-engine access per workspace before building in a client environment.
- **Limits:** no numeric limits stated for number of rules, keyword-list size, or expiry timeframes — the expiry timeframe and auto-response interval are free-set "values accordingly."
- **Custom translators:** the article does not document language-pair limits, cost, latency, or how custom-trained models are technically supplied beyond "contact your Success Manager."
- **Request Source / Asset-Expiry articles** describe the condition and one example action each, not the full action catalog available on those branches.
- Screenshots in the source articles are not reproduced here; field names are transcribed verbatim from the article text. Always verify exact labels against the live tenant, as UI labels drift between releases.
- Related GROOT topics: [[rule-engine]], [[approval-workflows]], [[editorial-calendar]], [[ai-in-publishing]], [[asset-manager]], [[dynamic-properties]], [[web-analytics]].

## Sources
- Request Source in Outbound Message Conditions — https://www.sprinklr.com/help/articles/automation-in-publishing/request-source-in-outbound-message-conditions/64548eff0d27fc559bbeb465
- Integrate Custom Translators in Sprinklr — https://www.sprinklr.com/help/articles/automation-in-publishing/integrate-custom-translators-in-sprinklr/650bcf31cc94fb3f6632c55d
- Restrict Users from Publishing an Asset That Is Going to Expire — https://www.sprinklr.com/help/articles/automation-in-publishing/restrict-users-from-publishing-an-asset-that-is-going-to-expire/6568d70044f32b4163d56d6c
- Configure Rules to Stop Publishing — https://www.sprinklr.com/help/articles/automation-in-publishing/configure-rules-to-stop-publishing/64549171f65d86626c82b8e2
- Configure Rules to Auto-Respond to Messages — https://www.sprinklr.com/help/articles/automation-in-publishing/configure-rules-to-autorespond-to-messages/64548fc40d27fc559bbeb467
- Highlight Non-Compliant Keywords — https://www.sprinklr.com/help/articles/automation-in-publishing/highlight-noncompliant-keywords/64548fe6f65d86626c82b8e0
