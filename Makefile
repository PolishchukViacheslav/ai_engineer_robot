PYTHON := .venv/bin/python

.PHONY: install run test eval check-secrets

install:
	python3 -m venv .venv
	$(PYTHON) -m pip install -r requirements.txt

run:
	$(PYTHON) main.py

test:
	$(PYTHON) -m pytest -q

eval:
	@echo "eval: not implemented yet (Session 5)"

check-secrets:
	gitleaks git . --no-banner --redact