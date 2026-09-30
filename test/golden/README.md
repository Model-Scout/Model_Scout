# Semantic 골든셋 (실제 모델 선정 사례 기반)

> 데이터가 어디서 왔고 각 필드가 무엇인지는 [GOLDEN_SET.md](GOLDEN_SET.md)에 정리돼 있다.

기존 [`retrieval_queries.jsonl`](../retrieval_queries.jsonl)은 조건(task·한국어·크기)만 검사하는 constraint 골든셋이다. 이 디렉터리는 **질의별 정답 모델 ID**를 붙인 semantic 골든셋이다. 정답은 실제 프로젝트·블로그·대회에서 한국어 모델을 고른 사례에서 가져왔다.

## 폴더 구성

```text
test/golden/
├── README.md                  이 문서
├── GOLDEN_SET.md              골든셋 데이터 설명 (출처, 필드, 구성 통계, 한계)
├── stage1_recall_gaps.md      DB에 없는 정답 모델과 Stage 1 규칙 변경 제안
├── convert_golden.py          labels/golden_queries.jsonl → labels/semantic_golden_queries.jsonl
├── audit_golden.py            라벨 점검 → reports/golden_audit.*
├── run_bm25_golden.py         API 키 없이 BM25 검색 → reports/semantic_golden_retrieval_bm25.json
├── sources/                   원자료 (웹 리서치 결과, 수정하지 않음)
│   ├── korean_model_selection_cases_round1.jsonl   1차 사례 32건 (c001~c032)
│   └── korean_model_selection_cases_round2.jsonl   2차 사례 25건 (r2-a001 등, 추가 학습 없이 쓴 사례)
├── labels/                    골든셋
│   ├── golden_queries.jsonl           질의 40개와 정답 라벨. 사람이 편집하는 유일한 원본
│   └── semantic_golden_queries.jsonl  자동 생성. 05_validate_retrieval.py 실행 형식 (직접 수정 금지)
└── reports/                   자동 생성 결과 (스크립트로 재생성)
    ├── golden_audit.md / .json                        라벨 신뢰도 등급과 정합성 점검
    ├── semantic_golden_retrieval_bm25.json            BM25 검색 결과
    └── semantic_golden_evaluation_bm25_offline.md / .json   BM25 기준선 채점
```

라벨을 고칠 때는 `labels/golden_queries.jsonl`만 수정하고 `convert_golden.py` → `audit_golden.py` 순서로 다시 실행한다. vector 검색 결과(`semantic_golden_retrieval.json`)와 그 채점 결과도 `reports/`에 생긴다.

### 질의 ID

`golden_queries.jsonl`은 label_type 순서(golden → derived_counterfactual → abstention → blocked → recall_check)로, 같은 유형 안에서는 ID 순으로 정렬돼 있다. ID는 리포트·커밋과 연결돼 있어 바꾸지 않는다. 그래서 접두어가 현재 유형과 다를 수 있다. **유형은 항상 `label_type` 필드가 기준이다.**

| 접두어 | 처음 만든 용도 | 현재 유형과 다른 것 |
|---|---|---|
| `g` | 사례 기반 질의 | g001은 blocked, g011·g012는 recall_check, g003·g016은 derived_counterfactual |
| `r` | recall_check | - |
| `a` | abstention (크기 경고) | - |

사례 ID는 1차가 `c001`~`c032`, 2차가 `r2-` 접두어(`r2-a001`, `r2-b001`, `r2-c101` 등)다. 각 질의의 `source_case_id`로 원 사례를 찾는다.

## 실행

```bash
python test/golden/convert_golden.py          # 라벨 원본 → 실행 스키마
python test/golden/audit_golden.py            # 라벨 점검 (API 불필요)

# 실제 서비스 검색(dense). OPENAI_API_KEY 필요, 질의 40개 임베딩
python 05_validate_retrieval.py --execute \
    --query-file test/golden/labels/semantic_golden_queries.jsonl \
    --report-json test/golden/reports/semantic_golden_retrieval.json \
    --report-md test/golden/reports/semantic_golden_retrieval.md
python test/evaluate_semantic_golden.py

# 키 없이 BM25 기준선 (수 분 소요)
python test/golden/run_bm25_golden.py
python test/evaluate_semantic_golden.py --report test/golden/reports/semantic_golden_retrieval_bm25.json
```

채점 결과는 검색 모드별로 `reports/semantic_golden_evaluation*.md`와 `.json`에 기록된다. `--execute` 없이 `05_validate_retrieval.py`를 돌리는 `lexical_offline` 모드는 정수 점수 동점이 많아(동점이면 model_id 역순) 쓰지 않는다.

### BM25 기준선 결과 (2026-09-30)

채점 가능 28개 중 recommend 24개에서 hit@5는 1/24다. 이 수치는 dense 검색 성능을 뜻하지 않는다.

- 질의는 한국어인데 Stage 4 문서는 대부분 영어 README라 BM25 토큰이 거의 겹치지 않는다. 형태소 분석도 없다.
- 24개 모두 정답이 hard filter를 통과했다. 라벨과 필터는 맞물린다.
- **11/24는 정답이 후보에 있었지만 canonical 중복 제거에서 사라졌다.** 같은 canonical을 가진 변환본·파인튜닝 모델이 먼저 오면 정답 행이 제거된다. 검색기 쪽 문제로 `stage1_recall_gaps.md`에 기록했다.
- must_exclude 위반은 0/28이고, 상업 조건 질의 6개 중 1개(g030)에서 비상업 라이선스 모델이 top-5에 나왔다. 검색기에 라이선스 필터가 없기 때문이다.

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
| `golden` | 25 | g002, g004~g010, g013~g015, g017~g030 | 지금 DB로 채점 가능 |
| `derived_counterfactual` | 2 | g003, g016 | 원 사례에 상업 조건만 추가한 파생 케이스. 실제 사례와 분리해서 보고 |
| `abstention` | 1 | a001 | 정답 모델 없음, 크기 경고 여부만 채점 |
| `blocked` | 1 | g001 | 정답 GGUF의 DB 라이선스가 `other`라 상업 조건에서 탈락. 원본 라이선스 역추적 전엔 통과 불가 |
| `recall_check` | 11 | g011, g012, r001~r009 | 정답 모델이 DB에 없음. Stage 1 규칙 변경 후 통과 여부로 recall 개선 확인 |

전체 40개 중 지금 채점되는 질의는 28개(`evaluable_now=true`)다. 그중 recommend 24개, must_exclude_only 3개(g003, g016, g030), warn_on_oversize 1개(a001)다.

채점 가능한 질의의 task 분포는 ASR 9 · text-generation 6 · 임베딩 4 · summarization 3 · translation 3 · image-text-to-text 2 · text-classification 1 · question-answering 0이다. 전체 점수보다 task별 표를 함께 본다.

## 라벨 신뢰도

`audit_golden.py`가 질의마다 두 가지를 점검한다.

1. **DB 정합성**: 정답이 검색기와 같은 hard filter를 통과하는지, must_exclude가 실제로 규칙을 위반하는지, 상업 조건 질의의 정답이 비상업 라이선스가 아닌지 본다. 하나라도 어긋나면 라벨 오류로 보고, 오류가 0이어야 점수를 믿는다. 현재 오류 0건.
2. **근거 강도(등급)**: A는 사례 confidence high·원문 인용 있음·원본 모델이 그대로 정답. B는 medium이거나 변환본 매핑이 필요한 경우. C는 low(비교 없이 사용만 기록). 현재 채점 가능 28개가 A 3 · B 17 · C 8이다.

채점 리포트는 등급별 표와 hit@k의 95% 부트스트랩 구간을 함께 보여 준다. 질의 수가 적어 구간이 넓으므로, 두 검색 방식의 차이가 구간 안이면 우열을 주장하지 않는다.

점검이 보장하지 않는 것과 보완 방법:

- **정답 누락(false negative)**: 사례에 없던 더 좋은 모델이 DB에 있으면 검색이 맞아도 오답이 된다. dense 결과가 나오면 틀린 질의의 top-5를 사람이 보고, 조건에 맞는 모델은 `acceptable`에 추가한다.
- **라벨러 판단**: 사례를 질의로 옮긴 판단(조건 해석, 매핑)은 한 사람이 했다. 팀원 한 명이 질의 10개 정도를 원문과 대조해 조건·정답에 동의하는지 표시하고, 불일치 비율을 이 문서에 기록하면 라벨 일치도를 보고할 수 있다.

## 사례를 라벨로 옮길 때 내린 판단

- **c003 (DoctorChat)**: Polyglot-ko를 의료 데이터로 파인튜닝한 사례라 범위 밖으로 뺐다. 파인튜닝 베이스 선정 사례 14건은 모두 `out_of_scope_finetune`이다.
- **c023**: 작성자는 TranslateGemma를 포기하고 Qwen3.5-4B를 골랐다. 정답은 Qwen3.5-4B이고 DB에 없어 recall_check(r003)다.
- **c027**: 원문은 Mac mini 16GB에 `batisay-ko-base`(Apache 2.0)를 권장한다. turbo는 "30분 이상 장문 통화 실시간" 조건일 때의 권장이다.
- **c021**: 탈락 이유가 주로 번역 품질이고 선택 모델 NHNDQ의 라이선스(CC-BY-4.0 표기, 베이스는 CC-BY-NC)가 불확실해 라이선스 검증에는 쓰지 않았다.
- **c002 (EEVE)**: 파인튜닝 없이 GGUF를 골라 쓴 사례라 포함했지만 정답이 DB에 없어 recall_check(g011)다.
- GGUF만 DB에 있는 경우(g001, g009) 원본과 GGUF 변환본을 모두 `expected_any`에 넣었다.
- **2차 사례**: 원본이 DB에 없으면 DB의 공식·주요 변환본(unsloth, bartowski, ThomasBaruzier, -hf 등)을 정답에 넣었다(g021~g029). abliterated·uncensored 파생 모델은 넣지 않았다.
- **r2-b001**: Llama 3.1은 MAU 7억 초과 시에만 별도 계약이 필요한 라이선스라 must_exclude가 아니라 needs_review로 넣었다.
- **r2-b004**: 작성자가 "상업적으로 쓰려면 답변 모델을 바꿔야 합니다"라고 적어 상업 조건 파생 질의(g016)를 만들었다.
- **r2-b002**: 선택 모델 Qwen3의 크기가 미정이라 정답 없이 EXAONE 4.0 제외 여부만 채점한다(g030).
- AUTUNE 이슈(NLI 모델 라이선스 탈락)는 최종안이 파인튜닝이라 넣지 않았다.

## 알려진 한계

- 라이선스 판정은 채점용 임시 정책이다. apache-2.0·mit 등은 상업 허용, 이름에 `nc`가 들어가면 위반, `other`·gemma·llama·미기재는 `확인 필요`로 본다. `05_validate_retrieval.py`는 아직 라이선스와 VRAM으로 필터하지 않는다.
- 검색 결과에 `확인 필요` 경고 필드가 아직 없어서, 경고가 필요한 모델이 top-k에 나오면 모두 경고 누락으로 집계된다.
- 정답·허용 순위는 model_id 완전 일치만 센다. canonical_model_id는 선언된 base model을 따르기 때문에(예: `NCSOFT/VARCO-VISION-14B` → `Qwen/Qwen2.5-14B-Instruct`) 다른 파인튜닝 모델도 같은 계열로 묶인다. 계열 일치는 별도 열로만 보고한다.
- 채점 가능한 질의가 28개라 여전히 작고 task가 치우쳐 있다. question-answering은 0개다.
- 상업 라이선스 조건이 있는 질의는 채점 가능 28개 중 6개다.
- 변환본으로 매핑한 정답이 많다(B등급 대부분). 원본 역추적을 구현하면 정답을 원본 기준으로 다시 정리해야 한다.
