FROM python:3.12-slim AS base

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        libpq-dev \
        gcc \
        netcat-openbsd \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY backend/requirements/base.txt /app/requirements/
RUN pip install -r /app/requirements/base.txt

# Copy application code
COPY backend/ /app/

# Copy entrypoint
COPY docker/backend/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]

# --- Development stage ---
FROM base AS development
COPY backend/requirements/local.txt /app/requirements/
RUN pip install -r /app/requirements/local.txt
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# --- Production stage ---
FROM base AS production
COPY backend/requirements/production.txt /app/requirements/
RUN pip install -r /app/requirements/production.txt
EXPOSE 8000
CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]