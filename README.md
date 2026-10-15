# AI Engineer Robot: Structured Extraction Service

Turns messy GitHub issues into validated JSON using a cloud LLM and a local LLM, then compares them with real metrics.

This repository is the course project for the AI Engineering course. Homework 1 is the first slice. Later stages (RAG, agent, API) will build on it. The long-term idea is in [docs/IDEA.md](docs/IDEA.md).

## Quickstart

Requirements: Python 3.11+, `make`. Optional: [Ollama](https://ollama.com) for the local model, [gitleaks](https://github.com/gitleaks/gitleaks) for `make check-secrets`.

```bash
make install                # creates .venv and installs requirements
cp .env.example .env        # then fill in one provider key
make run                    # run the pipeline
make test                   # run the tests
make check-secrets          # scan for leaked keys
```

Secrets live only in `.env` (git-ignored). Only `.env.example` is committed.

## Scope of the course

In scope:

1. Structured extraction with schema validation, cloud vs local comparison (Homework 1).
2. RAG with citations.
3. A task-planning agent with tools.
4. A FastAPI service with auth and cost tracking.

Not in scope: OCR, speech-to-text, multi-agent code generation, Jira or GitHub PR automation, webhooks, Prometheus and Grafana. They appear in the long idea document only as future direction.

## Homework 1 status

- [x] Data source chosen: [docs/DECISIONS.md](docs/DECISIONS.md)
- [x] Pydantic schema and JSON Schema: `src/extraction/schema.py`, `schema/technical_task.schema.json`
- [x] Project skeleton, secret scanning
- [ ] 30 texts and a 10-item golden set (Session 2)
- [ ] Cloud model baseline (Session 3)
- [ ] Local model and metrics (Sessions 4-5)
- [ ] Prompt versions and validation (Session 6)
- [ ] REPORT.md (Session 7)

## Layout

```text
src/extraction/   schema, prompts, runner, validator, providers
src/evaluation/   metrics
src/common/       config, logging, cost
prompts/          prompt versions and changelog
config/           models and sampling presets
data/             texts and golden set
results/          model outputs and metrics
tests/            pytest tests
docs/             idea and decisions
```