# Ham Radio Generative AI: Project Companion Guide

**Building and sharing real Amateur Radio projects with generative AI**
By Rus Healy, K2UA · Companion to *From Soldering Irons to Syntax*, Microwave Update 2026

**Website:** <https://rusk2ua.github.io/hamradiogenai/> · **Landing page:** <https://10ghzdx.com/mud2026> · **Slides:** [November 2026 update (PDF)](https://10ghzdx.com/wp-content/uploads/2026/11/From-Soldering-Irons-to-Syntax-%E2%80%94-updated-Nov-2026-1.pdf) · **Version:** 2026.11.14 ([changelog](CHANGELOG.md))

This is a living resource. The paper in the Microwave Update 2026 Proceedings is the August 2026 snapshot; this repository is where the material keeps evolving.

---

## Start here

| If you want to... | Read |
|---|---|
| Understand the approach | [The grounded builder](guide/principles.md): curate, isolate, stay the control operator |
| Pick your tools | [The workbench, October 2026](guide/workbench.md) |
| Write prompts that work | [The anatomy of a prompt and the staircase](guide/prompting.md) |
| Build something tonight | [Prompt library](guide/prompts.md): ten templates you can adapt |
| See real examples | [Project gallery](guide/projects.md): 14 public projects and the technique each one shows |
| Learn from real bugs | [Field notes](guide/lessons.md): defects caught against the rules, by tests, and on real hardware |
| Check your own repo | [What good looks like](guide/good-repo-checklist.md) |
| Connect AI to your data | [MCP, safely](guide/mcp.md) |
| Set up Git and GitHub | [Getting started with GitHub](guide/github-setup.md): the easy way, with Claude, or every step yourself |
| Answer the skeptics | [Common questions](guide/faq.md) |

## The short version

1. **Curate before you code.** Give the AI the primary source: the rules PDF, the datasheet, a real sample log. Don't let it guess.
2. **Isolate the context.** One project, one folder, one conversation.
3. **Be the control operator.** The AI writes syntax; logic, limits and compliance stay yours. Check output against the rules and real data.
4. **Write it plainly.** Say what you want and why, attach the real files, describe the output you'll check, and let it ask questions or say it's unsure. No role-play or magic words needed.
5. **Climb the staircase.** Spec, then file I/O, then core logic, then visuals, then polish, checking each step before the next.
6. **Say this first:** *"Ask me clarifying questions before you write any code."*

## Repository layout

```text
README.md                 this file
CHANGELOG.md              what changed and when
guide/                    the content, in Markdown (source of truth)
docs/index.html           the website, generated from guide/ (GitHub Pages)
tools/build_site.py       regenerates docs/index.html
tools/site_template.html  the website's look
```

## Updating the website

Edit the Markdown in `guide/`, then:

```bash
pip install -r tools/requirements.txt
python3 tools/build_site.py
git add -A && git commit -m "Describe the change" && git push
```

GitHub Pages serves `docs/` from the `main` branch (Settings → Pages → Deploy from a branch → `main` / `/docs`).

## Contact

73, Rus Healy, K2UA. Reach me through the email on my [QRZ.com page](https://www.qrz.com/db/K2UA). More at [10ghzdx.com](https://10ghzdx.com) and [github.com/rusk2ua](https://github.com/rusk2ua).
