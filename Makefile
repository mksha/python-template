.DEFAULT_GOAL := help

.PHONY: help install lint format test typecheck build clean

help: ## Show this help message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-15s\033[0m %s\n", $$1, $$2}'

install: ## Install project with dev dependencies
	uv sync --extra dev
	uv run pre-commit install

lint: ## Run linter
	uv run ruff check .

format: ## Format code
	uv run ruff format .

test: ## Run tests
	uv run pytest

test-cov: ## Run tests with coverage report
	uv run pytest --cov --cov-report=html

typecheck: ## Run type checker
	uv run mypy .

build: ## Build sdist and wheel
	uv build

clean: ## Remove build artifacts
	rm -rf dist/ build/ *.egg-info
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name '*.pyc' -delete
