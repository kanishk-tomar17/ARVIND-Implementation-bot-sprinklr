# Audience Profile Import (Journey Facilitator 139)
**Source:** Product Foundation Courses → Journey Facilitator / 139 Audience Profile import (video transcript + demo; Excel template screenshot) · **Help:** search `site:sprinklr.com/help import audience profiles excel template`

## What it is
Any customer profile in Sprinklr is modelled as an **Audience Profile** — it holds the info brands use to understand and personalise interactions. Once added, profiles can be used to:
- Create **segments** (see [[segment-manager]]).
- Take actions like sending **proactive messages** via Journey Facilitator (see [[journey-builder-basics]]).
- Analyse the **conversation history** the profile has had with the brand over time.

This video covers importing profiles for the three major channels: **Email, SMS, WhatsApp**.

## Configuration steps (demo)
1. **Download the Excel template.**
   - Open Sprinklr → **Marketing** section → under **Sprinklr Marketing**, click **Audience Profiles** (within Publish).
   - In the Audience Profiles window, click the **Options** icon (top-right) → **Import**.
   - In the **Import Audience Profiles** window → **Download Excel Template**.
2. **Fill the template.** The first 4 columns (A, B, C, D) are **mandatory** for every import:
   - **Email profile:** Social Network = `Email` · User ID = email address · User Screen Name = display name · Full Name.
   - **SMS profile:** Social Network = `SMS` · User ID = phone number **with country code** · User Screen Name = display name · Full Name.
   - **WhatsApp profile:** Social Network = `WhatsApp Business` · User ID = phone number **with country code** · User Screen Name = display name · Full Name.
   - **Profile-level custom fields** created in the platform also appear as columns — fill them to use later for decisioning/personalisation (see [[custom-fields]]).
   - Save the file.
3. **Import.** Import Audience Profiles window → **Upload** → select the saved Excel → **Save** (bottom-right) to start the import.
4. **Check the result.** A platform notification shows records **created / updated / failed**.
   - On **failure**, the platform returns an Excel file stating the exact reason per row (e.g. missing Number, User ID, or User Screen Name).
5. **Search profiles.** Use search + filters on the Audience import page; you can inspect every property on the profile, including the custom fields you uploaded.

## Notes / gaps
- Imported profiles feed [[segment-manager]] and [[journey-builder-basics]]; custom-field columns tie to [[custom-fields]].
- Part of Journey Facilitator: [[segment-manager]], [[campaigns]], [[journey-builder-basics]], [[journey-nodes]], [[channels-supported]], [[journey-reporting]].
