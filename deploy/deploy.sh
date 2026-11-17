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

case "$CORPUS" in v1|v2) ;; *) echo "MODEL_SCOUT_CORPUS must be v1 or v2, not $CORPUS" >&2; exit 1 ;; esac

# Only what the services read at runtime. Each corpus ships only its own folders, so a v2 deploy
# needs no local v1 files and leaves the server's v1 copy (the rollback) untouched, and vice versa.
ssh "$HOST" "mkdir -p $REMOTE/data/readmes $REMOTE/data/dataset_index $REMOTE/data/hypergraph_v2 $REMOTE/data/dataset_index_v2"
rsync -az "$DATA/hf_datasets_ner.jsonl" "$HOST:$REMOTE/data/"
rsync -az --delete "$DATA/readmes/" "$HOST:$REMOTE/data/readmes/"
if [ "$CORPUS" = v2 ]; then
  # Graph files, the documents' build record, the vector record, the vector file (restore it first:
  # python ai/20_sync_dataset_index.py --corpus v2 --restore-vectors) and the pin, which holds the
  # ordered chunk ids the vector rows must follow. The AI service checks them against
  # MODEL_SCOUT_DATA_VERSION and the Supabase v2 build record at start.
  test -f "$DATA/dataset_index_v2/embeddings.npy"
  rsync -az --delete "$DATA/hypergraph_v2/" "$HOST:$REMOTE/data/hypergraph_v2/"
  rsync -az "$DATA/dataset_index_v2/build_manifest.json" "$DATA/dataset_index_v2/manifest.json" \
    "$DATA/dataset_index_v2/embeddings.npy" ai/test/public_data/corpus_v2/data_version.json \
    "$HOST:$REMOTE/data/dataset_index_v2/"
  printf 'MODEL_SCOUT_CORPUS=v2\nMODEL_SCOUT_DATA_VERSION=%s\n' "$V2_DATA_VERSION" | ssh "$HOST" "cat > $REMOTE/.env.corpus"
else
  test -f "$DATA/dataset_index/embeddings.npy"
  rsync -az --delete "$DATA/hypergraph/" "$HOST:$REMOTE/data/hypergraph/"
  rsync -az "$DATA/dataset_index/manifest.json" "$DATA/dataset_index/embeddings.npy" "$HOST:$REMOTE/data/dataset_index/"
  echo "MODEL_SCOUT_CORPUS=v1" | ssh "$HOST" "cat > $REMOTE/.env.corpus"
fi

if [ "${1:-}" != "--data" ]; then
  for service in ai backend; do
    docker buildx build --platform linux/amd64 -f "$service/Dockerfile" -t "model-scout-$service:latest" --load .
    docker save "model-scout-$service:latest" | gzip | ssh "$HOST" 'gunzip | docker load'
  done
  # LF line ends whatever the checkout uses (a Windows clone has CRLF files).
  for f in compose.yml Caddyfile; do tr -d '\r' < "deploy/$f" | ssh "$HOST" "cat > $REMOTE/$f"; done
  if [ -f .env ]; then
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
  else
    # No repo-root .env on this machine: keep the keys and team login already on the server.
    ssh "$HOST" "cd $REMOTE && test -s .env.ai && test -s .env.backend && test -s docs_users" ||
      { echo "no .env here and the server lacks .env.ai, .env.backend or docs_users" >&2; exit 1; }
    echo "no .env here: kept the server's .env.ai, .env.backend and docs_users"
  fi
fi

ssh "$HOST" "cd $REMOTE && docker compose up -d --force-recreate --remove-orphans && docker image prune -f"
ssh "$HOST" "cd $REMOTE && docker compose ps"
