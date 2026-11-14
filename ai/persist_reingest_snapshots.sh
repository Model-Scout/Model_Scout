#!/usr/bin/env bash
set -euo pipefail

approved_run_id="${1:?approved dry-run ID is required}"
workflow_run_id="${2:?workflow run ID is required}"

git config user.name "model-scout-sync[bot]"
git config user.email "model-scout-sync[bot]@users.noreply.github.com"

git add \
  data/hf_models_stage1_core.jsonl \
  data/hf_models_stage1_low_popularity.jsonl \
  data/hf_models_stage1_likely.jsonl \
  data/hf_models_stage1_fallback.jsonl \
  data/hf_models_stage1_groups.jsonl \
  data/hf_models_stage1_state.json \
  data/hf_models_stage2_core.jsonl \
  data/hf_models_stage2_low_popularity.jsonl \
  data/hf_models_stage2_contract_core.jsonl \
  data/hf_models_stage2_contract_low_popularity.jsonl \
  data/hf_models_stage3_core.jsonl \
  data/hf_models_stage3_low_popularity.jsonl \
  data/hf_models_stage3_parent_child_core.jsonl \
  data/hf_models_stage3_parent_child_low_popularity.jsonl \
  data/hf_models_stage4_manifest.json \
  data/readmes/core \
  data/readmes/low_popularity

if test -f data/hf_models_benchmark_state.json; then
  git add data/hf_models_benchmark_state.json
fi
if test -f data/hf_models_stage3_parent_child_manifest.json; then
  git add data/hf_models_stage3_parent_child_manifest.json
fi
for path in data/hf_models_stage2_*_language_excluded.json; do
  if test -f "$path"; then git add "$path"; fi
done

if git diff --cached --quiet; then
  echo "커밋할 스냅샷 변경 없음"
  exit 0
fi

git commit -m "chore: persist Model Scout reingest snapshot (run ${workflow_run_id}, approved dry-run ${approved_run_id})"

# Stage 4 JSONL과 일회성 후보 파일은 DB 적재에는 필요하지만 저장소 스냅샷에는
# 포함하지 않는다. 커밋 뒤에도 이 tracked 파일들이 수정된 채 남아 있으면
# `git pull --rebase`가 실행을 거부하므로, 임시 runner의 worktree만 정리한다.
git restore --worktree .
if ! git diff --quiet; then
  echo "스냅샷 커밋 뒤 tracked worktree 변경이 남아 있다" >&2
  git status --short >&2
  exit 1
fi

for attempt in 1 2 3; do
  if git pull --rebase && git push origin HEAD:main; then
    exit 0
  fi
  echo "snapshot push attempt ${attempt}/3 failed" >&2
  sleep 10
done

echo "snapshot push failed; DB apply를 다시 실행하지 말고 persist-snapshots 복구 모드를 사용한다" >&2
exit 1
