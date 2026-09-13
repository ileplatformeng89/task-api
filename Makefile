.PHONY: help build up down restart logs migrate downgrade test coverage unit-tests lint format quality shell clean

help:
	@echo "Tasks API"
	@echo ""
	@echo "Docker:"
	@echo "  make build        Build Docker images"
	@echo "  make up           Start the application"
	@echo "  make down         Stop the application"
	@echo "  make restart      Restart the application"
	@echo "  make logs         Follow API logs"
	@echo "  make shell        Open a shell inside the API container"
	@echo ""
	@echo "Database:"
	@echo "  make migrate      Apply database migrations"
	@echo "  make downgrade    Revert the last migration"
	@echo ""
	@echo "Testing:"
	@echo "  make test         Run tests"
	@echo "  make coverage     Run tests with coverage"
	@echo "  make unit-tests   Run unit tests"
	@echo ""
	@echo "Quality:"
	@echo "  make lint         Run Ruff checks"
	@echo "  make format       Format the code"
	@echo "  make quality      Run all quality checks"
	@echo ""
	@echo "Cleanup:"
	@echo "  make clean        Stop containers and remove volumes"

build:
	docker compose build

up:
	docker compose up -d

down:
	docker compose down

restart:
	docker compose restart

logs:
	docker compose logs -f api

migrate:
	docker compose run --rm api migrate

downgrade:
	docker compose run --rm api downgrade

test:
	docker compose run --rm api test

coverage:
	docker compose run --rm api tests-coverage

unit-tests:
	docker compose run --rm api unit-tests

lint:
	docker compose run --rm api lint

format:
	docker compose run --rm api format

quality:
	docker compose run --rm api quality

shell:
	docker compose run --rm --entrypoint /bin/sh api

clean:
	docker compose down -v