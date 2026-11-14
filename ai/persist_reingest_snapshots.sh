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

git pull --rebase origin main

# main은 저장소 ruleset에 의해 직접 push가 금지되어 있다. 실행별 전용
# 브랜치로 올리고 사람이 PR을 검토·병합하게 한다.
snapshot_branch="automation/reingest-snapshot-${workflow_run_id}"
git switch -C "$snapshot_branch"
git push --set-upstream origin "HEAD:refs/heads/${snapshot_branch}"

repository="${GITHUB_REPOSITORY:-Model-Scout/Model_Scout}"
compare_url="https://github.com/${repository}/compare/main...${snapshot_branch}?expand=1"
echo "snapshot branch pushed: ${snapshot_branch}"
echo "create and merge the snapshot PR: ${compare_url}"
if test -n "${GITHUB_STEP_SUMMARY:-}"; then
  {
    echo "## Snapshot PR required"
    echo
    echo "DB apply는 이미 완료됐다. 아래 브랜치의 스냅샷 PR만 검토·병합한다."
    echo
    echo "- Branch: \`${snapshot_branch}\`"
    echo "- Approved dry-run: \`${approved_run_id}\`"
    echo "- [Create snapshot PR](${compare_url})"
  } >> "$GITHUB_STEP_SUMMARY"
fi
