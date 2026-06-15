# Live Chat User Authentication (Live Chat 093)
**Source:** Product Foundation Courses → Live Chat / 093 Live chat user authentication (video transcript + demo) · **Help:** search `site:sprinklr.com/help live chat user authentication pre-auth user hash` + Live Chat Handbook "Advanced Use Cases #10"

## What it is
If a user is **logged in on the website** hosting live chat, you can **securely pass their auth details from the website into the chat** so they're **not re-authenticated in chat** — support doesn't have to ask for personal details again.
- *Example (Yodel):* an **anonymous** user sees a blank customer-details form; a **logged-in** user has the form **pre-filled** with passed details.

## Use cases & benefits
- **No re-asking** for user details → better CX.
- **Personalise** with the passed details in the workflow — e.g. welcome message with a **name placeholder**; send an **email transcript** without asking for the email again.
- **Continue conversations across devices** — e.g. (Lenskart) logged in on web mid-conversation → log in on mobile with the same credentials → continue the same conversation (history carries over).

## SDK / pre-authentication — 6 details passed (website → live chat)
1. **ID** — **mandatory**; any unique value for the customer (use the email ID if unsure).
2. **First name** — optional (empty string allowed).
3. **Last name** — optional. *(At least one of first/last name is required.)*
4. **Profile image URL** — optional.
5. **Phone number** — optional.
6. **Email ID** — optional.

### User hash (important)
- A **user hash** must be generated using the **API key** (found in the live chat app's **Dev Tools**) — demo used a **Python** snippet.
- The hash **must use the exact same user details** passed in the SDK.

### Passing the details (two ways)
- Website **auto-refreshes** after login → the brand calls the **script**.
- Website does **not** auto-refresh → the brand calls the **SDK** (run in console).
- Flow: generate the user hash → add it to the SDK → pass it → initiate the conversation.

## Agent & customer experience
- **Agent:** an unauthenticated user shows as an **anonymous profile**; once details are passed (e.g. *John Doe*), the **profile name** appears.
- **Customer:** cross-device — log in on web, start a chat; log in on mobile with the same number → **historical + latest conversations** are present → continue seamlessly.

## Notes / gaps
- This is the "user pre-authentication" referenced in [[web-setup-sdks]] (091) and the cross-device continuity in [[mobile]] (092).
- The **user hash + API key** step is the security backbone — details and hash must match exactly or auth fails.
- Deeper scenarios: Live Chat Handbook **Advanced Use Cases #10**.
