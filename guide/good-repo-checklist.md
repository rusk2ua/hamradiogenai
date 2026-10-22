# What good looks like: the repo checklist

Every project in the [gallery](projects.md) aims for this. None of it is hard, and the AI will do nearly all of it if you ask once and make it a [house rule](prompts.md#7-your-house-rules-set-once).

- [ ] **README** that says what it is, how to run it, the current version, and what has and hasn't been tested
- [ ] **CHANGELOG** with the reason for each change, and who a fix affects
- [ ] **One versioning scheme**, used consistently (date-based `YYYY.MM.DD` or semantic `1.6.1`)
- [ ] **A LICENSE**, and credit for any upstream author whose work you built on
- [ ] **Sample data**, so a fresh clone runs immediately
- [ ] **Tests**, and CI that runs them on every push
- [ ] **Tests that pin the important numbers** to their source: multipliers to the rules, timing to the spec
- [ ] **No secrets**: placeholders for credentials, and a `.gitignore` for local files, virtual environments and `.DS_Store`
- [ ] **Commits use your GitHub noreply email**, never your personal one
- [ ] **Link restricted datasheets**; don't copy them into the repo
- [ ] **State what you haven't verified.** "Not yet run on real hardware" is a feature, not an embarrassment

## Protect your email before your first commit

Commits are public and permanent. Find your noreply address in GitHub **Settings → Emails** (it looks like `1234567+yourname@users.noreply.github.com`), then:

```bash
git config --global user.email "1234567+yourname@users.noreply.github.com"
```

In the same Emails settings you can turn on **"Block command line pushes that expose my email."** Then tell your AI tool to use the noreply address for every commit.
