#!/usr/bin/env bash
# Runs on the VPS (deploy/release.sh sends it over ssh): install, switch and roll back releases.
#
#   server_release.sh install  <id>   staging/<id> -> check SHA256SUMS and image IDs -> releases/<id>
#   server_release.sh activate <id>   recreate the containers from releases/<id> (its data, settings, images),
#                                     check them, then record it in CURRENT; a failed check re-activates
#                                     the previous release (or the pre-release layout, "legacy")
#   server_release.sh rollback <id|legacy>   activate an earlier release: same checks
#   server_release.sh status
#
# Layout under ROOT (/opt/model-scout):
#   releases/<id>/  compose.yml Caddyfile .env (MODEL_SCOUT_RELEASE) .env.corpus data/ release.json
#                   images.txt SHA256SUMS, plus copies of the server's .env.ai .env.backend docs_users
#   CURRENT         the active release id; HISTORY  one line per activation
#   legacy          /opt/model-scout/{compose.yml,data,...} as deploy/deploy.sh left them (:latest images)
# A release folder is never changed after install, so rolling back restores its data, settings and images.
set -euo pipefail

ROOT="${MODEL_SCOUT_ROOT:-/opt/model-scout}"
PROJECT=model-scout
SERVICES=(ai backend)
SECRETS=(.env.ai .env.backend docs_users)

die() { echo "server_release: $*" >&2; exit 1; }
valid_id() { [[ "$1" =~ ^[0-9]{8}T[0-9]{6}Z-[0-9a-f]{8}(-dirty)?-[0-9a-f]{8}$ ]] || die "bad release id: $1"; }

expected_image() {  # images.txt: "<service> <image id>"
  awk -v s="$2" '$1 == s {print $2}' "$1/images.txt"
}

install() {
  local id=$1 stage="$ROOT/staging/$1" dest="$ROOT/releases/$1"
  [ -d "$stage" ] || die "no staging/$id"
  [ -e "$dest" ] && die "releases/$id already installed (a release is never overwritten)"
  (cd "$stage" && sha256sum --quiet -c SHA256SUMS) || die "staging/$id does not match its SHA256SUMS"
  for s in "${SERVICES[@]}"; do
    local want got
    want=$(expected_image "$stage" "$s")
    got=$(docker image inspect -f '{{.Id}}' "model-scout-$s:$id" 2>/dev/null) || die "image model-scout-$s:$id not loaded"
    [ -n "$want" ] && [ "$got" = "$want" ] || die "model-scout-$s:$id is $got, release.json expects $want"
  done
  # The release keeps its own copy of the server's keys and team login, so a rollback restores them too.
  (umask 077; for f in "${SECRETS[@]}"; do
     [ -s "$ROOT/$f" ] || die "missing $ROOT/$f"
     cp -p "$ROOT/$f" "$stage/$f"
   done)
  mkdir -p "$ROOT/releases"
  mv "$stage" "$dest"
  echo "installed releases/$id"
}

compose() {  # compose <dir> <args...>: always the same project, whichever folder holds the files
  local dir=$1; shift
  docker compose -p "$PROJECT" --project-directory "$dir" -f "$dir/compose.yml" "$@" </dev/null
}

check_running() {  # check_running <dir> <expected-from: images.txt dir or "legacy">
  local dir=$1 problems=0
  for s in "${SERVICES[@]}"; do
    local cid got want state
    cid=$(compose "$dir" ps -q "$s")
    [ -n "$cid" ] || { echo "  $s: not running"; problems=1; continue; }
    got=$(docker inspect -f '{{.Image}}' "$cid")
    state=$(docker inspect -f '{{.State.Health.Status}} restarts={{.RestartCount}}' "$cid")
    if [ "$2" != legacy ]; then
      want=$(expected_image "$dir" "$s")
      [ "$got" = "$want" ] || { echo "  $s: runs $got, release expects $want"; problems=1; }
    fi
    [[ "$state" == healthy* ]] || { echo "  $s: $state"; problems=1; }
    echo "  $s: ${got:7:12} $state"
  done
  if [ "$2" != legacy ]; then
    local version
    version=$(sed -n 's/^MODEL_SCOUT_DATA_VERSION=//p' "$dir/.env.corpus")
    compose "$dir" exec -T ai python -c "import os; assert os.environ['MODEL_SCOUT_DATA_VERSION'] == '$version'" \
      || { echo "  ai: does not serve data_version $version"; problems=1; }
  fi
  return $problems
}

activate() {
  local id=$1 dir previous
  if [ "$id" = legacy ]; then dir=$ROOT; else dir="$ROOT/releases/$id"; fi
  [ -f "$dir/compose.yml" ] || die "no compose.yml for $id"
  docker compose up --help 2>/dev/null | grep -q -- --wait-timeout || die "docker compose lacks up --wait-timeout (Compose v2.17+)"
  previous=$(cat "$ROOT/CURRENT" 2>/dev/null || echo legacy)
  echo "activate $id (previous: $previous)"
  # --wait returns once every healthcheck passes; the AI checks its data against Supabase at start.
  if compose "$dir" up -d --force-recreate --remove-orphans --wait --wait-timeout 180 && check_running "$dir" "$id"; then
    echo "$id" > "$ROOT/CURRENT.tmp" && mv "$ROOT/CURRENT.tmp" "$ROOT/CURRENT"
    echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) $id (from $previous)" >> "$ROOT/HISTORY"
    echo "active: $id"
    return 0
  fi
  echo "activation of $id failed" >&2
  compose "$dir" logs --tail 40 ai backend >&2 || true
  if [ "${NO_FALLBACK:-}" != 1 ] && [ "$previous" != "$id" ]; then
    echo "re-activating $previous" >&2
    NO_FALLBACK=1 activate "$previous" || echo "re-activation of $previous failed too: check the server" >&2
  fi
  return 1
}

status() {
  echo "current: $(cat "$ROOT/CURRENT" 2>/dev/null || echo 'legacy (no release activated yet)')"
  ls -1 "$ROOT/releases" 2>/dev/null | sed 's/^/  installed: /' || true
  docker ps --filter "label=com.docker.compose.project=$PROJECT" --format '  {{.Names}} {{.Image}} {{.Status}}'
}

cmd=${1:-}; id=${2:-}
case "$cmd" in
  install) valid_id "$id"; install "$id" ;;
  activate) valid_id "$id"; activate "$id" ;;
  rollback) [ "$id" = legacy ] || valid_id "$id"; activate "$id" ;;
  status) status ;;
  *) die "usage: server_release.sh install|activate|rollback <id> | status" ;;
esac
