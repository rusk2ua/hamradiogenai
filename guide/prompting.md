# Prompting: the anatomy and the staircase

Anthropic's own advice is to treat the AI like a brilliant new colleague who has never seen your station. Write your prompt so that a sharp club member with no background could follow it. If they'd be confused, the AI will be too.

You don't need special words, role-play or formatting tricks. Plain sentences, the real files and the reason you want the result do most of the work.

## Anatomy of a prompt that works

| Part | What it says | Example |
|---|---|---|
| **Goal and why** | What you want, and what it's for | "I want maps of the grid squares I worked in the 10 GHz contest, so I can share them with the other rovers." |
| **Input** | The real material, attached | "My Cabrillo 3.0 log from the 2025 10 GHz and Up contest, attached." |
| **Output** | Exactly what you want back, and where it will run | "One high-resolution PNG per band. Darker squares for more contacts, labels only on grids I worked, map sized to fit the log. One command, on my Mac or my Windows PC." |
| **When unsure** | Permission to ask, and to admit it doesn't know | "Ask me questions before you start. If the log is unclear, say so instead of guessing." |

Why each part matters:

- **The why changes the result.** "So I can share them with the other rovers" tells the model the maps must stand on their own for someone else. Current models do noticeably better when they know the purpose.
- **Attach the real thing.** A real log beats any description of a log. The same goes for rules PDFs, datasheets and your station's actual numbers.
- **Describe an output you can check.** A file, a plot, a calculator you can re-run, a plan you can read. Not just "tell me the answer."
- **Permission to say "I'm not sure"** is what keeps the model from inventing an answer.

Not a developer? Leave the libraries out. Describe the result you want and where it will run, and let the model choose the tools. If you are a developer, name them.

### What you can skip

Older prompting guides suggested habits that today's models don't need:

- **Role-play openers** such as "You are an expert Python developer." Say what you want instead.
- **SHOUTING and absolutes** such as "NEVER do X." Give the reason instead: "Use only the attached rules, because the published ones online may be out of date."
- **One giant prompt with every rule you can think of.** Start short, look at what comes back, then add what was missing.

## Inputs and outputs from real projects

The same pattern, from the projects in the [gallery](projects.md):

| Project | Input: what I attached | Output: what I asked for |
|---|---|---|
| [10ghz-log-analyzer](https://github.com/rusk2ua/10ghz-log-analyzer) | My Cabrillo or CSV log, and the ARRL rules PDF | A submittable Cabrillo file with claimed score, plus polar plots by direction and band |
| [optical-receive-chain](https://github.com/rusk2ua/optical-receive-chain) | Photodiode and op-amp datasheets, and "flat from 500 Hz to 15 kHz" | A small calculator that prints stability, bandwidth and noise, not just a part value |
| [portable-10ghz-eme](https://github.com/rusk2ua/portable-10ghz-eme) | My station: 76 cm dish, 25 W, 1 dB noise figure, fixed horizontal polarization | The link budget first, then a step-by-step build doc for each pointing option |
| [remkey](https://github.com/rusk2ua/remkey) | How my station is wired: IC-7610, tower-top transverter, AnyDesk | A build plan covering what happens if the link drops mid-transmit, before any code |

The input is the real thing. The output is something you can check.

## Climb the staircase: build in steps you can check

Build in steps, each on working results from the last, so you're never debugging five new problems at once. It's the same as bringing up a microwave chain: LO, then mixer, then PA, then sequencing.

1. **Spec and architecture.** Write down the requirements and the approach before any code.
2. **File in, file out.** "Read this Cabrillo log and print the QSO count per band."
3. **Core logic and math.** Parsing, distance and bearing, scoring.
4. **Visuals and interface.** Maps, plots, a web page.
5. **Polish, test, document.** Edge cases, tests, README, changelog.

Today's models can take on much bigger jobs in one go than they could a year ago. The steps aren't there because the AI can't cope; they're there for you. Each one ends with something you can run and check before you build on it.

### The one habit to start with

> Ask me clarifying questions before you write any code.

Its questions surface design decisions you hadn't made yet.

Ready-to-adapt prompts are in the [prompt library](prompts.md).
