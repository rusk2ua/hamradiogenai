# MCP: connecting AI to your data, safely

The **Model Context Protocol (MCP)** is a standard plug between an AI assistant and your data or tools, much as a TNC connected a radio to a computer for packet. With an MCP server connected, you can ask things like:

- "Graph 10 GHz QSO counts by year for the last five years from the logs in my Logs folder."
- "Compare my QSO rates in ARRL DX and CQWW over the last three years."
- "Using only official AWS documentation, give me a step-by-step deployment process for ..."

That last pattern is grounding again, through a different pipe: connect an authoritative documentation server, then tell the model to use only it.

My [ham-mcp](https://github.com/rusk2ua/ham-mcp) project is a simple example: it lets an AI query ADIF and Cabrillo logs, and PDFs, stored in Google Drive or Amazon S3.

## The catch: a security minefield

As of May 2026 (figures cited in the Proceedings paper):

| Figure | What it means |
|---|---|
| **22,775** | MCP servers listed in the Glama directory. Most are weekend projects |
| **36.7%** | of public MCP servers carry server-side request forgery (SSRF) vulnerabilities |
| **41%** | have no authentication at all, including my own ham-mcp |
| **8.5%** | use OAuth |

These numbers will have moved; the lesson hasn't.

## Where to start

1. **Vendor-maintained servers first:** the Filesystem server, GitHub's official MCP server, and cloud providers' documentation servers.
2. **Add community servers only once you can read their code** and know what they can reach.
3. **Give each server the least access it needs**: one folder, not your home directory; read-only where possible.
4. Not every AI environment allows MCP connections. Check your tool's connector settings.
