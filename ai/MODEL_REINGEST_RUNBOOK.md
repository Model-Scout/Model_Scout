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
| `dry-run` | Stage 1~4 생성, 보고서 artifact, **승인용 번들 artifact**(`reingest-bundle-<run_id>`) | **읽기만** (직전 sync 기록, active ID, 용량) |
| `apply` | 승인한 dry-run 번들을 받아 검증 → 그대로 놓고 같은 트랜잭션에서 upsert·비활성화, 성공 후 스냅샷 커밋. **Stage 1~4 를 다시 만들지 않는다** | 씀 |

`apply` 는 `main` 에서 `confirm=APPLY` 와 `approved_run_id`(승인한 dry-run 의 run ID)가 있을 때만 돈다.
apply 에는 HF·OpenAI 키를 주지 않는다.

apply 는 번들 manifest 를 검증하고, 하나라도 다르면 DB 에 쓰기 전에 멈춘다.

| 검증 | 실패하면 |
|---|---|
| 같은 저장소, `main` 에서 만든 dry-run, `approved_run_id` 와 같은 run | 다른 산출물이다 |
| dry-run 의 커밋 SHA = 지금 main SHA | dry-run 이후 main 이 바뀌었다. **dry-run 을 다시 한다** |
| Stage 버전 | 코드와 산출물이 다르다 |
| 모든 파일의 SHA256·크기, 누락·manifest 에 없는 파일 | 번들이 손상·변조됐다 |
| 정렬한 Stage 4 모델 ID 의 sha256 | 적재할 모델 집합이 승인한 것과 다르다 |
| dry-run 때 읽은 Supabase 최신 sync run = 지금 최신 sync run | 그 사이 다른 sync 가 DB 를 바꿨다 |

번들 artifact 는 14일 보관한다. 그 안에 apply 하지 못하면 dry-run 을 다시 한다. DB 의 sync 기록
(`stage_versions`)에 `approved_dry_run_id`, `bundle_sha256`, `model_ids_sha256` 이 남는다.

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
| Stage 2 재사용 | 저장된 행의 Hub revision(SHA, 없으면 last_modified)이 지금 Stage 1 과 같을 때만 재사용 | 다르거나 기록이 없으면 다시 수집 |
| 계약 게이트 (재적재·증분 모두) | Stage 2 직후, Stage 3(LLM) 전. 직전 계약 레코드를 baseline 으로 값 손실·근거 하락 비교 | 같은 revision 에서 손실이면 중단. revision 이 바뀐 모델은 경고, 새 모델·첫 실행은 비교 생략(사유를 보고서에 기록) |
| Stage 2 → Stage 4 | `validate_corpus` 가 ID 집합 일치를 요구 | 적재 전 중단 |
| 비활성화 | DB active 의 10% 초과 비활성화 금지 | dry-run: 보고서 남기고 실패(종료 코드 3). apply: 트랜잭션 롤백, 스냅샷 커밋 없음 |
| DB 용량 | 지금 DB 크기 + 이번에 쓸 양 > `SUPABASE_DB_BUDGET_MB`(480) 이면 금지 | dry-run: 종료 코드 3. apply: DB 에 쓰기 전에 중단 |

DB 용량 가드가 있는 이유: 모델 테이블과 데이터셋 테이블(`20_sync_dataset_index.py`)이 같은 Supabase
무료 DB 를 쓴다. 500MB 를 넘으면 프로젝트가 읽기 전용이 돼 둘 다 멈춘다. 재적재는 모든 행을 다시 써서
옛 행이 VACUUM 전까지 남으므로 최고치를 "지금 + 쓸 양"으로 본다. 쓸 양은 지금 모델·evidence 테이블
크기(실측, 인덱스 포함) 한 벌에 새 계약 레코드(압축 전 길이)를 더한 값이다. 유료 플랜으로 바꾸면
workflow 의 `SUPABASE_DB_BUDGET_MB` 를 올린다.

이 판정은 dry-run 끝에 나온다. 몇 시간짜리 dry-run 전에 SQL Editor 에서 미리 본다.

```sql
select pg_size_pretty(pg_database_size(current_database())) as database,
       pg_size_pretty(pg_total_relation_size('public.model_scout_models')
                    + pg_total_relation_size('public.model_scout_evidence')) as models_and_evidence;
```

`database + models_and_evidence + 약 35MB(계약)` 가 480MB 아래여야 한다.

10% 는 정상 감소(Hub 삭제·비공개·다운로드 80 미만·언어 제외)를 넉넉히 덮고, 부분 수집 실패는
막는 값이다. 정상인데도 넘는다면 실행 옵션으로 우회하지 말고 `08_sync_supabase.py` 의 상수를
PR 로 바꾼다.

## 4. 보고서

dry-run 과 apply 모두 artifact 로 올린다.

- `reingest-report.json` — 전체 결과. `reingest.stage1_diff`, `deactivation.candidate_ids` 에 ID 전체 목록
- `reingest-report.summary.json` — 개수만. Step Summary 에 그대로 붙는다
- `reingest-report.stage1-diff.json` — 추가·제거·Core↔Low 이동, A/B/C 분포 (full-scan 만)
- `reingest-report.deactivation.json` — DB active, DB 에만 있는 ID, 비활성화 후보, 가드 판정
- `capacity`(보고서·summary 안) — DB 전체·테이블별 MB, 이번 쓰기 추정, 예상 최고치, 한도
- `reingest-coverage-before.md` / `-after.md` (Stage 2 기준 질문별 답변 가능률), `data/hf_models_stage4_manifest.json`

Stage 1~4 전체 산출물은 승인용 `reingest-bundle-<run_id>` artifact 에 포함하며 14일간
보관한다. 별도의 `reingest-report-*` artifact 에는 검토용 보고서와 coverage 를 30일간
보관한다. Stage 4 JSONL 은 apply 뒤 Git 스냅샷 커밋에는 포함하지 않는다.

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

## 7. 골든셋 v2 스냅샷

골든셋 v2 의 `eligible_count` 와 정답 후보는 2026-10-31 Supabase active 동결본에 백필을 덧씌운
`test/golden/v2/corpus_snapshot.jsonl`(약 121MB, gitignore 대상)에 묶여 있다. 이 파일은 재적재의
입력도 기준도 아니고 GitHub runner 에도 없다. 그래서 재적재 Action 은
`verify.py --structure-only`(질의 형식·ID 중복·유형별 개수·조건 키·조건 근거)만 돌린다.
coverage 도 저장소의 Stage 2 로만 재고, `contract/baseline.md` 를 덮어쓰지 않는다.

재적재가 끝나면 옛 스냅샷의 숫자는 더 이상 맞지 않는다. 새 Supabase active 코퍼스로
`python test/golden/v2/tools/dump_corpus.py` 를 실행해 스냅샷을 다시 뜨고, 전체 검증
`python test/golden/v2/tools/verify.py` 로 `eligible_count` 를 다시 확정한다. 이 파일을 Git 이나
LFS 에 올리지 않는다.

## 8. 운영 순서

1. 재적재 Action 을 GitHub UI 에서 잠시 활성화한다. schedule 은 건드리지 않는다.
2. `mode=validate` 를 실행한다.
3. `mode=dry-run`, `stage1_mode=full-scan` 을 실행한다.
4. 보고서를 검토한다. 추가·제거 ID, Core↔Low 이동, 언어 제외, Stage 4 행 수, 비활성화 후보,
   `capacity`(예상 최고치가 한도보다 충분히 낮은지)를 본다.
5. 다음 단계로 넘어가기 전에 중단 기준을 확인한다. 하나라도 해당하면 멈춘다.
   - 가드가 걸렸다.
   - 제거·비활성화 후보에 운영상 중요한 모델이 있다.
   - Stage 4 행 수가 예상과 크게 다르다.
6. Supabase SQL Editor 에서 `supabase_migration_contract_filters.sql` 을 적용한다. 플래그가 OFF 라
   서비스는 아직 15개 인자로 부른다. 구 시그니처는 migration 이 지우지만, 새 함수의 뒤 4개 인자는
   기본값이 있어 15개 인자 호출도 그대로 동작한다.
7. `mode=apply`, `approved_run_id=<3단계 run ID>`, `confirm=APPLY` 를 main 에서 실행한다. 3단계 이후
   main 에 다른 커밋이 들어갔다면 apply 가 거부하므로 3단계부터 다시 한다(6단계 SQL 은 커밋이 아니라 괜찮다).
8. DB 를 사후 검증한다.
   - 최신 `model_scout_sync_runs` 행이 `completed` 이고 `sync_mode=reingest`, `stage1_mode=full-scan` 인지 본다.
   - `source_watermark` 가 보고서의 `source_watermark` 와 같은지 본다.
   - active 행 수가 `stage4_rows` 와 같은지 본다.
   - SQL Editor 에서 `vacuum full public.model_scout_models; vacuum full public.model_scout_evidence;` 로
     옛 행 공간을 돌려받고 `select pg_size_pretty(pg_database_size(current_database()));` 로 크기를 본다.
     실행 중에는 테이블이 잠기므로 사용자가 적은 시간에 한다.
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
13. 골든셋 v2 스냅샷을 새 코퍼스로 다시 뜨고 eligible 수를 다시 확정한다(7절).

## 9. 되돌리기

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
