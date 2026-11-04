# Live Chat — bold / rich-text formatting (assets, bots, agent replies)

**Short answer:** a **Simple Text Template** asset (the one with Basic Details → Asset Specific: Languages / Current Language / Content / Define Snippet) is **plain text only**. No bold, no italics, no markdown rendering — `**text**` will be delivered literally to the customer. To get bold you must switch asset type or enable markdown on the channel.

## Three ways to get formatting

| Path | What it gives | Notes |
|---|---|---|
| **Rich Text asset** (Digital Asset Management → Create Asset → **Omni Chat Templates**, Template Type = *Quick Reply*, Channel = *Sprinklr Live Chat*) | bold, italic, bold-italic, underline, strikethrough, hyperlinks, unordered lists, embedded images, tables with headers; multilingual + RTL; can pull API data for dynamic content | Advanced markdown customisation needs backend enablement — raise it with the Success Manager or tickets@sprinklr.com. ([rich text assets](https://www.sprinklr.com/help/articles/live-chat-assets/rich-text-assets/685bc64920753412ba525615)) |
| **Rich Text Messages** in Care Console | agent selects text in the reply box and uses the **Text Formatting Toolbar** (bottom of reply box): bold, italic, underline, strikethrough, hyperlink | Agent-typed messages only, not bot/asset messages. Feature-flagged — enable via Success Manager. ([rich text messages](https://www.sprinklr.com/help/articles/rich-text-messages/rich-text-messages-on-sprinklr-live-chat/65cb2faa0d89816c571a83a6)) |
| **Third-party / custom bot payload** | set `content['markdownText'] = true` on the outgoing message so the widget renders markdown | Only for bots pushing content via API, not for the native asset picker. |

## Practical guidance for bot flows
- Bot/AI-Agent nodes that reference a **Simple Text** asset cannot be made bold — replace the asset with an Omni Chat Template (Rich Text) and point the node at that.
- Formatting is a **channel renderer** capability. The same asset text on WhatsApp uses WhatsApp's own syntax (`*bold*`), on Live Chat it's markdown-with-enablement. Don't assume one asset renders identically across channels.
- Fallbacks when markdown isn't enabled and you need emphasis: line breaks, ALL CAPS for a single keyword, emoji, or a Quick Select / Rich Text Carousel template where the label styling is built in.
- Placeholders like `%%[CASE_NUMBER:]` keep working in Rich Text assets.

**Sources:** the two help articles linked above (fetched 2026-08-25).
