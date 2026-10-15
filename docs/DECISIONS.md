# Decisions

## ADR-001: Data source

- Source: GitHub issues of hyperliquid-dex/hyperliquid-python-sdk
- License: MIT
- Entity type: technical task (bug / feature / refactor / docs / question)
- Why: API-heavy issues fit the api_changes field; good length variety (38 to 9924 chars); same repo can feed RAG later
- Backup: facebook/react issues (MIT)
- Privacy: issues contain emails, @usernames, real names and wallet addresses (0x + 40 hex chars). Session 2 anonymizer must remove all of them.
- Noise: long issues contain tables, logs and code blocks (example: Issue #291)
- Known weakness: almost all English; mixed-language quota will be filled with a few hand-translated texts, documented in data/README.md
