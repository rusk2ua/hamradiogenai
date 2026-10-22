# Prompt library

Templates modeled on how the projects in the [gallery](projects.md) were built. Copy one, replace the bracketed parts, attach your source material, and start a fresh conversation per project. Every one assumes you've said: **"Ask me clarifying questions before you write any code."**

---

## 1. Score a contest from the official rules

*Pattern behind [10ghz-log-analyzer](https://github.com/rusk2ua/10ghz-log-analyzer).*

```text
You're a Python developer who writes clear, well-commented scripts for
non-programmers. I'm a ham radio contester, not a developer.

I've attached the official rules for [CONTEST NAME] and a sample log in
[Cabrillo 3.0 / CSV with columns ...]. Score the log exactly as the rules
say. Do not look up the rules anywhere else. If the rules are ambiguous,
stop and ask me.

Start with step 1 only: read the log and print the number of QSOs per band.
Then we'll add scoring, then reports, one step at a time.

When we get to scoring, add a test that pins every multiplier and point
value to the rules section it came from.
```

## 2. Map grids worked from a log

*Pattern behind [grid-mapper](https://github.com/rusk2ua/grid-mapper).*

```text
I want a map of the Maidenhead grid squares in a contest log, one image
per band, with darker squares for more contacts and labels only on grids
I worked. Input is a Cabrillo log (sample attached). It should run with one
command on Mac or Windows. I don't know which mapping libraries to use;
pick sensible ones and tell me why. Size the map automatically to the area
the log covers.
```

## 3. Revise someone else's firmware, with credit

*Pattern behind [ve2ug-optical-beacon-project](https://github.com/rusk2ua/ve2ug-optical-beacon-project).*

```text
Attached is [AUTHOR, CALL]'s original sketch and documentation for
[PROJECT]. Review the firmware for timing and robustness problems and
propose fixes, but don't change the core behavior without asking.

Then set it up as a GitHub repo:
- README with a version table and a test-status table (what's verified,
  what isn't)
- CHANGELOG with "Added", "Changed", "Unchanged" (what's still the original
  author's) and the reason for each change
- credit the original author everywhere the design is described
- no real credentials in the code; placeholders with a warning
Convert the original PDF docs to Markdown under docs/.
```

## 4. Turn a design decision into a calculator

*Pattern behind `tools/tia_calc.py` in [optical-receive-chain](https://github.com/rusk2ua/optical-receive-chain).*

```text
I'm building a photodiode transimpedance amplifier: [PHOTODIODE] at
[BIAS], [OP-AMP], target flat response [F1] to [F2]. Datasheets attached.

Don't just tell me Rf and Cf. Write a small Python script, standard library
only, that calculates stability margin, bandwidth, noise and DC headroom,
with presets for [OP-AMP LIST], and prints a table. Say in the output which
numbers are ballpark datasheet values I should measure on my own build.
```

Swap in your own problem: path loss and link budget between two grids, rain fade at 24 GHz, dish wind load, feed offset.

## 5. Specify a station system before building it

*Pattern behind [remkey](https://github.com/rusk2ua/remkey).*

```text
I want to [GOAL, e.g. send CW with my own paddle to my shack remotely].
My station: [RIG, interfaces, what runs on the shack PC, how I reach it
remotely, what I won't change]. Constraints: [safety, latency, budget,
parts on hand].

Before any code, write docs/build-plan.md: the architecture, the failure
modes and what the system does in each (especially link loss while
transmitting), a parts list, and a phased build and test plan. Ask me
about anything you'd otherwise assume.

When we write code: tests that run without hardware, a simulation of the
firmware if possible, and CI on every push.
```

## 6. Put a web front end on a working command-line tool

*Pattern behind [10ghz-web-logger-analyzer](https://github.com/rusk2ua/10ghz-web-logger-analyzer).*

```text
My command-line tools [REPO LINKS] work and are tested. Build a web front
end that runs them unmodified (vendor them in with a sync script; never
hand-edit the copies). Users upload a log and download results.

Add a test proving the web app's outputs match the CLI's for the same log.
Deploy target: [my own computer only / AWS serverless / GitHub Pages
static site]. Give me a local mode that runs without the cloud.
```

## 7. Your house rules (set once)

Put this in a project's instructions, or ask Claude to remember it.

```text
House rules for all my GitHub projects:
- Commit as [NAME] <[ID]+[USER]@users.noreply.github.com>. Never use my
  personal email.
- Versioning: [date-based YYYY.MM.DD / semantic].
- Every change gets a CHANGELOG entry with the reason.
- README always has: what it is, how to run it, current version, and what
  has and hasn't been tested.
- No secrets in the repo. Placeholders plus .gitignore.
- Credit upstream authors. Link restricted datasheets; don't copy them.
```

## 8. Report a bug so it gets fixed properly

```text
I ran [COMMAND] on [INPUT, attached] and got this:

[PASTE THE FULL ERROR OR WRONG OUTPUT]

Expected: [WHAT THE RULES / DATASHEET SAY IT SHOULD BE].
Find the root cause before changing anything. Fix it in place, add a test
that would have caught it, and add a CHANGELOG entry that says who is
affected.
```
