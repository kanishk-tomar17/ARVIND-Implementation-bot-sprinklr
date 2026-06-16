# YouTube — Setup & Account Management (Sprinklr Social — YouTube)
**Source:** sprinklr.com/help — YouTube channel (multiple articles; see links below)

## What it is
- The end-to-end flow for connecting, configuring, and managing YouTube channels inside Sprinklr Social so you can publish, engage, moderate, and report on YouTube from one place.
- Accounts are added via Google OAuth (Sprinklr authorizes against a Google account that has at least one YouTube channel).
- Covers add/edit, granular Google consent, multi-account bulk actions, web analytics tagging, playlist-level publishing permissions, and deactivation.
- Account-level admin task: only admins can add accounts, and several actions (playlist permissions, deactivate) are restricted.

## Key features & how to use

### Add / Edit a YouTube account
- **Where:** Sprinklr Social tab → **Owned Social Accounts** (under Listen) → **Add Account** (top right).
- **Add flow:**
  1. In the **Add Account** picker ("Choose a channel you would like to add an account for"), search/scroll and select **YouTube** (red play-button tile).
  2. An **"Authorize Sprinklr on YouTube"** dialog appears — "Sprinklr needs permission to access your Google Account in order to manage your YouTube Channel." Ensure the correct Google account is logged in, then click **Go To YouTube**.
  3. In Google's **Sign in with Google** window, choose the Google account.
  4. Grant permissions (see granular consent below) — click **Allow** / **Continue**.
  5. Configure the account: **Account Details**, **Permissions**, **Workspace** sharing, **Subscribers**, **Timezone**, **Properties**.
  6. Click **Save**.
- **Account Details fields (Edit/Update dialog):** Account Name (required), **UserId** (read-only, system-assigned), **Owner** (required), **Custom Character Count**, **Default URL Shortener**, and **Groups to include Account in** → **Select Groups**.
- **Edit flow:** Owned Social Accounts → filter **All Channels** → YouTube → hover the row's **Options** (three-dot) icon → **Edit** → change fields → **Save**.
- **Prereqs:** admin role; stay logged into the associated Google account during setup; the Google account must have ≥1 linked YouTube channel; an account lives in a single Workspace initially.

### Granular permissions consent screen (Google OAuth)
- Google now shows a **granular** consent screen — users tick which permissions to approve individually (with **Select all** and a per-item checkbox), then click **Continue** (vs. the old all-or-nothing **Allow**).
- **All seven YouTube permissions are mandatory** for full Sprinklr functionality; leaving any unchecked breaks the matching feature:
  1. **See, edit, and permanently delete your YouTube videos, ratings, comments and captions** — publishing, moderation, message retrieval.
  2. **Manage your YouTube videos** — account addition, publishing, message collection.
  3. **View your YouTube account** — fetch paid analytics (CPM, impressions, revenue).
  4. **View and manage your assets and associated content on YouTube** — monetization & rights management.
  5. **View YouTube Analytics reports for your YouTube content** — reporting metrics (views, likes, followers).
  6. **Manage your YouTube account** — publishing & moderation.
  7. **View Content owner account details from YouTube** — monetization features.
- The consent app is branded e.g. "Sprinklr- GPlus Pages wants to access your Google Account."

### Manage multiple YouTube accounts at a time
- **Where:** Owned Social Accounts → click **All Channels** (top-left of the Accounts bar) → filter to **YouTube**.
- Tick the checkboxes for one or more YouTube accounts.
- In the top **Dashboard Bar**, choose a bulk action: **Deactivate** (remove accounts) or **Apply Macro** (run several actions across the selected accounts at once).

### Apply Web Analytics to a YouTube account
- **What it does:** appends tracking strings to web URLs in your campaigns so you can track user behaviour after a social click.
- **Steps:** Owned Social Accounts → **All Channels** → YouTube → hover the row's **Options** icon → **Web Analytics**.
- In the **Configure Web Analytics for YouTube-<Account>** popup: enter a **Domain**, select an **Analytics Profile** from the dropdown (or **Add New Analytics Profile** to configure additional profiles) → **Save**.

### Set permissions for YouTube playlists
- **What it does:** restrict which users/user groups can publish to which playlists on an account.
- **Steps:** Owned Social Accounts → **All Channels** → YouTube → hover **Options** → **Playlist Permissions**.
- The **"<Account> playlists"** dialog opens with a **Search playlists** box and rows you scope **Provisioned Users** against:
  - **All Playlists** — selected users get access across all playlists.
  - **No Playlist** — selected users get access to videos that don't belong to any playlist.
  - **A specific playlist** (e.g. "Robot Music Videos") — selected users get access to just that playlist.
- For each row, pick **Users** or **User Groups** in the **Provisioned Users** field → **Save** (bottom-right). Authorized users can then publish to their permitted playlists.

### Deactivate a YouTube account
- **Steps:** Owned Social Accounts → **All Channels** → YouTube → hover **Options** → **Deactivate**.
- Deactivation is **immediate**. Re-adding the account later requires re-activation **and** re-authentication (full OAuth again).
- Can also be done in bulk (see multi-account section).

### Why YouTube / What you can do (context)
- **Why it matters:** brand awareness, expanded reach, two-way customer engagement (comments, live, community), and monetization.
- **In Sprinklr you can:** pull native comments/replies into [[engagement-dashboards]] and reply with canned responses/quick macros; configure auto-response rules across accounts ([[rule-engine]]); moderate comments with approval workflows; publish video with thumbnail editing, private-video settings, monetization and global content-ownership claims ([[publishing]]); and track performance, demographics and engagement via [[reporting]].

## Common issues & fixes
- **Feature silently not working after adding the account (e.g. analytics blank, can't moderate/publish):** likely a permission was unchecked on the granular consent screen. Remove and re-add the account, and tick **all seven** YouTube permissions (or use **Select all**).
- **Account add fails / wrong channel connects:** make sure the correct Google account is logged into the browser before clicking **Go To YouTube**, and that the Google account has at least one linked YouTube channel.
- **Re-adding a deactivated account doesn't restore it instantly:** deactivation requires full re-authentication — you must run OAuth again, not just toggle status.

## Notes & gaps
- Only **admins** can add YouTube accounts.
- An account initially belongs to a **single Workspace**; cross-workspace sharing is set during configuration (Workspace step).
- **UserId** is system-assigned and not editable.
- The "Owner" field defaults to the connecting user but can be reassigned in the Edit dialog.
- Article text does not enumerate every option under **Subscribers**, **Timezone**, or **Properties** in the add flow, nor the full **Permissions** sub-section fields — confirm in-product.
- Web Analytics article doesn't list which analytics providers/profile types are supported beyond the generic **Analytics Profile** dropdown.
- See also: [[asset-manager]] for managing video assets and rights/monetization claims.

## Sources
- Add/Edit a YouTube account — https://www.sprinklr.com/help/articles/getting-started/addedit-a-youtube-account/64113b422680c35a78bb35c1
- Support for granular permissions consent screen during Google account authorization — https://www.sprinklr.com/help/articles/getting-started/support-for-granular-permissions-consent-screen-during-google-account-authorization/668e3841679a1c4c5c8014c9
- Why is YouTube important — https://www.sprinklr.com/help/articles/getting-started/why-is-youtube-important/63ff3dd832d12b63c5f55cfe
- What can I do with YouTube — https://www.sprinklr.com/help/articles/getting-started/what-can-i-do-with-youtube/63ff40327a695d65a1605913
- Manage multiple YouTube accounts at a time — https://www.sprinklr.com/help/articles/getting-started/manage-multiple-youtube-accounts-at-a-time/63ff2fe732d12b63c5f55cde
- Apply web analytics to YouTube account — https://www.sprinklr.com/help/articles/getting-started/apply-web-analytics-to-youtube-account/63feff847a695d65a16058a9
- Deactivate a YouTube account — https://www.sprinklr.com/help/articles/getting-started/deactivate-a-youtube-account/63ff017232d12b63c5f55c67
- Set permissions for YouTube playlists — https://www.sprinklr.com/help/articles/getting-started/set-permissions-for-youtube-playlists/63ff00627a695d65a16058aa
