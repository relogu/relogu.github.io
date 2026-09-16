# relogu.github.io

Source for [relogu.github.io](https://relogu.github.io), the personal academic
site of Lorenzo Sani. Built with [Jekyll](https://jekyllrb.com) and deployed by
GitHub Pages.

Originally based on
[academicpages](https://github.com/academicpages/academicpages.github.io), now
with a custom theme layer (see `_layouts/` and `assets/css/site.scss`).

## Running locally

```bash
bundle install
LANG=en_US.UTF-8 bundle exec jekyll serve --livereload
```

Then open <http://localhost:4000>. The `LANG` export matters: without a UTF-8
locale the SCSS compiler fails on non-ASCII characters.

## Adding content

Each item is one Markdown file in a collection directory:

| Directory       | What it is           | Filename                  |
| --------------- | -------------------- | ------------------------- |
| `_publications` | Papers and preprints | `YYYY-MM-DD-shortname.md` |
| `_talks`        | Talks and tutorials  | `YYYY-MM-DD-shortname.md` |
| `_teaching`     | Courses, supervising | `YYYY-term-shortname.md`  |

Copy an existing file in the same directory and edit it — the front matter
fields are load-bearing. Add `featured: true` to a publication to surface it in
the "Selected publications" section on the homepage.

> **Careful with apostrophes.** An apostrophe inside a single-quoted YAML value
> (`venue: 'NeurIPS'24'`, an author named `O'Shea`) makes Jekyll skip the file
> *without failing the build*. Use double quotes, or double the apostrophe.
> The CI workflow now catches this.

## Layouts

| Layout  | Used for                                             |
| ------- | ---------------------------------------------------- |
| `base`  | HTML shell: head, nav, footer, theme toggle          |
| `home`  | Homepage — hero, selected publications, recent talks |
| `list`  | Collection index, grouped by year                    |
| `entry` | A single publication, talk, or teaching item         |
| `page`  | A standalone page such as the CV                     |

Theme colours are CSS custom properties at the top of `assets/css/site.scss`.
The site follows the OS light/dark preference, and the header toggle overrides
it, persisted in `localStorage`.

## Automation

- **`.github/workflows/build.yml`** — builds the site on every push and PR, and
  fails if any file was skipped for broken front matter or a publication did
  not render.
- **`scripts/check_new_papers.py`** — lists arXiv papers with no page yet.
  Run `python3 scripts/check_new_papers.py` any time.
- **`.claude/commands/sync-site.md`** — instructions for the scheduled Claude
  agent that runs the check and opens a PR with draft entries.

## Licence

The underlying theme is © 2016 Michael Rose, MIT licensed (see `LICENSE`).
Site content is © Lorenzo Sani.
