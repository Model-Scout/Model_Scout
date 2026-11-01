---
language:
- ko
- en
license: other
license_name: source-rights-retained
pretty_name: yukbimsource — Maritime Rule & Web QA (Korean)
task_categories:
- question-answering
- text-generation
tags:
- maritime
- shipbuilding
- ship-classification
- korean
- synthetic
size_categories:
- 100K<n<1M
extra_gated_heading: "yukbimsource 이용 신청 / Access request"
extra_gated_description: "연구·개발 목적의 공유 데이터입니다. 아래 조건에 동의해야 접근할 수 있으며, 신청은 저장소 관리자가 수동으로 승인합니다. / Access is granted manually for research and development use under the terms below."
extra_gated_prompt: |
  이 데이터셋은 선급 규정 문서와 공개 웹 문서의 일부 인용을 포함합니다. 원문 권리는 각 권리자에게 있으며, 이 저장소는 원문에 대한 어떠한 라이선스도 부여하지 않습니다.
  모든 행은 언어 모델이 생성하고 언어 모델이 검사한 후보이며, 사람 검토를 거치지 않았습니다. 규정 준수, 설계, 안전 판단의 근거로 사용할 수 없습니다.

  This dataset contains excerpts of classification-society rules and public web documents. Source content retains its original rights; no license to the source content is granted. All rows are model-generated and model-checked candidates without human review and must not be used as the basis for compliance, design or safety decisions.
extra_gated_fields:
  이름 / Name: text
  소속 / Affiliation: text
  이메일 / Email: text
  사용 목적 / Intended use:
    type: select
    options:
    - 연구 / Research
    - 모델 학습·평가 / Model training or evaluation
    - other
  "원문 권리를 존중하고, 원문 인용을 재배포하지 않으며, 데이터를 제3자에게 다시 공유하지 않는 데 동의합니다 / I agree to respect source rights, not to redistribute source excerpts, and not to re-share this dataset with third parties": checkbox
  "평가 split(eval_rules, eval_web)을 학습에 사용하지 않는 데 동의합니다 / I agree not to train on the evaluation splits (eval_rules, eval_web)": checkbox
configs:
- config_name: rules_qa
  data_files:
  - split: train
    path: data/rules_qa/train-*.parquet
  - split: quarantine
    path: data/rules_qa/quarantine-*.parquet
- config_name: rules_qa_balanced
  data_files:
  - split: train
    path: data/rules_qa_balanced/train-*.parquet
- config_name: web_qa
  data_files:
  - split: train
    path: data/web_qa/train-*.parquet
- config_name: eval_rules
  data_files:
  - split: test
    path: data/eval_rules/test-*.parquet
- config_name: eval_web
  data_files:
  - split: test
    path: data/eval_web/test-*.parquet
---

# yukbimsource — 해사 규정·웹 문서 기반 한국어 QA

선급 규정 문서와 해사 웹 코퍼스([Hibiki12y/Haebimsource](https://huggingface.co/datasets/Hibiki12y/Haebimsource))를 근거로 만든 한국어 질의응답 데이터입니다. 학습 후보 QA와, 학습 원천과 분리된 평가셋을 함께 담고 있습니다.

> **이용 전 확인할 것**
> - 모든 행은 언어 모델이 만들고 언어 모델이 검사한 **후보**입니다. 사람 검토는 하지 않았습니다.
> - 규정 준수, 설계, 안전 판단의 근거로 쓰면 안 됩니다. 실제 판단에는 반드시 원문 규정의 최신판을 확인하세요.
> - 원문 인용의 권리는 각 선급 협회와 웹 문서 권리자에게 있습니다. 이 저장소는 원문에 대한 라이선스를 주지 않습니다(`source-rights-retained`).
> - 접근은 이용 조건에 동의한 사용자에게 관리자가 수동으로 승인합니다. 데이터를 제3자에게 다시 공유하지 마세요.

*English summary: Korean QA pairs grounded in classification-society rules (DNV, ABS, BV, LR, NK, KR, IACS) and maritime web documents, plus two held-out evaluation sets. All rows are model-generated and model-checked candidates (no human review). Source excerpts retain their original rights. Gated: access is approved manually under the terms above.*

## 구성

| config | split | 행 | 내용 |
|---|---|---:|---|
| `rules_qa` | train | 73,105 | 선급 규정 QA 학습 후보 |
| `rules_qa` | quarantine | 130 | 감사용 격리 행. 학습에 쓰지 않음 |
| `rules_qa_balanced` | train | 39,738 | `rules_qa/train`의 재균형 부분집합. **train과 합치면 중복** |
| `web_qa` | train | 166,516 | 해사 웹 문서 QA 후보와 독립 판정 결과 |
| `eval_rules` | test | 1,000 | 선급 규정 평가셋(held-out). 난이도 1/2/3 = 350/433/217 |
| `eval_web` | test | 1,000 | 웹 문서 평가셋(held-out dev/test 문서). 난이도 1/2/3 = 340/596/64 |

```python
from datasets import load_dataset
rules = load_dataset("Hibiki12y/yukbimsource", "rules_qa", split="train")
web = load_dataset("Hibiki12y/yukbimsource", "web_qa", split="train")
ev = load_dataset("Hibiki12y/yukbimsource", "eval_rules", split="test")
```

이용 승인 후 `huggingface-cli login`(또는 `HF_TOKEN`)으로 로그인한 상태에서 읽을 수 있습니다.

## 만든 방법

### 선급 규정 QA (`rules_qa`, `rules_qa_balanced`)
- 원천: 7개 선급(DNV, ABS, BV, LR, NK, KR, IACS) 규정 문서를 조항 단위(unit)로 나눈 266,411개 단위. 인용이 원문과 글자 그대로 같은 단위만 썼습니다.
- 생성과 검증: Qwen3.8-Flash-Next-FP8. 같은 모델이 검증했으므로 독립 검증이 아닙니다. 이후 같은 모델의 self-critique 수정과 용어 수정을 거쳤습니다.
- 답변 형식: 한국어 설명 + 원문 영어 인용 + 출처(문서·조항·쪽).
- 학습 입력 선택: `recommended_for_training=true` 행만 고르고, `recommended_answer_source`가 `original`이면 `original_question`/`original_answer`를 함께 씁니다. 자세한 규칙은 `docs/rules_qa_TRAINING_USE_GUIDE.ko.md`에 있습니다.
- 난이도 3(선급 간 비교, 3,866행)은 비교의 타당성을 전문가가 확인하기 전까지 학습 권장에서 제외했습니다.

### 웹 문서 QA (`web_qa`)
- 원천: Haebimsource의 학습 분할(train split) 문서 중 해사 관련 점수가 높은 문서에서 고른 500–2,000토큰 구간. 평가 문서, 규정 embargo 원문, 참고 교재와 겹치는 구간은 뺐습니다.
- 생성: Qwen3.8-Flash-Next-FP8. 원문 구간을 정확히 인용하고, 숫자·단위·양태·한국어 검사(HARD)와 같은 모델의 자체 검증을 통과한 행만 남겼습니다.
- 독립 판정: GLM-5.3-Flash(NVFP4)가 원문과 대조해 판정했습니다(`judge_*` 열).
  - `judge_status=judged` 134,286행: pass 104,241 · minor 23,916 · major 1,158 · reject 2 · incomplete 4,969
  - 나머지 32,230행은 GPU 정비로 판정하지 못했습니다(`judge_status`가 `not_judged` 계열, `judge_*` 열은 비어 있음).
  - 판정기 성능(주입 오류 탐지율 등)과 한계는 `docs/web_qa_judge_REPORT.ko.md`에 있습니다. 근거 없는 주장을 `minor`로 판정하는 경우가 많으므로, 엄격하게 쓰려면 `pass`만 고르는 것을 권합니다.
- `recommended_for_training`은 모두 false입니다. 학습에 쓸 선택 기준은 이용자가 정해야 합니다.

### 평가셋 (`eval_rules`, `eval_web`)
- 학습 원천과 분리된 원천으로 만들었습니다. 선급은 학습 QA가 쓰지 않은 규정 단위, 웹은 Haebimsource의 dev/test 문서입니다.
- 생성과 검증: GPT-6.1 Sol. 항목마다 생성에 참여하지 않은 서로 다른 검증자 두 명이 원문과 대조해 통과시켰습니다.
- 감사: 층화 무작위 100건을 다시 감사하고 탈락 항목을 재판정했습니다. 재판정 후 내용 오류는 선급 0/100, 웹 0/100(수리 후 감사)이었습니다. 모델 감사 추정치이며, 오류가 없다는 보증은 아닙니다.
- 난이도 기준은 `DIFFICULTY_RUBRIC.md`에 있습니다. 1 = 한 문장·목록 조회, 2 = 한 원천 안에서 조건·예외·사례 적용·순서·비교, 3 = 서로 다른 근거 두 개 이상을 결합.
- 중첩 필드(`evidence`, `verifier_*` 등)는 JSON 문자열입니다. `json.loads`로 읽으세요.
- **평가 split을 학습에 쓰지 마세요.** 학습 데이터를 직접 만들 때는 `holdout/*.json`에 적힌 원천(규정 unit과 중복 묶음, 웹 문서·그룹)도 빼야 평가가 오염되지 않습니다.

## 그 밖의 파일

| 경로 | 내용 |
|---|---|
| `holdout/` | 평가셋 원천 목록(학습 제외 대상) |
| `docs/` | 데이터셋별 보고서와 학습 사용 가이드(한국어) |
| `DIFFICULTY_RUBRIC.md` | 난이도 기준 |
| `review/human_eval_samples_20261016/` | 사람 평가용 난이도별 30건 샘플 4종과 평가 시트(csv) |
| `manifest.json` | parquet 파일별 sha256과 행 수 |

`docs/`의 보고서에는 제작 당시의 로컬 경로가 그대로 남아 있습니다. 재현용 기록이며, 이용자 환경의 경로가 아닙니다.

## 한계

- 사람 검토가 없습니다. 모델 판정은 사람 판정과 다를 수 있습니다.
- 선급 규정 QA는 생성과 검증에 같은 모델을 썼습니다.
- 원문 판본은 수집 시점의 판본입니다. 규정이 바뀌었을 수 있습니다.
- 웹 문서의 시점 의존 사실은 질문에 기준 시점이 없는 경우가 있습니다(`time_anchor`, `soft_flags` 참고).
- 언어 분포: 원문은 영어가 대부분이고, 질문과 답변은 한국어입니다.

## 문의

이용 조건, 권리 문제, 오류 신고는 이 저장소의 Discussions 탭으로 알려 주세요.
