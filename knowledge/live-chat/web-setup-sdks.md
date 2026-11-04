# Live Chat Web Setup & SDKs (Live Chat 091)
**Source:** Product Foundation Courses → Live Chat / 091 Live chat web setup and SDKs (video transcript + on-screen demo) · **Help:** search `site:sprinklr.com/help live chat embed code SPRChat SDK custom field`
**On-screen scenario:** demo brand site `acmesprinklr.com` (Acme) with a "Chat with us" widget; SDKs tested live in the browser **DevTools → Console** on a UAT page.

## SDKs — what they are
**SDK** (Software Development Kit) = a set of tools/**code snippets** used to **communicate between the website and the live chat app**. Brands call SDKs at points on their site to pass info into live chat and **govern actions/workflows**.

## Embedding live chat on a website
**Help:** [Installing Sprinklr Live Chat on a Website](https://www.sprinklr.com/help/articles/website-installation/installing-on-web/63bc490bf7c92723b10e6eed)
- Add a **JavaScript embed code** to the site → live chat appears automatically. This is done by the **client's own web team** — Sprinklr/RaptorCX generates the snippet and hands it over, it isn't pushed live by us.
- **Get the embed code:** **Sprinklr Service → Listen → Brand Care → Live Chat Care** → locate the app → **three dots → Embed Code** → choose **Modern** skin (recommended over legacy Classic) → copy the generated JS snippet.
- **Code structure:** `window.sprChatSettings = { appId: "XXXXXXXXX", skin: "MODERN" };` — `appId` uniquely identifies the Live Chat application.
- **Placement:** near the **bottom of the site's HTML, before `</body>`**. Consider a small delay before the script executes so it doesn't block critical page resources.
- **Multi-page site** → embed on **every page** where chat should appear.
- **Alternative:** can also be embedded via an **iFrame** (environment + application ID in the source URL) to place the widget in a specific page section instead of a floating widget.
- **Internal testing:** use the test link, add your **application ID + environment**, **whitelist the URL**, then test.

## Website-integration use cases (via SDKs)
Tested in DevTools → Console (right-click → Inspect → Console) on the deployed UAT site:

### Open / close the widget
- `window.SPRChat('open')` opens the widget; a corresponding **close** SDK closes it.
- Use: open from a **nav-menu item / button / hyperlink**, or **auto-open on page load** (call on the page `onload`).

### Open a new conversation with a custom welcome message
- Default opens with the default welcome message; you can customise the opening message from **brand, user, or both**:
  - **Custom brand message** — e.g. a "Know more about this laptop" button opens chat with a brand message *"Hi there, it looks like you're interested in buying a laptop"* (`sentByUser: false`).
  - **Custom user message** — opens with a user message (`sentByUser: true`), e.g. *"Hi, I need help choosing the right laptop."*
  - **Both** — brand message (`sentByUser: false`) + user message (`sentByUser: true`).

### Capture / update context via custom fields
- **Capture customer context at start:** set a **case custom field** when opening from a button (e.g. `product category = laptop`); tag multiple fields and **govern the bot journey/workflows** off them. (Copy the custom field name from **Sprinklr → Custom Fields** into the SDK.)
- **Update during/after conversation:** update a conversation-context / case custom field mid- or post-chat — e.g. set **transaction amount/ID after a purchase** to **attribute sales** to the conversation/case for reporting.
- **Update profile custom fields** via SDK (for a user already logged in on the site).

### User pre-authentication
- Pass authenticated details **securely** to the chat to **authenticate the user inside chat** — so you **never re-ask** for customer details in the flow, and can use those details in workflows. (Detailed in [[user-authentication]] — 093.)

## Notes / gaps
- The embed script is per-application; **Modern skin** is the default.
- SDKs are the bridge for **page-context → case/profile custom fields → bot/workflow logic** — the main way websites personalise the live chat.
- Sales attribution (transaction amount/ID via SDK after purchase) is a high-value reporting pattern → ties to [[reporting-metrics]].
