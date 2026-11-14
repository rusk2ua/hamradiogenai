# Changelog

Versions are date-based (`YYYY.MM.DD`).

## [2026.11.14]

### Changed
- Gallery entry for remkey: tower telemetry split into a tower-top node and a supply-box node at the tower base, a shack web dashboard, and a read-only cloud copy that people (with a password) and Claude can check from anywhere.
- Field notes: two more remkey findings from real hardware (a library installed into the wrong Python, and a summary page added because Claude's web reader wouldn't parse JSON) and one more CI catch.

## [2026.11.04]

### Added
- Project gallery: offset-microwave-dish-comparisons (10/24 GHz dish gain, surface error, W1GHZ dual-band feed) and portable-10ghz-eme (link budget and two pointing builds for 10 GHz moonbounce), plus an "In progress" list (ESP8266 moon tracker for 1296 EME, ESP8266 project ideas).
- Field notes page: real bugs from the gallery projects and how each was caught (rules and real logs, tests and CI, real hardware).
- Prompt library templates 9 (analyze a design, with tests and regenerated docs) and 10 (run the numbers before choosing the build).
- Repo checklist: add a test with every bug fix; check generated docs in CI.

### Changed
- Gallery entries for remkey (now running end to end on the real station over Tailscale), 10ghz-web-logger-analyzer (CI and a safer deploy script) and grid-mapper (street-map underlay).

## [2026.10.22] - Microwave Update 2026 edition

### Added
- Website (GitHub Pages) at `docs/index.html`, generated from the Markdown in `guide/` by `tools/build_site.py`.
- `guide/` split into focused pages: principles, workbench, prompting, prompt library, project gallery, repo checklist, MCP safety, GitHub setup guide and FAQ.
- Prompt library: eight adaptable templates based on how the gallery projects were built.
- Project gallery expanded from five to twelve projects, including the optical beacon and receive chain, remkey, the 10 GHz web analyzer, the PlutoSDR resources, ham-mcp and the LoTW tools, each with the technique it demonstrates.
- "What good looks like" repo checklist, including protecting your email with GitHub's noreply address.
- MCP security figures (as of May 2026) and where to start safely.

### Changed
- Tool comparison updated for October 2026: Claude is the primary tool; Gemini Notebook recommended for grounded research, image generation and podcast-style overviews; Kiro used rarely now; ChatGPT still not recommended. "Claude Cowork" is now described as part of Claude.
- GitHub setup guide: sets the noreply email before the first commit, starts repositories private, and notes GitHub Pages visibility on free accounts.
- FAQ privacy answer corrected: files an AI reads in a local folder are still sent to the model to be processed.
- README reduced to an index of the guide.

### Fixed
- Empty Kiro recommendation cell and the "poor consistently poor" typo in the old comparison table.
- Gemini Canvas vs. Gemini Notebook mismatch with the Proceedings paper.

## 2026-08-12 and earlier
- Original single-page companion guide accompanying the Proceedings paper (August 2026).
