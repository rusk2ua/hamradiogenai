# Project gallery

Real, public, AI-assisted ham radio projects by K2UA. Each one shows a technique worth copying.

## Microwave and contesting

| Project | What it does | Technique to copy |
|---|---|---|
| [10ghz-log-analyzer](https://github.com/rusk2ua/10ghz-log-analyzer) | Scores ARRL 10 GHz and Up logs, writes Cabrillo, plots points by compass direction and band | **Ground in the rules.** Scoring tied to the rules document; every fix documented with who it affects (see [field notes](lessons.md)) |
| [10ghz-web-logger-analyzer](https://github.com/rusk2ua/10ghz-web-logger-analyzer) · [live site](https://10ghz.microwavedx.com) | Web edition: upload a log, get Cabrillo, reports, polar plots and maps in one .zip | **Engine before dashboard.** Runs the CLI tools unmodified, with a web-vs-CLI parity test, CI on every push, and a deploy script that refuses unsafe changes |
| [grid-mapper](https://github.com/rusk2ua/grid-mapper) | Maidenhead grid density and path maps from a Cabrillo log, per band, with an optional street-map underlay | **Describe the output, not the libraries.** One command, automatic scaling |
| [offset-microwave-dish-comparisons](https://github.com/rusk2ua/offset-microwave-dish-comparisons) | How much gain 0.6–0.9 m offset and prime-focus dishes really give on 10.368 and 24.192 GHz: efficiency, illumination, blockage, surface error, and the W1GHZ dual-band feed | **Pin the math with tests, regenerate the docs.** A test guards the classic "efficiency squared" gain-formula mistake, and CI fails if the README tables drift from the code |
| [portable-10ghz-eme](https://github.com/rusk2ua/portable-10ghz-eme) | 10 GHz moonbounce with a 76 cm portable dish and Q65-60D: the link budget, then two pointing builds (manual sighting, or Mini-RAS auto-tracking) | **Link budget first, then decide the build.** The numbers showed a 2.7° beam makes hand pointing realistic, so the rotator became an option rather than a requirement |
| [eme-calculator-project](https://github.com/rusk2ua/eme-calculator-project) | EME dish siting: moon windows, tree loss by band, wind load | **Start small, iterate.** Experimental, and labeled that way |

## Optical and hardware

| Project | What it does | Technique to copy |
|---|---|---|
| [ve2ug-optical-beacon-project](https://github.com/rusk2ua/ve2ug-optical-beacon-project) | VE2UG's ESP8266 Q65/CW optical beacon, revised with an NTP sync guard, Wi-Fi timeout and diagnostics | **Respect the source.** Credit, an "Unchanged" list, honest test status |
| [optical-receive-chain](https://github.com/rusk2ua/optical-receive-chain) | 940 nm receiver: lens, PD49PI, TIA, TDA2050, with SVG schematics and test tools | **Make it show its math.** A re-runnable TIA calculator instead of a one-off answer |
| [remkey](https://github.com/rusk2ua/remkey) | Remote paddle CW for an IC-7610 driving a tower-top 10 GHz transverter, plus LoRa tower telemetry. Now running end to end on the real station over Tailscale | **Tests before the tower.** CI on three OSes and firmware simulation first; then real-station findings (VPN coexistence, a USB unplug mid-transmit) written straight back into the docs |
| [adalm-pluto-resources](https://github.com/rusk2ua/adalm-pluto-resources) | PlutoSDR firmware comparison and a GPSDO reference-clock mod | **Documentation is a deliverable.** Sourced, geography-aware guidance |

## Logs, data and results

| Project | What it does | Technique to copy |
|---|---|---|
| [nyqp-dashboard](https://github.com/rusk2ua/nyqp-dashboard) · [live site](https://rusk2ua.github.io/nyqp-dashboard/) | Interactive New York QSO Party results | **Zero-build static site.** HTML, CSS and Chart.js on free GitHub Pages hosting |
| [nyqp-cabrillo-fixer](https://github.com/rusk2ua/nyqp-cabrillo-fixer) | Turns irregular submitted logs into rules-compliant Cabrillo 3.0 | **Normalize messy data** before anything downstream sees it |
| [ham-mcp](https://github.com/rusk2ua/ham-mcp) | MCP server that lets an AI query ADIF and Cabrillo logs from Google Drive or S3 | **Connect your data.** (No authentication yet; see [MCP safety](mcp.md)) |
| [arrl-lotw-resources](https://github.com/rusk2ua/arrl-lotw-resources) | Python tools for downloading and working with your LoTW QSO history | **Read the API docs first**, then automate |

## In progress (not yet public)

- **ESP8266 moon tracker** for a 1296 MHz EME dish: a $3 D1 mini plus a GPS module computes the moon's position and drives a Green Heron RT-21 Az-El controller directly, with an OLED and a web display, replacing a PC running PstRotator.
- **ESP8266 project ideas:** a backlog of low-cost ESP8266 builds for radio, optical links, station automation and telemetry.
