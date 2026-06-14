# Live Chat Web Setup & SDKs (Live Chat 091)
**Source:** Product Foundation Courses → Live Chat / 091 Live chat web setup and SDKs (video transcript + on-screen demo) · **Help:** search `site:sprinklr.com/help live chat embed code SPRChat SDK custom field`
**On-screen scenario:** demo brand site `acmesprinklr.com` (Acme) with a "Chat with us" widget; SDKs tested live in the browser **DevTools → Console** on a UAT page.

## SDKs — what they are
**SDK** (Software Development Kit) = a set of tools/**code snippets** used to **communicate between the website and the live chat app**. Brands call SDKs at points on their site to pass info into live chat and **govern actions/workflows**.

## Embedding live chat on a website
- Add a **JavaScript embed code** to the site → live chat appears automatically.
- Multi-page site → embed on **all pages**, preferably **near the bottom** of the page code.
- **Internal testing:** use the test link, add your **application ID + environment**, **whitelist the URL**, then test.
- **Get the embed code:** Launchpad → **Live Chat Care** → the app → **three dots → Embed** → choose **Modern** (recommended) or Classic skin → copy the **script** to share with the client.

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
