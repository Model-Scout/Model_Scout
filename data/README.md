# Model Scout 데이터 파이프라인

이 디렉터리는 Hugging Face 모델을 수집하고, 한국어 근거를 분류하고, 기술 metadata와 근거 기반 semantic metadata를 결합해 추천 검색용 corpus로 만드는 결과를 보관한다.

## 전체 흐름

```text
Hugging Face Hub
  ↓
Stage 1. deterministic candidate collection
  ↓
Stage 2. fact-based technical metadata enrichment
  ↓
Stage 3. Atomic Evidence semantic enrichment
  ↓
Stage 4. embedding and retrieval index
```

현재 Stage 1~4 결과와 검색 후 상세 metadata hydrate가 완료되어 있다.

## Stage 1: Candidate Collection v7

Stage 1은 Hub metadata, model ID, structured language metadata와 deterministic rule만 사용한다. LLM이나 README 본문 해석은 사용하지 않는다.

### Candidate ontology

| Tier | Type | 의미 |
|---|---|---|
| `A_verified` | `korean_explicit` | structured language metadata에 normalized `ko`가 존재 |
| `A_verified` | `korean_translation_pair` | `ko-en`, `en-ko`, `ja-ko` 같은 명시적 번역 언어 pair |
| `A_verified` | `korean_name_strong` | KoELECTRA, KoBERT, KLUE 등 보수적인 Korean-specific naming |
| `B_likely` | `multilingual_explicit` | multilingual marker와 concrete language 2개 이상 |
| `B_likely` | `multilingual_tag_only` | multilingual marker와 concrete language 0~1개 |
| `C_fallback` | `family_heuristic` | 언어 metadata가 없고 known multilingual family만 일치 |

`Multilingual != Korean verified`이며, family heuristic도 한국어 지원을 보증하지 않는다. Core와 Low Popularity에는 `A_verified`만 들어간다.

### Stage 1 partition

| 파일 | 조건 | 현재 행 수 |
|---|---|---:|
| `hf_models_stage1_core.jsonl` | `A_verified` + downloads >= 500 | 1,451 |
| `hf_models_stage1_low_popularity.jsonl` | `A_verified` + downloads 80~499 | 2,116 |
| `hf_models_stage1_likely.jsonl` | `B_likely` + downloads >= 80 | 2,070 |
| `hf_models_stage1_fallback.jsonl` | `C_fallback` + downloads >= 80 | 14,013 |
| `hf_models_stage1_groups.jsonl` | 네 corpus union의 canonical/variant grouping | 8,472 |
| `hf_models_stage1_state.json` | version 7, config 및 task 통계 | 1 |

Popularity는 model quality가 아니라 offline retrieval priority다. Groups는 candidate confidence가 아니라 canonical/base-model과 quantized/converted variant lineage를 표현한다.

Stage 1 설정은 `MIN_DOWNLOADS=80`, `CORE_DOWNLOADS=500`, `LIMIT_PER_TASK=None`, `CUTOFF_CONFIRMATION=10`이며, 500 downloads는 Core에 포함된다.

## Stage 2: Technical Metadata Enrichment v6

Stage 2는 Core와 Low Popularity만 처리한다. Likely와 Fallback은 아직 enrichment하지 않는다. LLM을 사용하지 않고 Hugging Face current metadata, config, tokenizer config, README, model card metadata를 수집한다.

| 파일 | 역할 |
|---|---|
| `hf_models_stage2_core.jsonl` | Core technical metadata, 1,451개 |
| `hf_models_stage2_low_popularity.jsonl` | Low Popularity technical metadata, 2,116개 |
| `readmes/core/` | Core README, 1,447개 |
| `readmes/low_popularity/` | Low Popularity README, 2,110개 |

각 row는 Stage 1 snapshot을 `candidate`, `language.stage1`, `popularity.stage1`, `stage1_quality`에 보존한다. 현재 metadata는 `stage.source_stage1_version=7`, `stage.stage2_version=6`으로 기록된다.

`parameter_count`와 `context_length`가 `null`이면 0이 아니라 `unknown`이다. 각 row의 `model.metadata_status`에서 `known`과 `unknown`을 구분한다. 추천 필터가 해당 값을 요구할 때만 unknown을 제외하고, 일반 검색에서는 별도로 표시한다.

## Stage 3: Atomic Evidence Semantic Enrichment v1

Stage 3는 Stage 2의 Core와 Low Popularity를 대상으로 저비용 LLM을 사용해 README에서 atomic evidence span을 만들고, 각 semantic claim에 `evidence_refs`와 정확한 `supporting_quote`를 붙인다. candidate tier와 popularity를 재분류하지 않는다.

| 파일 | 역할 |
|---|---|
| `hf_models_stage3_core.jsonl` | Core semantic metadata, 1,451개 |
| `hf_models_stage3_low_popularity.jsonl` | Low Popularity semantic metadata, 2,116개 |

Core는 41개, Low는 84개의 긴 README를 full-readme repair로 보강했고, 현재 남은 잘림은 0개다. README 자체가 없는 모델은 Core 4개, Low 6개이며 `no_source`와 metadata-only 상태로 보존한다.

Stage 3 검증 결과는 두 pool 모두 중복 0, invalid evidence reference 0, uncited claim 0, quote mismatch 0이다.

## Stage 4: Embedding and Retrieval Index

Stage 4 입력은 Stage 3 Core와 Low Popularity다. Likely와 Fallback은 이번 인덱스에서 제외한다.

`04_build_embeddings.py`는 다음 문서를 만든다.

```text
identity, task, Korean evidence, languages,
architecture, parameters, context length,
quantization, artifacts, license, base model,
hardware estimate, popularity,
Stage 3 summary/strengths/limitations/use cases/benchmarks
```

검색은 다음 순서를 사용한다.

```text
hard filter → vector retrieval → evidence-aware rerank → canonical deduplication

Hugging Face task metadata와 모델 identity가 충돌하면 `task_conflict`를 기록한다. 해당 모델을 삭제하지 않고 ranking penalty만 적용해 recall을 유지한다. 현재 Core 4개, Low Popularity 7개가 conflict signal을 갖고 있으며, 기존 임베딩을 재생성하지 않고 오프라인으로 추가했다.
```

벡터 유사도만으로 언어·라이선스·하드웨어 조건을 판단하지 않는다. unknown parameter/context는 0으로 변환하지 않는다.

Stage 4 설계는 이 문서의 Stage 4 설명과 실행 코드에 반영되어 있다. 실행기는 기본적으로 dry-run이며, `--execute`를 명시할 때만 `text-embedding-3-small` API를 호출한다.

```bash
source ~/main/bin/activate
python 04_build_embeddings.py --pool all --limit 10
python 04_build_embeddings.py --pool all --limit 10 --execute
```

10개 stratified pilot은 `test/stage4_core_pilot.jsonl`과 `test/stage4_low_popularity_pilot.jsonl`에 임시로 기록된다. 전체 Stage 4 검증이 끝난 뒤에는 삭제해도 되며, task, candidate type, variant, evidence completeness, no_source를 섞어 선택한다.

## Benchmark 보조 신호

Stage 2 README snapshot의 benchmark 표와 `model-index` 수치는 `06_extract_benchmark_metadata.py`로 별도 sidecar에 저장한다.

| 파일 | 역할 |
|---|---|
| `hf_models_benchmark_core.jsonl` | Core의 benchmark 근거와 안전한 비교 가능 점수 |
| `hf_models_benchmark_low_popularity.jsonl` | Low Popularity의 benchmark 근거와 안전한 비교 가능 점수 |

숫자 없이 benchmark 이름만 있는 경우는 `mentions`로 보존한다. 표의 모델 열과 점수 열이 연결되지 않거나 현재 row의 모델명이 확인되지 않으면 순위에 사용하지 않는다. architecture, parameter, context, quantization, format, embedding dimension 같은 metadata 표도 benchmark 점수로 취급하지 않는다. 양자화 변형은 보고된 모델명에 GGUF/GPTQ/AWQ/MLX/ONNX/bit 등의 표기가 함께 있을 때만 현재 artifact의 점수로 인정한다.

숫자 점수는 질의가 dataset과 metric을 명시한 경우에만 동일한 `benchmark + dataset + metric + split + config`끼리 비교한다. README의 self-reported 수치는 실험 조건과 최신성을 보장하지 않으므로 보조 순위 신호로만 사용하며, task·한국어 근거·popularity·canonical 중복 제거를 대체하지 않는다.

### Benchmark metadata 통합

Benchmark 보조 정보는 `07_integrate_benchmark_metadata.py`로 Stage 4 각 row 안의 compact `benchmark_metadata` 필드에 통합한다. 검색기는 이 내장 필드를 우선 사용하므로 별도 benchmark sidecar 파일은 런타임에 필요하지 않다. 점수 없는 benchmark 이름은 `mentions`로 보존하고 ranking boost에는 사용하지 않는다. 원문 quote가 필요하면 row의 README 경로와 Stage 3 evidence를 함께 조회한다.
## 검색 결과 상세 정보 연결

Stage 4 row는 임베딩 검색과 필터링에 필요한 compact metadata를 보관한다. 검색 후에는
`05_validate_retrieval.py`의 hydrate 함수가 `(source_pool, model_id)`를 키로 Stage 2와 Stage 3 row를
hydrate한다.

Hydrate 결과에는 다음 정보가 추가된다.

- Stage 2 technical metadata: architecture, parameter count, context length, quantization, artifacts, license, hardware
- Stage 3 semantic metadata: summary, strengths, limitations, use cases, warnings
- claim별 `evidence_refs`, `supporting_quote`, README 경로와 content hash
- Stage 1~3 provenance와 semantic status

전체 README를 임베딩 결과에 중복 저장하지 않는다. 검색 순위는 Stage 4가 담당하고,
상위 결과의 상세 설명과 근거는 Stage 2·3에서 정확히 조회한다.
