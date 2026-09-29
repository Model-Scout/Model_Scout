# 데이터 산출물

`data/`는 Hugging Face 후보를 Stage 1~4 검색 corpus로 변환한 snapshot을 보관합니다. 추천 검색에 사용하는 pool은 `core`와 `low_popularity`이며, `likely`와 `fallback`은 Stage 1 참고 후보입니다.

## 현재 snapshot

아래 수량은 2026-09-28 현재 snapshot 기준입니다.

| 단계 | 파일 또는 디렉터리 | 행 수 / 수량 | 설명 |
|---|---|---:|---|
| Stage 1 | `hf_models_stage1_core.jsonl` | 1,478 | `A_verified`, downloads ≥ 500 |
| Stage 1 | `hf_models_stage1_low_popularity.jsonl` | 2,128 | `A_verified`, downloads 80~499 |
| Stage 1 | `hf_models_stage1_likely.jsonl` | 2,100 | `B_likely`, downloads ≥ 80 |
| Stage 1 | `hf_models_stage1_fallback.jsonl` | 14,244 | `C_fallback`, downloads ≥ 80 |
| Stage 1 | `hf_models_stage1_groups.jsonl` | 8,552 | canonical/base-model과 variant grouping |
| Stage 1 | `hf_models_stage1_state.json` | 1 | config, task 통계, watermark |
| Stage 2 | `hf_models_stage2_core.jsonl` | 1,478 | 기술 metadata |
| Stage 2 | `hf_models_stage2_low_popularity.jsonl` | 2,128 | 기술 metadata |
| Stage 2 | `readmes/core/` | 1,474 | Core README snapshot |
| Stage 2 | `readmes/low_popularity/` | 2,122 | Low Popularity README snapshot |
| Stage 3 | `hf_models_stage3_core.jsonl` | 1,478 | semantic summary와 claim 근거 |
| Stage 3 | `hf_models_stage3_low_popularity.jsonl` | 2,128 | semantic summary와 claim 근거 |
| Stage 3 | `hf_models_stage3_parent_child_core.jsonl` | 1,478 | Core evidence index |
| Stage 3 | `hf_models_stage3_parent_child_low_popularity.jsonl` | 2,128 | Low Popularity evidence index |
| Stage 4 | `hf_models_stage4_core.jsonl` | 1,478 | 1,536차원 임베딩 문서 |
| Stage 4 | `hf_models_stage4_low_popularity.jsonl` | 2,128 | 1,536차원 임베딩 문서 |
| Stage 4 | `hf_models_stage4_manifest.json` | 1 | 버전, pool, embedding model/dimension |

현재 추천 corpus는 총 3,606개입니다. 각 pool은 model ID 중복이 없고 Core와 Low Popularity 사이에도 중복을 허용하지 않습니다.

## Stage 1

수집 대상은 다음 9개 pipeline tag입니다.

`text-generation`, `feature-extraction`, `sentence-similarity`, `text-classification`, `question-answering`, `summarization`, `translation`, `image-text-to-text`, `automatic-speech-recognition`

설정은 `MIN_DOWNLOADS=80`, `CORE_DOWNLOADS=500`, `LIMIT_PER_TASK=None`, `CUTOFF_CONFIRMATION=10`입니다. `A_verified`는 구조화된 한국어 metadata, 명시적 번역 pair, 보수적인 한국어 모델명 규칙으로 구성됩니다. 다국어 표기와 family heuristic은 한국어 지원을 확정하지 않으므로 Core/Low에 넣지 않습니다.

Stage 1은 API 빈 응답, cutoff 미확인, 급격한 snapshot 감소를 정상 완료로 처리하지 않습니다. 실패하면 이전 snapshot을 유지합니다. 체크포인트와 watermark는 다음 증분 수집의 기준입니다.

## Stage 2

Hub metadata, config, tokenizer config, artifact index, README를 사용해 다음 정보를 채웁니다.

- task, language, architecture, artifact, license, base model
- parameter count와 context length 및 각각의 source/confidence
- quantization, model format, runtime compatibility
- popularity와 Stage 1 candidate lineage

확인할 수 없는 값은 `null` 또는 `unknown`으로 남깁니다. `runtime_compatibility`는 CPU, CUDA, MPS, vLLM, ONNX, llama.cpp에 대해 문서·artifact에서 확인한 보조 신호이고, 실제 실행 성공을 의미하지 않습니다.

## Stage 3

`03_generate_semantic_metadata.py`가 README에서 atomic evidence를 만들고 semantic claim에 `evidence_refs`와 `supporting_quote`를 연결합니다. 긴 README는 별도 repair로 보강합니다.

현재 원본 README snapshot의 잘림은 Core 7개, Low Popularity 12개입니다. 긴 README 보강은 Core 41개와 Low 84개에 수행했고, Stage 3 semantic repair 대상은 현재 0개입니다. README가 없는 모델은 Core 4개와 Low 6개이며 `no_source` metadata-only 상태로 유지합니다.

`evidence_index.py`는 LLM을 다시 호출하지 않고 Parent section과 Child claim의 ID 관계를 생성합니다. 이 sidecar는 Supabase `model_scout_evidence`에도 적재할 수 있습니다.

## Stage 4

`04_build_embeddings.py`는 Stage 3의 identity, task, language, technical metadata, runtime, popularity, semantic claims, benchmark projection을 하나의 `embedding_text`로 구성합니다. 기본 embedding model은 `text-embedding-3-small`이고 dimension은 1,536입니다.

기본 실행은 dry-run이며 API 호출은 `--execute`에서만 발생합니다. 증분 sync에서는 변경된 model ID만 처리하고, DB에 같은 `document_hash`와 embedding이 있으면 재사용합니다. Stage 4 vector는 Supabase pgvector가 운영 검색 저장소이고, 로컬 JSONL은 snapshot/재현 용도로 보관합니다.

## Benchmark projection

`06_extract_benchmark_metadata.py`는 README와 `model-index`에서 benchmark 이름, dataset, metric, split, 점수, quote를 보수적으로 추출합니다. 모델명과 점수의 연결이 불명확한 variant는 ranking에서 제외하고 `mentions` 또는 ambiguity 정보로 보존합니다. architecture, parameter, context, quantization 표는 benchmark 점수로 분류하지 않습니다.

benchmark 상태와 변경 fingerprint는 증분 처리에 사용됩니다. 성공한 sync가 끝나면 일회성 delta 파일은 정리되며, 다음 변경 감지를 위해 작은 상태 파일만 남습니다.

## Supabase 적재

운영 적재 대상은 Core와 Low Popularity의 모델 row 및 Parent–Child evidence입니다. Likely, Fallback, 원본 README 파일, pilot과 평가 report는 DB 적재 대상이 아닙니다.

```bash
python 08_sync_supabase.py --ensure-schema
python 08_sync_supabase.py --initial --apply
MODEL_SCOUT_TTL_HOURS=24 python 08_sync_supabase.py --refresh --apply
```

최초 적재 뒤에는 전체 snapshot을 다시 올리지 않습니다. 변경 모델만 Stage 2~4를 통과해 upsert하고, 후보에서 탈락한 row는 `active=false`로 비활성화합니다.

## 보존 원칙

- Stage 1~4 JSONL은 버전과 lineage 확인을 위해 보관합니다.
- Stage 4 vector의 운영 검색은 Supabase를 사용합니다.
- `hf_models_stage3_parent_child_manifest.json`은 evidence sidecar의 개수와 검증 결과를 설명합니다.
- `.stage*`, benchmark delta, incremental ID queue와 같은 임시 파일은 성공한 sync 뒤 자동 정리 대상입니다.
