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

## 2. Stage 1 Candidate Collection — v7

Stage 1은 Hub metadata, model_id, structured Model Card language metadata와 deterministic rule만 사용한다.
LLM, README fetch, 본문 semantic interpretation은 사용하지 않는다.

### 최종 ontology와 우선순위

아래 순서에서 가장 강한 evidence를 candidate.type으로 선택한다.

| Tier | Type | 근거 |
|---|---|---|
| A_verified | `korean_explicit` | structured language metadata에 normalized `ko` 존재 |
| A_verified | `korean_translation_pair` | 모델 이름에 경계가 명확한 `ko-en`, `en-ko`, `ja-ko` 등 ISO 언어 pair |
| A_verified | `korean_name_strong` | 보수적인 Korean-specific naming whitelist |
| B_likely | `multilingual_explicit` | multilingual marker + concrete language 2개 이상 |
| B_likely | `multilingual_tag_only` | multilingual marker + concrete language 0~1개 |
| C_fallback | `family_heuristic` | Korean evidence·multilingual marker·concrete language 없이 허용 family만 일치 |

그 외 type은 허용하지 않는다. Korean evidence가 항상 multilingual보다 우선한다.
A는 high, B는 medium, C는 low confidence이다. 이는 deterministic evidence 수준이며 실제 한국어 성능 보증은 아니다.

- `korean_explicit`: Hub tags, model.language/model.languages, Model Card structured language에서 `ko`, `kor`, `korean`, `ko-kr` 및 `language:` prefix를 정규화한다.
- `korean_translation_pair`: repo 이름의 완전한 ISO-639-1 token pair를 검사한다. `-`, `_`, `.`, `/` 구분자를 지원하며 owner 이름과 repo 이름을 연결해 pair를 만들지 않는다.
- `korean_name_strong`: kobert, koelectra, kogpt, kosimcse, ko-sbert, kosbert, korbert, klue, korquad, kullm, kollama, kogemma, koalpaca whitelist를 사용한다. Generic `ko`, `kor`만으로 A가 되지 않는다. Kokoro, koala, kosmos, token, unknown은 strong Korean name이 아니다.
- Multilingual marker는 multilingual, multilinguality, multi-lingual, multi-language를 정규화한다. Marker는 concrete language count에서 제외한다. Marker 없는 다중 언어 목록만으로 B를 만들지 않는다.
- Fallback family는 qwen, aya, gemma, llama, mistral, bloom, xlm, mt5, mbert, multilingual-e5, bge-m3이다. 명시적 non-Korean language 목록이 있으면 family fallback을 금지한다.

Evidence에는 regex 대신 `explicit_language:korean`, `translation_pair:ko-en`,
`strong_korean_name:koelectra`, `multilingual_tag`, `explicit_language_list:de,en,fr,ro`, `family:qwen`처럼 의미가 드러나는 label을 저장한다.

`language.korean_explicit`은 **structured metadata에 ko가 존재하는지**만 나타낸다.
Translation pair나 strong name으로 A가 되어도 false일 수 있다.
`language.languages`, `multilingual_marker`, `language_count`, `concrete_language_count`는 candidate 검증과 구분한다.

### Popularity / corpus partition

**Core / Low에는 A_verified만 들어간다.**
**Multilingual != Korean verified. Family heuristic != Korean verified.**
Popularity는 offline retrieval priority이며 model quality가 아니다.

| 파일 | 조건 / 역할 |
|---|---|
| `hf_models_stage1_core.jsonl` | A_verified + downloads >= 500 |
| `hf_models_stage1_low_popularity.jsonl` | A_verified + 80 <= downloads < 500 |
| `hf_models_stage1_likely.jsonl` | B_likely + downloads >= 80 |
| `hf_models_stage1_fallback.jsonl` | C_fallback + downloads >= 80 |
| `hf_models_stage1_groups.jsonl` | 네 corpus union의 canonical/base-model 및 variant lineage grouping |
| `hf_models_stage1_state.json` | version 7, 실행 설정 및 task 통계 |

**500 downloads는 Core**, 499는 Low이다. 다운로드가 커도 B/C를 Core로 올리지 않는다.
Groups는 candidate confidence가 아니라 canonical/base-model 및 quantized/converted variant lineage grouping이다.
기존 task 목록, `MIN_DOWNLOADS=80`, `CORE_DOWNLOADS=500`, `LIMIT_PER_TASK=None`,
`CUTOFF_CONFIRMATION=10`, grouping 및 metadata completeness score 구조를 유지한다.

State는 `core_downloads_inclusive=true`를 기록하고 checkpoint 경로는 `.stage1_v7_checkpoint/`처럼 version에서 생성한다.
같은 tier에서도 `TYPE_RANK`로 더 강한 type을 선택하며 matched_tasks 및 기존 evidence를 병합·중복 제거한다.

### 검증 및 실행 상태

`validate_outputs()`는 각 corpus의 tier/type, 다운로드 경계, deterministic evidence, 중복 ID, version,
metadata flag, groups와 corpus union의 일치를 검증한다.
CORE AUDIT / LOW AUDIT에 total, korean_explicit, korean_translation_pair, korean_name_strong, invalid_type을 출력한다.
`invalid_type=0`이어야 하며 B/C type은 Core/Low에 하나도 허용하지 않는다.

```bash
source ~/main/bin/activate
python -m py_compile 01_collect_models.py
python -m unittest -v test_stage1
```

요청된 20개 fake-model regression과 추가 invariant 검증은 네트워크 없이 실행한다.
오염 audit은 임시 synthetic corpus를 대상으로 하며 기존 실제 JSONL을 v7 결과라고 주장하지 않는다.
**이번 작업에서는 전체 collection, 기존 JSONL 재생성, Stage 2 실행, Supabase 작업을 수행하지 않았다.**
새 v7 결과는 다음 전체 Stage 1 실행이 완료·검증된 후 생성된다.

Stage 2는 v7 ontology에 맞춰 version 6으로 갱신되었다. 이번 호환성 수정에서는 enrichment를 실행하지 않았다.

---

## 3. Stage 2 — Fact-based Technical Metadata Enrichment (v6)

Stage 1 v7 Core와 Low Popularity를 순서대로 처리한다. `TEST_LIMIT=None`으로 전체가 대상이며 Likely/Fallback은 아직 enrichment하지 않는다.
기존 technical metadata 수집 기능을 유지하고 LLM이나 semantic interpretation은 사용하지 않는다.

| 파일 | 역할 |
|---|---|
| `hf_models_stage2_core.jsonl` | Core technical enrichment |
| `hf_models_stage2_low_popularity.jsonl` | Low Popularity technical enrichment |
| `readmes/core/` | Core README |
| `readmes/low_popularity/` | Low Popularity README |

`stage.source_stage1_version=7`, `stage.stage2_version=6`로 기록한다.
입력 및 output validation은 A의 `korean_explicit`, `korean_translation_pair`, `korean_name_strong`을 허용한다.
Core는 Stage 1 downloads >= 500, Low는 80~499이어야 한다. 현재 다운로드로 pool을 재분류하지 않는다.

Stage 1 `candidate`, `family`는 그대로 유지하고 `language.stage1`, `popularity.stage1`, `stage1_quality`에 원본 snapshot을 보존한다.
Task는 `task.primary`와 `task.matched`, 최신 인기도는 `popularity.current`에 저장한다.
추가 language verification은 원본 candidate를 변경하지 않는다.

Pool별 output/README/resume/checkpoint를 분리한다. 같은 version·pool·Stage 1 snapshot일 때만 resume으로 skip한다.
기존 output은 보존하며 같은 model_id가 성공적으로 갱신되면 새 row로 교체한다.
Stage 1에 없는 항목과 갱신 실패한 이전 row는 추후 정리 전까지 남으므로 이전 version이 섞일 수 있다.
현재 입력으로 처리한 row만 새 version validation 대상으로 삼는다.

Stage 1 v7 검증 후 Core와 Low Popularity 전체 enrichment를 완료했다. 이후 metadata repair도 별도 output 검증 후 반영했다.

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

## 추천 필터의 미확인 metadata 처리

`model.parameter_count`와 `model.context_length`가 `null`이면 값이 없는 것이 아니라 **정보 미확인(`unknown`)**이다. 추천·하드웨어 필터는 이를 `0` 또는 최솟값으로 변환하면 안 된다.

Stage 2 v6 이후 생성되는 row에는 다음 상태를 함께 기록한다.

```json
"model": {
  "parameter_count": null,
  "context_length": null,
  "metadata_status": {
    "parameter_count": "unknown",
    "context_length": "unknown"
  }
}
```

양수인 신뢰 가능한 값만 `known`으로 표시한다. `unknown` 모델은 사용자가 파라미터 수나 context length를 명시적으로 요구할 때만 제외하고, 일반 후보 검색에서는 별도 표시한 채 유지한다. `hardware.weights_only` 추정치도 파라미터 수가 없으면 `null`로 남긴다.
