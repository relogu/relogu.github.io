---
description: Check for new papers, blog posts and talks, and open a PR adding them to the site
---

Keep https://relogu.github.io up to date. GitHub Pages deploys the `relogu`
branch: run `git fetch origin`, create a fresh branch off `origin/relogu`, and
open a pull request back into `relogu` — never push to it directly. Ignore
`master`; it is a stale copy of the academicpages template, not the site.

Each run looks for three kinds of content: papers (steps 1–3), blog posts
(step 4) and talks (step 5). Put everything you find in one pull request.

## 1. Find missing papers

```bash
python3 scripts/check_new_papers.py --json
```

This lists arXiv papers by Lorenzo Sani with no entry in `_publications/`. It
already filters out known same-name authors (see `EXCLUDE_ARXIV_IDS` in the
script). It recognises an existing entry by any arXiv ID in the file (the
`paperurl`, the citation, or an `arxiv:` field) and, failing that, by title. If
it lists a paper that already has a page, add `arxiv: "XXXX.XXXXX"` to that page
instead of creating a second one.

Before writing an entry, sanity-check the author list in the JSON. If Lorenzo
Sani appears but none of the usual collaborators do (Nicholas D. Lane, Alex
Iacob, Xinchi Qiu, Meghdad Kurmanji, William F. Shen, Zeyu Cao, Andrej
Jovanović), it is probably a different person: add the arXiv ID to
`EXCLUDE_ARXIV_IDS` instead of creating a page, and say so in the PR body.

## 2. Check for venue upgrades

For each existing preprint in `_publications/` (`venue: 'Preprint'` or
`venue: 'arXiv'`), re-check its arXiv `comment` and `journal_ref` fields. When a
paper has been accepted somewhere, update `venue` to the full conference name,
e.g. `ICML 2026 - The Forty-Third International Conference on Machine Learning`.
Only claim an acceptance the arXiv metadata actually states — never infer one.

If you point `paperurl` at the conference version (OpenReview, proceedings)
instead of arXiv, keep the arXiv ID in an `arxiv: "XXXX.XXXXX"` field right
after `paperurl`. Without it, step 1 can report the paper as missing again.

## 3. Write the paper entries

One file per paper at `_publications/YYYY-MM-DD-shortname.md`, matching the
existing files exactly:

```markdown
---
title: "Full Paper Title"
collection: publications
permalink: /publication/YYYY-MM-DD-shortname
excerpt: 'One sentence, plain language, what the paper does.'
date: YYYY-MM-DD
venue: "Preprint"
paperurl: 'https://arxiv.org/abs/XXXX.XXXXX'
citation: 'Author One, Author Two (YEAR). Title. arXiv:XXXX.XXXXX.'
---
<the excerpt sentence>

[Read the paper here.](https://arxiv.org/abs/XXXX.XXXXX)

Abstract:

> <full arXiv abstract>

Recommended citation: <same as citation field>
```

**YAML gotcha, and the reason this repo has a CI check:** an apostrophe inside a
single-quoted scalar silently breaks the file, and Jekyll skips it without
failing the build. `venue: 'NeurIPS'24'` and an author named `O'Shea` have both
caused this. Use double quotes, or double the apostrophe (`''`). This applies to
posts and talks too.

Set `featured: true` only if the paper is clearly a headline result (Lorenzo is
first or joint-first author at a top venue). Otherwise leave it off.

## 4. Find new blog posts

`_posts/` holds a short link-post for every blog post Lorenzo wrote or
co-wrote, and for Cambridge news stories about his work. Check:

- https://flower.ai/blog — each post lists its authors. Follow the pages
  (`?page=2`, …) until the posts are older than the newest file in `_posts/`.
- https://www.cst.cam.ac.uk/news — stories rarely name authors, so also search
  the web for `"Lorenzo Sani" site:cst.cam.ac.uk/news` and read each candidate
  to confirm it covers his work.

Skip anything whose URL is already a `link:` in `_posts/`
(`grep -h '^link:' _posts/*.md`). Write one file per post at
`_posts/YYYY-MM-DD-shortname.md`, dated when the original was published and
matching the existing files:

```markdown
---
title: "Original Post Title"
date: YYYY-MM-DD
permalink: /posts/YYYY/MM/shortname/
link: "https://flower.ai/blog/..."
tags:
  - federated learning
---
<Two or three sentences in your own words: what the post covers and why it
matters. Do not copy text from the original.>

[Read the full post on Flower.ai.](https://flower.ai/blog/...)
```

For a Cambridge story, the last line is `[Read the full article on the
Department of Computer Science and Technology website.](URL)`. These pages are
previews that send readers to the original, not reprints.

## 5. Find new talks

Talks come from Lorenzo's Google Calendar, through the Google Calendar
connector. If its tools are not available in this session, skip this step and
say so in the PR body, or in your final message if there is no PR.

**Calendars.** Check three calendars from `list_calendars`:

- `primary`, Lorenzo's personal calendar;
- `ls985@cam.ac.uk`, his Cambridge calendar, where most talks live;
- the calendar named `CaMLSys`, the group calendar. His talks show up there as
  copies titled like "Lorenzo's Talk @ …", with the description "Duplicate
  event for visibility in the CaMLSys calendar".

Ignore the rest (holidays, family, bookings, household). `lorenzo@flower.ai`
only exposes free/busy, so skip it too.

**Dates.** Look at events from 45 days before today up to yesterday; the
overlap with last month's run is deliberate. Always pass both `startTime` and
`endTime`, because without them `list_events` returns only upcoming events.
Use `orderBy: startTime` and `pageSize: 250`, and follow `nextPageToken`. Large
results are saved to a file; read them with `jq`.

**What counts.** A talk is an event where Lorenzo speaks: invited talks,
keynotes, tutorials, workshop or working-group sessions he runs, panels,
conference presentations, AMAs and reading-group presentations. These are not
talks: practice talks; rebuttal, literature-review and other internal
presentations; vivas and thesis defences; seminars by other speakers;
conferences and events he only attended (check the public programme when in
doubt); posters; meetings and 1:1s; travel; personal events. If an event is
marked tentative, use the date it actually happened.

**Duplicates.** Skip talks already in `_talks/*.md` (the same event within a
week) or added by an open pull request (`gh pr list --repo
relogu/relogu.github.io`, then check each PR's files).

**When unsure, ask privately.** If an event might be a talk but the calendar
doesn't make that clear, or you can't establish its title and host, don't
create a page and don't guess. List each such event (date, calendar, title) at
the end of your final message so Lorenzo can decide in this session. In the PR
body, give only the count, e.g. "2 calendar events need Lorenzo's decision
(see the run summary)". This repository is public: never copy calendar titles,
descriptions, attendees or meeting links into the PR body or commits, and put
on a talk page only what that page needs.

**Write the entries.** Confirm the title, host and date from public sources
(event pages, programmes, recordings) where you can. One file per talk at
`_talks/YYYY-MM-DD-shortname.md`, matching the existing files:

```markdown
---
title: "Talk Title @ Event or Host"
collection: talks
type: "Talk"
permalink: /talks/YYYY-MM-DD-shortname
venue: "Event or host institution"
date: YYYY-MM-DD
location: "City, Country"
---

On the 16th of June 2025, I presented <work> at <event>, invited by <host>.
For more details regarding this project please visit the [project page](https://relogu.github.io/publication/...).
```

`type` is one of "Talk", "Keynote", "Tutorial", "Workshop" or "Research
Presentation". For an online talk, write the venue as "Online, <host>" and the
location as the host's city, or "Online" when there is no single host city.
Keep the body to one to three sentences in the first person: when it was, who
invited Lorenzo or presented with him, and a link to the related publication
page on this site if there is one.

## 6. Verify before opening the PR

```bash
LANG=en_US.UTF-8 bundle exec jekyll build 2>&1 | grep -i "error\|YAML Exception"
ls _publications/*.md | wc -l
grep -L 'http-equiv="refresh"' _site/publication/*.html | wc -l
ls _talks/*.md | wc -l
ls _site/talks/*.html | grep -v '/index.html$' | wc -l
```

Each pair of counts must match. The `grep -L` skips the redirect stubs that
`redirect_from` writes into the publication folder, and the talks count leaves
out the `/talks/` listing page. Do not open the PR if the build logs a YAML
exception.

## 7. Open the PR

If steps 1–5 found nothing new, stop without opening a PR. A no-op PR every
month is worse than silence.

Name the repo and base explicitly. A clone with an `upstream` remote (the
academicpages template) can otherwise send the PR there.

```bash
gh pr create --repo relogu/relogu.github.io --base relogu --assignee relogu \
  --title "Site update: <what changed>" --body "..."
```

Make the title say what changed, e.g. "Site update: 2 new publications, 1
talk". In the body, list each paper, post and talk added with its link, each
venue changed, and anything you deliberately skipped and why (for calendar
events, only the count; see step 5). Do not merge it — Lorenzo reviews.

## Out of scope

Do not invent teaching entries or bio changes, and do not add posts or talks
that don't come from the sources above. Those come from Lorenzo directly. If
you notice the bio or CV looks stale, mention it in the PR body rather than
editing it.
