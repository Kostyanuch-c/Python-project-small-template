.PHONY: pre-commit-install
pre-commit-install:
	@pre-commit install

.PHONY: pre-commit-run
pre-commit-run:
	@pre-commit run --all-files

.PHONY: typecheck
typecheck:
	@mypy core

.PHONY: lint
lint:
	@isort --check-only core
	@flake8 core

check: lint typecheck
