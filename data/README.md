# 데이터 산출물

이 디렉터리는 Hugging Face 모델을 Stage 1~4 검색 corpus로 변환한 snapshot을 보관합니다. 수량은 2026-09-28 기준입니다.

## 현재 snapshot

| 단계 | 파일 또는 디렉터리 | 행/수량 | 설명 |
|---|---|---:|---|
| Stage 1 | `hf_models_stage1_core.jsonl` | 1,478 | `A_verified`, downloads ≥ 500 |
| Stage 1 | `hf_models_stage1_low_popularity.jsonl` | 2,128 | `A_verified`, downloads 80~499 |
| Stage 1 | `hf_models_stage1_likely.jsonl` | 2,100 | `B_likely`, 참고 후보 |
| Stage 1 | `hf_models_stage1_fallback.jsonl` | 14,244 | `C_fallback`, 참고 후보 |
| Stage 1 | `hf_models_stage1_groups.jsonl` | 8,552 | canonical/base-model과 variant grouping |
| Stage 1 | `hf_models_stage1_state.json` | 1 | 수집 설정, task 통계, watermark |
| Stage 2 | `hf_models_stage2_core.jsonl` | 1,478 | 기술 metadata |
| Stage 2 | `hf_models_stage2_low_popularity.jsonl` | 2,128 | 기술 metadata |
| Stage 2 | `readmes/core/` | 1,474 | Core README snapshot |
| Stage 2 | `readmes/low_popularity/` | 2,122 | Low Popularity README snapshot |
| Stage 3 | `hf_models_stage3_core.jsonl` | 1,478 | semantic summary와 claim 근거 |
| Stage 3 | `hf_models_stage3_low_popularity.jsonl` | 2,128 | semantic summary와 claim 근거 |
| Stage 3 | `hf_models_stage3_parent_child_core.jsonl` | 1,478 | Core evidence index |
| Stage 3 | `hf_models_stage3_parent_child_low_popularity.jsonl` | 2,128 | Low Popularity evidence index |
| Stage 3 | `hf_models_stage3_parent_child_manifest.json` | 1 | evidence index 검증 결과 |
| Stage 4 | `hf_models_stage4_core.jsonl` | 1,478 | 1,536차원 임베딩 문서 |
| Stage 4 | `hf_models_stage4_low_popularity.jsonl` | 2,128 | 1,536차원 임베딩 문서 |
| Stage 4 | `hf_models_stage4_manifest.json` | 1 | embedding model과 dimension |

운영 추천 corpus는 Core와 Low Popularity를 합친 3,606개입니다. 두 pool 사이의 model ID 중복은 없어야 하며, Stage 4 임베딩은 모두 1,536차원이어야 합니다.

## Stage 1

수집 대상 task는 다음 9개입니다.

`text-generation`, `feature-extraction`, `sentence-similarity`, `text-classification`, `question-answering`, `summarization`, `translation`, `image-text-to-text`, `automatic-speech-recognition`

주요 설정은 `MIN_DOWNLOADS=80`, `CORE_DOWNLOADS=500`, `LIMIT_PER_TASK=None`, `CUTOFF_CONFIRMATION=10`입니다. API 빈 응답이나 task 실패가 있으면 snapshot을 publish하지 않고 이전 상태를 유지합니다. 후보에서 탈락한 모델은 증분 sync에서 DB `active=false`로 비활성화합니다.

## Stage 2

config, tokenizer config, artifact index와 README에서 task, language, architecture, artifact, license, base model, parameter count, context length, quantization, model format, runtime compatibility를 추출합니다. 값이 확인되지 않으면 `null` 또는 `unknown`으로 유지하고, source와 confidence를 함께 기록합니다.

README snapshot은 Core 1,474개와 Low Popularity 2,122개입니다. 원본 snapshot에서 잘림이 남은 모델은 Core 7개, Low Popularity 12개입니다. 긴 README 보강은 Core 41개와 Low Popularity 84개에 수행했습니다. README가 없는 모델은 Core 4개, Low Popularity 6개이며 metadata-only로 유지합니다.

## Stage 3

`hf_models_stage3_*.jsonl`은 README 기반 semantic summary, strengths, limitations, use cases와 claim별 evidence를 담습니다. 각 claim은 evidence reference와 supporting quote를 가리킵니다.

`evidence_index.py`가 LLM 호출 없이 Parent section과 Child claim 관계를 생성합니다.

- Core: parent 8,890개, child 15,767개
- Low Popularity: parent 10,912개, child 19,371개
- 전체: parent 19,802개, child 35,138개

Parent–Child sidecar는 Supabase `model_scout_evidence`에 backfill할 수 있으며, 모델 검색 행과 분리해 저장됩니다.

## Stage 4

Stage 3의 identity, task, language, 기술 metadata, runtime, popularity, semantic claims와 benchmark projection을 합쳐 `embedding_text`를 만듭니다. 기본 실행은 dry-run이고 `--execute`에서만 OpenAI 임베딩 API를 호출합니다. 증분 sync에서는 변경된 ID만 임베딩하며, DB에 같은 `document_hash`가 있으면 기존 vector를 재사용합니다.

운영 검색 vector는 Supabase pgvector에 저장합니다. JSONL snapshot은 재현성과 복구를 위해 보관합니다.

## Benchmark sidecar

`hf_models_benchmark_core.jsonl`과 `hf_models_benchmark_low_popularity.jsonl`은 README/model-index에서 추출한 재생성 가능한 sidecar입니다. 숫자가 없는 benchmark 이름은 `mentions`로만 보존하고, 모델명·점수 연결이 불명확하거나 dataset/metric/split/config가 다르면 ranking에 사용하지 않습니다.

현재 추출 통계:

| pool | README | numeric results | ranking eligible | mentions only | variant ambiguous |
|---|---:|---:|---:|---:|---:|
| Core | 1,474 | 32,376 | 23,479 | 884 | 8,897 |
| Low Popularity | 2,122 | 117,172 | 56,107 | 1,066 | 61,065 |

benchmark sidecar와 `.hf_models_benchmark_state_*` 파일은 TTL 실행에서 변경 모델을 판별하는 데 사용합니다. 성공한 sync 뒤의 delta와 임시 ID queue는 자동 정리 대상이지만, state와 canonical sidecar를 삭제하면 다음 증분 실행이 전체 재검사로 돌아갈 수 있습니다.

## Supabase 적재

```bash
source ~/main/bin/activate
python 08_sync_supabase.py --ensure-schema
python 08_sync_supabase.py --initial --apply
MODEL_SCOUT_TTL_HOURS=24 python 08_sync_supabase.py --refresh --apply
```

필요할 때만 다음 backfill을 실행합니다.

```bash
python 08_sync_supabase.py --backfill-runtime --apply
python 08_sync_supabase.py --backfill-search-metadata --apply
python 08_sync_supabase.py --backfill-evidence --apply
```

`model_scout_models`에는 3,606개 모델의 검색 metadata와 vector가, `model_scout_evidence`에는 Parent–Child 근거가, `model_scout_sync_runs`에는 실행 이력이 저장됩니다.

## 보존·정리 원칙

- Stage 1~4 JSONL과 manifest는 snapshot lineage와 복구를 위해 보관합니다.
- `graphify-out/`와 `.DS_Store`는 버전 관리하지 않습니다.
- `.stage1*_checkpoint/`, benchmark delta, incremental ID queue는 중간 산출물이며 성공한 sync 뒤 정리할 수 있습니다.
- benchmark state와 canonical sidecar는 TTL 변경 감지에 필요하므로 삭제하지 않습니다.
