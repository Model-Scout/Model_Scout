---
type: "dataset"
id: "Horizon-Labs/multilingual-zeroshot-synthetic"
source: "huggingface"
url: "https://huggingface.co/datasets/Horizon-Labs/multilingual-zeroshot-synthetic"
downloads: 125
summary: "33개 언어로 된 253,346개 텍스트의 다국어 제로샷 분류용 합성 데이터셋입니다."
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
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# Horizon-Labs/multilingual-zeroshot-synthetic

> dataset · [Hugging Face](https://huggingface.co/datasets/Horizon-Labs/multilingual-zeroshot-synthetic)

33개 언어로 된 253,346개 텍스트의 다국어 제로샷 분류용 합성 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, tags, task_categories = `text-classification` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `253,346 texts in 33 languages, each with a set of candidate labels, the correct label(s), and often a hypothesis template.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `each with a set of candidate labels, the correct label(s), and often a hypothesis template.` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `34 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `256` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `odc-by` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `253,346 texts in 33 languages` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `This is the classification part of the training data of multilingual-zeroshot-small / base / large.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 1022자 ≈ 256 토큰 (viewer statistics, default/train)
