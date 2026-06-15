# Email Account Types & Addition Process (Email Care 132)
**Source:** Product Foundation Courses → Email Care / 132 Account types and addition process (3-part video transcript + demo) · **Help:** search `site:sprinklr.com/help add email account exchange gmail SES`

## The 3 email account types
1. **Microsoft Exchange** (3 sub-types: Exchange Online, On-Premise, …)
2. **Gmail** (hosted by Google)
3. **Sprinklr domain / Amazon SES** account

All added via **All Settings → Accounts → Add Account → Email**.

## 1. Microsoft Exchange
### Exchange Online (cloud, Office 365)
Hosted by Microsoft (login at `login.microsoftonline.com`).
- Add Account → search **Microsoft** → **Microsoft Exchange account** → enter **Display name, Email ID** → click **Use OAuth** → redirected to Microsoft login → log in with the brand account → account auto-added.
- **CRITICAL precaution:** OAuth often silently uses the account **already logged into the browser** (e.g. your personal account) instead of prompting. **Always add Exchange Online accounts in an Incognito tab** with no other email accounts logged in, to avoid adding your personal account to the client environment.

### On-Premise (on-prem Exchange Server)
Hosted on the **brand's own servers/data center**; each has a **specific login URL** (not `login.microsoftonline.com`).
- Add Account → Microsoft Exchange → Display name, Email → **do NOT use OAuth**. Instead enter **User ID (email), password**, and the brand's **account URL** (the URL they use to log into their on-prem account natively, reformatted as required). Ask the brand for that URL.

## 2. Gmail
- Add Account → search **Email** (not "Gmail") → **Email** → set **Account type = Gmail** → IMAP/SMTP host URL & ports **auto-fill** (leave as-is).
- Enter **Display name, Email ID**, and for password use a **Google App Password** (not the account password):
  - Google Account → **Security** → turn on **2-Step Verification** → **App passwords** → create one (custom name e.g. "Sprinklr") → **Generate** → copy the **16-digit app password** → paste in Sprinklr.
- App passwords require 2-step verification (more secure). **Save** → account added.

## 3. Sprinklr domain / Amazon SES account
Amazon **SES** = AWS cloud email-sending service. Use when the brand wants an email ID to send/receive but **doesn't want to add their own mailbox**.
- These can **only be a sub-domain of `sprinklersupport.com`** (e.g. `help@acme.sprinklersupport.com`); must have something before `@…sprinklersupport.com`.
- **Steps:**
  1. **Raise a support ticket** to enable the required **DPs (dynamic properties)** first — without them the **"Sprinklr" account type won't appear** in the Add Account dropdown.
  2. **Raise/clone the JIRA** (sample JIRA in the doc — clone it, don't edit the sample): "Add domain `<sub>.sprinklersupport.com` in `<env>` SES and verify" + "add following emails in the existing rule set" (the email IDs to add). Verifying the domain alone isn't enough — **IT OPS must add the email IDs to the rule set**.
  3. **Approval:** the JIRA needs approval from **Vishwa Prashanth Modi (AVP Engineering)** — mandatory for any SES account.
  4. After approval, post in **Ask IT OPS** group, tag the **NOC Task team** to action the JIRA.
  5. Once NOC confirms it's added to the rule set, go to **Accounts → Add Account → Email → Account type = Sprinklr** (visible only after the DP is enabled) to finish.

## Notes / gaps
- This 132 topic spans 3 videos (Exchange, Gmail, SES) — combined here. Account permissions/handling tie to Governance [[accounts-account-groups]].
- Part of Email Care: [[webforms-external-gw]], [[email-signature]], [[email-collaboration]], [[manual-case-merge]], [[ignore-duplicate-autoresponse]], [[email-templates]].
