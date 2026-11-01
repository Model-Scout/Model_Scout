---
type: "dataset"
id: "SOGANG-ISDS/VLM_CCA"
source: "huggingface"
url: "https://huggingface.co/datasets/SOGANG-ISDS/VLM_CCA"
downloads: 21
summary: "한국 문화 관련 이미지와 질문으로 구성된 VLM 문화 맥락 인식 평가용 멀티모달 VQA 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
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
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[문화·관광]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# SOGANG-ISDS/VLM_CCA

> dataset · [Hugging Face](https://huggingface.co/datasets/SOGANG-ISDS/VLM_CCA)

한국 문화 관련 이미지와 질문으로 구성된 VLM 문화 맥락 인식 평가용 멀티모달 VQA 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[이미지 이해]] — metadata · readme, tags, task_categories = `visual-question-answering` · 신뢰도 high
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — metadata · modality, task:visual_qa = `image` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:generation, task:visual_qa = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation, task:visual_qa = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-4.0` · 신뢰도 high
- **도메인**: [[문화·관광]] — ner · readme = `The Korean Culture VQA Dataset for Visual Language Model's Cultural Context Awareness (VLM-CCA) is a multimodal benchmark designed to evaluate vision-language m` · 신뢰도 medium
- **데이터 용도**: [[평가용]] — ner · dataset_id/tags, readme = `The dataset is distributed as JSONL records. Each record corresponds to a single VQA item aligned to an image.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high
