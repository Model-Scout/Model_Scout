---
type: "dataset"
id: "MAximeSobrier/WiLI-2018-corrected"
source: "huggingface"
url: "https://huggingface.co/datasets/MAximeSobrier/WiLI-2018-corrected"
downloads: 46
summary: "WiLI-2018 데이터셋의 오류를 수정한 다국어 문장 데이터로 언어 식별에 사용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# MAximeSobrier/WiLI-2018-corrected

> dataset · [Hugging Face](https://huggingface.co/datasets/MAximeSobrier/WiLI-2018-corrected)

WiLI-2018 데이터셋의 오류를 수정한 다국어 문장 데이터로 언어 식별에 사용됨.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories = `text-classification` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:classification = `sentence,label` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `sentence,label` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `232 languages` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `odbl` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `WiLI-2018, the Wikipedia language identification benchmark dataset` · 신뢰도 medium
- **데이터 용도**: [[평가용]] — ner · readme = `test.csv: 168 lines removed, 1283 labels updated` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `train.csv: 127 lines removed, 1157 labels updated` · 신뢰도 medium
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high
