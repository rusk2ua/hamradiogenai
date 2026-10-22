# Prompting: the staircase and the anatomy

## Climb the Progressive Prompting Staircase

Never ask for the whole application in one prompt. Build it in steps, each on working code from the last, so you're never debugging five new problems at once. It's the same as bringing up a microwave chain: LO, then mixer, then PA, then sequencing.

1. **Spec and architecture.** Write down the requirements and the approach before any code.
2. **File in, file out.** "Read this Cabrillo log and print the QSO count."
3. **Core logic and math.** Parsing, distance and bearing, scoring.
4. **Visuals and interface.** Maps, plots, a web page.
5. **Polish, test, document.** Edge cases, tests, README, changelog.

### The one rule to say first

> Always ask me clarifying questions before you begin writing code.

It forces the model to work from your constraints instead of guessing. Better still, its questions surface design decisions you hadn't made yet.

## Anatomy of a strong technical prompt

| Part | What it says | Example |
|---|---|---|
| **Role** | Who the AI is and what it values | "You're a Python developer who values clean, single-file scripts." |
| **Context** | What you're building and why | "A grid-square map of a 10 GHz contest log, to share with other rovers." |
| **Constraints** | The hard limits | "Python only, runs on Mac and Windows, no database. Score per the attached rules." |
| **Input** | The shape of your data | "A Cabrillo 3.0 log. Sample attached." |
| **Output** | The deliverable | "One high-resolution PNG per band, darker grids for more contacts." |

Not a developer? Leave the libraries out. Describe the picture you want and where it will run (your own computer, or a cloud account). The model will choose sensible libraries. If you are a developer, name them.

Ready-to-adapt prompts are in the [prompt library](prompts.md).
