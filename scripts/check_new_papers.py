#!/usr/bin/env python3
"""Report arXiv papers by Lorenzo Sani that have no entry in _publications/.

Used by the scheduled site-update agent (see .claude/commands/sync-site.md) and
runnable by hand:

    python3 scripts/check_new_papers.py          # human-readable
    python3 scripts/check_new_papers.py --json   # machine-readable
"""

import argparse
import json
import pathlib
import re
import sys
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

AUTHOR = "Lorenzo Sani"
# Papers by a different person with the same name. Add to this list rather than
# letting the agent rediscover them every run.
EXCLUDE_ARXIV_IDS = {
    "2503.00096",  # BixBench -- FutureHouse computational biology, different L. Sani
}

ATOM = "{http://www.w3.org/2005/Atom}"
ARXIV = "{http://arxiv.org/schemas/atom}"
ROOT = pathlib.Path(__file__).resolve().parent.parent

# An arXiv ID mentioned in a publication file: an arxiv.org link, an
# "arXiv:XXXX.XXXXX" citation, or an `arxiv: "XXXX.XXXXX"` front matter field.
# The ID pattern is strict so a trailing full stop is not captured.
ARXIV_ID_RE = re.compile(
    r"""(?:arxiv\.org/(?:abs|pdf)/|arxiv:\s*["']?)(\d{4}\.\d{4,5})""",
    re.IGNORECASE,
)
# Shortest subtitle (normalized) that is trusted to identify a paper on its own.
MIN_SUBTITLE_KEY = 20


def fetch_arxiv(author: str, max_results: int = 100) -> list[dict]:
    query = urllib.parse.urlencode(
        {
            "search_query": f'au:"{author}"',
            "start": 0,
            "max_results": max_results,
            "sortBy": "submittedDate",
            "sortOrder": "descending",
        }
    )
    url = f"https://export.arxiv.org/api/query?{query}"
    with urllib.request.urlopen(url, timeout=60) as resp:
        tree = ET.fromstring(resp.read())

    papers = []
    for entry in tree.findall(f"{ATOM}entry"):
        raw_id = entry.findtext(f"{ATOM}id", "").rsplit("/abs/", 1)[-1]
        base_id = re.sub(r"v\d+$", "", raw_id)
        comment = entry.find(f"{ARXIV}comment")
        journal = entry.find(f"{ARXIV}journal_ref")
        papers.append(
            {
                "arxiv_id": base_id,
                "title": " ".join(entry.findtext(f"{ATOM}title", "").split()),
                "date": entry.findtext(f"{ATOM}published", "")[:10],
                "updated": entry.findtext(f"{ATOM}updated", "")[:10],
                "authors": [
                    a.findtext(f"{ATOM}name", "")
                    for a in entry.findall(f"{ATOM}author")
                ],
                "abstract": " ".join(entry.findtext(f"{ATOM}summary", "").split()),
                "comment": " ".join(comment.text.split()) if comment is not None else None,
                "journal_ref": journal.text if journal is not None else None,
                "url": f"https://arxiv.org/abs/{base_id}",
            }
        )
    return papers


def normalize_title(title: str) -> str:
    """Fold a title to a comparable key: lowercase alphanumerics only."""
    return re.sub(r"[^a-z0-9]+", "", title.lower())


def title_keys(title: str) -> set[str]:
    """Keys a title can match on: the whole title, and the part after the first
    colon, so "LUNAR: LLM Unlearning via ..." matches the arXiv title
    "LLM Unlearning via ..."."""
    keys = {normalize_title(title)}
    if ":" in title:
        subtitle = normalize_title(title.split(":", 1)[1])
        if len(subtitle) >= MIN_SUBTITLE_KEY:
            keys.add(subtitle)
    return keys


def known_publications() -> tuple[set[str], set[str]]:
    """arXiv IDs and title keys already present in _publications/.

    Some entries link to OpenReview or a proceedings page instead of arXiv. They
    should carry an `arxiv:` front matter field; title matching is the fallback
    for entries that don't, since a title can differ from arXiv's.
    """
    ids, titles = set(), set()
    for path in (ROOT / "_publications").glob("*.md"):
        text = path.read_text()
        ids.update(ARXIV_ID_RE.findall(text))
        m = re.search(r"^title:\s*(.+?)\s*$", text, re.MULTILINE)
        if m:
            titles.update(title_keys(m.group(1).strip("\"'")))
    return ids, titles


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", action="store_true", help="emit JSON")
    ap.add_argument("--author", default=AUTHOR)
    args = ap.parse_args()

    known_ids, known_titles = known_publications()
    missing = [
        p
        for p in fetch_arxiv(args.author)
        # Guard against arXiv's fuzzy author matching returning near-misses.
        if any(args.author.split()[-1] in a for a in p["authors"])
        and p["arxiv_id"] not in known_ids
        and not title_keys(p["title"]) & known_titles
        and p["arxiv_id"] not in EXCLUDE_ARXIV_IDS
    ]

    if args.json:
        json.dump(missing, sys.stdout, indent=2)
        print()
        return 0

    if not missing:
        print(f"Up to date: no new arXiv papers for {args.author}.")
        return 0

    print(f"{len(missing)} paper(s) missing from _publications/:\n")
    for p in missing:
        print(f"  {p['date']}  arXiv:{p['arxiv_id']}")
        print(f"    {p['title']}")
        if p["journal_ref"]:
            print(f"    Journal ref: {p['journal_ref']}")
        if p["comment"]:
            print(f"    Comment: {p['comment'][:120]}")
        print()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
