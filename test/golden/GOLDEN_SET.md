# Semantic 골든셋 데이터 설명

이 문서는 골든셋 파일에 **어떤 정보가 어디서 왔고, 각 항목이 무엇을 뜻하는지** 설명한다. 실행 방법과 폴더 구성은 [README.md](README.md)를 본다.

## 한눈에 보기

| 항목 | 값 |
|---|---|
| 원자료 | 한국어 프로젝트의 오픈 모델 선정 사례 57건 (1차 32 + 2차 25) |
| 골든셋 질의 | **28개** (`labels/golden_queries.jsonl`), 모두 현재 DB로 채점 가능 |
| 골든셋에서 뺀 질의 | 12개 (`labels/recall_check_queries.jsonl`). 정답 모델이 DB에 없어 Stage 1 수집 점검용으로만 사용 |
| 정답 형태 | 질의별 Hugging Face 모델 ID 목록 (정답 · 허용 · 제외 · 경고 필요) |
| 작성일 | 2026-09-26 ~ 2026-09-30 |

## 1. 정보를 어디서 가져왔나

### 수집 방법

Claude·GPT 웹 검색으로 "한국어 프로젝트에서 어떤 오픈 모델을 어떤 조건 때문에 골랐는지"가 드러난 글을 모았다. 2회 수집했다.

| 차수 | 건수 | 수집 조건 | 파일 |
|---|---:|---|---|
| 1차 | 32 | 한국어 프로젝트의 모델 선정 사례 전반 (파인튜닝 포함) | `sources/korean_model_selection_cases_round1.jsonl` |
| 2차 | 25 | **추가 학습 없이** 모델을 그대로 쓴 사례만. 상업 라이선스 사례 우선, 1차 URL 제외 | `sources/korean_model_selection_cases_round2.jsonl` |

### 출처 종류

| 출처 | 1차 | 2차 | 예시 |
|---|---:|---:|---|
| GitHub 저장소·이슈·PR | 14 | 22 | 부트캠프 과제, 개인 프로젝트의 모델 선정 기록 |
| 블로그·커뮤니티 글 (`real_case`) | 8 | 3 | velog, 아카라이브, 기업·개인 기술 블로그 |
| 벤치마크 글 | 5 | 0 | AutoRAG 한국어 임베딩 비교, VARCO-VISION 발표 |
| 대회 풀이 | 5 | 0 | DACON, 부스트캠프 대회 |

- 57건 모두 URL이 실제로 존재함을 확인했다(직접 열람 55, 검색으로 확인 2).
- 작성일은 2021-08 ~ 2026-09이며, 30건은 작성일을 확인하지 못했다.
- 사례 신뢰도(`confidence`)는 high 12 · medium 26 · low 19다. low는 모델을 비교하지 않고 사용만 기록한 경우다.

### 사례 중 골든셋에 쓴 것

| 사례 분류 (`usage_label`) | 1차 | 2차 | 처리 |
|---|---:|---:|---|
| `golden` | 10 | 17 | 질의로 만들고 정답 부여 |
| `recall_check` | 6 | 4 | 질의로 만들었지만 정답 모델이 DB에 없어 골든셋에서 제외 (`recall_check_queries.jsonl`) |
| `abstention` | 1 | 0 | 정답 없이 경고 동작만 채점 |
| `out_of_scope_finetune` | 14 | 0 | 제외. 파인튜닝할 베이스 모델을 고른 사례라 서비스 범위("추가 학습 없이 사용") 밖 |
| `no_label` | 1 | 4 | 제외. 모델 ID를 특정할 수 없거나 HF 모델이 아님 |

## 2. 사례 파일의 정보 (`sources/`)

사례 한 줄이 글 하나다. 웹 리서치가 채운 값이며 사람이 편집하지 않는다.

| 필드 | 내용 | 예시 |
|---|---|---|
| `case_id`, `round` | 사례 ID와 수집 차수 | `r2-b001`, `2` |
| `source_type`, `source_url` | 출처 종류와 주소 | `github`, 저장소 URL |
| `org_or_author`, `published_date` | 작성 주체와 날짜 | |
| `project_summary` | 프로젝트 한 줄 요약 | "게임 버그 리포트를 노트북에서 분류하는 로컬 LLM 선정" |
| `requirement_quote` | 요구사항이 드러난 **원문 인용** (없으면 null) | "외부 API 전송이 불가" |
| `conditions` | 글에서 읽어낸 조건: task, 라이선스, 실행 환경, VRAM, 최대 크기, context, 파인튜닝 여부 | |
| `selected` | 최종 선택한 모델 ID, 별칭, 선택 이유 원문, 이유 태그 | `Qwen/Qwen2.5-7B-Instruct` |
| `rejected_or_compared` | 비교했거나 탈락시킨 모델과 이유 | Llama 3.1 (라이선스 조건) |
| `reported_metrics` | 글에 적힌 수치 | CER, recall@5, VRAM 사용량 |
| `confidence` | 사례 신뢰도 high / medium / low | |
| `url_check` | URL 확인 결과와 날짜 | `exists_fetched` |
| `usage_label` | 골든셋에서의 용도 (위 표) | |

이유 태그(`reason_tags`)는 `korean_quality`, `license_commercial`, `license_restricted`, `model_size`, `memory`, `speed`, `cpu_runnable`, `long_context`, `cost`, `accuracy_benchmark`, `other` 중에서 고른다.

## 3. 골든셋 질의의 정보 (`labels/golden_queries.jsonl`)

사례 하나를 **사용자가 서비스에 입력할 법한 요구사항 문장**으로 바꾸고, 정답을 붙인 것이다. 사람이 편집하는 원본이다. 골든셋에서 뺀 `recall_check_queries.jsonl`도 같은 형식이다.

### 예시 (g021)

```json
{
  "query_id": "g021",
  "source_case_id": "r2-b001",
  "label_type": "golden",
  "query": "유저 계정과 미출시 콘텐츠가 담긴 한국어 게임 버그 리포트를 QA 담당자 노트북에서 분류·정리할 로컬 LLM이 필요해. 외부 API로 보낼 수 없고, Q4 양자화 기준 7~8B급이 상한이야. 회사 업무라 상업적으로 쓸 수 있어야 해.",
  "conditions": {"tasks": ["text-generation"], "language": "ko", "license_requirement": "commercial",
                 "runtime": "gpu", "gpu_vram_gb": 8.0, "max_params_b": 8.0, "min_context": null, "finetune_planned": false},
  "expected_behavior": "recommend",
  "expected_any": ["Qwen/Qwen2.5-7B-Instruct", "unsloth/Qwen2.5-7B-Instruct", "ThomasBaruzier/Qwen2.5-7B-Instruct-GGUF", "..."],
  "needs_review": [{"model_id": "meta-llama/Llama-3.1-8B-Instruct", "reason": "Llama 3.1 Community License 조건"}],
  "evidence_quote": "유저 계정·미출시 콘텐츠가 포함되어 외부 API 전송이 불가",
  "evaluable_now": true
}
```

### 필드

| 구분 | 필드 | 내용 |
|---|---|---|
| 연결 | `query_id`, `source_case_id`, `source_url` | 질의 ID와 근거 사례 |
| 입력 | `query` | 사례를 바탕으로 쓴 자연어 요구사항. 사례의 제약(보안, 하드웨어, 라이선스)을 문장에 담았다 |
| 조건 정답 | `conditions.tasks` | DB의 task 분류에 맞춘 목록. 예: 번역을 LLM으로 한 사례는 `translation` + `text-generation` |
| | `conditions.license_requirement` | `commercial`(상업 이용 필수) · `any`(상관없음) · `unknown`(글에 없음) |
| | `conditions.runtime`, `gpu_vram_gb`, `max_params_b`, `min_context` | 실행 환경과 크기 제약 |
| 정답 | `expected_any` | 이 중 하나가 top-5에 있으면 정답. 사례가 고른 모델과, 원본이 DB에 없을 때는 DB의 변환본(GGUF 등) |
| | `acceptable` | 추천돼도 틀리지 않은 모델. 사례에서 비교 후 근소하게 밀린 모델, 같은 모델의 다른 형식 |
| | `must_exclude` | 추천되면 치명적 오류인 모델과 위반 규칙. 예: 상업 조건인데 비상업(NC) 라이선스 |
| | `needs_review` | 추천하려면 `확인 필요` 경고가 붙어야 하는 모델. 예: 조건부 라이선스 |
| 채점 방식 | `expected_behavior` | `recommend`(정답을 찾아야 함) · `must_exclude_only`(제외 모델만 안 나오면 됨) · `warn_on_oversize`(크기 초과 모델에 경고) |
| | `label_type` | `golden` · `derived_counterfactual` · `abstention` · `blocked` · `recall_check` |
| | `evaluable_now`, `blocked_by` | 지금 채점 가능한지, 막힌 이유 |
| 근거 | `evidence_quote` | 정답이나 조건을 뒷받침하는 원문 인용 (골든셋 28개 중 23개) |
| | `source_verification` | 원문을 직접 열어 대조한 결과: 상태(`confirmed` / `confirmed_with_correction`), 확인일, 사용 모델 확인 여부, 조건 확인 여부, 확인한 원문 요지 |
| | `reliability` | 신뢰도 등급(A/B/C), 사례 신뢰도, 원문 확인 여부, 변환본 매핑 여부, 주의 사항. `audit_golden.py`가 계산해 채우며 직접 수정하지 않는다 |
| | `notes`, `known_failure_cause` | 라벨링 판단 메모, 실패해도 검색 문제가 아닌 알려진 원인 |

`labels/semantic_golden_queries.jsonl`은 위 파일을 `convert_golden.py`가 검색 스크립트(`05_validate_retrieval.py`) 형식으로 바꾼 것이다. 조건 필드 이름이 `max_parameters_billion`, `korean_required` 등으로 바뀌고 라벨은 `labels` 안에 들어간다. 직접 수정하지 않는다.

## 4. 구성 통계

### 유형

| label_type | 개수 | 채점 | 설명 |
|---|---:|---|---|
| `golden` | 25 | ✅ | 실제 사례 기반, 정답이 DB에 있음 |
| `derived_counterfactual` | 2 | ✅ | 실제 사례에 상업 조건만 추가한 파생 질의 (g003, g016) |
| `abstention` | 1 | ✅ | 정답 없이 크기 경고만 채점 (a001) |

골든셋에서 뺀 12개는 `recall_check` 11개(정답 모델이 DB에 없음)와 `blocked` 1개(g001, 정답 변환본의 DB 라이선스가 `other`)다.

### 골든셋 28개의 특징

| 특징 | 분포 |
|---|---|
| task | ASR 9 · text-generation 6 · 임베딩 4 · summarization 3 · translation 3 · image-text-to-text 2 · text-classification 1 · question-answering 0 |
| 채점 방식 | recommend 24 · must_exclude_only 3 · warn_on_oversize 1 |
| 라이선스 조건 | commercial 6 · any 9 · unknown 13 |
| 실행 환경 | gpu 11 · on_prem 11 · cpu 6 |
| 크기 제약 | VRAM 명시 12 · 최대 파라미터 명시 2 |
| 여러 task로 확장한 질의 | 9 |
| 정답 모델 수 (recommend 평균) | expected_any 2.2개 · acceptable 1.8개 |
| 수집 차수 | 1차 10 · 2차 18 |
| 신뢰도 등급 | A 3 · B 17 · C 8 ([reports/golden_audit.md](reports/golden_audit.md)) |

신뢰도 등급 기준은 A: 사례 신뢰도 high·원문 인용 있음·사례가 고른 원본 모델이 그대로 정답, B: medium이거나 변환본으로 매핑해야 정답에 도달, C: low다.

## 5. 원문 확인 결과 (2026-10-01)

골든셋 28개의 근거가 된 사례 25건(URL 21개)을 직접 열어 대조했다.

- **25건 모두 원문이 존재하고, 사례가 고른 모델을 실제로 사용했음을 확인했다.** 라이선스 탈락 근거(g016, g030의 EXAONE 비상업 라이선스, g021의 Llama 3.1 조건)도 원문 문장으로 확인했다.
- 질의로 옮기는 과정의 오류 2건을 고쳤다.
  - **g008**: 원문은 large-v3를 RTX 3060 12GB 이상에서 권장한다. 질의의 VRAM 조건을 8GB에서 12GB로 수정했다.
  - **g019**: "GPU 없는 PC·오프라인" 조건이 원문에 없어 질의에서 뺐다. 원문에 있는 "RAM 4GB 이상"만 남겼다.
- 선택 이유가 원문에 없는 사례가 있다: g013(e5-small), g014(KR-FinBERT, 기존 파이프라인과의 일관성만 언급), g022(qwen2.5:7b). 모델을 썼다는 사실은 맞지만 "왜 골랐는지"는 근거가 없다. 셋 다 등급이 B 이하다.
- 질의별 확인 내용은 `labels/golden_queries.jsonl`의 `source_verification.note`에 있다.

### 신뢰도 등급 분포

| 등급 | 개수 | 질의 | 기준 |
|---|---:|---|---|
| A | 3 | g005, g015, g016 | 사례 신뢰도 high, 원문 인용 있음, 원문 직접 확인, 사례가 고른 원본 모델이 그대로 정답 |
| B | 17 | 나머지 | 사례 신뢰도 medium이거나, 변환본(GGUF 등)으로 매핑해야 정답에 도달 |
| C | 8 | g007, g008, g013, g014, g017, g018, g019, g020 | 사례 신뢰도 low (모델 비교 없이 사용만 기록) |

등급은 라벨 파일의 `reliability.tier`와 [reports/golden_audit.md](reports/golden_audit.md)에서 볼 수 있다. 채점 리포트도 등급별 점수를 따로 보여 준다.

## 6. 이 데이터의 성격과 한계

- **정답은 "실제 프로젝트가 고른 모델"이다.** 기록이 정확한지(사례를 틀리지 않게 옮겼는지)는 점검했지만, 그 모델이 조건에 맞는 **최선의 답**인지는 보장하지 않는다. 한 팀의 선택이고, 정답이 대부분 한두 개라 조건을 만족하는 다른 좋은 모델을 찾으면 오답으로 집계된다.
- **변환본 매핑이 많다.** 원본이 DB에 없어 unsloth·bartowski 등의 변환본을 정답으로 넣은 질의가 B등급의 대부분이다. 사례 작성자가 그 변환본을 고른 것은 아니다.
- **task가 치우쳐 있다.** ASR이 채점 가능 질의의 3분의 1이고 question-answering은 없다. 전체 점수보다 task별 점수를 함께 본다.
- **질의 수가 작다.** 28개라 hit@k의 신뢰구간이 넓다.

정답의 정확도를 높이려면 질의마다 DB 후보를 모아 두 사람이 기준(필수 조건 통과·용도 근거)에 따라 0/1/2점으로 판정하고, 두 사람의 일치도를 함께 보고하는 방식으로 보완한다.
