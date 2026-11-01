---
type: "dataset"
id: "SungJoo/KBMC"
source: "huggingface"
url: "https://huggingface.co/datasets/SungJoo/KBMC"
downloads: 52
summary: "한국어 의료 분야 개체명 인식(NER) 데이터셋으로 질병, 신체, 치료명 태깅 데이터 포함."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[정보 추출]]"
input_modality:
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
  - "[[의료·보건]]"
data_format:
  - "[[CSV]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# SungJoo/KBMC

> dataset · [Hugging Face](https://huggingface.co/datasets/SungJoo/KBMC)

한국어 의료 분야 개체명 인식(NER) 데이터셋으로 질병, 신체, 치료명 태깅 데이터 포함.

## 분류

- **작업**: [[텍스트 분류]] — metadata · task_categories = `text-classification` · 신뢰도 low
- **작업**: [[정보 추출]] — tag_match · readme, tags = `NER` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:information_extraction = `sentence: The sentence text.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `tags: The named entities in the sentence.` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `94` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[의료·보건]] — tag_match · readme, tags = `medical` · 신뢰도 medium
- **데이터 형식**: [[CSV]] — metadata · format = `csv` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `Tags` 열 p90 141자 ≈ 94 토큰 (viewer statistics, default/train)
