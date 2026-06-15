# Segment Manager (Journey Facilitator 140)
**Source:** Product Foundation Courses → Journey Facilitator / 140 Segment Manager (video transcript + demo; Create New Segment screen screenshot) · **Help:** search `site:sprinklr.com/help audience segment manager create segment`

## What it is
An **audience segment** is a group of individuals who share common characteristics or meet specific conditions (age, gender, purchase history, etc.). Once a brand's data source is connected to Sprinklr, millions of user data points are imported and **periodically refreshed**; the **Segment Manager** is the tool to manage that data.

## Why it matters
Instead of targeting the entire database, segmenting narrows focus to **specific groups more likely to respond** — essential for effective journey campaigns (see [[campaigns]], [[journey-builder-basics]]).

## Configuration steps (demo)
1. **Open Segment Manager.** Sprinklr search bar → type **Segment Manager** → open the window.
2. From here you can **create new segments** or **manage saved segments**.
3. **Create Segment** (top-right button) → opens the **Create New Segment** page.
4. **Select attributes** that define the target audience — chosen from a dropdown:
   - Profile lists, custom fields, profile creation date, etc.
   - *Example:* users with birthdays on 22 June who are in the partner profile list "22 June".
   - **Target** section: set the **operator between filter groups** — **OR** (any condition met) or **AND** (all conditions met); add filter rows (Select Attribute → operator → value), **Add New Filter Group**, and optionally **Exclude from above filters**.
5. **Basic Details:** enter **Segment Name** and **Segment Expiry Date** (defines the segment's lifespan so it stays current). Optionally mark **Is Dynamic Segment**.
6. **Calculate Reach** (Segment Summary panel) shows the total user count for the target.
7. **Save** (bottom-right) → segment is added to the **Segment Manager board**.

## Segment Manager board
Shows each segment's **name, status, source, type, reach** and other properties. A **% completion bar** indicates how many users have been processed; once it hits **100%**, the final segment size shows in the **Size/Reach** column (e.g. 3,500 members).

## Notes / gaps
- Segments are built from profiles imported via [[audience-profile-import]] and feed [[campaigns]] / [[journey-builder-basics]]; attributes include [[custom-fields]].
- Part of Journey Facilitator: [[audience-profile-import]], [[campaigns]], [[journey-builder-basics]], [[journey-nodes]], [[channels-supported]], [[journey-reporting]].
