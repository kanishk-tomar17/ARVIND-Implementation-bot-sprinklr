# Apple Messages for Business Supported Templates (Messaging 059)
**Source:** Product Foundation Courses → Messaging / 059 Apple Messages for Business Supported Templates (video transcript + "List Picker Templates" slide screenshot) · **Help:** search `site:sprinklr.com/help Apple Messages for Business templates list picker time picker forms quick reply`

## What they are
Apple Messages for Business provides multiple **interactive templates** for a rich in-conversation experience: **List Picker, Time Picker, Authentication, Apple Pay, Forms, Quick Reply**. Apple specifies guidelines for using these templates/user flows.

## Common build path
Sprinklr Social → **Digital Asset Management** → **Assets** → **Create Asset** → **Omnichannel Templates** → Create Asset window → basic details (name) + **Channel = Apple Messages for Business** + choose **Template Type**. (Same path for every template below.)

## 1. Forms template
Collects customer info via a forms interface inside the Apple Messaging UI — high interactivity without leaving the conversation. A form can contain **multiple pages**.
- **Asset-specific:** upload an **image**, give a **title/subtitle**, select image **style**.
- Configure the **button** (button title) and the **message** (title/subtitle).
- **Questions** — add multiple; each has a title, subtitle, and **response type** (four kinds):
  - **Date Picker** — default date, allowed date range, date format, placeholder.
  - **Input** — text response; hint text, max input length, input type.
  - **Picker** — multiple pick-list values to choose from.
  - **Select** — multiple values to choose from; can also **upload an icon**.
- Configure the **reply message** (shown after the customer responds) → asset details → **Save**. Ready to send from any publishing avenue.

## 2. Quick Reply template
Predefined response options; customer makes a choice with a single tap.
- **2–5 customizable choices**; user selects **only one**.
- **Limitations:** up to **5** quick replies per message; supported on **iOS 15+**.
- **Recommended use (per Apple):** yes/no questions, predefined metrics (e.g. ratings), or when options don't need visual cues (images). *If visuals are needed, use a List Picker.*
- **Build:** body → configure a **postback message** → create buttons (max 5), each with a **label**; action defaults to **text** (Quick Reply only accepts text responses) → Save.

## 3. List Picker template
Lets the customer choose from a **list of items** shown with details (name, description, image) in the Messages app; customer can choose **one or more** items to send as a reply.
- **Capabilities:**
  - **Item Information** — name, description, image per item.
  - **Item Sections** — divide the list into sections by category.
  - **Multi-Selection** — allow customers to choose multiple items across sections.
  - **Reply Bubble** — define content for the bubbles shown when messages are received/replied to.
- **Best practice:** include thumbnail images and icons for each item.

## Other templates
**Time Picker, Authentication, Apple Pay** are also supported interactive types (introduced in this module; configure via the same Omnichannel Template Builder).

## Notes / gaps
- Requires an Apple Messages account added + Apple-approved via [[apple-messages-account-addition]]. Built in the same Omnichannel Template Builder as [[whatsapp-templates]]/[[facebook-templates]].
- Part of Messaging: [[channels-overview]], [[whatsapp-templates]], [[facebook-templates]], [[google-business-messaging-templates]].
