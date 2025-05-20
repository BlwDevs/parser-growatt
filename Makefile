# Variáveis
PYTHON = python3
VENV = env
PIP = $(VENV)/bin/pip

# Comandos principais
.PHONY: setup run docker-build docker-up docker-down clean

setup:
	$(PYTHON) -m venv $(VENV)
	$(PIP) install -r requirements.txt

run:
	$(VENV)/bin/python main.py

build:
	docker-compose build

docker-run:
	docker compose down && docker compose up

docker-down:
	docker-compose down

clean:
	rm -rf $(VENV)
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete