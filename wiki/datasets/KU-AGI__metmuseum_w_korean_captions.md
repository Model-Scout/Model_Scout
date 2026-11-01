---
type: "dataset"
id: "KU-AGI/metmuseum_w_korean_captions"
source: "huggingface"
url: "https://huggingface.co/datasets/KU-AGI/metmuseum_w_korean_captions"
downloads: 21
summary: "Metropolitan Museum 소장품 100점의 메타데이터와 한국어/영어 캡션, 이미지 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[임베딩]]"
  - "[[이미지 생성]]"
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
  - "[[상업 이용 가능]]"
domain:
  - "[[문화·관광]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# KU-AGI/metmuseum_w_korean_captions

> dataset · [Hugging Face](https://huggingface.co/datasets/KU-AGI/metmuseum_w_korean_captions)

Metropolitan Museum 소장품 100점의 메타데이터와 한국어/영어 캡션, 이미지 데이터셋입니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `Metropolitan Museum of Art 소장품 100점에 대한 메타데이터와 한국어/영어 캡션 데이터셋입니다.` · 신뢰도 low
- **작업**: [[이미지 생성]] — metadata · task_categories = `text-to-image` · 신뢰도 low
- **작업**: [[이미지 이해]] — metadata · tags, task_categories = `image-to-text` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · modality, readme, task:image_generation, task:visual_qa = `image: 작품 이미지 (긴 변 1024px, parquet 임베드)` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:embedding, task:image_generation, task:visual_qa = `text` · 신뢰도 high
- **출력 형식**: [[이미지 (출력 형식)|이미지]] — task_rule · task:image_generation = `image` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:visual_qa = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `472` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc0-1.0` · 신뢰도 high
- **도메인**: [[문화·관광]] — ner · readme = `Metropolitan Museum of Art 소장품 100점에 대한 메타데이터와 한국어/영어 캡션 데이터셋입니다.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `from datasets import load_dataset
ds = load_dataset("KU-AGI/metmuseum_w_korean_captions", split="train")` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

샘플 길이: `description_en` 열 p90 708자 ≈ 472 토큰 (viewer statistics, default/train)
