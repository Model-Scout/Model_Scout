---
type: "dataset"
id: "MoritzLaurer/multilingual-NLI-26lang-2mil7"
source: "huggingface"
url: "https://huggingface.co/datasets/MoritzLaurer/multilingual-NLI-26lang-2mil7"
downloads: 2926
summary: "26개 언어로 된 273만 개의 NLI 텍스트 쌍 데이터셋으로 다국어 자연어 추론 및 제로샷 분류에 활용 가능하다."
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
input_length:
  - "[[단문]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# MoritzLaurer/multilingual-NLI-26lang-2mil7

> dataset · [Hugging Face](https://huggingface.co/datasets/MoritzLaurer/multilingual-NLI-26lang-2mil7)

26개 언어로 된 273만 개의 NLI 텍스트 쌍 데이터셋으로 다국어 자연어 추론 및 제로샷 분류에 활용 가능하다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories, task_ids = `text-classification` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `This dataset contains 2 730 000 NLI text pairs in 26 languages` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `The dataset can be used to train models for multilingual NLI (Natural Language Inference) or zero-shot classification.` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `27 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `110` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `This dataset contains 2 730 000 NLI text pairs in 26 languages spoken by more than 4 billion people.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `The dataset can be used to train models for multilingual NLI (Natural Language Inference) or zero-shot classification.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high

샘플 길이: `premise_original` 열 p90 438자 ≈ 110 토큰 (viewer statistics, default/ar_anli)

## 이 데이터로 학습한 모델

- [[BalaRajesh1__mmbert-small-nli|BalaRajesh1/mmbert-small-nli]]
