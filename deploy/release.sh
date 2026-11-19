#!/usr/bin/env bash
# One release = one code commit + two images + one frozen v2 data set, built once, checked locally,
# then shipped as is. Nothing is rebuilt after `verify`.
#
#   deploy/release.sh build                  images (linux/amd64, from the committed code, LF) and the
#                                            release folder deploy/.releases/<id>/ (data, settings, hashes)
#   deploy/release.sh verify <id> [--query]  run that release on Docker Desktop (deploy/compose.local.yml)
#                                            and check it; --query also sends one real question
#                                            (OpenAI calls, under one cent) and checks where it was stored
#   deploy/release.sh down                   stop the local validation containers
#   deploy/release.sh ship <id>              VPS: send the verified images and folder, check them there,
#                                            install, activate (a failed check re-activates the previous)
#   deploy/release.sh rollback <id|legacy>   VPS: activate an installed earlier release
#   deploy/release.sh status                 VPS: active release and containers
#
# Release id: <UTC time>-<commit>[-dirty]-<data_version>, so two code deploys of the same data differ.
# A "-dirty" build (uncommitted tracked changes, taken with git stash create) is for local checks only:
# ship refuses it.
#
# Only what changes the served code or data goes in a release. A data change (new v2 build) follows the
# data runbook in deploy/README.md first; this script never loads or changes the Supabase tables.
set -euo pipefail

cd "$(dirname "$0")/.."
HOST="${DEPLOY_HOST:-model-scout}"
REMOTE=/opt/model-scout
RELEASES=deploy/.releases
LOCAL_ENV=deploy/.local/ai.env
PIN=ai/test/public_data/corpus_v2/data_version.json
SERVICES=(ai backend)
# Build inputs: an untracked file here would be missing from the image, so build stops on one.
# Same list as the Dockerfiles copy (:(glob) keeps ai/*.py from matching ai/test/*.py).
BUILD_INPUTS=(ai/Dockerfile backend/Dockerfile .dockerignore ai/requirements.txt ai/requirements_mcp.txt
  ai/taxonomy.yaml backend/requirements.txt backend/app shared ':(glob)ai/*.py'
  ai/retrieval_lab/__init__.py ai/retrieval_lab/router.py ai/retrieval_lab/classifier.py ai/retrieval_lab/pre_retrieval.py)

die() { echo "release: $*" >&2; exit 1; }
# Docker on Windows needs a Windows path for bind mounts (Git Bash's pwd -W); elsewhere pwd is that path.
HERE_NATIVE=$(pwd -W 2>/dev/null || pwd)
compose_local() { RELEASE_DIR="$HERE_NATIVE/$RELEASES/$1" MODEL_SCOUT_RELEASE="$1" docker compose -f deploy/compose.local.yml "${@:2}"; }
release_dir() {
  [[ "$1" =~ ^[0-9]{8}T[0-9]{6}Z-[0-9a-f]{8}(-dirty)?-[0-9a-f]{8}$ ]] || die "bad release id: $1"
  [ -f "$RELEASES/$1/release.json" ] || die "no release $1 (deploy/release.sh build)"
  echo "$RELEASES/$1"
}
image_id() { docker image inspect -f '{{.Id}}' "model-scout-$1:$2"; }
# Python: the repo's venv when there is one (Git Bash's "python" can be the Windows Store stub).
PY=python3
for p in .venv/Scripts/python.exe .venv/bin/python; do [ -x "$p" ] && PY="$PWD/$p" && break; done
json_get() {  # json_get <file> <key> [<key>...]; tr: Windows Python ends lines with \r\n
  "$PY" -c "import json,sys; d=json.load(open(sys.argv[1], encoding='utf-8'))
for k in sys.argv[2:]: d=d[k]
print(d)" "$@" | tr -d '\r'
}

build() {
  local untracked
  untracked=$(git status --porcelain --untracked-files=all -- "${BUILD_INPUTS[@]}" | grep '^??' || true)
  [ -z "$untracked" ] || die "untracked build inputs (commit or remove them):"$'\n'"$untracked"
  local commit base dirty="" short version stamp id dir src
  base=$(git rev-parse HEAD)
  commit=$(git stash create)  # empty when the tracked tree is clean
  if [ -n "$commit" ]; then dirty="-dirty"; else commit=$base; fi
  short=${base:0:8}
  version=$(json_get "$PIN" data_version)
  stamp=$(date -u +%Y%m%dT%H%M%SZ)
  id="$stamp-$short$dirty-${version:0:8}"
  dir="$RELEASES/$id"
  echo "release $id (code $commit${dirty:+, includes uncommitted changes}, data $version)"

  # The served data must be the pinned build.
  (cd ai && "$PY" -X utf8 public_v2_pipeline.py --verify-pin)
  test -f ai/data/dataset_index_v2/embeddings.npy || die "no v2 vectors (python ai/20_sync_dataset_index.py --corpus v2 --restore-vectors)"

  # Code from git objects, so the image is the commit with LF line ends whatever this checkout uses.
  src=$(mktemp -d)
  trap 'rm -rf "$src"' RETURN
  git -c core.autocrlf=false archive "$commit" | tar -x -C "$src"
  for s in "${SERVICES[@]}"; do
    docker buildx build --platform linux/amd64 -f "$src/$s/Dockerfile" -t "model-scout-$s:$id" --load "$src"
  done

  # Data: only what the VPS serves (as deploy.sh sends for v2). Hard links, not copies, where possible;
  # SHA256SUMS below catches any later change to the linked files.
  mkdir -p "$dir/data/dataset_index_v2"
  for p in hf_datasets_ner.jsonl readmes hypergraph_v2; do
    cp -al "ai/data/$p" "$dir/data/" 2>/dev/null || cp -a "ai/data/$p" "$dir/data/"
  done
  for f in build_manifest.json manifest.json embeddings.npy; do
    ln "ai/data/dataset_index_v2/$f" "$dir/data/dataset_index_v2/$f" 2>/dev/null || cp -p "ai/data/dataset_index_v2/$f" "$dir/data/dataset_index_v2/"
  done
  tr -d '\r' < "$PIN" > "$dir/data/dataset_index_v2/data_version.json"
  # Settings, LF whatever the checkout uses.
  for f in compose.yml Caddyfile server_release.sh; do tr -d '\r' < "deploy/$f" > "$dir/$f"; done
  printf 'MODEL_SCOUT_CORPUS=v2\nMODEL_SCOUT_DATA_VERSION=%s\n' "$version" > "$dir/.env.corpus"
  printf 'MODEL_SCOUT_RELEASE=%s\n' "$id" > "$dir/.env"
  : > "$dir/images.txt"
  for s in "${SERVICES[@]}"; do echo "$s $(image_id "$s" "$id")" >> "$dir/images.txt"; done
  "$PY" -X utf8 - "$dir" "$id" "$commit" "$base" "${dirty:+true}" "$PIN" <<'EOF'
import json, sys, datetime, subprocess
from pathlib import Path
d, rid, commit, base, dirty, pin_path = sys.argv[1:7]
pin = json.load(open(pin_path, encoding="utf-8"))
manifest = json.load(open(Path(d) / "data/dataset_index_v2/manifest.json", encoding="utf-8"))
images = dict(line.split() for line in open(Path(d) / "images.txt", encoding="utf-8") if line.strip())
record = {
    "release_id": rid,
    "created_at": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
    "code": {"commit": commit, "base_commit": base, "dirty": dirty == "true",
             "branch": subprocess.run(["git", "rev-parse", "--abbrev-ref", "HEAD"], capture_output=True, text=True).stdout.strip()},
    "platform": "linux/amd64",
    "images": images,
    "data": {"data_version": pin["data_version"], "corpus_id": pin["stages"]["hypergraph"]["stage_id"],
             "documents_id": pin["stages"]["documents"]["stage_id"],
             "vectors_sha256": (manifest.get("embedding_run") or {}).get("vectors_sha256"),
             "chunk_ids_sha256": pin.get("chunk_ids_sha256")},
}
(Path(d) / "release.json").write_text(json.dumps(record, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
EOF
  (cd "$dir" && find . -type f ! -name SHA256SUMS ! -name verified.json | LC_ALL=C sort | sed 's|^\./||' | xargs -d '\n' sha256sum > SHA256SUMS)
  echo "built $dir ($(wc -l < "$dir/SHA256SUMS") files)"
  echo "next: deploy/release.sh verify $id"
}

local_env() {  # the AI's runtime keys only, like deploy.sh's .env.ai; never printed
  local source
  for source in .env ai/.env; do [ -f "$source" ] && break; done
  [ -f "$source" ] || die "no .env or ai/.env for the AI's OpenAI key and Supabase read settings"
  mkdir -p deploy/.local
  (umask 077; grep -E '^(OPENAI_API_KEY|SUPABASE_DB_(HOST|PORT|NAME|USER)|SUPABASE_PASSWORD|MODEL_CONTRACT_FILTERS_ENABLED)=' "$source" > "$LOCAL_ENV")
  for k in OPENAI_API_KEY SUPABASE_DB_HOST SUPABASE_PASSWORD; do grep -q "^$k=" "$LOCAL_ENV" || die "$source lacks $k"; done
}

verify() {
  local id=$1 query=${2:-} dir
  dir=$(release_dir "$id")
  rm -f "$dir/verified.json"  # a pass from an earlier run must not outlive a failed one
  (cd "$dir" && sha256sum --quiet -c SHA256SUMS) || die "$dir changed since build"
  local_env
  compose_local "$id" up -d --force-recreate --wait --wait-timeout 240 || { compose_local "$id" logs --tail 60; die "local start failed"; }
  "$PY" -X utf8 deploy/local/check_release.py "$dir" ${query:+--query}
  echo "verified: $dir/verified.json (containers keep running: deploy/release.sh down)"
}

ship() {
  local id=$1 dir
  dir=$(release_dir "$id")
  [[ "$id" != *-dirty-* ]] || die "$id holds uncommitted code: commit, build and verify again"
  [ -f "$dir/verified.json" ] || die "$id was not verified (deploy/release.sh verify $id)"
  (cd "$dir" && sha256sum --quiet -c SHA256SUMS) || die "$dir changed since build"
  for s in "${SERVICES[@]}"; do
    local want got
    want=$(awk -v s="$s" '$1 == s {print $2}' "$dir/images.txt")
    got=$(image_id "$s" "$id")
    [ "$got" = "$want" ] || die "local model-scout-$s:$id is $got, the verified image was $want"
    json_get "$dir/verified.json" images "$s" | grep -qx "$want" || die "verified.json names another $s image"
  done
  ssh "$HOST" "docker compose version && mkdir -p $REMOTE/staging && rm -rf $REMOTE/staging/$id" </dev/null
  # Images by ID: docker save/load keeps it, and install checks it against images.txt.
  docker save "model-scout-ai:$id" "model-scout-backend:$id" | gzip -1 | ssh "$HOST" 'gunzip | docker load'
  # Into staging first; install checks every hash before the folder becomes releases/<id>.
  tar -C "$dir" --exclude=verified.json -cf - . | ssh "$HOST" "mkdir -p $REMOTE/staging/$id && tar -x -C $REMOTE/staging/$id"
  ssh "$HOST" "bash -s -- install $id" < "$dir/server_release.sh"
  ssh "$HOST" "bash -s -- activate $id" < "$dir/server_release.sh"
  echo "shipped $id. Check: deploy/release.sh status, deploy/inspect_server.sh"
}

remote() { tr -d '\r' < deploy/server_release.sh | ssh "$HOST" "bash -s -- $*"; }  # LF: a Windows checkout has CRLF

case "${1:-}" in
  build) build ;;
  verify) [ -n "${2:-}" ] || die "verify <id>"; verify "$2" "$([ "${3:-}" = --query ] && echo 1)" ;;
  down) RELEASE_DIR=. MODEL_SCOUT_RELEASE=none docker compose -f deploy/compose.local.yml down -v ;;  # -v: the local postgres too
  ship) [ -n "${2:-}" ] || die "ship <id>"; ship "$2" ;;
  rollback) [ -n "${2:-}" ] || die "rollback <id|legacy>"; remote rollback "$2" ;;
  status) remote status ;;
  *) sed -n '2,20p' "$0"; exit 1 ;;
esac
