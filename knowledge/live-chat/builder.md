# Live Chat Builder (Live Chat 086)
**Source:** Product Foundation Courses → Live Chat - Live Chat Builder (086, video transcript + demo) · **Help:** search `site:sprinklr.com/help live chat builder embed`

## What it is
**Live Chat Builder** is the feature in Sprinklr used to **configure a live chat application** — customise and set up every aspect of the chat experience to the brand's names/requirements. This topic covers: what the builder is, creating a new live chat app, deploying it for UAT/testing, and embedding it on the brand's website.

## Prerequisite — permission
Make sure you have the **Manage Sprinklr Live Chat** permission: User → **Permissions** → search "live chat" → enable it.

## Create a live chat application
1. Open the **Launchpad → Sprinklr Services → Listen → Live Chat Care**. This lists all existing live chat applications for the partner (view, edit, search, create).
2. Click **Create** a new application and fill:
   - **Account name** — internal name used inside Sprinklr to identify the account.
   - **Account display name** — the **brand name shown to end customers** (e.g. "Sprinklr Support").
   - **URLs (whitelisting)** — list of URLs where live chat will be operational. Use **`*`** to allow it on **all** websites where the embed code is present; otherwise list specific URLs.
   - **Language** — a **default language**; for multilingual, add **additional languages** → **auto-translation** of all **static labels** based on the user's browser locale.
3. **Personalize your live chat** — 3 subsections:
   - **Style** — theme, colour, background, background patterns, and the **chat trigger icon** + its **visibility criteria** (conditions like time spent on page, page URL, business hours, whether the customer already has a conversation open). Default: trigger icon "always appear".
   - **Home screen** — brand **logo**, title, description, media on the starter conversation card; **chat actions** (maximize widget, clear session, delete all conversations, close all conversations).
   - **Conversation screen** — title, description, **welcome messages** (with conditions for different welcome messages); chat actions (delete/close chat, **download chat transcript**, start new chat).
4. **Audio and Video** — enable audio/video calls on the account if a **video account** is enabled in the platform (e.g. a **Chime** account). Related: [[video-cobrowsing]].
5. **Co-browsing** — collaborative browsing where agent + customer browse the brand's site together (annotations, screen control) — covered in the [[video-cobrowsing]] video.
6. **Advanced settings** — numerous extra settings/customisations exposed as toggles.
7. Click **Create**. (Enrollment section covered separately.)

## Test the application (UAT)
- Sprinklr provides a **test URL**: add your **live chat App ID** + **environment**, and **whitelist** that test URL.
- Find the **App ID** on the **Live Chat Care** screen; paste into the test URL, set environment (e.g. **prod**), hit enter → the live chat renders for testing with all your customisations.

## Deploy on the brand's website (embed)
- Live chat is added by embedding a **one-time JavaScript code** on the website — it auto-embeds the chat.
- For multi-page sites, embed the JS on **all pages**, preferably **near the bottom**.
- **Whitelist** the URLs where the code is embedded, or the chat won't show.
- To get the code: app → **three dots (⋯) → Embed** → choose a **skin**:
  - **Modern skin** — new, stylish, all latest features → **use this**.
  - **Classic skin** — legacy clients only.
- Copy the embed code from the next screen and share with the client.

## Notes / gaps
- This is the build-and-deploy core; deeper customisation lives in [[customisation]], rules in [[rule-actions]], deflection in [[chat-deflection]], web/SDK setup in [[web-setup-sdks]], proactive prompts in [[proactive-prompts]].
- For more, the Live Chat **Knowledge Base article** / Live Chat product team.
