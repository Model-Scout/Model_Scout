---
type: "dataset"
id: "Ryoo72/K-MMStar"
source: "huggingface"
url: "https://huggingface.co/datasets/Ryoo72/K-MMStar"
downloads: 24
summary: "NCSOFT/K-MMStar 데이터셋을 사용하기 쉽게 가공한 이미지-질문-답변 데이터입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[이용 조건 미확인]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# Ryoo72/K-MMStar

> dataset · [Hugging Face](https://huggingface.co/datasets/Ryoo72/K-MMStar)

NCSOFT/K-MMStar 데이터셋을 사용하기 쉽게 가공한 이미지-질문-답변 데이터입니다.

## 분류

- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · modality, readme = `"image": examples["image"]` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `"answer": examples["answer"]` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `157` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `dataset = load_dataset("NCSOFT/K-MMStar")` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `question` 열 p90 235자 ≈ 157 토큰 (viewer statistics, default/val)
