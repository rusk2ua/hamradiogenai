# The Grounded Builder

Amateur Radio has always been a maker's hobby. We didn't stop building when tubes gave way to transistors, or through-hole to surface mount. Software has been the wall for many of us: hardware follows physics, but software can feel like a labyrinth of syntax, toolchains and frameworks.

Generative AI is a new building material, like copper wire or silicon. It handles the syntax. You still decide what to build, and you still decide whether it works.

Ask a generic chatbot a generic question and you get **AI slop**: bloated, buggy, plausible-looking code. The fix isn't a better chatbot. It's three habits.

## 1. Curate before you code

Never let the model guess the rules or the formulas. Hand it the primary source:

- the contest sponsor's rules (the ARRL rules PDF, not a web search for them)
- datasheets and application notes
- a real sample log, in the exact format you'll feed it
- the math you trust: path loss, Maidenhead conversion, a scoring table

Left to search the web on its own, a model can land on out-of-date or non-authoritative sources. Curation is the filter.

## 2. Isolate the context

One project, one folder, one conversation. Give it only the sources that matter to this project. Mixing your EME siting calculator and your remote keyer in one thread blurs both.

## 3. Be the control operator

The AI writes syntax. **Logic, error boundaries and compliance stay yours.** You are the architect; the AI is the high-speed technician. In practice that means:

- check output against the rules document and against real logs, not by reading the code
- ask for tests that pin the important numbers (a multiplier table, a timing budget) to the source
- write down what you haven't verified yet

Two real examples from [10ghz-log-analyzer](https://github.com/rusk2ua/10ghz-log-analyzer): a blank spreadsheet row that was forward-filled into a phantom duplicate QSO (fixed in v1.5.1), and band multipliers above 122 GHz that didn't match section 5.2 of the rules (fixed in v1.6.1). Both looked fine at a glance. Both were caught by checking against the rules and real logs.
