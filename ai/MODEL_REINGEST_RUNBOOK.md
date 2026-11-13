# 모델 재적재 운영 절차

모델 데이터를 Hugging Face 에서 다시 만들어 Supabase 에 반영하는 절차다.
수치(행 수·날짜)는 금방 낡으므로 여기 적지 않는다. 실행할 때 dry-run 보고서에서 읽는다.

## 1. 파이프라인과 Supabase 의 관계

```
Stage 1   01_collect_models.py        Hub 후보 수집. A/B/C, Core/Low 분류
Stage 2   02_enrich_metadata.py       Hub API·카드·config·siblings 사실 수집 + 언어 게이트
Stage 2.5 contract/validate.py        데이터 계약 검증 (유료 단계 앞의 게이트)
Stage 3   03_generate_semantic_...    README 기반 의미·제약 (LLM, README 바뀐 것만)
Stage 3.5 06_extract_benchmark_...    벤치마크 (API 호출 없음)
Stage 4   04_build_embeddings.py      filter_metadata·embedding_text·embedding (hash 바뀐 것만)
sync      08_sync_supabase.py         Stage 4 결과를 Supabase 에 반영
```

Stage 2 로 가는 것은 A 후보 중 Core ∪ Low 뿐이다. Likely(B)·Fallback(C)은 후보
분포로만 보고된다. `05_validate_retrieval.py` 는 Stage 5 가 아니라 검색 검증 도구다.

## 2. Action 입력

`model-scout-reingest.yml` (수동 실행 전용, schedule 없음)

| mode | 하는 일 | DB |
|---|---|---|
| `validate` | 컴파일·계약 스키마·오프라인 테스트. 네트워크 호출 없음 | 안 읽음 |
| `dry-run` | Stage 1~4 생성, 보고서 artifact | **읽기만** (직전 sync 기록, active ID) |
| `apply` | dry-run 과 같은 생성 + 같은 트랜잭션에서 upsert·비활성화, 성공 후 스냅샷 커밋 | 씀 |

`apply` 는 `main` 에서 `confirm=APPLY` 일 때만 돈다.

| stage1_mode | Stage 1 | watermark | 비활성화 대상 |
|---|---|---|---|
| `reuse` (기본) | 저장소 파일 그대로 | 직전 값 유지 | 언어 게이트 제외분만 (DB 에만 있는 행은 보고만) |
| `full-scan` | Hub 에서 처음부터 수집 (`01 --no-resume`) | **Stage 1 스캔 시작 시각** | DB active − 새 Stage 4 전체 |

watermark 를 스캔 **완료** 시각으로 두지 않는다. 스캔은 몇 시간 걸리고, 그 사이 Hub 에서
바뀐 모델은 다음 `--refresh` 가 다시 봐야 한다.

## 3. 안전장치와 중단 기준

| 구간 | 가드 | 걸리면 |
|---|---|---|
| Stage 1 수집 | 01: 모든 task 성공, 파티션별 50% 이상 감소 금지 | 공개 Stage 1 그대로. 재적재 중단 |
| 기존 → 새 Stage 1 | 처리 대상(Core ∪ Low)에서 10% 초과 제거 금지. Core↔Low 이동은 제거로 세지 않는다 | Stage 1 백업 복원. Stage 2 전에 중단 |
| 새 Stage 1 → Stage 2 | 언어 게이트 제외(이번 Stage 1 에 있는 것만)를 뺀 기대치의 98% 미만이면 중단 | 유료 단계 전에 중단 |
| Stage 2 → Stage 4 | `validate_corpus` 가 ID 집합 일치를 요구 | 적재 전 중단 |
| 비활성화 | DB active 의 10% 초과 비활성화 금지 | dry-run: 보고서 남기고 실패(종료 코드 3). apply: 트랜잭션 롤백, 스냅샷 커밋 없음 |

10% 는 정상 감소(Hub 삭제·비공개·다운로드 80 미만·언어 제외)를 넉넉히 덮고, 부분 수집 실패는
막는 값이다. 정상인데도 넘는다면 실행 옵션으로 우회하지 말고 `08_sync_supabase.py` 의 상수를
PR 로 바꾼다.

## 4. 보고서

dry-run 과 apply 모두 artifact 로 올린다.

- `reingest-report.json` — 전체 결과. `reingest.stage1_diff`, `deactivation.candidate_ids` 에 ID 전체 목록
- `reingest-report.summary.json` — 개수만. Step Summary 에 그대로 붙는다
- `reingest-report.stage1-diff.json` — 추가·제거·Core↔Low 이동, A/B/C 분포 (full-scan 만)
- `reingest-report.deactivation.json` — DB active, DB 에만 있는 ID, 비활성화 후보, 가드 판정
- `contract/baseline.md`, `data/hf_models_stage4_manifest.json`

Stage 1~4 전체 스냅샷은 용량이 커서 artifact 로 올리지 않는다. 필요하면 별도 입력으로 켜는
후속 작업으로 한다.

## 5. SQL migration, Action, 기능 플래그

세 가지는 서로 다른 것을 바꾼다. 순서가 어긋나면 검색이 깨진다.

| 무엇 | 바꾸는 것 | 누가 |
|---|---|---|
| `supabase_migration_contract_filters.sql` | RPC `match_model_scout_models` 를 15개 → 19개 인자로 교체 | Supabase SQL Editor 에서 사람이 1회 |
| 재적재 Action | 모델 행의 데이터(`filter_metadata.commercial_status` 등) | Action apply |
| `MODEL_CONTRACT_FILTERS_ENABLED` | 09 가 19개 인자로 부를지 | 서버 `.env` (deploy.sh 가 `.env.ai` 로 넘긴다) |

플래그 기본값은 OFF 다. OFF 면 09 는 예전 15개 인자로 부르고, 17 은 예전처럼 Top-N 뒤에
라이선스로 거른다. migration 전에 켜면 19개 인자 함수가 없어 검색이 실패한다. 이 실패는
삼키지 않고 그대로 드러낸다. 재적재 전에 켜면 계약 필드가 없는 행이 조건 검색에서 전부 빠진다.

검색 순위는 이번에 바꾸지 않는다(Dense/Sparse 0.65/0.35 유지). 다만 `search_tsv` 가
`filter_metadata::text` 전체를 색인한다(가중치 C). 재적재 뒤에는 `permitted`, `gguf`,
`bfloat16` 같은 계약 값이 sparse 점수에 섞일 수 있다. full-scan dry-run 뒤 대표 질의의
before/after 와 골든셋으로 판단한다.

## 6. 하이퍼그래프와 모델 테이블

하이퍼그래프(`13_build_hypergraph.py` → `data/hypergraph/`)는 모델·데이터셋을 taxonomy 개념에
연결한 그래프다. 추천 그래프(17)는 Supabase 에서 찾은 모델로 이 그래프에서 데이터셋을 찾는다.
그래프에 없는 모델은 "관련 데이터셋 없음"이 되므로, 그래프의 모델 집합이 Supabase active 행과
같아야 한다.

| `--model-source` | 동작 |
|---|---|
| `auto` (기본, 로컬 개발) | Stage 4 두 파일이 실제 JSONL 이면 로컬, 아니면 Supabase |
| `local` | 실제 JSONL 이 아니면(없음·빈 파일·LFS pointer·손상) 실패 |
| `supabase` | 로컬 파일을 보지 않고 Supabase active 행 |

Stage 4 파일은 Git LFS 라서 LFS 없이 checkout 하면 pointer 파일만 있다. 운영 `dataset-refresh.yml` 은
full·rebuild 두 경로 모두 `--model-source supabase` 다. 사용한 원본·모델 수·정렬된 모델 ID 의 sha256
은 `data/hypergraph/report.json` 의 `models`(v2 는 `build_manifest.json` 의 counts)와 Step Summary 에
남는다. 같은 실행에서 읽은 ID 가 기준이므로 다른 시점의 로컬 수치와 비교하지 않는다.

공공데이터 v2 전환은 이 절차에 포함되지 않는다. 기본 corpus 는 v1 이고 `20_sync_dataset_index.py` 도
v1 만 다룬다.

## 7. 운영 순서

1. 재적재 Action 을 GitHub UI 에서 잠시 활성화한다. schedule 은 건드리지 않는다.
2. `mode=validate` 를 실행한다.
3. `mode=dry-run`, `stage1_mode=full-scan` 을 실행한다.
4. 보고서를 검토한다. 추가·제거 ID, Core↔Low 이동, 언어 제외, Stage 4 행 수, 비활성화 후보를 본다.
5. 다음 단계로 넘어가기 전에 중단 기준을 확인한다. 하나라도 해당하면 멈춘다.
   - 가드가 걸렸다.
   - 제거·비활성화 후보에 운영상 중요한 모델이 있다.
   - Stage 4 행 수가 예상과 크게 다르다.
6. Supabase SQL Editor 에서 `supabase_migration_contract_filters.sql` 을 적용한다. 플래그가 OFF 라
   서비스는 아직 15개 인자로 부른다. 구 시그니처는 migration 이 지우지만, 새 함수의 뒤 4개 인자는
   기본값이 있어 15개 인자 호출도 그대로 동작한다.
7. `mode=apply`, `stage1_mode=full-scan`, `confirm=APPLY` 를 main 에서 실행한다.
8. DB 를 사후 검증한다.
   - 최신 `model_scout_sync_runs` 행이 `completed` 이고 `sync_mode=reingest`, `stage1_mode=full-scan` 인지 본다.
   - `source_watermark` 가 보고서의 `source_watermark` 와 같은지 본다.
   - active 행 수가 `stage4_rows` 와 같은지 본다.
9. Dataset refresh Action 을 잠시 활성화하고 `mode=rebuild` 로 한 번 실행한다. Step Summary 의
   active 모델 수, model entity 수, `model_ids_sha256` 를 확인한다. 모델 수가 8단계 active 행 수와
   같아야 한다.
10. 9단계가 커밋한 그래프를 `git pull` 로 받는다. 배포에 쓰는 `.env` 에
    `MODEL_CONTRACT_FILTERS_ENABLED=true` 를 넣고 `deploy/deploy.sh` 로 재배포한다. 하이퍼그래프
    데이터도 이때 같이 올라간다.
11. 서비스 smoke test 를 한다.
    - 일반 질의를 확인한다.
    - "상업용 + GGUF + 승인 없이" 질의를 확인한다. 카드의 `상업 이용`, `GGUF 파일`, `승인 없이 내려받기` check 를 본다.
12. 두 Action(재적재, Dataset refresh)을 다시 비활성화한다.

## 8. 되돌리기

- dry-run 은 DB 와 저장소를 바꾸지 않는다. 버리면 끝이다.
- 플래그를 켠 뒤 검색이 이상하면 `MODEL_CONTRACT_FILTERS_ENABLED` 를 지우고 재배포한다. 데이터와
  migration 은 그대로 두어도 예전 동작(15개 인자 + 후처리)으로 돌아간다.
- apply 가 실패하면 트랜잭션이 롤백되고 스냅샷 커밋 단계는 돌지 않는다.
- apply 는 성공했는데 스냅샷 push 가 세 번 다 실패하면 Action 이 실패로 끝난다. DB 는 이미 반영됐으므로
  다시 apply 하지 말고, 그 run 의 스냅샷 커밋을 수동으로 올린다.
- apply 가 성공했는데 결과가 잘못됐다면 이렇게 되돌린다.
  - 비활성화된 행은 지워지지 않는다(`active=false`, `stale_at`). 보고서의 `deactivation.candidate_ids` 로 `active=true` 를 되돌릴 수 있다.
  - 스냅샷 커밋은 `git revert` 로 되돌린다.
  - 다음 `--refresh` 의 watermark 는 가장 최근 completed run 의 `source_watermark` 다. 필요하면 그 run 을 `failed` 로 바꿔 이전 watermark 로 돌린다.
