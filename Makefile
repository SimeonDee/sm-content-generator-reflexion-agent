# Python interpreter and virtual environment
PYTHON = python3.13
VENV = .venv
BIN = $(VENV)/bin

# Application settings
MAIN = main.py
PACKAGE = src
TEST_DIR = src/tests

# Install all dependencies
.PHONY: install
install:
	$(PYTHON) -m venv $(VENV)
	$(BIN)/python -m pip install --upgrade pip
	$(BIN)/pip install -r requirements.txt

# Run the application
.PHONY: run
run:
	$(BIN)/python $(MAIN)

# Clean up Python bytecode files and caches
.PHONY: clean
clean:
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete
	find . -type d -name ".pytest_cache" -delete
	find . -type d -name ".ruff_cache" -delete
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info

# Format code using black
.PHONY: format
format:
	$(BIN)/pip install black
	$(BIN)/black $(PACKAGE) $(MAIN)

# Lint code using ruff
.PHONY: lint
lint:
	$(BIN)/pip install ruff
	$(BIN)/ruff check $(PACKAGE) $(MAIN)

# Run tests (when you add them)
.PHONY: test
test:
	$(BIN)/pip install pytest
	$(BIN)/pytest $(TEST_DIR) -v

# Run type checking with mypy
.PHONY: type-check
type-check:
	$(BIN)/pip install mypy
	$(BIN)/mypy $(PACKAGE) $(MAIN)

# Set up development environment
.PHONY: dev-setup
dev-setup: install
	$(BIN)/pip install black ruff pytest mypy

# Run all checks
.PHONY: check-all
check-all: format lint type-check test

# Default target
.DEFAULT_GOAL := help

# Help target
.PHONY: help
help:
	@echo "Available targets:"
	@echo "  install     : Create virtual environment and install dependencies"
	@echo "  run        : Run the application"
	@echo "  clean      : Remove Python bytecode files and caches"
	@echo "  format     : Format code using black"
	@echo "  lint       : Lint code using ruff"
	@echo "  test       : Run tests"
	@echo "  type-check : Run type checking with mypy"
	@echo "  dev-setup  : Set up development environment with all tools"
	@echo "  check-all  : Run all checks (format, lint, type-check, test)"