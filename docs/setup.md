# Setup

## Prerequisites

- Docker and Docker Compose installed on your machine
- Git

## Quick Start

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd task-manager
   ```

2. Start the development environment:

   ```bash
   docker compose up --build
   ```

   This starts two containers:
   - **db** — PostgreSQL 16 on port 5432
   - **backend** — Django development server on port 8000

3. Open the application:

   ```
   http://localhost:8000
   ```

## First-Time Setup

The entrypoint script automatically runs database migrations on container start. No manual steps required.

## Useful Commands

| Command | Description |
|---------|-------------|
| `docker compose up --build` | Build and start all services |
| `docker compose down` | Stop all services |
| `docker compose logs -f` | Follow container logs |
| `docker compose exec backend python manage.py <command>` | Run Django management commands |
| `docker compose exec backend pytest` | Run the test suite |

## Environment Variables

Copy `.env.example` to `.env` and adjust as needed:

```bash
cp .env.example .env
```

The default values in `docker-compose.yml` work for local development without a `.env` file.

## Running Tests

```bash
docker compose exec backend pytest
```

## Project Structure

See [architecture.md](architecture.md) for a detailed explanation of the directory layout and technology decisions.