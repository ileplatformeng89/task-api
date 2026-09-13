#!/bin/sh

set -eu

APP_HOST="${APP_HOST:-0.0.0.0}"
APP_PORT="${APP_PORT:-8000}"

case "${1:-}" in

    serve)
        echo "Starting Tasks API"
        exec uv run uvicorn app.main:app \
            --host "${APP_HOST}" \
            --port "${APP_PORT}"
        ;;

    serve-dev)
        echo "Starting Tasks API in development mode"
        exec uv run uvicorn app.main:app \
            --host "${APP_HOST}" \
            --port "${APP_PORT}" \
            --reload
        ;;

    migrate)
        echo "Applying database migrations"
        exec uv run alembic upgrade head
        ;;

    downgrade)
        echo "Reverting last database migration"
        exec uv run alembic downgrade -1
        ;;

    alembic)
        shift
        exec uv run alembic "$@"
        ;;

    test)
        echo "Running tests"
        exec uv run pytest
        ;;

    tests-coverage)
        echo "Running tests with coverage"
        exec uv run pytest --cov=app --cov-report=term-missing --cov-fail-under=90
        ;;

    unit-tests)
        echo "Running unit tests"
        exec uv run pytest tests/unit
        ;;

    lint)
        echo "Running Ruff checks"
        exec uv run ruff check .
        ;;

    format)
        echo "Formatting code"
        uv run ruff check . --fix
        exec uv run ruff format .
        ;;

    quality)
        echo "Running quality checks"
        uv run ruff check .
        exec uv run ruff format --check .
        ;;

    *)
        echo "Invalid command: ${1:-<empty>}"
        echo
        echo "Available commands:"
        echo "  serve"
        echo "  serve-dev"
        echo "  migrate"
        echo "  downgrade"
        echo "  alembic"
        echo "  test"
        echo "  tests-coverage"
        echo "  unit-tests"
        echo "  lint"
        echo "  format"
        echo "  quality"
        exit 1
        ;;

esac