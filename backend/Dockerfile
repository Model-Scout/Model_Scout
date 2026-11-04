# Built from the repo root: docker buildx build -f backend/Dockerfile .
# READMEs are not baked in; deploy/compose.yml mounts them at /app/readmes.
FROM python:3.11-slim

WORKDIR /app
COPY backend/requirements.txt backend/
RUN pip install --no-cache-dir -r backend/requirements.txt
COPY backend/app backend/app

ENV HOST=0.0.0.0 PORT=8000 PYTHONUNBUFFERED=1 PYTHONDONTWRITEBYTECODE=1 READMES_DIR=/app/readmes
USER nobody
CMD ["python", "backend/app/main.py"]
