---
type: "dataset"
id: "HAERAE-HUB/HAERAE-VISION"
source: "huggingface"
url: "https://huggingface.co/datasets/HAERAE-HUB/HAERAE-VISION"
downloads: 71
summary: "실제 한국어 시각 질문응답 데이터셋으로, 불충분한 질문과 명확한 질문을 포함합니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[질의응답]]"
  - "[[이미지 이해]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# HAERAE-HUB/HAERAE-VISION

> dataset · [Hugging Face](https://huggingface.co/datasets/HAERAE-HUB/HAERAE-VISION)

실제 한국어 시각 질문응답 데이터셋으로, 불충분한 질문과 명확한 질문을 포함합니다.

## 분류

- **작업**: [[질의응답]] — metadata · task_categories = `question-answering` · 신뢰도 low
- **작업**: [[이미지 이해]] — metadata · readme, task_categories = `visual-question-answering` · 신뢰도 high
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · modality, readme, task:visual_qa = `Both share the same images and reference answers` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:question_answering, task:visual_qa = `two question types: original: Under-specified, authentic user queries explicit: Clarified queries with full context` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering, task:visual_qa = `Both share the same images and reference answers` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `157` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `A Korean visual QA benchmark featuring real-world, under-specified questions.` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

샘플 길이: `question_explicit` 열 p90 235자 ≈ 157 토큰 (viewer statistics, default/train)
