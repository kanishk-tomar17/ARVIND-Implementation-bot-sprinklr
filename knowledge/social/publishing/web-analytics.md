# Web Analytics (Publishing) (Sprinklr Social — Publishing)
**Source:** sprinklr.com/help — Publishing sub-area (multiple articles; see links below)

## What it is
- Tracks how published content drives traffic and conversions by appending tracking parameters (UTMs) to the links in your posts.
- Built around two pieces: **Web Analytics Profiles** (reusable parameter templates) and the **UTM Manager** (a UI to build, store, and reuse tagged URLs).
- Profiles can map to a tracking platform (Custom, Google Analytics, Site Catalyst, Core Metrics, Geo Riot) and apply across Paid, Publishing, and FPX modules.
- Used by consultants to standardise campaign tagging so downstream reporting and attribution stay consistent.
- Related: [[utm-manager]], [[editorial-calendar]], [[ai-in-publishing]], [[asset-manager]].

## Key features & how to use

### Web Analytics Profile (create & apply)
- **Prerequisites:**
  - Posts must contain links — tracking only works when a post has a URL.
  - Does **not** work on auto-imported posts (exception: bit.ly shortened links).
  - Requires normal URLs; shortened links won't work if the profile is applied afterward.
  - Special characters in parameters are automatically encoded.
- **Create a profile:**
  1. New Tab icon → **Governance Console** → **All Settings** (within Platform Setup).
  2. Select **Web Analytics** from Platform Settings.
  3. Click **Add Analytics Profile** (top-right corner).
  4. Fill the **Create Analytics Profile** window.
  5. Click **Save**.
- **Fields in the Create Analytics Profile window:**
  - **Name** — unique profile identifier.
  - **Module Type** — Paid, Publishing, or FPX.
  - **Analytics Profile Type** — Custom, Google Analytics, Site Catalyst, Core Metrics, or Geo Riot.
  - **Domain** — client domain (supports `*` wildcards).
  - **Parameter** — the URL parameter name.
  - **Variable(s)** — the values to track.
- **Profile settings:**
  - **Prepend Query Parameters** (checkbox) — attaches parameters to the beginning of the URL.
  - **Remove extra separators** — eliminates gaps left by empty variables.
  - Custom separators for UTM parameters are configurable (requires Success Manager setup).
- **Configure domains (map a profile to a domain):**
  1. Go to Web Analytics settings (steps 1–2 above).
  2. Click **Edit Domain Analytics for client**.
  3. Enter domain info and select the Analytics Profile.
  4. Save.
- **Apply to ad accounts:**
  1. New Tab → **Governance Console** → **Accounts** (in Platform Setup).
  2. Hover the Options icon next to the account.
  3. Select **Web Analytics**.
  4. Enter Domain details and select the Analytics Profile.
  5. Click **Save**.

### UTM Manager (build & reuse tagged URLs)
- **Prerequisites:**
  - **Dynamic Property (DP) enablement** — the feature must be enabled by the Product Support team based on user requirements.
  - **"Configure UTM Entity" permission** — needed to add/remove and update parameters.
- **Configure the UTM form:**
  1. Select the **UTM Medium** (e.g., Email, SMS).
  2. Add required parameters using the **+** icon.
  3. Reorder parameters using the 6-dot drag handle.
  4. Enable/disable parameters via the toggle switches.
- **Create a new UTM:**
  1. Click the **Add UTM** icon in the UTM Manager.
  2. Enter the **UTM Name**.
  3. Input the **page URL**.
  4. Add standard and custom parameter details.
  5. Add additional properties (optional).
  6. Click **Save**.
- **URL preview** auto-generates as parameters are filled; it can be copied and shared.
- **Actions on existing UTMs:** Edit (name, URL, parameter values), Clone (exact copy), Delete.
- **Governance:** filters available to fetch relevant UTMs; access is permission-based.

## Common issues & fixes
- **Tracking not applied to a post** — confirm the post actually contains a link; profiles only tag posts with URLs.
- **Auto-imported posts not tracked** — expected behaviour; only bit.ly shortened links are the exception.
- **Shortened link not picking up parameters** — use a normal (un-shortened) URL; applying a profile to an already-shortened link won't work.
- **Empty UTM values leaving gaps in the URL** — enable **Remove extra separators** on the profile.
- **Cannot add/edit UTM parameters** — confirm the user has the **Configure UTM Entity** permission and that DP enablement has been done by Product Support.

## Notes & gaps
- Custom UTM separators require Success Manager involvement — not self-serve.
- UTM Manager requires Product Support to enable the underlying Dynamic Property before use.
- No specific error messages, usage limits, or quotas are documented for the UTM Manager.
- The help articles do not detail the exact filter options available in the UTM Manager.
- The articles do not specify how applied parameters surface in reporting/dashboards (see [[web-analytics]] reporting topics if available).
- Permissions referenced: **Configure UTM Entity**. Governance Console access is needed to create/manage profiles.

## Sources
- Create a Web Analytics Profile — https://www.sprinklr.com/help/articles/web-analytics/create-a-web-analytics-profile/64569bffe66f2e36b45154c4
- UTM Manager — https://www.sprinklr.com/help/articles/web-analytics/utm-manager/6656cf53b35fa9007da6df95
