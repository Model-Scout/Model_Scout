---
type: "dataset"
id: "SY95/WCCA-AK-images"
source: "huggingface"
url: "https://huggingface.co/datasets/SY95/WCCA-AK-images"
downloads: 330
summary: "한국 디자이너 앙드레 김의 오뜨 꾸뛰르 의상 3D 스캔 및 다중 시점 이미지 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[임베딩]]"
  - "[[텍스트 생성]]"
  - "[[이미지 인식]]"
input_modality:
  - "[[코드 (입력 형식)|코드]]"
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[코드 (출력 형식)|코드]]"
  - "[[이미지 (출력 형식)|이미지]]"
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[문화·관광]]"
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# SY95/WCCA-AK-images

> dataset · [Hugging Face](https://huggingface.co/datasets/SY95/WCCA-AK-images)

한국 디자이너 앙드레 김의 오뜨 꾸뛰르 의상 3D 스캔 및 다중 시점 이미지 데이터셋입니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `3D model files for computational analysis and reconstruction` · 신뢰도 low
- **작업**: [[텍스트 생성]] — ner · readme = `generative exploration of artistic vision` · 신뢰도 low
- **작업**: [[이미지 인식]] — metadata · readme, task_categories = `image-classification` · 신뢰도 medium
- **입력 형식**: [[코드 (입력 형식)|코드]] — ner · readme = `3D model files (18 FBX + 18 MTL + 18 OBJ)` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · modality, readme, task:vision = `multi-view images capturing 100 haute couture garments` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:embedding, task:generation = `text` · 신뢰도 high
- **출력 형식**: [[코드 (출력 형식)|코드]] — ner · readme = `3D model files for computational analysis and reconstruction` · 신뢰도 low
- **출력 형식**: [[이미지 (출력 형식)|이미지]] — ner · readme = `High-resolution multi-view photographs of garments` · 신뢰도 low
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `8` · 신뢰도 medium
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[문화·관광]] — ner · readme = `one of Korea's most iconic fashion designers` · 신뢰도 low
- **도메인**: [[일반]] — ner · readme = `This dataset bridges computer vision research and cultural heritage preservation` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `This dataset supports multiple research directions` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `optimized-parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `filename` 열 p90 12자 ≈ 8 토큰 (viewer statistics, default/train)
