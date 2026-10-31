---
type: "dataset"
id: "mks0813/pixel_image_dataset"
source: "huggingface"
url: "https://huggingface.co/datasets/mks0813/pixel_image_dataset"
downloads: 14
summary: "픽셀 아트 스타일 이미지와 영어 프롬프트로 구성된 텍스트-이미지 모델 미세조정용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[이미지 생성]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[이미지 (출력 형식)|이미지]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# mks0813/pixel_image_dataset

> dataset · [Hugging Face](https://huggingface.co/datasets/mks0813/pixel_image_dataset)

픽셀 아트 스타일 이미지와 영어 프롬프트로 구성된 텍스트-이미지 모델 미세조정용 데이터셋입니다.

## 분류

- **작업**: [[이미지 생성]] — metadata · readme, tags, task_categories = `text-to-image` · 신뢰도 high
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — metadata · modality, task:image_generation = `image` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:image_generation = `English prompts describing each image` · 신뢰도 high
- **출력 형식**: [[이미지 (출력 형식)|이미지]] — ner · readme, task:image_generation = `Pixel art style image (1024x1024)` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `146` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `designed for text-to-image model fine-tuning` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `optimized-parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

샘플 길이: `prompt` 열 p90 219자 ≈ 146 토큰 (viewer statistics, default/train)
