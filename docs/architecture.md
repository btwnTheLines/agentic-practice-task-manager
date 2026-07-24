# Architecture

## System Overview

The Task Management System is a monolithic Django application with server-rendered HTML templates. PostgreSQL serves as the primary database. The entire development environment runs in Docker containers.

## Technology Decisions

| Component | Choice | Rationale |
|-----------|--------|-----------|
| Backend | Django | Full-featured framework with built-in admin, auth, and ORM. Matches project learning goals. |
| Frontend | HTML + Tailwind + JS | Server-rendered templates keep the stack simple. No SPA framework needed for this scope. |
| Database | PostgreSQL | Production-grade relational database. Docker makes local setup trivial. |
| Testing | Pytest | Industry standard for Python testing. pytest-django provides Django integration. |
| Containers | Docker + Compose | Standardized dev environment. Eliminates "works on my machine" issues. |
| CI | GitHub Actions | Native integration with GitHub. Free for public repositories. |

## Directory Layout

```
backend/              # Django project root
  config/             # Project configuration (settings, urls, wsgi)
  manage.py           # Django management entry point
  requirements/       # Pinned dependencies per environment
docker/               # Docker build files
  backend/            # Django Dockerfile and entrypoint
docs/                 # Project documentation
frontend/             # Static assets (HTML, CSS, JS)
tests/                # Test suite
```

## Environment Separation

Three settings modules inherit from `base.py`:

- **local.py** — Development: DEBUG=True, PostgreSQL via Docker
- **production.py** — Production: DEBUG=False, env-var-based config, security middleware

## Data Flow

```
Browser → Django (port 8000) → PostgreSQL (port 5432)
         ↑
    Tailwind CSS (compiled to static files)
```

## Key Constraints

- No application code until Sprint 3. This structure exists solely to support the development environment and CI pipeline.
- Frontend build tooling (Tailwind CLI, npm) will be introduced in Sprint 3 when templates are created.