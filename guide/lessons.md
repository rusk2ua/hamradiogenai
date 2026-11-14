# Field notes: bugs caught, and how

Real defects from the projects in the [gallery](projects.md). Every one looked fine at a glance. None was caught by reading code; each was caught by checking against a primary source, a real log, real hardware, or a test. This is what "be the control operator" means in practice.

## Caught against the rules and real logs

| Project | What was wrong | How it was caught | The fix |
|---|---|---|---|
| 10ghz-log-analyzer v1.5.1 | A blank spreadsheet row was forward-filled into a phantom duplicate QSO | Comparing the output with the actual log | Forward-fill only date, band, grid and time; never invent a call sign |
| 10ghz-log-analyzer v1.6.1 | Bands above 122 GHz scored 6x and 10x; the rules give every band from 122 GHz up 5x | Checking the score against rules section 5.2 | Multipliers corrected, and a test now pins the table to the rules |
| 10ghz-log-analyzer v1.6.2 | A "142 GHz" band with Cabrillo code `142G`. There is no such band: the allocation is 134 GHz, code `134G` | Reviewing a slide about the previous bug, two nights before a talk | Renamed everywhere; old logs that say `142` still load and score correctly |
| 10ghz-log-analyzer v1.6.3 | Every Cabrillo file said it was made by v1.5.3, whatever the release | Reading a generated log's header | One version number, used everywhere |

The pattern: a band table, a multiplier, a version string. Small, confident and wrong. **You are the domain expert, and this is exactly where you'll notice.**

## Caught by tests and CI

- **The gain formula.** Written as `(η·π·D/λ)²` instead of `η·(π·D/λ)²`, the dish gain equation squares the efficiency and understates gain by 1.25–1.55 dB. In [offset-microwave-dish-comparisons](https://github.com/rusk2ua/offset-microwave-dish-comparisons), a test named `test_efficiency_not_squared` guards against it, and CI fails if the README's tables no longer match what the code computes.
- **A firmware image that wouldn't compile.** In [remkey](https://github.com/rusk2ua/remkey), CI builds every Arduino image on every push. It caught a break before anyone flashed a board, and caught another when the telemetry split added a struct the Arduino IDE's generated prototypes couldn't see (the fix: move the struct into a header).
- **A flaky test that was really a timing race.** remkey's "keyer unplugged mid-transmit" test sometimes failed on slow runners. The cause was the test replugging the keyer before the client had heard PTT drop. The fix was in the test, not the code, plus a per-test timeout so a hung test fails fast and names itself.
- **A deploy that could roll itself back.** In [10ghz-web-logger-analyzer](https://github.com/rusk2ua/10ghz-web-logger-analyzer), changing the budget-alert email would make AWS replace two fixed-name budgets, fail, and roll back the whole update. `deploy.sh` now reuses the existing address and refuses a different one, with tests run against a fake AWS CLI.

## Caught on real hardware

remkey's software passed CI on three operating systems before it touched the radio. Running it on the real station still turned up things no test could:

- A VPN on the shack PC blocked inbound connections on the remote-access network, so the docs now describe running Tailscale alongside NordVPN, with measured latency.
- Unplugging the paddle's USB keyer mid-transmission needed a graceful PTT release and automatic reconnect.
- Adding the cloud copy, `pip install` put the AWS library into a different Python than the one the station service runs in (a virtual environment). The fix was an install script that finds the right one, and an error message that names the Python it's running.
- Claude's web reader wouldn't parse the raw JSON feed, so the uploader also writes a plain HTML summary page for it to read.

Each finding went straight back into the README and build plan, so the next builder doesn't hit it.

## The takeaways

1. **Check output against the source,** not against your sense that it looks right.
2. **When you find a bug, add a test that would have caught it,** and a changelog line that says who's affected.
3. **Let CI check your docs too,** when they're generated from code.
4. **Write down what hardware testing teaches you,** in the repo, the same day.
