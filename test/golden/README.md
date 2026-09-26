# Semantic 골든셋 (실제 모델 선정 사례 기반)

기존 [`retrieval_queries.jsonl`](../retrieval_queries.jsonl)은 조건(task·한국어·크기)만 검사하는 constraint 골든셋이다. 이 디렉터리는 **질의별 정답 모델 ID**를 붙인 semantic 골든셋이다. 정답은 실제 프로젝트·블로그·대회에서 한국어 모델을 고른 사례에서 가져왔다.

## 파일

| 파일 | 역할 |
|---|---|
| `korean_model_selection_cases_v2.jsonl` | 원자료. 한국어 모델 선정 사례 32건 (URL 확인 결과 `url_check`, 용도 `usage_label` 포함) |
| `golden_retrieval_queries_v2.jsonl` | 사례에서 만든 질의 18개와 정답 라벨 (중립 스키마, 사람이 편집하는 원본) |
| `convert_golden.py` | 원본을 `05_validate_retrieval.py`가 읽는 스키마로 변환 |
| `semantic_golden_queries.jsonl` | 변환 결과. `--query-file`로 바로 실행 가능 |
| `stage1_recall_gaps.md` | 사례에서 뽑혔지만 DB에 없는 모델과 Stage 1 규칙 변경 제안 |

라벨을 고칠 때는 `golden_retrieval_queries_v2.jsonl`을 수정하고 `convert_golden.py`를 다시 실행한다.

## 실행

```bash
python test/golden/convert_golden.py
python 05_validate_retrieval.py --execute \
    --query-file test/golden/semantic_golden_queries.jsonl \
    --report-json test/golden/semantic_golden_retrieval.json \
    --report-md test/golden/semantic_golden_retrieval.md
python test/evaluate_semantic_golden.py
```

`--execute`는 질의 18개를 `text-embedding-3-small`로 임베딩하므로 `OPENAI_API_KEY`가 필요하다. `--execute` 없이 돌리는 `lexical_offline` 모드는 정수 점수 동점이 많아 순위를 믿을 수 없다(동점이면 model_id 역순). 파이프라인이 돌아가는지만 확인하는 용도로 쓴다.

결과는 `semantic_golden_evaluation.md`와 `.json`에 기록된다.

## 라벨 필드

| 필드 | 뜻 | 채점 |
|---|---|---|
| `query` | 사례에서 재구성한 자연어 요구사항 | 검색 입력 |
| `conditions` | 사례 원문 기준 정답 조건. `tasks`는 DB task 분류에 맞춘 목록 | 조건 추출 정확도 채점용 |
| `expected_any` | 이 중 하나가 top-k에 있으면 정답 | hit@k, MRR |
| `acceptable` | 정답은 아니지만 추천돼도 틀리지 않은 모델 | acceptable hit@k |
| `must_exclude` | 추천되면 치명적 오류 (라이선스·하드웨어·언어 위반) | 1건이라도 나오면 실패 |
| `needs_review` | 추천 시 `확인 필요` 경고가 붙어야 하는 모델 | 경고 없이 나오면 실패 |
| `expected_behavior` | `recommend`, `must_exclude_only`, `warn_on_oversize` | 아래 참고 |
| `evaluable_now` | 현재 DB로 채점 가능한지 | false면 점수에서 제외 |
| `blocked_by` | 막힌 이유 (`answer_not_in_db`, `gguf_license_other`, `param_count_unknown`) | 추적용 |
| `known_failure_cause` | 실패해도 검색 문제가 아닌 경우의 원인 | 리포트에 함께 표시 |

`expected_behavior`

- `recommend` — `expected_any` 중 하나가 top-k에 있고, must_exclude·비상업 라이선스·경고 누락이 없어야 통과.
- `must_exclude_only` — 정답 모델 없이 `must_exclude`와 비상업 라이선스 모델이 top-k에 없으면 통과 (g003).
- `warn_on_oversize` — `warn_rule`의 VRAM 예산을 넘거나 parameter_count가 unknown인 추천 모델에 모두 `확인 필요` 경고가 있어야 통과 (a001).

## label_type

| label_type | 개수 | 질의 | 의미 |
|---|---:|---|---|
| `golden` | 8 | g002, g004~g010 | 지금 DB로 채점 가능 |
| `derived_counterfactual` | 1 | g003 | g002 사례에 상업 조건만 추가한 파생 케이스. 실제 사례와 분리해서 보고 |
| `abstention` | 1 | a001 | 정답 모델 없음, 크기 경고 여부만 채점 |
| `blocked` | 1 | g001 | 정답 GGUF의 DB 라이선스가 `other`라 상업 조건에서 탈락. 원본 라이선스 역추적 전엔 통과 불가 |
| `recall_check` | 7 | g011, g012, r001~r005 | 정답 모델이 DB에 없음. Stage 1 규칙 변경 후 통과 여부로 recall 개선 확인 |

지금 채점되는 질의는 10개(`evaluable_now=true`)다.

## 사례를 라벨로 옮길 때 내린 판단

- **c003 (DoctorChat)**: Polyglot-ko를 의료 데이터로 파인튜닝한 사례라 범위 밖으로 뺐다. 파인튜닝 베이스 선정 사례 14건은 모두 `out_of_scope_finetune`이다.
- **c023**: 작성자는 TranslateGemma를 포기하고 Qwen3.5-4B를 골랐다. 정답은 Qwen3.5-4B이고 DB에 없어 recall_check(r003)다.
- **c027**: 원문은 Mac mini 16GB에 `batisay-ko-base`(Apache 2.0)를 권장한다. turbo는 "30분 이상 장문 통화 실시간" 조건일 때의 권장이다.
- **c021**: 탈락 이유가 주로 번역 품질이고 선택 모델 NHNDQ의 라이선스(CC-BY-4.0 표기, 베이스는 CC-BY-NC)가 불확실해 라이선스 검증에는 쓰지 않았다.
- **c002 (EEVE)**: 파인튜닝 없이 GGUF를 골라 쓴 사례라 포함했지만 정답이 DB에 없어 recall_check(g011)다.
- GGUF만 DB에 있는 경우(g001, g009) 원본과 GGUF 변환본을 모두 `expected_any`에 넣었다.

## 알려진 한계

- 라이선스 판정은 채점용 임시 정책이다. apache-2.0·mit 등은 상업 허용, 이름에 `nc`가 들어가면 위반, `other`·gemma·llama·미기재는 `확인 필요`로 본다. `05_validate_retrieval.py`는 아직 라이선스와 VRAM으로 필터하지 않는다.
- 검색 결과에 `확인 필요` 경고 필드가 아직 없어서, 경고가 필요한 모델이 top-k에 나오면 모두 경고 누락으로 집계된다.
- 정답·허용 순위는 model_id 완전 일치만 센다. canonical_model_id는 선언된 base model을 따르기 때문에(예: `NCSOFT/VARCO-VISION-14B` → `Qwen/Qwen2.5-14B-Instruct`) 다른 파인튜닝 모델도 같은 계열로 묶인다. 계열 일치는 별도 열로만 보고한다.
- 채점 가능한 질의가 10개라 통계적으로 작다. 상업 라이선스 조건이 있는 실제 사례도 2건뿐이다.
