[![Python CI](https://github.com/Kostyanuch-c/Practic/actions/workflows/ci.yaml/badge.svg)](https://github.com/Kostyanuch-c/Practic/actions/workflows/ci.yaml)
[![Maintainability](https://qlty.sh/gh/Kostyanuch-c/projects/Python-project-small-template/maintainability.svg)](https://qlty.sh/gh/Kostyanuch-c/projects/Python-project-small-template)
[![Code Coverage](https://qlty.sh/gh/Kostyanuch-c/projects/Python-project-small-template/coverage.svg)](https://qlty.sh/gh/Kostyanuch-c/projects/Python-project-small-template)

# Python Project Small Template

A minimal and clean **Python project template** — perfect for starting new small libraries, tools, or scripts with best practices already in place.

## What's Included

* `setup.cfg` — Preconfigured for **mypy**, **flake8**, **isort**, and **black**.
* `requirements-dev.txt` — Development dependencies (**pytest**, **mypy**, **flake8**, etc.).
* `pre-commit` — Auto-formatting, linting, and code-style checks before commits.
* `Makefile` — Basic commands for testing and type checking.
* `tests/` — Folder with an initial example test.
* `CI workflow` — Runs linters and tests automatically on every push or pull request.

## Quick Start

1. Clone the repository

   ```bash
   git clone https://github.com/Kostyanuch-c/Python-project-small-template.git
   cd Python-project-small-template
   ```

2. Create and activate a virtual environment

   ```bash
   python3 -m venv venv
   source venv/bin/activate      
   ```

3. Install development dependencies

   ```bash
   pip install -r requirements-dev.txt
   ```

4. Run tests

   ```bash
   make test
   ```
## Development Commands

| Command              | Description                            |
| -------------------- | -------------------------------------- |
| `make test`          | Run all tests                          |
| `make check`         | Run mypy, flake8 ,isort --check-only   |
| `make pre-commit-run`| Auto-format and check all files        |
