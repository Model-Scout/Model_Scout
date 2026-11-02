# Built from the repo root: docker buildx build -f backend/Dockerfile .
# Data is not baked in; deploy/compose.yml mounts it at /app/ai/data.
FROM python:3.11-slim

WORKDIR /app
COPY ai/requirements.txt ai/requirements_mcp.txt ai/
COPY backend/requirements.txt backend/
RUN pip install --no-cache-dir -r backend/requirements.txt

COPY ai/*.py ai/taxonomy.yaml ai/
COPY backend/app backend/app

ENV HOST=0.0.0.0 PORT=8000 PYTHONUNBUFFERED=1 PYTHONDONTWRITEBYTECODE=1
USER nobody
CMD ["python", "backend/app/main.py"]
