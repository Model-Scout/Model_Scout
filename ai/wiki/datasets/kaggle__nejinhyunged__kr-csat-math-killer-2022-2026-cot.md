---
type: "dataset"
id: "kaggle/nejinhyunged/kr-csat-math-killer-2022-2026-cot"
source: "kaggle"
url: "https://www.kaggle.com/datasets/nejinhyunged/kr-csat-math-killer-2022-2026-cot"
downloads: 21
summary: "한국 대학수학능력시험 수학 킬러 문제(2022-2026) 고난도 추론 벤치마크 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
  - "[[질의응답]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[교육]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/nejinhyunged/kr-csat-math-killer-2022-2026-cot

> dataset · [Kaggle](https://www.kaggle.com/datasets/nejinhyunged/kr-csat-math-killer-2022-2026-cot)

한국 대학수학능력시험 수학 킬러 문제(2022-2026) 고난도 추론 벤치마크 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `Every problem includes a meticulously structured, step-by-step reasoning trace.` · 신뢰도 low
- **작업**: [[질의응답]] — ner · readme = `A high-difficulty reasoning benchmark featuring the most challenging math proble` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering = `instruction: Task-specific prompts for the model.input: The translated problem statement including LaTeX formulas.` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering = `output: A detailed "Reasoning Path" followed by the final answer in a $\boxed{...}$.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `Apache 2.0` · 신뢰도 high
- **도메인**: [[교육]] — ner · readme = `from the South Korean College Scholastic Ability Test (CSAT/Suneung)` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `optimized for direct fine-tuning and instruction tuning.` · 신뢰도 medium
