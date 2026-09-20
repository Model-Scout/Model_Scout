# Model Scout Data Pipeline

Model Scout의 데이터 파이프라인은 Hugging Face Hub의 모델을 단순 수집하는 것이 아니라,

1. 검색 가능한 후보 모델을 넓게 수집하고
2. 언어 지원 근거와 popularity를 기준으로 후보군을 분리하고
3. base model과 quantized / converted variant 관계를 정규화하고
4. 실제 모델의 기술 metadata와 README를 수집한 뒤
5. 이후 semantic enrichment와 retrieval index로 확장

하는 구조로 설계한다.

현재 구현 범위는 **Stage 1 ~ Stage 2**이다.

> Stage 3 ~ Stage 4는 아직 구현하지 않았다.

---

## 1. 전체 데이터 파이프라인

```text
Hugging Face Hub
        │
        ▼
Stage 1. Candidate Collection
        │
        ├─ Task-based Discovery
        ├─ Adaptive Popularity Cutoff
        ├─ Noise Filtering
        ├─ Language Evidence Classification
        ├─ Popularity Partition
        ├─ Base-model / Variant Canonicalization
        └─ Metadata Quality Features
        │
        ▼
Stage 1 Candidate Corpus
        │
        ▼
Stage 2. Metadata Enrichment
        │
        ├─ Hugging Face current metadata
        ├─ config.json
        ├─ tokenizer_config.json
        ├─ README.md
        ├─ Model Card metadata
        ├─ parameter count
        ├─ architecture
        ├─ context length
        ├─ dtype
        ├─ quantization
        ├─ artifact format
        ├─ license
        ├─ base model
        ├─ datasets / metrics
        ├─ language evidence
        └─ weight-memory estimate
        │
        ▼
Stage 2 Metadata Corpus
        │
        ▼
Stage 3. Semantic Enrichment
        │
        └─ TODO
        │
        ▼
Stage 4. Chunking / Embedding / Retrieval Index
        │
        └─ TODO
```

---

## 2. Stage 1 — Candidate Collection

Stage 1은 Hugging Face 모델 공간을 그대로 저장하는 단계가 아니라,  
**Model Scout가 검색 가능한 후보 corpus로 정규화하는 Pre-Retrieval Index Construction 단계**이다.

핵심 흐름은 다음과 같다.

```text
HF Hub
  ↓
Task-based Discovery
  ↓
Adaptive Popularity Cutoff
  ↓
Noise Filtering
  ↓
Language Evidence Classification
  ├─ A Verified
  ├─ B Likely
  └─ C Fallback
  ↓
Popularity Partition
  ├─ Main: downloads >= 500
  ├─ Low: 100 <= downloads < 500
  └─ Excluded: downloads < 100
  ↓
Base-model / Variant Canonicalization
  ↓
Metadata Quality Features
  ↓
Stage 1 Corpus
```

### Language Evidence 분류

- **A Verified**: 한국어 또는 multilingual 지원에 대한 명시적 metadata 근거가 있는 모델
- **B Likely**: bilingual language list, Korean-specific name, multilingual tag 등 보조 근거가 있는 모델
- **C Fallback**: Qwen, Gemma, Llama, Mistral 등 family heuristic으로만 잡힌 후보

### Popularity 분기

downloads는 모델 품질 자체를 의미하지 않고, offline corpus의 우선순위를 나누는 운영 기준으로 사용한다.

- `downloads >= 500` → 기본 검색 대상
- `100 <= downloads < 500` → 신규 / niche 모델을 위한 확장 후보
- `downloads < 100` → offline corpus에서는 제외하고 추후 online fallback 대상으로 활용

### Stage 1 결과 파일

| 파일 | 개수 | 역할 |
|---|---:|---|
| `hf_models_stage1_core.jsonl` | 5,630 | 메인 추천 corpus |
| `hf_models_stage1_low_popularity.jsonl` | 7,167 | 저인기지만 언어 근거가 있는 후보 |
| `hf_models_stage1_fallback.jsonl` | 12,118 | family heuristic 기반 recall 보강 |
| `hf_models_stage1_groups.jsonl` | 11,342 groups | base model / quantized variant 묶음 |
| `hf_models_stage1_state.json` | 1 | 실행 정책 및 task별 수집 통계 |

---

## 3. Stage 2 — Fact-based Technical Metadata Enrichment (v3)

Stage 2는 Stage 1 v4 후보의 기술 정보를 보강한다. **LLM과 semantic interpretation은 사용하지 않는다.**

### 대상 및 실행 순서

| Stage 1 pool | Stage 2 대상 |
|---|---|
| Core | 전체 technical enrichment 기능 적용 |
| Low Popularity | 전체 technical enrichment 기능 적용 |
| Likely | 아직 미수집 |
| Fallback | 아직 미수집 |

`SOURCE_POOLS = ["core", "low_popularity"]` 순서로 공통 처리 함수를 실행한다.
각 pool의 입력, output, error log, README 디렉터리와 resume은 독립적이다.
기본 `TEST_LIMIT = 100`은 각 pool의 입력 앞 100개에 별도로 적용한다.
향후 전체 수집 시 `TEST_LIMIT = None`으로 변경한다. **이번 수정에서는 실제 enrichment를 실행하지 않았다.**

### 수집 및 보존 정보

기존 Hugging Face current metadata, config.json, tokenizer_config.json, README.md,
Model Card metadata, parameter count, architecture, context length, dtype, quantization,
artifact format, license, base model, datasets, metrics, language evidence,
weight-memory estimate 수집 기능을 유지한다.

Stage 1 정보를 재분류하지 않고 다음 경로에 보존한다.

| Stage 1 | Stage 2 |
|---|---|
| `primary_task`, `matched_tasks` | `task.primary`, `task.matched` |
| `candidate` | `candidate` 전체, tier/type/confidence/evidence 포함 |
| `language` | `language.stage1` 전체 snapshot |
| `popularity` | `popularity.stage1` |
| `family` | `family` |
| `quality` | `stage1_quality` |
| `stage.stage1_version` | `stage.source_stage1_version` |

최신 다운로드와 좋아요는 `popularity.current`에 별도로 기록한다.
Stage 2에서 현재 다운로드를 보고 source pool을 옮기지 않는다.
Core와 Low Popularity는 동일한 output schema를 사용하며 `stage.source_pool`로 구분한다.
`stage.stage2_version = 3`, `metadata_enriched = true`, `semantic_enriched = false`와
`enriched_at`을 기록한다. Stage 1 v4 입력은 `source_stage1_version = 4`로 전달된다.

### Language verification

`language.declared_languages`, `korean`, `multilingual`, `bilingual` 검증 구조를 유지한다.
`korean_name`은 `stage1:korean_name` evidence로 인정한다.
`multilingual_tag_only` 또는 Model Card의 multilingual marker만으로 high-confidence verified로 승격하지 않는다.
Model Card의 실제 언어 목록이 3개 이상이거나 marker와 실제 언어 2개 이상이 함께 있어야 strong evidence로 인정한다.
Marker는 언어 개수에서 제외하고, 검증 근거가 없으면 `verified = null`로 유지한다.
이 추가 검증은 보존된 `candidate`나 `language.stage1`을 변경하지 않는다.

### Output 파일

| 파일 | 역할 |
|---|---|
| `hf_models_stage2_core.jsonl` | Stage 1 Core의 technical metadata enrichment |
| `hf_models_stage2_low_popularity.jsonl` | Stage 1 Low Popularity의 technical metadata enrichment |
| `hf_models_stage2_core_errors.jsonl` | Core enrichment error log |
| `hf_models_stage2_low_popularity_errors.jsonl` | Low Popularity enrichment error log |
| `readmes/core/` | Core model README |
| `readmes/low_popularity/` | Low Popularity model README |

`source.readme.path`에 실제 pool별 README 경로를 저장한다.
기존 v2 결과나 공용 README cache는 이번 코드 수정으로 삭제·변경하지 않는다.
향후 실행 시 v2 output row는 resume 대상으로 인정하지 않고 v3로 다시 생성한다.

### Resume, checkpoint, validation

동일한 Stage 2 version, source pool 및 Stage 1 snapshot을 가진 output row만 skip한다.
입력에서 사라진 row와 이전 version row는 새 output에서 제외하며, `TEST_LIMIT` 밖의 유효한 기존 결과는 보존한다.
Checkpoint는 각 pool에서 25개 처리마다 저장하고 로그에 pool 이름을 표시한다.
중단 시 현재 pool을 저장하고 종료하므로 다음 pool을 시작하지 않는다.

Error row에는 `model_id`, `source_pool`, `error_type`, `error`, `stage2_version`, `created_at`을 기록한다.
오류로 output에 추가되지 않은 모델은 다음 실행에서 다시 시도한다.

`validate_stage2_rows(rows, source_pool)`은 향후 실행의 개별 결과·checkpoint·최종 저장 전에 다음을 검증한다.

- Core: A_verified, Stage 1 downloads >= 500, source_pool = core
- Low Popularity: A_verified, Stage 1 downloads 100~499, source_pool = low_popularity
- 공통: source_stage1_version = 4, stage2_version = 3, 공통 schema, pool별 README 경로

오류 메시지에 문제가 있는 `model_id`와 위반 조건을 포함한다.
이번 작업에서는 이 validation이나 enrichment를 실행하지 않고 문법·정적 검토만 수행한다.

Stage 2는 fact extraction이고, README와 Model Card의 semantic interpretation은 이후 Stage 3의 역할이다.

---

## Summary

현재 파이프라인은 다음 두 단계까지 구현되어 있다.

```text
Stage 1
Hugging Face 모델 공간
→ 검색 가능한 candidate corpus로 정규화

Stage 2
Candidate corpus
→ 실제 Hugging Face metadata 기반 technical enrichment
```

이후에는 다음 흐름으로 확장할 예정이다.

```text
사용자 요구사항
        ↓
Hard Constraint
        ↓
Candidate Retrieval
        ↓
Semantic / Metadata Matching
        ↓
Variant / Hardware Matching
        ↓
Ranking
        ↓
Final Recommendation
```

현재 목표는 Stage 1~2를 통해  
**검색과 추천에 사용할 신뢰 가능한 모델 후보 데이터 기반을 구축하는 것**이다.