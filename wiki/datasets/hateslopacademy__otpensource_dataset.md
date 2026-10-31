---
type: "dataset"
id: "hateslopacademy/otpensource_dataset"
source: "huggingface"
url: "https://huggingface.co/datasets/hateslopacademy/otpensource_dataset"
downloads: 98
summary: "무신사 패션 아이템 데이터로 패션 추천, 트렌드 분석, 이미지-텍스트 생성에 활용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
  - "[[임베딩]]"
  - "[[텍스트 생성]]"
  - "[[이미지 이해]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[상거래·상품]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# hateslopacademy/otpensource_dataset

> dataset · [Hugging Face](https://huggingface.co/datasets/hateslopacademy/otpensource_dataset)

무신사 패션 아이템 데이터로 패션 추천, 트렌드 분석, 이미지-텍스트 생성에 활용됨.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories, task_ids = `text-classification` · 신뢰도 medium
- **작업**: [[임베딩]] — ner · readme = `NLP-based trend analysis for the fashion industry` · 신뢰도 low
- **작업**: [[텍스트 생성]] — ner · readme = `image-to-text generation models` · 신뢰도 medium
- **작업**: [[이미지 이해]] — metadata · tags, task_categories, task_ids = `image-to-text` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · modality, readme, task:visual_qa = `Each entry also includes an image URL linking to the item's image.` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:embedding, task:generation, task:visual_qa = `detailed attributes such as `category`, `gender`, `season`, `color`, `material`` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:visual_qa = `image-to-text generation models` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `24` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[상거래·상품]] — tag_match · readme, tags = `e-commerce` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `It is intended for use in AI applications related to fashion recommendation systems, trend analysis, and image-to-text generation.` · 신뢰도 low
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `product_name` 열 p90 37자 ≈ 24 토큰 (viewer statistics, default/train)
