---
type: "dataset"
id: "chipsnug/ko-quant-loss-v0"
source: "huggingface"
url: "https://huggingface.co/datasets/chipsnug/ko-quant-loss-v0"
downloads: 47
summary: "한국어와 영어의 양자화 손실 차이를 측정한 데이터셋으로, 공개 모델의 정보 손실 비교에 사용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[표 (출력 형식)|표]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[CSV]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# chipsnug/ko-quant-loss-v0

> dataset · [Hugging Face](https://huggingface.co/datasets/chipsnug/ko-quant-loss-v0)

한국어와 영어의 양자화 손실 차이를 측정한 데이터셋으로, 공개 모델의 정보 손실 비교에 사용됨.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `This dataset measures how much more information Korean loses than English when an open model is quantized` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `Q1 — KL vs Q8_0 on parallel text (FLORES-101 devtest, sentences 1–300)` · 신뢰도 high
- **출력 형식**: [[표 (출력 형식)|표]] — ner · readme = `It is a mirror of the result tables in https://github.com/chipsnug/koqloss` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `using the same content in both languages` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `It is a mirror of the result tables in https://github.com/chipsnug/koqloss` · 신뢰도 low
- **데이터 형식**: [[CSV]] — metadata · format = `csv` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high
