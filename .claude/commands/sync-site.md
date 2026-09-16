---
description: Check for new papers and open a PR adding them to the site
---

Keep https://relogu.github.io up to date. GitHub Pages deploys the `relogu`
branch: run `git fetch origin`, create a fresh branch off `origin/relogu`, and
open a pull request back into `relogu` — never push to it directly. Ignore
`master`; it is a stale copy of the academicpages template, not the site.

## 1. Find what's missing

```bash
python3 scripts/check_new_papers.py --json
```

This lists arXiv papers by Lorenzo Sani with no entry in `_publications/`. It
already filters out known same-name authors (see `EXCLUDE_ARXIV_IDS` in the
script). If it reports nothing and step 2 finds nothing, stop without opening a
PR — a no-op PR each week is worse than silence.

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

## 3. Write the entries

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
caused this. Use double quotes, or double the apostrophe (`''`).

Set `featured: true` only if the paper is clearly a headline result (Lorenzo is
first or joint-first author at a top venue). Otherwise leave it off.

## 4. Verify before opening the PR

```bash
LANG=en_US.UTF-8 bundle exec jekyll build 2>&1 | grep -i "error\|YAML Exception"
ls _publications/*.md | wc -l
grep -L 'http-equiv="refresh"' _site/publication/*.html | wc -l
```

Those two counts must match; the `grep -L` skips the redirect stubs that
`redirect_from` writes into the same folder. Do not open the PR if the build
logs a YAML exception.

## 5. Open the PR

Name the repo and base explicitly. A clone with an `upstream` remote (the
academicpages template) can otherwise send the PR there.

```bash
gh pr create --repo relogu/relogu.github.io --base relogu --assignee relogu \
  --title "Site update: N new publication(s)" --body "..."
```

In the body, list each paper added with its arXiv link, each venue changed, and
anything you deliberately skipped and why. Do not merge it — Lorenzo reviews.

## Out of scope

Do not invent talks, teaching entries, or bio changes. Those come from Lorenzo
directly. If you notice the bio or CV looks stale, mention it in the PR body
rather than editing it.
