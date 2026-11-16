#!/usr/bin/env bash
# Read-only look at what the server runs: corpus, data versions, code, memory. Writes nothing; prints no secrets.
#   ssh-add ~/.ssh/iwinv_model_scout
#   deploy/inspect_server.sh > server_state.txt
set -euo pipefail
HOST="${DEPLOY_HOST:-model-scout}"
REMOTE=/opt/model-scout

ssh "$HOST" "REMOTE=$REMOTE bash -s" <<'EOF'
cd "$REMOTE"
echo "== .env.corpus"; cat .env.corpus 2>/dev/null || echo "(none: v1 default)"
echo "== env files (key names only)"; for f in .env.ai .env.backend; do echo "$f: $(cut -d= -f1 "$f" 2>/dev/null | tr '\n' ' ')"; done
echo "== containers"; docker compose ps --format '{{.Service}} {{.State}} {{.Status}} {{.Image}}'
echo "== images"; docker image inspect model-scout-ai:latest model-scout-backend:latest --format '{{.RepoTags}} {{.Id}} created {{.Created}}'
echo "== ai container corpus env"; docker compose exec -T ai env </dev/null | grep -E '^MODEL_SCOUT_' || echo "(no MODEL_SCOUT_* set)"
echo "== data files (sha256)"
for f in data/dataset_index/manifest.json data/dataset_index/embeddings.npy data/hypergraph/build_manifest.json \
         data/hypergraph_v2/build_manifest.json data/dataset_index_v2/build_manifest.json data/dataset_index_v2/manifest.json \
         data/dataset_index_v2/embeddings.npy data/dataset_index_v2/data_version.json; do
  if [ -f "$f" ]; then echo "$(sha256sum "$f" | cut -c1-16) $(stat -c '%s %y' "$f") $f"; else echo "missing $f"; fi
done
echo "== recorded ids"
docker compose exec -T ai python - <<'PY'
import json, pathlib
d = pathlib.Path("/app/ai/data")
def ids(p, *keys):
    try:
        j = json.loads((d / p).read_text(encoding="utf-8"))
    except Exception as e:
        return f"{p}: {type(e).__name__}"
    out = {}
    for k in keys:
        v = j
        for part in k.split("."):
            v = v.get(part) if isinstance(v, dict) else None
        out[k] = str(v)[:16] if v else v
    return f"{p}: {out}"
print(ids("hypergraph_v2/build_manifest.json", "stage_id"))
print(ids("dataset_index_v2/build_manifest.json", "stage_id"))
print(ids("dataset_index_v2/manifest.json", "documents_id", "model", "embedding_run.vectors_sha256"))
print(ids("dataset_index_v2/data_version.json", "data_version", "chunk_ids_sha256"))
print(ids("dataset_index/manifest.json", "model"))
PY
echo "== code in the ai image (sha256 of key files)"
docker compose exec -T ai sh -c 'cd /app/ai && sha256sum hypergraph_search.py 17_recommend_graph.py api.py 2>/dev/null | cut -c1-16,65-' </dev/null
echo "== which corpus the running process reports"
docker compose exec -T -w /app/ai ai python -c "import hypergraph_search as h; print('CORPUS', getattr(h, 'CORPUS', 'v1 (pre-v2 code, no CORPUS setting)'))" </dev/null 2>&1 | tail -1
echo "== memory"; docker stats --no-stream --format '{{.Name}} {{.MemUsage}} {{.MemPerc}}'
echo "== recent ai log lines mentioning corpus"; docker compose logs --tail 300 ai 2>&1 | grep -iE 'corpus|data_version|CorpusMismatch' | tail -10 || true
EOF
