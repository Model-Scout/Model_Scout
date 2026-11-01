---
type: "dataset"
id: "nlp-with-deeplearning/Ko.WizardLM_evol_instruct_V2_196k"
source: "huggingface"
url: "https://huggingface.co/datasets/nlp-with-deeplearning/Ko.WizardLM_evol_instruct_V2_196k"
downloads: 43
summary: "WizardLM_evol_instruct_V2_196k 데이터셋을 자체 번역기로 한국어로 번역한 대화형 학습 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 생성]]"
  - "[[질의응답]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# nlp-with-deeplearning/Ko.WizardLM_evol_instruct_V2_196k

> dataset · [Hugging Face](https://huggingface.co/datasets/nlp-with-deeplearning/Ko.WizardLM_evol_instruct_V2_196k)

WizardLM_evol_instruct_V2_196k 데이터셋을 자체 번역기로 한국어로 번역한 대화형 학습 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **작업**: [[질의응답]] — metadata · task_categories = `question-answering` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:question_answering = `WizardLM/WizardLM_evol_instruct_V2_196k을 번역한 데이터셋입니다.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering = `WizardLM/WizardLM_evol_instruct_V2_196k을 번역한 데이터셋입니다.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `8` · 신뢰도 medium
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-sa-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `WizardLM/WizardLM_evol_instruct_V2_196k` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `이 데이터 세트에는 알파카와 샤레GPT의 143K 혼합 진화 데이터가 포함되어 있다.` · 신뢰도 low
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `idx` 열 p90 12자 ≈ 8 토큰 (viewer statistics, default/train)
