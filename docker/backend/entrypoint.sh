#!/bin/sh
set -e

# Wait for PostgreSQL to be available
if [ -n "$DATABASE_HOST" ]; then
    echo "Waiting for PostgreSQL at $DATABASE_HOST:$DATABASE_PORT..."
    while ! nc -z "$DATABASE_HOST" "$DATABASE_PORT"; do
        sleep 1
    done
    echo "PostgreSQL is available."
fi

# Run database migrations
python manage.py migrate --noinput

# Execute the main command
exec "$@"