#!/usr/bin/env python3
"""
build_map.py — Regenerate knowledge/sprinklr-map.json (GROOT's help-center "GPS").

WHAT IT DOES
  Enumerates EVERY article on sprinklr.com/help via the Community GraphQL API
  (NOT by scraping HTML — the help center is a client-rendered SPA, so
  requests+BeautifulSoup returns an empty shell). For each of the 6 product-area
  roots it walks the category tree, pulls the articles in every category (with
  pagination), derives search keywords, cross-links any article we've already
  distilled locally, and writes one JSON object per line to sprinklr-map.json.

WHY GraphQL, not BS4
  `category(id){categories}` + `conversations(categoryIds:[id])` return title +
  path + category as clean JSON in a handful of calls. No per-page fetch, works
  on the SPA, ~3k articles in minutes.

USAGE
  1. Fill in the CONFIG block below with a FRESH token/cookie (they rotate per
     browser session — see the comment for exactly where to copy them from).
  2. python build_map.py
  3. Output: ../sprinklr-map.json  (one JSON object per line)

Requires: Python 3.8+, `requests`  (pip install requests)
"""

import json
import re
import time
import sys
from pathlib import Path

import requests

# ============================================================================
# CONFIG  —  EDIT THIS BLOCK ONLY. Paste fresh values, don't touch the logic.
# ----------------------------------------------------------------------------
# Where to get these (they rotate every browser session):
#   1. Open https://www.sprinklr.com/help/ in Chrome (logged in / any page).
#   2. DevTools (F12) -> Network tab -> filter "community".
#   3. Click any  POST  www.sprinklr.com/help/schema/community  request.
#   4. Request Headers -> copy the value of  x-csrf-token       -> CSRF_TOKEN below.
#      Request Headers -> Cookies -> copy  communityToken=...   -> COMMUNITY_TOKEN.
#      Request Headers -> Cookies -> copy  connect.sid=...       -> CONNECT_SID.
#   (communityToken and x-csrf-token are the SAME value. connect.sid is the session.)
CSRF_TOKEN       = "2325ed7d-7385-489a-917d-c2a03480bdef"
COMMUNITY_TOKEN  = "2325ed7d-7385-489a-917d-c2a03480bdef"   # cookie: communityToken (== CSRF_TOKEN)
CONNECT_SID      = "PASTE_connect.sid_VALUE_HERE"           # cookie: connect.sid (URL-encoded, starts s%3A...)

COMMUNITY_ID     = "4e8e4610-73cc-4dcd-8768-50db50021004"   # stable; rarely changes
ENDPOINT         = "https://www.sprinklr.com/help/schema/community"
OUTPUT_PATH      = Path(__file__).resolve().parent.parent / "sprinklr-map.json"
KNOWLEDGE_DIR    = Path(__file__).resolve().parent.parent   # knowledge/  (for local_kb cross-link)

# The 6 product-area roots (categoryId -> display name).
AREA_ROOTS = {
    "63a06e77ade47b6ab9419d92": "Sprinklr Service",
    "6321cb9db940857ea124f7fd": "Sprinklr Insights",
    "6321cbd6b940857ea1251413": "Sprinklr Social",
    "6321cbcab940857ea1250e42": "Sprinklr Marketing",
    "6941408e45e9db0a32ceec04": "Sprinklr AI",
    "6458c37d72241235fc75aa78": "Platform",
}
# ============================================================================

ALL_ROOT_IDS = set(AREA_ROOTS.keys())
STOPWORDS = {"the", "and", "for", "with", "your", "how", "from", "this", "that",
             "are", "can", "use", "using", "via", "sprinklr", "help"}

SESSION = requests.Session()
SESSION.headers.update({
    "content-type": "application/json",
    "x-community-id": COMMUNITY_ID,
    "x-baselanguage": "en_US",
    "x-language": "en_US",
    "x-csrf-token": CSRF_TOKEN,
    "user-agent": "Mozilla/5.0 (build_map.py)",
    "origin": "https://www.sprinklr.com",
    "referer": "https://www.sprinklr.com/help/",
})
SESSION.cookies.set("communityToken", COMMUNITY_TOKEN, domain="www.sprinklr.com")
if CONNECT_SID and "PASTE" not in CONNECT_SID:
    SESSION.cookies.set("connect.sid", CONNECT_SID, domain="www.sprinklr.com")


def gql(query, retries=3):
    """POST a GraphQL query; return the parsed `data` dict or None on failure."""
    for attempt in range(retries):
        try:
            r = SESSION.post(ENDPOINT, data=json.dumps({"query": query}), timeout=30)
            if r.status_code != 200 or not r.text.strip():
                time.sleep(1.0)
                continue
            j = r.json()
            if j.get("errors"):
                time.sleep(1.0)
                continue
            return j.get("data")
        except Exception:
            time.sleep(1.0)
    return None


def q_category(cid):
    return ('{ community { category(id:"%s"){ id:categoryId title '
            'categories{ id:categoryId title } } } }') % cid


def q_conversations(cid, page):
    return (
        '{ community { conversations(conversationType:"POST" includeCustomPages:"false" '
        'includeComments:"false" includeHierarchyDetails:"false" appendLastReplyByUser:"false" '
        'first:100 types:[] excludeTypes:[{type:POLLS}{type:CONTEST}{type:CONTEST_ENTRY}'
        '{type:EVENT}{type:SURVEY}] topicIds:[] folderIds:[] sortKey:{type:ORDER} sortOrder:"ASC" '
        'dateFrom:0 page:%d isScopedEntity:true currentCategoryId:"%s" categoryIds:["%s"] '
        'applyUserSort:"false" tags:{} customFields:{} filterByCurrentCategory:true '
        'highlightKeywordEnabled:false){ totalCount edges{ node{ path title type } } } } }'
    ) % (page, cid, cid)


def walk_categories(root_id, root_name):
    """BFS the category tree from a root; yield (category_id, path_string)."""
    out = []
    seen = {root_id}
    queue = [(root_id, root_name)]
    while queue:
        cid, path = queue.pop(0)
        out.append((cid, path))
        data = gql(q_category(cid))
        cat = (data or {}).get("community", {}).get("category") or {}
        for child in (cat.get("categories") or []):
            kid = child.get("id")
            if kid and kid not in seen and kid not in ALL_ROOT_IDS:
                seen.add(kid)
                queue.append((kid, f"{path} > {child.get('title','')}".strip()))
    return out


def articles_in_category(cid):
    """Return all KB_ARTICLE nodes in a category, paginating until totalCount is reached."""
    collected, page, total = [], 0, None
    while True:
        data = gql(q_conversations(cid, page))
        conv = (data or {}).get("community", {}).get("conversations") or {}
        if total is None:
            total = conv.get("totalCount", 0)
        edges = conv.get("edges") or []
        for e in edges:
            n = e.get("node") or {}
            if n.get("type") == "KB_ARTICLE":
                collected.append({"path": n["path"], "title": (n.get("title") or "").strip()})
        # stop when the page came back short, empty, or we've reached totalCount
        if len(edges) < 100 or (total is not None and _unique_count(collected) >= total):
            break
        page += 1
    if total is not None and _unique_count(collected) < total:
        print(f"    !! pagination gap in {cid}: got {_unique_count(collected)} of {total}")
    return collected


def _unique_count(items):
    return len({_conv_id(i["path"]) for i in items})


def _conv_id(path):
    return path.rstrip("/").split("/")[-1]


def make_keywords(topic, category):
    combined = f"{topic} {category}".lower()
    words = re.findall(r"[a-z0-9]{3,}", combined)
    out = []
    for w in words:
        if w not in STOPWORDS and w not in out:
            out.append(w)
    return out


def build_local_kb_index():
    """Scan distilled KB files for cited help URLs -> {conversationId: 'relative/path.md'}."""
    index = {}
    url_re = re.compile(r"sprinklr\.com/help/articles/\S*?/([0-9a-f]{16,})")
    for md in KNOWLEDGE_DIR.rglob("*.md"):
        try:
            text = md.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue
        rel = md.relative_to(KNOWLEDGE_DIR).as_posix()
        for m in url_re.finditer(text):
            index.setdefault(m.group(1), rel)
    return index


def main():
    if "PASTE" in CONNECT_SID:
        print("WARNING: CONNECT_SID not set. If calls return empty, paste a fresh connect.sid "
              "cookie into the CONFIG block.\n")

    local_kb = build_local_kb_index()
    print(f"Found {len(local_kb)} already-distilled article URLs to cross-link.\n")

    entries, grand_total, seen_articles = [], 0, set()
    for root_id, area in AREA_ROOTS.items():
        print(f"== {area} ==")
        cats = walk_categories(root_id, area)
        print(f"  {len(cats)} categories")
        area_count = 0
        for cid, path in cats:
            for art in articles_in_category(cid):
                conv_id = _conv_id(art["path"])
                if conv_id in seen_articles:
                    continue          # dedupe across categories (keep first/most-specific)
                seen_articles.add(conv_id)
                entries.append({
                    "area": area,
                    "category": path,
                    "topic": art["title"],
                    "url": f"https://www.sprinklr.com/help/articles/{art['path']}",
                    "keywords": make_keywords(art["title"], path),
                    "local_kb": local_kb.get(conv_id),
                })
                area_count += 1
        print(f"  -> {area_count} unique articles")
        grand_total += area_count

    with OUTPUT_PATH.open("w", encoding="utf-8") as f:
        for e in entries:
            f.write(json.dumps(e, ensure_ascii=False) + "\n")

    linked = sum(1 for e in entries if e["local_kb"])
    print(f"\nDONE. {grand_total} articles -> {OUTPUT_PATH}")
    print(f"  {linked} cross-linked to local distilled KB; {grand_total - linked} JIT-only.")
    if grand_total < 1000:
        print("  WARNING: total looks low — token may be stale or pagination truncated.", file=sys.stderr)


if __name__ == "__main__":
    main()
