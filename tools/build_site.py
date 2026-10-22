#!/usr/bin/env python3
"""Build docs/index.html (the GitHub Pages site) from the Markdown in guide/.

The Markdown files are the source of truth. Edit them, then run:

    pip install -r tools/requirements.txt
    python3 tools/build_site.py

Links between guide pages (for example `prompts.md#7-...`) become in-page
anchors on the site, so the same files read correctly on GitHub and on the web.
"""
import re
import sys
from pathlib import Path

import markdown

ROOT = Path(__file__).resolve().parent.parent
GUIDE = ROOT / "guide"
TEMPLATE = ROOT / "tools" / "site_template.html"
OUT = ROOT / "docs" / "index.html"

# Page order and navigation labels. The slug is the file name without .md and
# becomes the section's id on the site.
PAGES = [
    ("principles", "Principles"),
    ("workbench", "Workbench"),
    ("prompting", "Prompting"),
    ("prompts", "Prompt library"),
    ("projects", "Projects"),
    ("good-repo-checklist", "Checklist"),
    ("mcp", "MCP safety"),
    ("github-setup", "Get started"),
    ("faq", "FAQ"),
]


def current_version() -> str:
    """The newest version heading in CHANGELOG.md, e.g. '2026.10.22'."""
    text = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
    match = re.search(r"^## \[?(\d{4}\.\d{2}\.\d{2})", text, re.MULTILINE)
    return match.group(1) if match else "unversioned"


def rewrite_links(html: str) -> str:
    """Turn links to sibling guide pages into anchors on the single page."""
    slugs = {slug for slug, _ in PAGES}

    def fix(match: re.Match) -> str:
        target, _anchor = match.group(1), match.group(2)
        if target in slugs:
            return f'href="#{target}"'
        return match.group(0)

    return re.sub(r'href="([a-z0-9-]+)\.md(#[^"]*)?"', fix, html)


def main() -> int:
    md = markdown.Markdown(extensions=["tables", "fenced_code", "sane_lists"])
    sections = []
    for slug, _label in PAGES:
        path = GUIDE / f"{slug}.md"
        if not path.exists():
            print(f"missing {path}", file=sys.stderr)
            return 1
        body = md.reset().convert(path.read_text(encoding="utf-8"))
        # GitHub task-list checkboxes read better as plain bullets on the site.
        body = body.replace("<li>[ ] ", "<li>")
        sections.append(f'<section class="doc" id="{slug}">\n{rewrite_links(body)}\n</section>')

    nav = "\n".join(f'<a class="link" href="#{slug}">{label}</a>' for slug, label in PAGES)
    page = (
        TEMPLATE.read_text(encoding="utf-8")
        .replace("{{NAV}}", nav)
        .replace("{{CONTENT}}", "\n".join(sections))
        .replace("{{VERSION}}", current_version())
    )
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(page, encoding="utf-8")
    (OUT.parent / ".nojekyll").touch()
    print(f"wrote {OUT.relative_to(ROOT)} ({len(page):,} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
