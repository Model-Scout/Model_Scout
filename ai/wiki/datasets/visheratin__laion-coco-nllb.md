---
type: "dataset"
id: "visheratin/laion-coco-nllb"
source: "huggingface"
url: "https://huggingface.co/datasets/visheratin/laion-coco-nllb"
downloads: 1510
summary: "LAION-COCO 데이터셋을 NLLB-200 모델로 200개 언어로 번역한 이미지 캡션 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[번역]]"
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
  - "[[비상업 전용]]"
domain:
  - "[[일반]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# visheratin/laion-coco-nllb

> dataset · [Hugging Face](https://huggingface.co/datasets/visheratin/laion-coco-nllb)

LAION-COCO 데이터셋을 NLLB-200 모델로 200개 언어로 번역한 이미지 캡션 데이터셋입니다.

## 분류

- **작업**: [[번역]] — metadata · task_categories = `translation` · 신뢰도 low
- **작업**: [[이미지 이해]] — metadata · task_categories = `image-to-text` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · modality, readme, task:visual_qa = `id - unique ID of the image.
url - original URL of the image from the LAION-COCO dataset.` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:translation, task:visual_qa = `captions - a list of captions translated to the languages from the Flores 200 dataset.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:translation, task:visual_qa = `captions - a list of captions translated to the languages from the Flores 200 dataset.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `196 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `16` · 신뢰도 medium
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `LAION COCO translated into 200 languages` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `eng_caption` 열 p90 63자 ≈ 16 토큰 (viewer statistics, default/test)
