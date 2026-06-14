# Live Chat Mobile Implementation (Live Chat 092)
**Source:** Product Foundation Courses → Live Chat / 092 Live chat mobile implementation (video transcript + demo) · **Help:** search `site:sprinklr.com/help live chat mobile webview react native SDK push notification`

## Three deployment approaches (iOS + Android)
| Approach | How it works | Trade-offs |
|---|---|---|
| **Web View** | Live chat opens in an **embedded browser** inside the brand's app | Fastest to implement; **no app upgrade** needed for live-chat code changes; "decent" CX (runs in a browser) |
| **React Native SDK** | Integrated **natively**, part of the brand's app | Longer implementation; **app upgrade required** for any code change; seamless, faster CX |
| **Native SDK** | Integrated **natively**, part of the brand's app | Longest implementation (most technical nuance); app upgrade required for code changes; best CX/performance |
- Live chat **configuration** changes are the same across all three; **UI/UX customisations** work for all. Only **code** changes differ (native/RN need a parent-app upgrade).

## UAT on mobile
- **Web View:** use the testing URL, change parameters for your app, open in any **mobile browser**.
- **Native / React Native:** use the example **APK** ("Messenger Example", **Android-only** for testing, though integration supports both Android & iOS — link in the doc/drive folder). Why test here: some things render differently or aren't supported in native/RN, and to test **mobile-specific flows** (custom fields / rules by device type).
  - **Change environment configuration:** add your **app ID** + details → launch your app (watch for trailing spaces in the app ID).
  - **Locale** = user language: single-language → enter the primary locale (and set the same in the **builder**); multi-language → add primary/secondary/additional languages in the builder, then test locales. App translates by **browser locale**; if the locale isn't in the builder's additional languages, the **default language** shows.
  - Set **environment** (e.g. production) and **skin** (Classic/Modern).
  - **Entry-point/landing options to test:** open **new conversation** (fresh case) vs **last conversation**; **with home page** vs **without** (conversation screen only) — back-button behaviour differs. Plus **logout** (test anonymous), **change user details**, **change locale**, **get open conversations**, **update user** (auth).

## Use cases of mobile integration
- **Push notifications** — in-app/mobile notifications for brand replies. Supported; **enable via documentation + the live chat product/support team**. (Demo: Bath & Body Works — replies arrive as notifications when the user leaves the app, tap to return to the chat.)
- **User authentication** — authenticate the user (e.g. signed in on the website) so they can **continue a conversation across devices** (desktop → mobile) if authenticated. (Detailed in [[user-authentication]] — 093.)
- **Passing contextual information** — govern workflows / tag custom fields by **device type** (separate flows for mobile vs web).
- **Entry points & landing pages** — multiple entry points / landing screens and conversation scope (as in the UAT app).

## Notes / gaps
- Approach choice is a CX-vs-implementation-cost trade-off: **Web View** for speed/low-maintenance, **Native/RN** for the best in-app experience.
- Push notifications require a **support/product-team enablement** step — not self-serve.
- Cross-device continuity depends on [[user-authentication]] (093).
