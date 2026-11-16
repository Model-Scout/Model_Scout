# Built from the repo root: docker buildx build -f ai/Dockerfile .
# Data is not baked in; deploy/compose.yml mounts it at /app/ai/data.
FROM python:3.11-slim

WORKDIR /app
COPY ai/requirements.txt ai/requirements_mcp.txt ai/
RUN pip install --no-cache-dir -r ai/requirements.txt -r ai/requirements_mcp.txt

COPY ai/*.py ai/taxonomy.yaml ai/
# Only the request router and model query classifier serve traffic; the rest of retrieval_lab is offline experiments.
COPY ai/retrieval_lab/__init__.py ai/retrieval_lab/router.py ai/retrieval_lab/classifier.py ai/retrieval_lab/pre_retrieval.py ai/retrieval_lab/

ENV HOST=0.0.0.0 PORT=8000 PYTHONUNBUFFERED=1 PYTHONDONTWRITEBYTECODE=1
USER nobody
CMD ["python", "ai/api.py"]
