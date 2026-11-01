---
type: "dataset"
id: "Pixel-Linguist/rendered-sts17"
source: "huggingface"
url: "https://huggingface.co/datasets/Pixel-Linguist/rendered-sts17"
downloads: 349
summary: "STS-17 데이터셋의 텍스트를 이미지로 렌더링하여 비전 인코더의 텍스트 이해 능력을 평가하는 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
  - "[[임베딩]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[ar]]"
  - "[[de]]"
  - "[[영어]]"
  - "[[es]]"
  - "[[fr]]"
  - "[[it]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[nl]]"
  - "[[tr]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# Pixel-Linguist/rendered-sts17

> dataset · [Hugging Face](https://huggingface.co/datasets/Pixel-Linguist/rendered-sts17)

STS-17 데이터셋의 텍스트를 이미지로 렌더링하여 비전 인코더의 텍스트 이해 능력을 평가하는 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · task_ids = `text-scoring` · 신뢰도 low
- **작업**: [[임베딩]] — metadata · readme, task_ids = `semantic-similarity-scoring` · 신뢰도 medium
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · modality, readme = `This dataset is rendered to images from STS-17.` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:classification, task:embedding = `text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `We envision the need to assess vision encoders' abilities to understand texts.` · 신뢰도 low
- **언어**: [[ar]] — metadata · languages = `ar` · 신뢰도 high
- **언어**: [[de]] — metadata · languages = `de` · 신뢰도 high
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[es]] — metadata · languages = `es` · 신뢰도 high
- **언어**: [[fr]] — metadata · languages = `fr` · 신뢰도 high
- **언어**: [[it]] — metadata · languages = `it` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `9 languages` · 신뢰도 high
- **언어**: [[nl]] — metadata · languages = `nl` · 신뢰도 high
- **언어**: [[tr]] — metadata · languages = `tr` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `We envision the need to assess vision encoders' abilities to understand texts.` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `A natural way will be assessing them with the STS protocols, with texts rendered into images.` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
