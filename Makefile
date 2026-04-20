.PHONY: help install install-dev test test-cov lint format clean pre-commit

help:
	@echo "Targets disponíveis:"
	@echo "  install      - Instala dependências de produção"
	@echo "  install-dev  - Instala dependências de desenvolvimento"
	@echo "  test         - Executa testes com pytest"
	@echo "  test-cov     - Executa testes com cobertura"
	@echo "  lint         - Executa ruff + mypy"
	@echo "  format       - Formata código com black e isort"
	@echo "  pre-commit   - Roda pre-commit em todos os arquivos"
	@echo "  clean        - Remove arquivos temporários"

install:
	pip install -r requirements.txt

install-dev: install
	pip install -e ".[dev]"

test:
	pytest

test-cov:
	pytest --cov=uol_login_scraper --cov-report=term-missing --cov-report=xml

lint:
	ruff check .
	mypy uol_login_scraper.py || true

format:
	black .
	isort .

pre-commit:
	pre-commit run --all-files

clean:
	rm -rf .pytest_cache .mypy_cache .ruff_cache htmlcov .coverage coverage.xml
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name '*.py[cod]' -delete
