# WhatsApp Account Addition (Messaging 053)
**Source:** Product Foundation Courses → Messaging / 053 WhatsApp Account Addition (video transcript + "Sprinklr Account Addition Flow" slide screenshot) · **Help:** search `site:sprinklr.com/help add WhatsApp Business account embedded signup WABA`

## What it is
Adding a **WhatsApp Business** account to Sprinklr lets brands do proactive + reactive messaging, streamline agent workflows, and use conversational AI/chatbots on WhatsApp.

## Terminology & hierarchy (top → bottom)
- **Facebook Business Manager** — brand's hub to manage all Meta social/messaging channels.
- **WABA (WhatsApp Business Account)** — sits under the Business Manager; a **collection of phone numbers** (WhatsApp Business profiles).
- **WhatsApp Business Profile** — the actual **phone number** you add to the WABA. This is what gets added in Sprinklr.

## Prerequisites
- **Admin-level access** to the Facebook Business Manager — be logged in with that admin profile while adding the account on both Sprinklr and Business Manager.
- The number to add **must NOT be active** on the WhatsApp Business app or with another vendor (WhatsApp policy — an active number elsewhere can't be added).
- The number **must be able to receive an OTP via call or SMS** (needed for verification).

## High-level flow (3 steps)
1. **Create** a Facebook Business Manager + WhatsApp Business account (or use existing ones).
2. **Create the WhatsApp Business profile** (add the phone number).
3. **Connect and verify** the WhatsApp Business number.

## Configuration steps (Sprinklr demo)
1. Open a new page → **Messaging Accounts** under **Listen**.
2. On the accounts screen → **Add Account**.
3. Select **WhatsApp Business** → on the **Add WhatsApp Business Account** window, ensure the **Embedded Sign-up flow** toggle is **ON** → **Add Account**.
4. Redirects to **Login with Facebook** — sign in with the profile that has **admin access** to Business Manager → Get Started.
5. **Share permissions** with Sprinklr for WhatsApp Business account access → Continue.
6. **Choose a Meta business account** (the Facebook Business Manager) → Next.
7. **Create or choose** a WhatsApp Business account, then create a **new WhatsApp Business profile** (add a new number).
8. Set the **WhatsApp Business profile display name** (shown to end users), choose a **business category**, optionally add a **business description** and **website**.
9. Enter the **number** + choose the **OTP method** → Next.
10. Enter the **verification code** received → redirected back to Sprinklr; the WhatsApp account is added.

## Notes / gaps
- This is account onboarding; sending templated messages on WhatsApp requires HSM templates — see [[whatsapp-templates]] and [[channels-supported]] (Journey Facilitator).
- Part of Messaging: [[channels-overview]], [[facebook-account-addition]], [[apple-messages-account-addition]], [[google-business-messaging-account-addition]].
