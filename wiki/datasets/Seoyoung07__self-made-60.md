---
type: "dataset"
id: "Seoyoung07/self-made-60"
source: "huggingface"
url: "https://huggingface.co/datasets/Seoyoung07/self-made-60"
downloads: 12
summary: "한국 수어 단어 인식 평가용으로 제작된 60개 수어 영상 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[임베딩]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
  - "[[영상 (입력 형식)|영상]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[조건부 이용]]"
dataset_role:
  - "[[평가용]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# Seoyoung07/self-made-60

> dataset · [Hugging Face](https://huggingface.co/datasets/Seoyoung07/self-made-60)

한국 수어 단어 인식 평가용으로 제작된 60개 수어 영상 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `Korean Sign Language isolated-word recognition pipeline` · 신뢰도 low
- **작업**: [[임베딩]] — metadata · task_categories = `feature-extraction` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:classification, task:embedding = `text` · 신뢰도 medium
- **입력 형식**: [[영상 (입력 형식)|영상]] — ner · modality, readme = `60 self-recorded Korean Sign Language isolated-word MP4 clips` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `File names are the target Korean word labels, for example: 간호사.mp4` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **데이터 용도**: [[평가용]] — ner · dataset_id/tags, readme = `This dataset is intended for reproducible evaluation of the submitted Korean Sign Language isolated-word recognition pipeline.` · 신뢰도 medium
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high
