---
type: "dataset"
id: "slone/nllb-200-10M-sample"
source: "huggingface"
url: "https://huggingface.co/datasets/slone/nllb-200-10M-sample"
downloads: 200
summary: "NLLB-200 데이터셋에서 추출한 1천만 문장쌍 샘플로 다국어 번역 모델 미세조정에 사용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[번역]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
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
  - "[[대규모 데이터]]"
---
# slone/nllb-200-10M-sample

> dataset · [Hugging Face](https://huggingface.co/datasets/slone/nllb-200-10M-sample)

NLLB-200 데이터셋에서 추출한 1천만 문장쌍 샘플로 다국어 번역 모델 미세조정에 사용됨.

## 분류

- **작업**: [[번역]] — metadata · readme, task_categories = `translation` · 신뢰도 high
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:translation = `This is a sample of nearly 10M sentence pairs` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:translation = `This is a sample of nearly 10M sentence pairs` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `172 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `31` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `odc-by` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `The following language codes are supported.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `This dataset can be used for fine-tuning massively multilingual translation models.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high

샘플 길이: `text2` 열 p90 126자 ≈ 31 토큰 (viewer statistics, default/train)

## 같은 데이터의 사본·중복 등록

- `vansh62/nllb-200-10M-sample`
