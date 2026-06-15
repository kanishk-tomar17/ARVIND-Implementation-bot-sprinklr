# AI in Engagement (Sprinklr Social — Engagement)
**Source:** sprinklr.com/help — Engagement sub-area (multiple articles; see links below)

## What it is
- A set of Sprinklr AI capabilities layered into the [[engagement-dashboards]] and Reply Publisher to make agents faster and safer.
- Three distinct tools: an **Intuition model** that predicts whether an inbound message is worth engaging, **Smart Response Compliance** that vets outbound replies for brand risk, and a **Comment Summarizer** that aggregates and analyzes post comments.
- All three combine Sprinklr AI with the [[rule-engine]] and report into [[reporting]].
- Each is gated by a specific workspace permission, so consultants must enable roles before agents can use them.

## Key features & how to use

### Intuition model — predicted engageability of messages
- **Purpose:** classifies inbound social messages as **Engageable** (needs brand engagement) or **Non-Engageable** (no response needed), across channels and both owned and earned data.
- **What it reads:** text content only. **Photos / Videos / Links are NOT used to classify a message.**
- Classification works across three approaches:
  - **Message-based analysis** — customer intention (excitement, product love, purchase intent, education needs, service requests) and content (complaints, usage queries, praise, non-branded mentions, mild language). Excludes trolls, spam, conspiracy theories, news shares, unsolicited ideas, strong profanity, and references to illegal activity.
  - **Social profile conditions** — engages genuine profiles (not on exclusion lists), verified accounts, and influencers (configurable); avoids parody, commercial, and employee accounts and profiles with offensive bios.
  - **Conversation history** — messages in active conversations or with open cases are marked engageable; messages older than a configured period (e.g. 4 days) are marked non-engageable.
- **Accuracy:** stated as 80%+ overall (human teams ~85% under the same guidelines).
- **Feedback loop:** users can correct classifications; the model retrains on that feedback.
- **Config approach:** hybrid — Sprinklr AI plus the [[rule-engine]].

### Smart Response Compliance — vetting outbound replies
- **Purpose:** AI-powered check that vets outbound social responses against community standards and flags brand-risk content.
- **Four compliance categories:**
  - **Biased Content** — discriminatory responses (race, religion, gender, age) and controversial opinions.
  - **Profanity** — abuses, slurs, adult content.
  - **Relevance** — whether the response is relevant to the prior conversation.
  - **Tonality** — whether the tone is aggressive or lacks warmth/empathy.
- **How to use:**
  1. Go to **Engagement Dashboards** under **Sprinklr Social > Engage**.
  2. Select the desired dashboard from Engagement Home.
  3. Hover over a message and click the **Reply** icon.
  4. In the **Reply Publisher** window, the AI runs the compliance check.
  5. A **yellow flag** appears if the response falls under any violation category.
  6. Click **Send** to publish.
- **Important:** non-compliant posts are **not blocked** — flags are warnings only.
- **Permission:** users need the **Enable Response Compliance** permission (Platform Setup > Workspace Roles > Create Role).
- **Enforcement via rules:** in **Sprinklr Social > Triage > Manage Rules > Create New Rule** set Rule Scope (Customer/Workspace), Context = **Outbound**, Conditions (**Is Biased, Is Improper Tone, Is Irrelevant, Is Profane**), and Actions (e.g. approval mechanisms). See [[rule-engine]].
- **Reporting:** build widgets in **Sprinklr Social > Analyze > Reporting** using dimensions **Relevance, Response Tone, Biased Content, Profanity**. See [[reporting]].
- **Feedback loop:** users can give feedback on flagged content to retrain the model for brand-specific behavior.

### Comment Summarizer & Insights — Sprinklr AI comment summaries
- **Purpose:** automatically aggregates and analyzes all comments on a social post, with sentiment (positive / negative / neutral) and intent detection (questions, complaints, feedback).
- **Channel support:** Facebook, Instagram, and LinkedIn (article notes expansion to all social/review channels; multi-language translation noted as future).
- **Use on an existing dashboard:**
  1. Open an Engagement Dashboard and select a channel (Facebook Posts, Instagram Media, or LinkedIn Company Status Update).
  2. Find a post with **10+ comments**.
  3. Click the **Generate Summary** icon (top-right corner).
  4. View the summary and insights on the right side.
- **Use on a new dashboard:**
  1. New Tab > Sprinklr Social > Engagement Dashboards.
  2. **Create Dashboard**, fill mandatory fields.
  3. **New Column** / **Add Column**.
  4. Select channel and column type.
  5. Fill Name and Account/Account Group fields.
  6. **Create Column**, then follow the existing-dashboard steps.
- **Permission:** role needs the **Engagement AI** permission to see the Generate Summary button.

## Common issues & fixes
- **Generate Summary button missing** — the role lacks the **Engagement AI** permission; add it.
- **Summary won't generate** — the post has fewer than the required **10 comments** minimum.
- **Comment summary unavailable on a column** — only supported on engagement dashboards (channel and workflow columns); **not** available on outbound columns, editorial calendars, or reporting dashboards.
- **Response Compliance flag ignored / post still sent** — by design: flags are warnings, not blocks. Use a Triage outbound rule to add an approval/enforcement step.
- **Intuition misclassifying messages** — correct the classification in-product; the model retrains on the feedback.

## Notes & gaps
- **Permissions are prerequisites:** Enable Response Compliance (compliance) and Engagement AI (comment summary) must be granted via workspace roles before agents can use these.
- Intuition reads **text only** — image/video/link-only posts won't be classified reliably.
- Stated accuracy figures (80%+ Intuition) are model-level, not guarantees per message.
- The articles do **not** specify: exact licensing/SKU requirements, the configurable "older than X days" default for Intuition, rate/volume limits, or the full list of channels for the expanded Comment Summarizer rollout.
- Related areas for end-to-end setup: [[care-console]], [[sla-monitoring]], [[data-engine]].

## Sources
- Get predicted engageability of messages with Intuition model — https://www.sprinklr.com/help/articles/leverage-ai-for-better-engagement/get-predicted-engageability-of-messages-with-intuition-model/6454a453f65d86626c82b91a
- Smart Response Compliance — https://www.sprinklr.com/help/articles/leverage-ai-for-better-engagement/smart-response-compliance/6454a6010d27fc559bbeb4a5
- Generate Comment Summary using Sprinklr AI — https://www.sprinklr.com/help/articles/sprinklr-ai/generate-comment-summary-using-sprinklr-ai/687103c96862622c547443a8
