---
type: "dataset"
id: "shreyanshu09/BD-EnKo"
source: "huggingface"
url: "https://huggingface.co/datasets/shreyanshu09/BD-EnKo"
downloads: 287
summary: "BD-EnKo 데이터셋은 블록 다이어그램 이미지와 고품질 요약문을 포함하며 요약 연구에 활용됩니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[요약]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# shreyanshu09/BD-EnKo

> dataset · [Hugging Face](https://huggingface.co/datasets/shreyanshu09/BD-EnKo)

BD-EnKo 데이터셋은 블록 다이어그램 이미지와 고품질 요약문을 포함하며 요약 연구에 활용됩니다.

## 분류

- **작업**: [[요약]] — ner · readme = `This dataset contains different types of block diagram images with their high-quality summaries.` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · modality, readme = `This dataset contains different types of block diagram images` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:summarization = `with their high-quality summaries.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:summarization = `with their high-quality summaries.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `704` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `This dataset contains different types of block diagram images with their high-quality summaries.` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `| Types | Train | | Validation | |` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `| Types | Train | | Validation | |` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `ground_truth` 열 p90 1056자 ≈ 704 토큰 (viewer statistics, default/validation)
