---
type: "dataset"
id: "kms7530/ko-coco-bal"
source: "huggingface"
url: "https://huggingface.co/datasets/kms7530/ko-coco-bal"
downloads: 143
summary: "MS COCO 영어 캡션을 한국어로 번역하고 통합해 하나의 문장으로 생성한 이미지 설명 데이터셋입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 생성]]"
  - "[[이미지 생성]]"
  - "[[번역]]"
  - "[[이미지 이해]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[이미지 (출력 형식)|이미지]]"
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
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
  - "[[중규모 데이터]]"
---
# kms7530/ko-coco-bal

> dataset · [Hugging Face](https://huggingface.co/datasets/kms7530/ko-coco-bal)

MS COCO 영어 캡션을 한국어로 번역하고 통합해 하나의 문장으로 생성한 이미지 설명 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `하나의 문장으로 변환된 결과:"` · 신뢰도 low
- **작업**: [[이미지 생성]] — metadata · task_categories = `text-to-image` · 신뢰도 low
- **작업**: [[번역]] — ner · readme = `기존의 MS COCO의 영어 캡션을 한국어 문장으로 번역(AIHub)한 데이터셋` · 신뢰도 medium
- **작업**: [[이미지 이해]] — metadata · task_categories = `image-to-text` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · modality, readme, task:image_generation, task:visual_qa = `image | PIL을 이용해 읽어온 이미지 객체.` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:image_generation, task:translation, task:visual_qa = `captions_en | MS COCO의 원본 영문 설명 리스트.` · 신뢰도 high
- **출력 형식**: [[이미지 (출력 형식)|이미지]] — task_rule · task:image_generation = `image` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation, task:translation, task:visual_qa = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `81` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license = `cc` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `MS COCO의 영어 캡션을 한국어 문장으로 번역(AIHub)한 데이터셋` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `본 데이터셋은 기존의 MS COCO의 영어 캡션을 한국어 문장으로 번역(AIHub)한 데이터셋의 한국어 묘사문을 통합하여 하나의 문장으로 생성한 데이터셋 입니다.` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `caption_ko` 열 p90 122자 ≈ 81 토큰 (viewer statistics, default/validation)
