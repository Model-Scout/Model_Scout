# Stage 1 수집 누락 점검 목록

작성 2026-09-26 · 근거: 한국어 모델 선정 사례 57건(`korean_model_selection_cases_v2.jsonl` 32건, `korean_model_selection_cases_round2.jsonl` 25건)과 Stage 1~2 데이터 대조 결과

## 요약

- 실무 사례에서 뽑힌 모델이 DB에서 빠지는 원인은 크게 네 가지다: **다국어 모델 강등**, **원본 없이 GGUF 변환본만 수집**, **수집 대상 task 밖(fill-mask)**, **원인 미확인 누락**.
- 가장 영향이 큰 것은 다국어 모델 강등이다. `BAAI/bge-m3`는 한국어 임베딩 사례 3건(c004, c006, c007)에서 모두 1위였는데, 모델 카드 메타데이터에 `ko`가 없어 Fallback으로 분류돼 빠졌다.
- fill-mask 계열(klue/roberta, KcELECTRA 등)은 파인튜닝 베이스 선정 사례에서만 나왔다. 현재 범위가 "추가 학습 없이 사용"이므로 **이 누락은 고칠 필요가 없다**.

## 누락 모델 목록

| 모델 | 근거 사례 | DB 상태 | 원인 | 제안 |
|---|---|---|---|---|
| `BAAI/bge-m3` | c004, c006, c007 (셋 다 1위) | Fallback | 메타데이터에 `ko` 없음 → A_verified 아님 | 다국어 승격 규칙 (A) |
| `Qwen/Qwen3.5-4B` | c023 선택, c001 비교 | Fallback | 다국어, `ko` 태그 없음 | 다국어 승격 규칙 |
| `Qwen/Qwen3.5-9B` | c001 최종 2위 | Fallback | 다국어, `ko` 태그 없음 | 다국어 승격 규칙 |
| `google/gemma-2-9b-it` | c022 비교 | Fallback | 다국어, `ko` 태그 없음 | 다국어 승격 규칙 |
| `PaddlePaddle/PaddleOCR-VL-1.5` | c029 선택 | Likely | 다국어 OCR, `ko` 태그 없음 | 다국어 승격 규칙. 한국어 근거는 MDPBench KO 86.0 |
| `google/gemma-4-E4B-it`, `google/gemma-4-E2B-it` | c001, c018 선택 | 원본 없음, GGUF(batiai 등)만 있음 | 미확인. 가설: pipeline_tag가 수집 9개 task 밖(any-to-any 등)이거나 게이트 동의 필요 | 원본 태그 확인 후 GGUF의 `base_model`로 원본 역추적 (B) |
| `nlpai-lab/KURE-v1` | c006 비교 | 원본 없음, GGUF만 있음 (KURE-v2는 Core) | 미확인 | 원본 역추적 (B) |
| `Qwen/Qwen2.5-VL-7B-Instruct` | c031 선택 | 수집 안 됨 | 미확인. 가설: 언어 태그 없음 + 다국어 강등 | 다국어 승격 규칙 |
| `kakaocorp/kanana-2-3b-instruct` | c001 비교(탈락) | 수집 안 됨 | 미확인. 가설: 게이트 모델이거나 수집 시점 이후 공개 | 수집 로그에서 해당 ID 조회 |
| **`yanolja/EEVE-Korean-Instruct-10.8B-v1.0`** (원본) | c002 (변환본 선택) | **수집 안 됨** | 미확인. 대표적인 한국어 LLM이라 우선 점검 대상 | 수집 로그에서 ID 조회, 제외 사유 확인 |
| `heegyu/EEVE-Korean-Instruct-10.8B-v1.0-GGUF`, `teddylee777/EEVE-Korean-Instruct-10.8B-v1.0-gguf` | c002 선택 | 수집 안 됨 | 원본 누락과 같은 원인 추정 | 원본 수집 후 B안으로 변환본 연결 |
| `batiai/batisay-ko-base` | c027 선택 | 수집 안 됨. 같은 회사 모델은 turbo만 Low Popularity에 있음 | 미확인. 가설: 다운로드 수 기준 미달 | 한국어 전용·Apache 2.0 모델은 인기 기준 완화 검토 |
| `Systran/faster-whisper-small` | c026 선택(기본값) | Core ✅ | — | — |
| `CohereLabs/aya-expanse-8b` | c022 선택 | Core ✅ (cc-by-nc-4.0) | — | — |
| `Qwen/Qwen2.5-7B-Instruct`, `Qwen/Qwen2.5-1.5B-Instruct-GGUF` (원본·공식 GGUF) | r2-b001, r2-b003, r2-b007 | 수집 안 됨. unsloth·ThomasBaruzier 등 변환본만 Core | 미확인. 가장 널리 쓰이는 모델 중 하나라 우선 점검 | 원본 역추적 (B) |
| `dragonkue/bge-reranker-v2-m3-ko` | r2-a003, r2-a004 | 수집 안 됨 | 미확인. 리랭커는 HF task가 text-ranking일 수 있어 수집 task 밖일 가능성 | text-ranking task 수집 여부 결정 |
| `Qwen/Qwen3-ASR-1.7B` | r2-c101, r2-c107 | Fallback. 공식 `-hf` 버전은 Core | 원본 카드에 `ko` 태그 없음 | 다국어 승격 규칙 (A) |
| `Qwen/Qwen3.6-35B-A3B` | r2-b008 | Fallback | 다국어, `ko` 태그 없음 | 다국어 승격 규칙 |
| `mlx-community/*` 변환본 (whisper-large-v3-turbo, gemma-4-e4b-it-4bit) | r2-c102, r2-b006 | 수집 안 됨 | 미확인 | 원본이 있으면 변환본은 원본 추천의 실행 옵션으로 충분 |
| klue/roberta-*, `beomi/KcELECTRA-base`, `monologg/koelectra-base-v3-discriminator` | c008~c014 등 | 수집 안 됨 | HF task가 fill-mask → 수집 대상 밖 | **수정 불필요**. 모두 파인튜닝 베이스 사례 |

## 규칙 변경 제안

### A. 다국어 모델 승격 규칙

현재 규칙 "Multilingual ≠ Korean verified"는 오추천을 막는 데는 안전하지만, 실무자가 가장 많이 고르는 모델을 빠뜨린다. 근거를 기록하는 조건부 승격을 제안한다.

1. 대상: 수집 9개 task 안에 있고, 언어 태그가 `multilingual`이거나 비어 있으며, task별 다운로드 상위 N위 안의 모델.
2. 승격 조건 (하나 이상 충족):
   - README 본문에 한국어 지원 언급 또는 언어 목록에 Korean 포함
   - README에 한국어 벤치마크 수치가 있음 (MIRACL-ko, KMMLU, Ko-MTEB, KsponSpeech 등)
   - 외부 한국어 벤치마크나 사례에서 사용 근거가 있음 (이 사례 목록 활용 가능)
3. 승격된 모델은 `korean_evidence_level = "B_readme"` 같은 별도 등급으로 저장한다. 추천 결과에 "한국어 근거: README 명시(메타데이터 태그 없음)"로 노출해 `확인 필요` 구분을 유지한다.

비용은 README를 읽는 LLM 판정 호출이다. 다운로드 상위 모델로 제한하면 수백 건 수준으로 관리할 수 있다.

### B. GGUF 변환본 → 원본 역추적

GGUF만 있고 원본이 없으면 원본 카드의 라이선스·성능 근거를 쓰지 못하고, 변환본이 원본보다 앞서 추천될 수 있다.

1. 수집한 GGUF의 `base_model` 메타데이터를 따라 원본 repo를 추가 수집한다.
2. 원본과 변환본을 같은 `model_family`로 묶고, 추천은 원본 기준으로 보여 준 뒤 실행 형식(GGUF 양자화본)을 옵션으로 붙인다.

## 메타데이터 공백

모델이 DB에 있어도 아래 공백 때문에 정답이 필터에서 탈락한다. 수집 누락과 원인이 다르므로 따로 관리한다.

| 공백 | 예시 | 영향 | 제안 |
|---|---|---|---|
| task 분류 불일치 | EXAONE-3.5·aya-expanse는 text-generation(사례는 번역), ko-sroberta·bge-m3는 sentence-similarity(사례는 RAG 임베딩), Qwen3.5-4B는 image-text-to-text | 요구에서 뽑은 task 하나로 필터하면 정답이 빠짐 | 조건 추출 단계에 task 확장 표를 둔다. 예: translation·summarization → +text-generation, feature-extraction ↔ sentence-similarity, text-generation → +image-text-to-text |
| GGUF 라이선스 `other` | `batiai/gemma-4-E4B-it-GGUF`, `batiai/gemma-4-E2B-it-GGUF` | 원본이 상업 허용이어도 변환본이 상업 조건 필터에서 탈락 (g001) | B안의 원본 역추적 시 라이선스도 원본에서 상속하고 `license_source = "base_model"`로 표시 |
| parameter_count unknown | nllb-200 계열 3종 | VRAM·크기 조건으로 거를 수 없음 (g005) | safetensors 메타데이터나 파일 크기로 추정값 보강, `param_count_estimated = true` 표시 |
| 파라미터 수와 모델명 불일치 | VARCO-VISION-14B의 실제 파라미터 15.2B | 모델명 기준으로 조건을 잡으면 탈락 | 크기 필터에 약 10% 허용 범위를 두거나, 사용자에게 실제 값 명시 |
| canonical이 base model로 묶임 | `NCSOFT/VARCO-VISION-14B`의 canonical이 `Qwen/Qwen2.5-14B-Instruct` | `dedupe_canonical`이 서로 다른 모델을 하나로 합쳐 후보가 사라짐. BM25 기준선에서 recommend 24개 중 **11개는 정답이 후보에 있었는데 같은 canonical의 다른 행이 먼저 와서 제거됨** (예: `openai/whisper-large-v3` 자리를 turbo 변환본이 차지) | 양자화·형식 변환(GGUF/AWQ/FP8 등)만 canonical로 묶고 파인튜닝은 별도 모델로 유지. 같은 canonical 안에서는 원본을 대표 행으로 우선 |

## Recall 점검으로 쓰는 법

`golden_retrieval_queries_v2.jsonl`에서 `label_type = "recall_check"`인 11개(bge-m3, Qwen3.5-4B, PaddleOCR-VL-1.5, Qwen2.5-VL, EEVE, batisay-ko-base, bge-reranker-v2-m3-ko, Qwen3.6-35B-A3B)는 현재 DB에선 정답이 나올 수 없다. 규칙을 바꾼 뒤 `test/evaluate_semantic_golden.py` 리포트의 "아직 채점하지 않는 질의" 표에서 정답이 DB에 들어왔는지 확인하고, 들어왔으면 `evaluable_now`를 true로 바꿔 채점에 포함한다.
