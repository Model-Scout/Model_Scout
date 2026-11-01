---
type: "dataset"
id: "ranjaykrishna/visual_genome"
source: "huggingface"
url: "https://huggingface.co/datasets/ranjaykrishna/visual_genome"
downloads: 2418
summary: "Visual Genome은 이미지 내 객체와 관계를 밀도 있게 주석한 시각 인지 및 관계 이해용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[정보 추출]]"
  - "[[이미지 인식]]"
  - "[[이미지 이해]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# ranjaykrishna/visual_genome

> dataset · [Hugging Face](https://huggingface.co/datasets/ranjaykrishna/visual_genome)

Visual Genome은 이미지 내 객체와 관계를 밀도 있게 주석한 시각 인지 및 관계 이해용 데이터셋입니다.

## 분류

- **작업**: [[정보 추출]] — ner · readme = `They collect dense annotations of objects, attributes, and relationships within each image.` · 신뢰도 low
- **작업**: [[이미지 인식]] — metadata · task_categories = `object-detection` · 신뢰도 low
- **작업**: [[이미지 이해]] — metadata · readme, task_categories, task_ids = `image-to-text` · 신뢰도 medium
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · readme, task:vision, task:visual_qa = `108,077 image` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:information_extraction, task:visual_qa = `5.4 Million Region Descriptions` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:visual_qa = `5.4 Million Region Descriptions` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Visual Genome is a dataset, a knowledge base, an ongoing effort to connect structured image concepts to language.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `models used to tackle the rich content in images for cognitive tasks are still being trained using the same datasets designed for perceptual tasks.` · 신뢰도 medium
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

## 이 데이터로 학습한 모델

- [[unum-cloud__uform3-image-text-multilingual-base|unum-cloud/uform3-image-text-multilingual-base]]
