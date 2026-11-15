#!/usr/bin/env bash
# Builds the images here and ships them to the VPS, which is too small to build on.
#   ssh-add ~/.ssh/iwinv_model_scout   # once, so the passphrase is asked only here
#   deploy/deploy.sh                   # images, compose files, runtime data, env files, Swagger login, restart
#   deploy/deploy.sh --data            # data only, after a dataset refresh
#   MODEL_SCOUT_CORPUS=v2 deploy/deploy.sh          # serve the frozen v2: graph, build records and
#                                                  # vector file (searched in memory, like v1)
#   MODEL_SCOUT_CORPUS=v1 deploy/deploy.sh --data   # back to v1 (its files stay on the server)
set -euo pipefail

cd "$(dirname "$0")/.."
HOST="${DEPLOY_HOST:-model-scout}"
REMOTE=/opt/model-scout
DATA=ai/data
CORPUS="${MODEL_SCOUT_CORPUS:-v1}"
# The frozen v2 the server must find in Supabase (ai/test/public_data/corpus_v2/data_version.json).
V2_DATA_VERSION=$(sed -n 's/^ *"data_version": "\([0-9a-f]*\)".*/\1/p' ai/test/public_data/corpus_v2/data_version.json | head -1)
test -n "$V2_DATA_VERSION"

ssh "$HOST" "mkdir -p $REMOTE/data/dataset_index $REMOTE/data/readmes $REMOTE/data/hypergraph_v2 $REMOTE/data/dataset_index_v2"

# Only what the services read at runtime.
test -f "$DATA/dataset_index/embeddings.npy"
rsync -az --delete "$DATA/hypergraph/" "$HOST:$REMOTE/data/hypergraph/"
rsync -az "$DATA/dataset_index/manifest.json" "$DATA/dataset_index/embeddings.npy" "$HOST:$REMOTE/data/dataset_index/"
rsync -az "$DATA/hf_datasets_ner.jsonl" "$HOST:$REMOTE/data/"
rsync -az --delete "$DATA/readmes/" "$HOST:$REMOTE/data/readmes/"
if [ "$CORPUS" = v2 ]; then
  # Graph files, the documents' build record, the vector record and the vector file (restore it first:
  # python ai/20_sync_dataset_index.py --corpus v2 --restore-vectors). The AI service checks them
  # against MODEL_SCOUT_DATA_VERSION and the Supabase v2 build record at start.
  test -f "$DATA/dataset_index_v2/embeddings.npy"
  rsync -az --delete "$DATA/hypergraph_v2/" "$HOST:$REMOTE/data/hypergraph_v2/"
  rsync -az "$DATA/dataset_index_v2/build_manifest.json" "$DATA/dataset_index_v2/manifest.json" \
    "$DATA/dataset_index_v2/embeddings.npy" "$HOST:$REMOTE/data/dataset_index_v2/"
  printf 'MODEL_SCOUT_CORPUS=v2\nMODEL_SCOUT_DATA_VERSION=%s\n' "$V2_DATA_VERSION" | ssh "$HOST" "cat > $REMOTE/.env.corpus"
else
  echo "MODEL_SCOUT_CORPUS=v1" | ssh "$HOST" "cat > $REMOTE/.env.corpus"
fi

if [ "${1:-}" != "--data" ]; then
  for service in ai backend; do
    docker buildx build --platform linux/amd64 -f "$service/Dockerfile" -t "model-scout-$service:latest" --load .
    docker save "model-scout-$service:latest" | gzip | ssh "$HOST" 'gunzip | docker load'
  done
  rsync -az deploy/compose.yml deploy/Caddyfile "$HOST:$REMOTE/"
  # Runtime keys only: collection keys stay off the server, and the public-facing backend never holds the OpenAI key.
  grep -E '^(SUPABASE_DB_(HOST|PORT|NAME|USER)|SUPABASE_PASSWORD)=' .env |
    ssh "$HOST" "umask 077; cat > $REMOTE/.env.backend"
  # MODEL_CONTRACT_FILTERS_ENABLED stays off (absent) until the contract migration and reingest are done.
  grep -E '^(OPENAI_API_KEY|SUPABASE_DB_(HOST|PORT|NAME|USER)|SUPABASE_PASSWORD|MODEL_CONTRACT_FILTERS_ENABLED)=' .env |
    ssh "$HOST" "umask 077; cat > $REMOTE/.env.ai; rm -f $REMOTE/.env"
  # Team login for Swagger; only the bcrypt hash leaves this machine.
  password=$(grep -E '^DOCS_PASSWORD=' .env | cut -d= -f2-)
  test -n "$password" || { echo "set DOCS_PASSWORD in .env" >&2; exit 1; }
  echo "team $(docker run --rm caddy:2-alpine caddy hash-password --plaintext "$password")" |
    ssh "$HOST" "umask 077; cat > $REMOTE/docs_users"
fi

ssh "$HOST" "cd $REMOTE && docker compose up -d --force-recreate --remove-orphans && docker image prune -f"
ssh "$HOST" "cd $REMOTE && docker compose ps"
