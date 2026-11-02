#!/usr/bin/env bash
# Builds the API image here and ships it to the VPS, which is too small to build on.
#   ssh-add ~/.ssh/iwinv_model_scout   # once, so the passphrase is asked only here
#   deploy/deploy.sh                   # image, compose files, runtime data, .env, restart
#   deploy/deploy.sh --data            # data only, after a dataset refresh
set -euo pipefail

cd "$(dirname "$0")/.."
HOST="${DEPLOY_HOST:-model-scout}"
REMOTE=/opt/model-scout
DATA=ai/data

ssh "$HOST" "mkdir -p $REMOTE/data/dataset_index"

# Only what the API reads at runtime.
test -f "$DATA/dataset_index/embeddings.npy"
rsync -az --delete "$DATA/hypergraph/" "$HOST:$REMOTE/data/hypergraph/"
rsync -az "$DATA/dataset_index/manifest.json" "$DATA/dataset_index/embeddings.npy" "$HOST:$REMOTE/data/dataset_index/"
rsync -az "$DATA/hf_datasets_ner.jsonl" "$HOST:$REMOTE/data/"

if [ "${1:-}" != "--data" ]; then
  docker buildx build --platform linux/amd64 -f backend/Dockerfile -t model-scout-api:latest --load .
  docker save model-scout-api:latest | gzip | ssh "$HOST" 'gunzip | docker load'
  rsync -az deploy/compose.yml deploy/Caddyfile "$HOST:$REMOTE/"
  # Runtime keys only: the collection keys in .env stay off the server.
  grep -E '^(OPENAI_API_KEY|SUPABASE_DB_(HOST|PORT|NAME|USER)|SUPABASE_PASSWORD)=' .env |
    ssh "$HOST" "umask 077; cat > $REMOTE/.env"
fi

ssh "$HOST" "cd $REMOTE && docker compose up -d --force-recreate && docker image prune -f"
ssh "$HOST" "cd $REMOTE && docker compose ps"
