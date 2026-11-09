# Model Scout 모델 데이터 계약

이 문서는 **모델 한 건이 반드시 가져야 하는 사실의 목록과, 그 사실을 모를 때
무엇을 해야 하는지**를 정한다. Stage 1~5의 구현과 분리된 상위 규약이다.

기계가 검사하는 정식 정의는 [`model-record.schema.json`](model-record.schema.json)이다.
이 문서와 스키마가 어긋나면 **스키마가 맞다**.

- 수집 경로: [`source-map.md`](source-map.md)
- 현재 충족률: [`baseline.md`](baseline.md) (`python contract/coverage.py`로 재생성)
- 예시 레코드: [`examples.json`](examples.json)

---

## 0. 이 계약이 왜 필요했나

기존 파이프라인은 "HF가 주는 것 중 쓸 만한 것을 꺼내 쓰는" 구조였다. 그래서
어떤 필드가 왜 비었는지 아무도 설명할 수 없었다.

```python
# 02_enrich_metadata.extract_parameter_count()
safetensors = safe_get(info, "safetensors", None)
if safetensors is None:
    return None          # 여기서 끝난다. 왜 모르는지 기록이 없다.
```

GGUF 전용 레포에는 safetensors가 없다. 그래서 파라미터 수를 모르는 모델이
1,527개(39.4%) 생겼다. HF API가 `gguf.total`로 같은 사실을 주고 있었는데
읽지 않았다. 원칙 위반이 아니라 **수집 범위에 대한 정의가 없었던 것**이다.

계약의 제1원칙은 여기서 나온다.

> **값이 없어도 필드는 존재한다. 왜 모르는지도 기록한다.**
>
> 키를 생략하는 것은 "모른다"와 "해당 없다"와 "수집에 실패했다"를 구별할 수
> 없게 만든다. 세 경우에 사용자에게 할 말이 다르다.

---

## 1. 사용자가 실제로 물을 질문

타깃 사용자는 부트캠프 수료생, 청년 개발자, 프로젝트·창업 준비자다. 모델
연구자가 아니다. 이들이 묻는 것은 "이 모델이 SOTA인가"가 아니라
**"내 상황에서 이걸 써도 되는가"**다.

| # | 질문 | 답하려면 필요한 사실 | 답변 정책 |
|---|---|---|---|
| Q1 | 상업 서비스에 쓸 수 있는 한국어 모델? | `legal.commercial_status`, `legal.license_raw`, `legal.license_file`, `legal.base_model_constraint`, `capability.korean` | `permitted`만 정답. `review_required`/`unknown`은 별도 '확인 필요' 목록 |
| Q2 | RTX 5080(16GB)에서 돌아가는 모델? | `technical.parameter_count_total`/`_active`, `technical.dtype`, `artifacts.*.total_bytes`, `artifacts.quantization`, `technical.context_length` | 파라미터만으로 단정하지 않는다. 추정 조건을 함께 표시 |
| Q3 | 맥북·CPU·Ollama에서 되나? | `artifacts.gguf`/`mlx`, `deployment.llama_cpp`/`mps`/`cpu`의 status | `documented`/`artifact_present`/`inferred`/`unknown`을 구분해 말한다 |
| Q4 | 한국어 임베딩/RAG 모델? | `capability.primary_task`, `capability.korean`, `technical.embedding_dimensions`, `capability.reranker` | 고신뢰 근거가 있는 것 우선 |
| Q5 | 긴 문서를 번역할 모델? | `technical.context_length`, `capability.translation_pairs`, `capability.languages` | 컨텍스트와 번역 방향을 둘 다 확인. 하나만 맞으면 추천하지 않는다 |
| Q6 | 성능이 가장 좋은 모델? | `quality.results[]`의 `benchmark`/`dataset`/`metric`/`score`/`comparability` | **같은 benchmark·metric 안에서만** 비교. 자기 보고 점수는 그렇게 표시 |
| Q7 | 내려받아 포트폴리오/서비스에 써도 되나? | `identity.gated`, `legal.commercial_status`, `legal.redistribution`, `artifacts.*` | 법적 확정 답변이 아니라 근거와 주의사항을 준다 |

이 표가 계약 필드의 유일한 선정 근거다. **이 표에 쓰이지 않는 필드는 수집하지
않는다.** "있으면 좋을 것 같아서" 넣은 필드는 채우지 못했을 때 왜 비었는지
설명할 사람이 없다.

### 현재 답변 가능률

| 질문 | 운영 데이터 | 백필 반영 스냅샷 |
|---|---:|---:|
| Q1 상업 이용 한국어 | 57.6% | 57.6% |
| Q2 내 GPU에 들어가나 | 55.3% | 80.3% |
| Q3 Ollama로 되나 | 37.8% | 37.8% |
| Q4 한국어 임베딩 | 11.3% | 11.3% |
| Q5 장문 번역 | 41.2% | 64.5% |
| Q6 성능 비교 | 5.3% | 11.3% |
| Q7 배포해도 되나 | **0.0%** | **0.0%** |

Q7이 0%인 이유는 `gated`를 **어느 단계에서도 수집하지 않기 때문**이다.
필드가 비어 있는 것이 아니라 필드가 없다.

---

## 2. 모든 사실에 붙는 네 가지 메타

계약 필드는 값 하나로 끝나지 않는다. 네 가지가 같이 붙는다.

**값은 평평하게 두고, 출처는 `provenance.fields` 한 곳에 모은다.** 모든 필드를
`{value, status}` 객체로 감싸면 하드 필터와 Supabase RPC가 전부 깨진다. 지금
`filter_metadata.parameter_count`를 직접 읽고 있기 때문이다.

```json
{
  "technical": { "parameter_count_total": 27009346304 },

  "provenance": {
    "schema_version": 1,
    "pipeline_run_id": "reingest-2026-11-06-01",
    "fields": {
      "technical.parameter_count_total": {
        "status": "verified",
        "confidence": "high",
        "source": ["hf_api:gguf.total"],
        "retrieved_at": "2026-11-06T04:12:00Z"
      }
    }
  }
}
```

`provenance.fields`에 항목이 있어야 하는 필드 목록은 스키마의
`$defs.contract_fields`에 있다. 23개다. `validate.py`가 그 목록을 읽어
빠진 항목을 잡는다 — 목록을 두 군데 적지 않는다.

### status — 이 값을 어떻게 알게 됐나

| status | 뜻 | 하드 필터 취급 |
|---|---|---|
| `verified` | 1차 출처를 기계가 판독한 값. `gguf.total`, `safetensors.total`, `config.json` | 값으로 사용 |
| `documented` | 모델 카드나 공식 문서에 글로 명시된 값 | 값으로 사용 |
| `inferred` | 확정된 다른 값에서 유도. 파일 크기 → 파라미터 추정 등 | 값으로 사용 + "추정" 표시 |
| `conflict` | 출처 둘 이상이 서로 다른 값을 말한다 | **값 사용 금지.** 사람 검토 큐로 |
| `unknown` | 어디에도 없다 | 값 없음. 수치 조건 질의에서 탈락 |
| `not_applicable` | 이 모델에 해당하지 않는 개념 (임베딩 모델의 `context_length` 등) | 조건에서 제외 |

`conflict`와 `unknown`을 구별하는 것이 핵심이다. 전자는 "우리가 정리하지
못했다", 후자는 "출처가 말하지 않았다"다. 전자는 고칠 수 있다.

### confidence

| confidence | 언제 |
|---|---|
| `high` | `verified` — HF가 실제 파일을 파싱해 내놓은 값 |
| `medium` | `documented`, 또는 선언된 `base_model`에서 상속한 값 |
| `low` | `inferred` |
| `none` | `unknown`, `conflict` |

**모델명에서 숫자를 긁어내는 것은 어떤 등급도 아니다. 금지한다.**
`Mistral-Small-4-119B-GGUF`에서 정규식은 `4B`를 잡지만 실제는 119B다.

### source — 어디서 왔나

출처는 자유 문자열이 아니라 아래 접두사 중 하나로 시작한다. 사람이
"이 값이 어디서 왔지"를 추적할 수 있어야 한다.

```
hf_api:<경로>           hf_api:gguf.total, hf_api:safetensors.total, hf_api:gated
hf_file:<파일>:<키>     hf_file:config.json:max_position_embeddings
hf_blob:<파일명>        hf_blob:model-Q4_K_M.gguf   (크기·존재)
model_card:<섹션>       model_card:cardData.license
readme:<위치>           readme:table[1].row[64].column[6]
official_doc:<URL>      official_doc:https://ai.google.dev/gemma/terms
derived_from:<model_id> derived_from:google/gemma-3-27b-it
```

### retrieved_at + schema_version

레코드마다 `provenance.retrieved_at`과 `provenance.schema_version`을 적는다.
스키마가 바뀌면 전체 재적재가 필요한지 판단할 근거다.

---

## 3. 라이선스 처리 — 가장 많이 묻고 가장 많이 틀리는 것

### 분류는 새로 만들지 않는다

`taxonomy.yaml`의 `commercial_use` 패싯이 이미 분류를 한다. 매핑 테이블을
또 만들면 두 벌이 생기고 어느 쪽이 맞는지 아무도 모른다.

```
taxonomy.normalize("commercial_use", raw)  →  legal.commercial_status
─────────────────────────────────────────────────────────────────
  commercial       →  permitted
  non_commercial   →  prohibited
  conditional      →  review_required
  unknown / None   →  unknown
```

| commercial_status | 어떤 라이선스가 | 현재 수 | 사용자에게 할 말 |
|---|---|---:|---|
| `permitted` | apache-2.0, mit, bsd-*, cc0, cc-by-*, mpl-2.0, openmdw-1.1 | 2,231 (57.6%) | "저장소가 선언한 라이선스는 상업 이용을 허용하는 계열입니다. 고지·표기 의무는 원문을 확인하세요." |
| `prohibited` | cc-by-nc-*, cc-by-nc-sa-*, cc-by-nc-nd-* | 260 (6.7%) | "비상업 용도로만 허용됩니다." |
| `review_required` | llama2/3/3.1/3.2/3.3/4, gemma, openrail*, gpl/lgpl/agpl, cc-by-nd, exaone, qwen, **other** | 1,104 (28.5%) | "자체 약관이나 추가 조건이 있어 직접 확인이 필요합니다." + 약관 링크 |
| `unknown` | 라이선스 필드 자체가 없음 | 277 (7.2%) | "저장소에 라이선스 정보가 없어 상업 이용 여부를 확인할 수 없습니다." |

### `permitted`가 "법적으로 안전"을 뜻하지 않는다

이게 가장 중요한 단서 조건이다.

```
legal.commercial_status 는
  "이 저장소가 선언한 라이선스가 어느 계열인가"를 말한다.

다음은 말하지 않는다.
  · base model / adapter 의 원래 약관      → legal.base_model_constraint 로 따로
  · 학습 데이터의 라이선스                 → 모델 레코드가 답할 수 없다
  · 서비스 운영 방식(재배포·API 제공 등)   → 사용자 상황이다
```

`apache-2.0` 모델이 Llama 기반 파인튜닝이면 Llama 약관이 따라온다.
그래서 `legal.base_model_constraint`를 별도 필드로 둔다. `base_models`를
따라가 원본의 `commercial_status`를 보고, 원본이 더 제한적이면
**더 제한적인 쪽을 표시**한다 (값은 덮어쓰지 않고 둘 다 보여준다).

### `other` 949개 — 가장 큰 덩어리

`other`는 "라이선스가 없다"가 아니라 **"HF 태그 어휘에 없는 라이선스"**다.
저장소에 실제 `LICENSE` 파일이 있는 경우가 많다.

```
Stage 2A에서 LICENSE / LICENSE.md / LICENSE.txt / COPYING / NOTICE 를 받는다
        ↓
있으면  legal.license_file = {path, sha256, chars}
        status = documented, confidence = medium
        → 사람이 읽고 판정할 수 있는 상태가 된다 (review queue)
        ↓
없으면  status = unknown 유지
```

**LLM에 라이선스 원문을 읽혀 자동 판정하지 않는다.** 법적 성격이 있는
판단이고, 틀렸을 때 사용자가 입는 피해가 "모른다"고 말하는 것보다 크다.
원문과 출처를 모아 두는 데까지가 파이프라인의 일이다.

### 검색 정책

```
"상업적으로 쓸 수 있는" 이 질의에 있을 때
  → permitted 만 정답 후보
  → review_required / unknown 은 결과에 섞지 않는다
  → 별도 "확인이 필요한 후보" 목록으로만 보여준다

조건이 없는 일반 질의
  → 전부 후보로 둔다
  → 단 commercial_status 를 결과에 항상 함께 표시한다
```

후자가 중요하다. 라이선스 조건이 없다고 NC 모델을 말없이 추천하면
사용자가 창업에 쓰고 나서 문제를 알게 된다.

---

## 4. "내 GPU에 들어가나" 처리

### 파라미터 수만으로 답하지 않는다

```
필요 메모리 ≈ 파라미터 수 × dtype 바이트 + KV 캐시 + 활성화 + 런타임 오버헤드
```

지금은 `hardware.weights_only.{fp16,int8,int4}_gib`만 있다. 가중치만이라고
이름에 적혀 있는데, 사용자는 "16GB에 들어간다"로 읽는다.

계약은 세 가지를 따로 둔다.

| 필드 | 무엇 | 왜 따로 |
|---|---|---|
| `technical.parameter_count_total` | 전체 파라미터 | VRAM은 전체 기준 |
| `technical.parameter_count_active` | MoE 활성 파라미터 | 속도는 활성 기준. `24B-A2B`는 전체 24B / 활성 2B |
| `artifacts.<format>.total_bytes` | 실제 파일 크기 합 | 추정이 아닌 측정값. GGUF 양자화본은 이게 가장 정확하다 |

MoE에서 total/active를 구별하지 않으면 **"3B 이하" 질의의 답이 뒤집힌다.**
`gguf.total`이 어느 쪽인지 단정할 수 없는 모델은 `status: conflict`로 두고
사람이 판정한다.

### 답변 형식

단정하지 않고 조건을 같이 말한다.

```
❌ "RTX 5080(16GB)에서 돌아갑니다"
✅ "Q4_K_M 양자화 파일이 4.1GB입니다(측정값). 가중치만 기준이며
    컨텍스트 길이에 따라 KV 캐시가 추가로 필요합니다."
```

---

## 5. unknown / conflict 를 하드 필터가 어떻게 다루나

이게 검색 결과를 가장 크게 좌우하는 규칙이다.

```
수치 조건(min/max)이 질의에 있고 값이 unknown 이면
  → 탈락시킨다

이유: Supabase 의 match_model_scout_models() 가 그렇게 동작한다.
      PostgreSQL 이 JSON 값을 캐스팅하면 없는 값은 NULL 이 되고
      WHERE 절이 그 행을 제외한다. 로컬 평가가 통과시키면
      오프라인 평가와 운영 검색의 후보 집합이 달라진다.
```

`ai/05_validate_retrieval.numeric_ok()`가 이 규칙을 구현한다. 주석에
"deliberately mirrors the SQL predicates"라고 적혀 있다.

따라오는 결론:

- **값을 모르면 그 모델은 수치 조건 검색에서 사라진다.** 그래서 메타데이터를
  채우는 일이 "있으면 좋은 것"이 아니라 검색 가능성 그 자체다.
- `require_known_parameters` / `require_known_context`는 수치 조건이 있는
  질의에서는 **중복**이다. "스펙이 공개된 모델만"을 명시적으로 묻는 질의를
  위해서만 남긴다.
- `conflict`는 `unknown`과 같이 취급한다. 틀린 값으로 필터를 통과시키는 것이
  탈락보다 나쁘다.

---

## 6. 계약 필드 전체 목록

그룹별 요약이다. 타입·필수 여부의 정식 정의는 스키마에 있다.

```
identity        모델을 가리키고 재현하는 데 필요한 것
  model_id, author, repo_url, revision, last_modified, gated, private

discovery       왜 이 모델이 코퍼스에 있는지
  candidate_tier, candidate_type, korean_evidence, downloads, likes,
  popularity_tier, canonical_model_id, is_variant, variant_types

capability      무엇을 하는 모델인지
  primary_task, matched_tasks, languages, korean, multilingual,
  translation_pairs, modality, embedding_dimensions, reranker

technical       크기와 구조
  architecture, model_type, parameter_count_total, parameter_count_active,
  context_length, dtype

artifacts       실제로 내려받을 수 있는 파일
  safetensors, gguf, onnx, ct2, mlx, pytorch_bin
  각 포맷마다: present, file_count, total_bytes, shard_count, quantization

deployment      어디서 돌아가나
  cpu, cuda, mps, vllm, llama_cpp, onnx   각각 status/confidence/evidence/conditions
  vram_estimate: weights_only {fp16, int8, int4}, basis, caveat

legal           써도 되나
  license_raw, license_file, commercial_status, base_model_constraint,
  redistribution, review_required, review_reason, user_message

quality         성능 근거
  results[]: benchmark, dataset, metric, score, split, self_reported,
             comparability, evidence_ref, ranking_eligible

semantic        설명과 근거 (사실 필드가 아니다)
  summary, strengths, limitations, use_cases, atomic_evidence[]

provenance      위 전부에 대한 메타
  fields{<필드경로>: {status, confidence, source[], retrieved_at}},
  schema_version, pipeline_run_id, conflicts[], review_queue[]
```

`semantic`은 **사실 필드가 아니다.** LLM이 README에서 뽑은 설명이므로
하드 필터가 읽지 않는다. 설명과 근거 제시에만 쓴다.

---

## 7. 계약 위반이란 무엇인가

`python contract/validate.py`가 검사한다. 하나라도 걸리면 적재하지 않는다.

| 검사 | 왜 |
|---|---|
| 계약 필드가 레코드에 없다 | 키 생략은 "모른다"와 구별이 안 된다 |
| `status: verified` 인데 `source`가 비었다 | 근거 없는 고신뢰 값. 추측이 승격된 것이다 |
| `status: unknown` 인데 `value`가 있다 | 둘 중 하나가 틀렸다 |
| `confidence: high` 인데 `status`가 `inferred`/`unknown` | 등급 규칙 위반 |
| `source`가 정의된 접두사로 시작하지 않는다 | 추적 불가 |
| 기존 `verified` 값을 새 `inferred` 값이 덮었다 | 품질 하락. 재적재 사고의 전형 |
| `schema_version`이 코드의 버전과 다르다 | 혼합 버전 데이터 |

마지막 항목이 백필 작업에서 실제로 발생했다. Stage 4 문서를 직접 조립했더니
`task`·`candidate`·`popularity`·`search_aliases` 등 12개 키가 빠져
하드 필터가 전부 탈락시켰다. 스키마 검증이 있으면 적재 전에 잡힌다.
