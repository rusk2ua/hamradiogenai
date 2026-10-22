# Ham Radio Generative AI: Project Companion Guide

**Building and sharing real Amateur Radio projects with generative AI**
By Rus Healy, K2UA · Companion to *From Soldering Irons to Syntax*, Microwave Update 2026

**Website:** <https://rusk2ua.github.io/hamradiogenai/> · **Landing page:** <https://10ghzdx.com/mud2026> · **Version:** 2026.10.22 ([changelog](CHANGELOG.md))

This is a living resource. The paper in the Microwave Update 2026 Proceedings is the August 2026 snapshot; this repository is where the material keeps evolving.

---

## Start here

| If you want to... | Read |
|---|---|
| Understand the approach | [The grounded builder](guide/principles.md): curate, isolate, stay the control operator |
| Pick your tools | [The workbench, October 2026](guide/workbench.md) |
| Write prompts that work | [The staircase and the anatomy of a prompt](guide/prompting.md) |
| Build something tonight | [Prompt library](guide/prompts.md): eight templates you can adapt |
| See real examples | [Project gallery](guide/projects.md): 12 public projects and the technique each one shows |
| Check your own repo | [What good looks like](guide/good-repo-checklist.md) |
| Connect AI to your data | [MCP, safely](guide/mcp.md) |
| Set up Git and GitHub | [Step-by-step setup guide](guide/github-setup.md) |
| Answer the skeptics | [Common questions](guide/faq.md) |

## The short version

1. **Curate before you code.** Give the AI the primary source: the rules PDF, the datasheet, a real sample log. Don't let it guess.
2. **Isolate the context.** One project, one folder, one conversation.
3. **Be the control operator.** The AI writes syntax; logic, limits and compliance stay yours. Check output against the rules and real data.
4. **Climb the staircase.** Spec, then file I/O, then core logic, then visuals, then polish. Never one giant prompt.
5. **Say this first:** *"Ask me clarifying questions before you write any code."*

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
