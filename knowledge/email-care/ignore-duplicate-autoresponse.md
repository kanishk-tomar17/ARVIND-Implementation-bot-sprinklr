# Ignore Duplicate & Auto-Response Emails (Email Care 137)
**Source:** Product Foundation Courses → Email Care / 137 Ignore duplicate & auto response emails (video transcript + demo) · **Help:** search `site:sprinklr.com/help duplicate message auto submitted email rule`

## What it is
Two **inbound rules** to stop unwanted cases from being created:
1. **Prevent multiple cases from duplicate emails**
2. **Avoid auto-response (out-of-office) emails creating new cases**

## 1. Prevent duplicate-email cases
If a customer mistakenly sends a **duplicate email**, Sprinklr's email integration may grab each instance and create **separate cases** → inefficiency/confusion.
- **Inbound rule** condition: in message properties, select **"Check for duplicate message"** and a window (e.g. **2 hours**) → detects duplicates within that window.
- **Yes path action:** e.g. **Ignore Message** (or whatever action you want) applied to the duplicate emails.

## 2. Avoid auto-response / out-of-office emails
Out-of-office emails are automated replies (vacation, etc.). To prevent them generating **new cases**, link them to the same case (or ignore).
- **Inbound rule** condition: in message properties, select **"Is auto submitted email = Yes"** → matches all out-of-office / auto-response emails.
- Apply an **action accordingly** (e.g. associate to same case / ignore) on those emails.

## Notes / gaps
- Both are inbound rules using message properties (**Check for duplicate message**, **Is auto submitted email**) — see [[inbound-rules]].
- Part of Email Care: [[account-types]], [[webforms-external-gw]], [[email-signature]], [[email-collaboration]], [[manual-case-merge]], [[email-templates]].
