#!/usr/bin/env bash
# Before a deploy: keep what the server runs now, on the server, so deploy/rollback.sh can bring it back.
#   deploy/snapshot_server.sh            # prints the snapshot folder
# Keeps: the images the containers run now, by image ID, tagged per snapshot (:rb-<stamp>, which
# `docker image prune -f` leaves alone: it removes only untagged images) and listed in images.txt, so
# rolling back to an older snapshot brings back that snapshot's images, not the latest ones; the
# compose/Caddy/env files (secrets stay on the server, mode 600); and hard-linked copies of the data
# folders (rsync replaces files instead of editing them, so the links keep the old content at no extra
# disk cost). Writes only under $REMOTE/rollback/ and the :rb-<stamp> tags. Each kept image holds its
# disk space until its tag is removed (docker rmi model-scout-ai:rb-<stamp>).
set -euo pipefail
HOST="${DEPLOY_HOST:-model-scout}"
REMOTE=/opt/model-scout

ssh "$HOST" "REMOTE=$REMOTE bash -s" <<'EOF'
set -euo pipefail
cd "$REMOTE"
stamp=$(date -u +%Y%m%dT%H%M%SZ)
snap="rollback/$stamp"
mkdir -p "$snap"
chmod 700 rollback "$snap"
for f in compose.yml Caddyfile docs_users .env.ai .env.backend .env.corpus; do
  [ -f "$f" ] && cp -p "$f" "$snap/"
done
chmod 600 "$snap"/.env* "$snap"/docs_users 2>/dev/null || true
for d in hypergraph hypergraph_v2 dataset_index dataset_index_v2; do
  [ -d "data/$d" ] && cp -al "data/$d" "$snap/$d"
done
for s in ai backend; do
  # the image the running container was started from (the :latest tag may already point at a newer load)
  id=$(docker inspect --format '{{.Image}}' "$(docker compose ps -q "$s" </dev/null)" 2>/dev/null || docker image inspect --format '{{.Id}}' "model-scout-$s:latest")
  docker tag "$id" "model-scout-$s:rb-$stamp"
  echo "$s model-scout-$s:rb-$stamp $id" >> "$snap/images.txt"
done
(cd "$snap" && find . -type f ! -name '.env*' ! -name docs_users ! -name SHA256SUMS -exec sha256sum {} + | sort -k2) > "$snap/SHA256SUMS"
echo "$stamp" > rollback/LATEST
echo "snapshot $REMOTE/$snap"; cat "$snap/images.txt"; cat "$snap/.env.corpus" 2>/dev/null || echo "(no .env.corpus: v1 default)"
EOF
