#!/usr/bin/env bash
# Bring the server back to a snapshot from deploy/snapshot_server.sh: that snapshot's images (by the
# image IDs it recorded), compose/env files and data.
#   deploy/rollback.sh                 # the latest snapshot
#   deploy/rollback.sh 20261116T...Z   # a given one
# A snapshot that served v2 starts only if Supabase still holds that v2 build (the AI service checks the
# build record at start). If the v2 tables were reloaded since, either reload that build first (with the
# commit that built it) or roll back to v1: MODEL_SCOUT_CORPUS=v1 deploy/deploy.sh --data.
set -euo pipefail
HOST="${DEPLOY_HOST:-model-scout}"
REMOTE=/opt/model-scout

ssh "$HOST" "REMOTE=$REMOTE STAMP=${1:-} bash -s" <<'EOF'
set -euo pipefail
cd "$REMOTE"
stamp="${STAMP:-$(cat rollback/LATEST)}"
snap="rollback/$stamp"
test -d "$snap"
(cd "$snap" && sha256sum -c --quiet SHA256SUMS)
# the images this snapshot recorded, checked by ID before anything is replaced
while read -r s tag id; do
  [ "$(docker image inspect --format '{{.Id}}' "$tag")" = "$id" ] || { echo "$tag is not $id: stop" >&2; exit 1; }
done < "$snap/images.txt"
[ "$(wc -l < "$snap/images.txt")" -eq 2 ] || { echo "$snap/images.txt must list ai and backend" >&2; exit 1; }
for f in compose.yml Caddyfile docs_users .env.ai .env.backend .env.corpus; do
  if [ -f "$snap/$f" ]; then cp -p "$snap/$f" "$f"; elif [ "$f" = .env.corpus ]; then rm -f .env.corpus; fi
done
for d in hypergraph hypergraph_v2 dataset_index dataset_index_v2; do
  [ -d "$snap/$d" ] && rsync -a --delete "$snap/$d/" "data/$d/"
done
while read -r s tag id; do docker tag "$id" "model-scout-$s:latest"; done < "$snap/images.txt"
docker compose up -d --force-recreate --remove-orphans </dev/null
docker compose ps </dev/null
echo "rolled back to $snap"; cat "$snap/images.txt"; cat .env.corpus 2>/dev/null || echo "(no .env.corpus: v1 default)"
EOF
