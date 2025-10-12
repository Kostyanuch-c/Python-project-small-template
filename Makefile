.PHONY: lint
lint:
	@isort --check-only core
	@flake8 core

.PHONY: format
format:
	@isort .

.PHONY: pre-commit-install
pre-commit-install:
	@pre-commit install

.PHONY: pre-commit-run
pre-commit-run:
	@pre-commit run --all-files