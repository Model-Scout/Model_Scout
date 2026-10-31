---
type: "dataset"
id: "multilingual-vlm-conflict/combined"
source: "huggingface"
url: "https://huggingface.co/datasets/multilingual-vlm-conflict/combined"
downloads: 215
summary: "이미지와 충돌하는 캡션을 포함한 23개 언어 다국어 이미지-텍스트 충돌 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[이미지 이해]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
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
# multilingual-vlm-conflict/combined

> dataset · [Hugging Face](https://huggingface.co/datasets/multilingual-vlm-conflict/combined)

이미지와 충돌하는 캡션을 포함한 23개 언어 다국어 이미지-텍스트 충돌 데이터셋입니다.

## 분류

- **작업**: [[이미지 이해]] — metadata · readme, task_categories = `image-text-to-text` · 신뢰도 medium
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · modality, readme, task:visual_qa = `Each example pairs an image with a truthful `original_caption`` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:visual_qa = `Each example pairs an image with a truthful `original_caption` and a `conflicting_caption`` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:visual_qa = ``question` asks about precisely the element that changes; `image_bias` is the true value grounded in the image, `text_bias` the altered value asserted by the co` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `23 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `152` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `All 10 datasets of the multilingual-vlm-conflict suite in one place, in English plus 22 languages translated` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `All 10 datasets of the multilingual-vlm-conflict suite in one place` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `optimized-parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `conflicting_open-ended_answer` 열 p90 607자 ≈ 152 토큰 (viewer statistics, default/train)
