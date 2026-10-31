---
type: "dataset"
id: "ArbelTepper/extended_test_xnli"
source: "huggingface"
url: "https://huggingface.co/datasets/ArbelTepper/extended_test_xnli"
downloads: 142
summary: "XNLI 테스트셋을 14개에서 48개 언어로 확장한 다국어 자연어 추론 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
  - "[[질의응답]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# ArbelTepper/extended_test_xnli

> dataset · [Hugging Face](https://huggingface.co/datasets/ArbelTepper/extended_test_xnli)

XNLI 테스트셋을 14개에서 48개 언어로 확장한 다국어 자연어 추론 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories, task_ids = `text-classification` · 신뢰도 medium
- **작업**: [[질의응답]] — ner · readme = `premise/hypothesis pairs` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:classification, task:question_answering = `text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:question_answering = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `49 languages` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `The XNLI test set extended from 14 to 48 languages` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `The XNLI test set (5,010 premise/hypothesis pairs) for 48 languages` · 신뢰도 medium
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high
