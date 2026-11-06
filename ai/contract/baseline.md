# Coverage baseline

`python contract/coverage.py --compare --out contract/baseline.md`로 재생성한다.
숫자를 손으로 적지 않는다. 재적재 후 같은 명령으로 before/after를 비교한다.

측정 시점: 2026-11-06 · 대상 커밋: `be74496d`

## 세 소스가 무엇인지

| 소스 | 레코드 | 무엇인가 |
|---|---:|---|
| `stage2` | 3,872 | `data/hf_models_stage2_{pool}.jsonl` — 운영 파이프라인의 사실 수집 결과 |
| `stage4` | 3,853 | `data/hf_models_stage4_{pool}.jsonl` — 검색 문서. Supabase에 올라가는 형태 |
| `snapshot` | 3,872 | `test/golden/v2/corpus_snapshot.jsonl` — Supabase active 동결본 + `ai/backfill` 반영 |

`snapshot`만 백필이 반영돼 있다. `ai/backfill`은 `out/` 폴더에만 썼고
운영 `data/`를 교체하지 않았다. **이 작업의 목표가 저 격차를 사이드 폴더가**
**아니라 파이프라인이 만들게 하는 것이다.**

## 한눈에 — 질문별 답변 가능률

| 사용자 질문 | `stage2` | `stage4` | `snapshot` |
|---|---:|---:|---:|
| Q1 상업 서비스에 쓸 수 있는 한국어 모델 | 57.6% | 57.7% | 57.6% |
| Q2 내 GPU(16GB)에서 돌아가는 모델 | 55.3% | 55.4% | 80.3% |
| Q3 Ollama/llama.cpp로 돌릴 수 있는 모델 | 37.8% | 37.7% | 37.8% |
| Q4 한국어 임베딩/RAG 모델 | 11.3% | 11.3% | 11.3% |
| Q5 긴 문서를 번역할 모델 | 41.2% | 41.2% | 64.5% |
| Q6 성능이 가장 좋은 모델 | 5.3% | 0.0% | 11.3% |
| Q7 내려받아 배포해도 되는 모델 | 0.0% | 0.0% | 0.0% |

### 읽는 법

- **Q7이 0%다.** `identity.gated`를 어느 단계에서도 수집하지 않는다.
  "이 모델 내려받아 써도 되나"에 답할 데이터가 레코드에 없다. 그런데
  HF 응답에는 `gated`가 99.3%로 들어오고 있다 — 안 읽은 것뿐이다.
- **Q2·Q5는 `snapshot`만 높다.** 백필이 올린 값이다. 운영 데이터는 그대로다.
- **Q6은 `stage4`에서 0%다.** 벤치마크는 `06`/`07`이 sync 시점에 붙이므로
  Stage 4 파일에는 없다. 단계 간 사실 위치가 일관되지 않다는 신호다.
- **Q4가 낮은 것은 결함이 아니다.** 임베딩 과제 모델이 실제로 그만큼이다.
  분모가 전체 코퍼스이므로 "부족"이 아니라 "분포"다.
- **`legal.commercial_status`가 92.8%인데 Q1은 57.6%다.** 분류는 되지만
  `permitted`가 그만큼이라는 뜻이다. 나머지는 NC·조건부·미확인이다.

## 계약 필드 coverage

| 계약 필드 | `stage2` | `stage4` | `snapshot` |
|---|---:|---:|---:|
| `identity.model_id` | 100.0% | 100.0% | 100.0% |
| `identity.revision` | 0.0% | 0.0% | 0.0% |
| `identity.last_modified` | 0.0% | 0.0% | 0.0% |
| `identity.gated` | 0.0% | 0.0% | 0.0% |
| `capability.primary_task` | 100.0% | 100.0% | 100.0% |
| `capability.languages` | 97.5% | 97.5% | 97.5% |
| `capability.korean_verified` | 100.0% | 100.0% | 100.0% |
| `technical.parameter_count_total` | 60.6% | 60.6% | 85.5% |
| `technical.parameter_count_active` | 0.0% | 0.0% | 0.0% |
| `technical.context_length` | 62.3% | 62.4% | 92.1% |
| `technical.architecture` | 63.2% | 63.2% | 95.7% |
| `technical.model_type` | 64.7% | 64.8% | 96.1% |
| `technical.dtype` | 60.6% | 0.0% | 0.0% |
| `artifacts.format_flags` | 100.0% | 100.0% | 100.0% |
| `artifacts.total_bytes` | 0.0% | 0.0% | 0.0% |
| `deployment.vram_fp16_gib` | 55.3% | 55.4% | 80.3% |
| `deployment.vram_int4_gib` | 55.3% | 55.4% | 80.3% |
| `legal.license_raw` | 92.8% | 92.8% | 92.8% |
| `legal.commercial_status` | 92.8% | 92.8% | 92.8% |
| `quality.benchmark_score` | 5.3% | 0.0% | 11.3% |
| `discovery.downloads` | 100.0% | 100.0% | 100.0% |

---

# 소스: `stage2`

측정 대상 `stage2` — 레코드 3,872개

## 질문별 답변 가능률

필터가 그 질문을 걸 수 있고, 답에 쓸 사실이 레코드에 있는 모델의 수다.

| 사용자 질문 | 필요한 계약 필드 | 답변 가능 | 비율 |
|---|---|---:|---:|
| Q1 상업 서비스에 쓸 수 있는 한국어 모델 | `legal.commercial_status, capability.korean_verified` | 2,231 | 57.6% |
| Q2 내 GPU(16GB)에서 돌아가는 모델 | `technical.parameter_count_total 또는 artifacts.total_bytes` | 2,143 | 55.3% |
| Q3 Ollama/llama.cpp로 돌릴 수 있는 모델 | `artifacts.gguf` | 1,463 | 37.8% |
| Q4 한국어 임베딩/RAG 모델 | `capability.primary_task, capability.korean_verified` | 436 | 11.3% |
| Q5 긴 문서를 번역할 모델 | `technical.context_length, capability.primary_task` | 1,595 | 41.2% |
| Q6 성능이 가장 좋은 모델 | `quality.benchmark_score` | 205 | 5.3% |
| Q7 내려받아 배포해도 되는 모델 | `legal.commercial_status, identity.gated` | 0 | 0.0% |

## 계약 필드 coverage

| 계약 필드 | 있음 | 비율 |
|---|---:|---:|
| `identity.model_id` | 3,872 | 100.0% |
| `identity.revision` | 0 | 0.0% |
| `identity.last_modified` | 0 | 0.0% |
| `identity.gated` | 0 | 0.0% |
| `capability.primary_task` | 3,872 | 100.0% |
| `capability.languages` | 3,777 | 97.5% |
| `capability.korean_verified` | 3,872 | 100.0% |
| `technical.parameter_count_total` | 2,345 | 60.6% |
| `technical.parameter_count_active` | 0 | 0.0% |
| `technical.context_length` | 2,413 | 62.3% |
| `technical.architecture` | 2,447 | 63.2% |
| `technical.model_type` | 2,505 | 64.7% |
| `technical.dtype` | 2,348 | 60.6% |
| `artifacts.format_flags` | 3,872 | 100.0% |
| `artifacts.total_bytes` | 0 | 0.0% |
| `deployment.vram_fp16_gib` | 2,143 | 55.3% |
| `deployment.vram_int4_gib` | 2,143 | 55.3% |
| `legal.license_raw` | 3,595 | 92.8% |
| `legal.commercial_status` | 3,595 | 92.8% |
| `quality.benchmark_score` | 205 | 5.3% |
| `discovery.downloads` | 3,872 | 100.0% |

## 라이선스 → commercial_status

| commercial_status | 모델 수 | 비율 | 뜻 |
|---|---:|---:|---|
| `permitted` | 2,231 | 57.6% | 선언된 라이선스가 상업 이용을 허용하는 계열 |
| `prohibited` | 260 | 6.7% | 비상업 전용(NC). 상업 질의에서 제외 |
| `review_required` | 1,104 | 28.5% | 추가 약관 확인 필요(llama/gemma/GPL/other 등) |
| `unknown` | 277 | 7.2% | 라이선스 자체가 없음. 판단 불가 |

### 원시 라이선스 값 상위

| license | 모델 수 | 분류 |
|---|---:|---|
| `apache-2.0` | 1,784 | `permitted` |
| `other` | 949 | `review_required` |
| `mit` | 392 | `permitted` |
| `None` | 277 | `unknown` |
| `cc-by-nc-4.0` | 197 | `prohibited` |
| `gemma` | 84 | `review_required` |
| `cc-by-nc-sa-4.0` | 61 | `prohibited` |
| `llama3.1` | 18 | `review_required` |
| `llama3` | 17 | `review_required` |
| `cc-by-4.0` | 16 | `permitted` |
| `cc-by-sa-4.0` | 14 | `permitted` |
| `llama2` | 14 | `review_required` |
| `openmdw-1.1` | 12 | `permitted` |
| `gpl-3.0` | 11 | `review_required` |
| `llama3.2` | 7 | `review_required` |


---

# 소스: `stage4`

측정 대상 `stage4` — 레코드 3,853개

## 질문별 답변 가능률

필터가 그 질문을 걸 수 있고, 답에 쓸 사실이 레코드에 있는 모델의 수다.

| 사용자 질문 | 필요한 계약 필드 | 답변 가능 | 비율 |
|---|---|---:|---:|
| Q1 상업 서비스에 쓸 수 있는 한국어 모델 | `legal.commercial_status, capability.korean_verified` | 2,223 | 57.7% |
| Q2 내 GPU(16GB)에서 돌아가는 모델 | `technical.parameter_count_total 또는 artifacts.total_bytes` | 2,134 | 55.4% |
| Q3 Ollama/llama.cpp로 돌릴 수 있는 모델 | `artifacts.gguf` | 1,451 | 37.7% |
| Q4 한국어 임베딩/RAG 모델 | `capability.primary_task, capability.korean_verified` | 436 | 11.3% |
| Q5 긴 문서를 번역할 모델 | `technical.context_length, capability.primary_task` | 1,589 | 41.2% |
| Q6 성능이 가장 좋은 모델 | `quality.benchmark_score` | 0 | 0.0% |
| Q7 내려받아 배포해도 되는 모델 | `legal.commercial_status, identity.gated` | 0 | 0.0% |

## 계약 필드 coverage

| 계약 필드 | 있음 | 비율 |
|---|---:|---:|
| `identity.model_id` | 3,853 | 100.0% |
| `identity.revision` | 0 | 0.0% |
| `identity.last_modified` | 0 | 0.0% |
| `identity.gated` | 0 | 0.0% |
| `capability.primary_task` | 3,853 | 100.0% |
| `capability.languages` | 3,758 | 97.5% |
| `capability.korean_verified` | 3,853 | 100.0% |
| `technical.parameter_count_total` | 2,336 | 60.6% |
| `technical.parameter_count_active` | 0 | 0.0% |
| `technical.context_length` | 2,403 | 62.4% |
| `technical.architecture` | 2,437 | 63.2% |
| `technical.model_type` | 2,495 | 64.8% |
| `technical.dtype` | 0 | 0.0% |
| `artifacts.format_flags` | 3,853 | 100.0% |
| `artifacts.total_bytes` | 0 | 0.0% |
| `deployment.vram_fp16_gib` | 2,134 | 55.4% |
| `deployment.vram_int4_gib` | 2,134 | 55.4% |
| `legal.license_raw` | 3,577 | 92.8% |
| `legal.commercial_status` | 3,577 | 92.8% |
| `quality.benchmark_score` | 0 | 0.0% |
| `discovery.downloads` | 3,853 | 100.0% |

## 라이선스 → commercial_status

| commercial_status | 모델 수 | 비율 | 뜻 |
|---|---:|---:|---|
| `permitted` | 2,223 | 57.7% | 선언된 라이선스가 상업 이용을 허용하는 계열 |
| `prohibited` | 260 | 6.7% | 비상업 전용(NC). 상업 질의에서 제외 |
| `review_required` | 1,094 | 28.4% | 추가 약관 확인 필요(llama/gemma/GPL/other 등) |
| `unknown` | 276 | 7.2% | 라이선스 자체가 없음. 판단 불가 |

### 원시 라이선스 값 상위

| license | 모델 수 | 분류 |
|---|---:|---|
| `apache-2.0` | 1,777 | `permitted` |
| `other` | 939 | `review_required` |
| `mit` | 391 | `permitted` |
| `None` | 276 | `unknown` |
| `cc-by-nc-4.0` | 197 | `prohibited` |
| `gemma` | 84 | `review_required` |
| `cc-by-nc-sa-4.0` | 61 | `prohibited` |
| `llama3.1` | 18 | `review_required` |
| `llama3` | 17 | `review_required` |
| `cc-by-4.0` | 16 | `permitted` |
| `cc-by-sa-4.0` | 14 | `permitted` |
| `llama2` | 14 | `review_required` |
| `openmdw-1.1` | 12 | `permitted` |
| `gpl-3.0` | 11 | `review_required` |
| `llama3.2` | 7 | `review_required` |


---

# 소스: `snapshot`

측정 대상 `snapshot` — 레코드 3,872개

## 질문별 답변 가능률

필터가 그 질문을 걸 수 있고, 답에 쓸 사실이 레코드에 있는 모델의 수다.

| 사용자 질문 | 필요한 계약 필드 | 답변 가능 | 비율 |
|---|---|---:|---:|
| Q1 상업 서비스에 쓸 수 있는 한국어 모델 | `legal.commercial_status, capability.korean_verified` | 2,231 | 57.6% |
| Q2 내 GPU(16GB)에서 돌아가는 모델 | `technical.parameter_count_total 또는 artifacts.total_bytes` | 3,109 | 80.3% |
| Q3 Ollama/llama.cpp로 돌릴 수 있는 모델 | `artifacts.gguf` | 1,463 | 37.8% |
| Q4 한국어 임베딩/RAG 모델 | `capability.primary_task, capability.korean_verified` | 436 | 11.3% |
| Q5 긴 문서를 번역할 모델 | `technical.context_length, capability.primary_task` | 2,498 | 64.5% |
| Q6 성능이 가장 좋은 모델 | `quality.benchmark_score` | 439 | 11.3% |
| Q7 내려받아 배포해도 되는 모델 | `legal.commercial_status, identity.gated` | 0 | 0.0% |

## 계약 필드 coverage

| 계약 필드 | 있음 | 비율 |
|---|---:|---:|
| `identity.model_id` | 3,872 | 100.0% |
| `identity.revision` | 0 | 0.0% |
| `identity.last_modified` | 0 | 0.0% |
| `identity.gated` | 0 | 0.0% |
| `capability.primary_task` | 3,872 | 100.0% |
| `capability.languages` | 3,777 | 97.5% |
| `capability.korean_verified` | 3,872 | 100.0% |
| `technical.parameter_count_total` | 3,311 | 85.5% |
| `technical.parameter_count_active` | 0 | 0.0% |
| `technical.context_length` | 3,565 | 92.1% |
| `technical.architecture` | 3,706 | 95.7% |
| `technical.model_type` | 3,722 | 96.1% |
| `technical.dtype` | 0 | 0.0% |
| `artifacts.format_flags` | 3,872 | 100.0% |
| `artifacts.total_bytes` | 0 | 0.0% |
| `deployment.vram_fp16_gib` | 3,109 | 80.3% |
| `deployment.vram_int4_gib` | 3,109 | 80.3% |
| `legal.license_raw` | 3,595 | 92.8% |
| `legal.commercial_status` | 3,595 | 92.8% |
| `quality.benchmark_score` | 439 | 11.3% |
| `discovery.downloads` | 3,872 | 100.0% |

## 라이선스 → commercial_status

| commercial_status | 모델 수 | 비율 | 뜻 |
|---|---:|---:|---|
| `permitted` | 2,231 | 57.6% | 선언된 라이선스가 상업 이용을 허용하는 계열 |
| `prohibited` | 260 | 6.7% | 비상업 전용(NC). 상업 질의에서 제외 |
| `review_required` | 1,104 | 28.5% | 추가 약관 확인 필요(llama/gemma/GPL/other 등) |
| `unknown` | 277 | 7.2% | 라이선스 자체가 없음. 판단 불가 |

### 원시 라이선스 값 상위

| license | 모델 수 | 분류 |
|---|---:|---|
| `apache-2.0` | 1,784 | `permitted` |
| `other` | 949 | `review_required` |
| `mit` | 392 | `permitted` |
| `None` | 277 | `unknown` |
| `cc-by-nc-4.0` | 197 | `prohibited` |
| `gemma` | 84 | `review_required` |
| `cc-by-nc-sa-4.0` | 61 | `prohibited` |
| `llama3.1` | 18 | `review_required` |
| `llama3` | 17 | `review_required` |
| `cc-by-4.0` | 16 | `permitted` |
| `llama2` | 14 | `review_required` |
| `cc-by-sa-4.0` | 14 | `permitted` |
| `openmdw-1.1` | 12 | `permitted` |
| `gpl-3.0` | 11 | `review_required` |
| `llama3.2` | 7 | `review_required` |

