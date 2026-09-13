FROM mcr.microsoft.com/devcontainers/python:3.14

ENV UV_LINK_MODE=copy

# PostgreSQL client
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# uv
COPY --from=ghcr.io/astral-sh/uv:0.12 /uv /uvx /bin/