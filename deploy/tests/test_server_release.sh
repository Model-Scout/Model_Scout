#!/usr/bin/env bash
# deploy/server_release.sh against a fake docker in a temporary ROOT (no server, no containers):
# install checks hashes and image IDs, activate records CURRENT, a failed activation falls back to the
# previous release, rollback restores an earlier one.   bash deploy/tests/test_server_release.sh
set -euo pipefail
here=$(cd "$(dirname "$0")/.." && pwd)
work=$(mktemp -d)
trap 'rm -rf "$work"' EXIT
export MODEL_SCOUT_ROOT="$work/root" FAKE="$work/fake"
mkdir -p "$MODEL_SCOUT_ROOT/staging" "$FAKE" "$work/bin"
for f in .env.ai .env.backend docs_users; do echo secret > "$MODEL_SCOUT_ROOT/$f"; done
printf 'services: {}\n' > "$MODEL_SCOUT_ROOT/compose.yml"  # the pre-release ("legacy") layout

# Fake docker: images in $FAKE/images ("<ref> <id>"), the folder last brought up in $FAKE/up,
# a release folder listed in $FAKE/broken fails to come up.
cat > "$work/bin/docker" <<'EOF'
#!/usr/bin/env bash
args=" $* "
dir=$(sed -n 's/.*--project-directory \([^ ]*\).*/\1/p' <<<"$args")
case "$args" in
  *" compose up --help "*) echo "      --wait-timeout int" ;;
  *" image inspect "*) ref=${!#}; awk -v r="$ref" '$1 == r {print $2; f=1} END {exit !f}' "$FAKE/images" ;;
  *" compose "*" up "*) grep -qxF "$dir" "$FAKE/broken" 2>/dev/null && exit 1; echo "$dir" > "$FAKE/up" ;;
  *" compose "*" ps -q "*) svc=${!#}; echo "cid-$svc" ;;
  *" compose "*" exec "*|*" compose "*" logs "*) exit 0 ;;
  *" inspect -f {{.Image}} "*) svc=${!##cid-}; tag=$(basename "$(cat "$FAKE/up")")
     awk -v r="model-scout-$svc:$tag" '$1 == r {print $2}' "$FAKE/images" ;;
  *" inspect -f {{.State.Health.Status}}"*) echo "healthy restarts=0" ;;
  *) echo "fake docker: unhandled:$args" >&2; exit 2 ;;
esac
EOF
chmod +x "$work/bin/docker"
export PATH="$work/bin:$PATH"

A=20261119T010000Z-aaaaaaaa-aa1a71d3 B=20261119T020000Z-bbbbbbbb-aa1a71d3
stage() {  # stage <id>: a minimal release folder plus its loaded images
  local d="$MODEL_SCOUT_ROOT/staging/$1"
  mkdir -p "$d/data"
  printf 'services: {}\n' > "$d/compose.yml"
  echo "MODEL_SCOUT_DATA_VERSION=aa1a71d35a121150" > "$d/.env.corpus"
  echo "data $1" > "$d/data/file.txt"
  printf 'ai sha256:ai-%s\nbackend sha256:be-%s\n' "$1" "$1" > "$d/images.txt"
  printf 'model-scout-ai:%s sha256:ai-%s\nmodel-scout-backend:%s sha256:be-%s\n' "$1" "$1" "$1" "$1" >> "$FAKE/images"
  (cd "$d" && find . -type f ! -name SHA256SUMS | sort | sed 's|^\./||' | xargs sha256sum > SHA256SUMS)
}
run() { bash "$here/server_release.sh" "$@"; }
fail() { echo "FAIL: $*" >&2; exit 1; }

stage "$A"
echo tampered >> "$MODEL_SCOUT_ROOT/staging/$A/data/file.txt"
run install "$A" 2>/dev/null && fail "install accepted a changed file"
rm -rf "$MODEL_SCOUT_ROOT/staging/$A"; sed -i "/$A/d" "$FAKE/images"; stage "$A"
run install "$A" >/dev/null
[ -f "$MODEL_SCOUT_ROOT/releases/$A/.env.ai" ] || fail "release lacks its copy of the keys"
run install "$A" 2>/dev/null && fail "a second install overwrote releases/$A"

run activate "$A" >/dev/null
[ "$(cat "$MODEL_SCOUT_ROOT/CURRENT")" = "$A" ] || fail "CURRENT is not $A"

stage "$B"; run install "$B" >/dev/null
echo "$MODEL_SCOUT_ROOT/releases/$B" > "$FAKE/broken"
run activate "$B" >/dev/null 2>&1 && fail "a broken release was reported active"
[ "$(cat "$MODEL_SCOUT_ROOT/CURRENT")" = "$A" ] || fail "CURRENT moved off $A after a failed activation"
[ "$(cat "$FAKE/up")" = "$MODEL_SCOUT_ROOT/releases/$A" ] || fail "did not fall back to $A"

: > "$FAKE/broken"
run activate "$B" >/dev/null && [ "$(cat "$MODEL_SCOUT_ROOT/CURRENT")" = "$B" ] || fail "activate $B"
run rollback "$A" >/dev/null && [ "$(cat "$MODEL_SCOUT_ROOT/CURRENT")" = "$A" ] || fail "rollback to $A"
# A, the fall-back re-activation of A, B, the rollback to A.
[ "$(wc -l < "$MODEL_SCOUT_ROOT/HISTORY")" = 4 ] || fail "HISTORY should hold 4 activations"
run activate "bad id" 2>/dev/null && fail "accepted a malformed id"
echo "server_release.sh: all checks passed"
