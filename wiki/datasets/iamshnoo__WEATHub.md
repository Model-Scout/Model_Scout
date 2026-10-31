---
type: "dataset"
id: "iamshnoo/WEATHub"
source: "huggingface"
url: "https://huggingface.co/datasets/iamshnoo/WEATHub"
downloads: 126
summary: "WEATHub은 24개 언어의 단어 연관성을 측정해 언어 모델 내 편향을 분석하는 데이터셋입니다."
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
  - "[[한국어]]"
  - "[[다국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# iamshnoo/WEATHub

> dataset · [Hugging Face](https://huggingface.co/datasets/iamshnoo/WEATHub)

WEATHub은 24개 언어의 단어 연관성을 측정해 언어 모델 내 편향을 분석하는 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `- `bias_eval` : The dataset is used to measure biased associations.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `It contains words organized into groups of (target1, target2, attribute1, attribute2)` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `It contains words organized into groups of (target1, target2, attribute1, attribute2)` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `24 languages` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `WEATHub is a dataset containing 24 languages.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `This dataset corresponds to the data described in the paper "Global Voices, Local Biases: Socio-Cultural Prejudices across Languages"` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high
