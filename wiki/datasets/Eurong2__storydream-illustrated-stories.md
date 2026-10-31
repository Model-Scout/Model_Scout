---
type: "dataset"
id: "Eurong2/storydream-illustrated-stories"
source: "huggingface"
url: "https://huggingface.co/datasets/Eurong2/storydream-illustrated-stories"
downloads: 245
summary: "StoryDream은 50개 이야기의 3단계 난이도별 일러스트와 텍스트를 제공하는 한국어/영어 그림책 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[임베딩]]"
  - "[[텍스트 생성]]"
  - "[[이미지 생성]]"
  - "[[문서 검색]]"
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
  - "[[교육]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[미디어 파일]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# Eurong2/storydream-illustrated-stories

> dataset · [Hugging Face](https://huggingface.co/datasets/Eurong2/storydream-illustrated-stories)

StoryDream은 50개 이야기의 3단계 난이도별 일러스트와 텍스트를 제공하는 한국어/영어 그림책 데이터셋입니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `11,680 illustrated story pages across 50 story/language combinations, each page pairing an image with its story text.` · 신뢰도 low
- **작업**: [[텍스트 생성]] — ner · readme = `illustrations were generated for this dataset.` · 신뢰도 low
- **작업**: [[이미지 생성]] — metadata · task_categories = `text-to-image` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `11,680 illustrated story pages across 50 story/language combinations, each page pairing an image with its story text.` · 신뢰도 low
- **작업**: [[이미지 이해]] — metadata · task_categories = `image-to-text` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · modality, readme, task:image_generation, task:visual_qa = `each page pairing an image with its story text.` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:embedding, task:generation, task:image_generation, task:retrieval, task:visual_qa = `each page pairing an image with its story text.` · 신뢰도 high
- **출력 형식**: [[이미지 (출력 형식)|이미지]] — task_rule · task:image_generation = `image` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:visual_qa = `each page pairing an image with its story text.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `125` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[교육]] — ner · readme = `reading difficulty; 1 is easiest` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Read these before training on the pairs.` · 신뢰도 medium
- **데이터 형식**: [[미디어 파일]] — metadata · format = `imagefolder` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 187자 ≈ 125 토큰 (viewer statistics, default/train)
