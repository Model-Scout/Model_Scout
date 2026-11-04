# Built from the repo root: docker buildx build -f ai/Dockerfile .
# Data is not baked in; deploy/compose.yml mounts it at /app/ai/data.
FROM python:3.11-slim

WORKDIR /app
COPY ai/requirements.txt ai/requirements_mcp.txt ai/
RUN pip install --no-cache-dir -r ai/requirements.txt -r ai/requirements_mcp.txt

COPY ai/*.py ai/taxonomy.yaml ai/

ENV HOST=0.0.0.0 PORT=8000 PYTHONUNBUFFERED=1 PYTHONDONTWRITEBYTECODE=1
USER nobody
CMD ["python", "ai/api.py"]
