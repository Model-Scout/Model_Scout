---
type: "dataset"
id: "kaggle/infobayai/video-ugc"
source: "kaggle"
url: "https://www.kaggle.com/datasets/infobayai/video-ugc"
downloads: 13
summary: "STEM 및 비-STEM 교육용 고품질 UGC 비디오 데이터로 LLM 학습과 평가에 활용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
  - "[[영상 (입력 형식)|영상]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[교육]]"
dataset_role:
  - "[[평가용]]"
---
# kaggle/infobayai/video-ugc

> dataset · [Kaggle](https://www.kaggle.com/datasets/infobayai/video-ugc)

STEM 및 비-STEM 교육용 고품질 UGC 비디오 데이터로 LLM 학습과 평가에 활용됨.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `structured for use in **LLM training**, evaluation, and instruction tuning (SFT/RLHF)` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:generation = `text` · 신뢰도 medium
- **입력 형식**: [[영상 (입력 형식)|영상]] — ner · readme = `This repository includes: -A small preview subset of the UGC Videos data` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `structured for use in **LLM training**, evaluation, and instruction tuning (SFT/RLHF)` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `Attribution 4.0 International (CC BY 4.0)` · 신뢰도 high
- **도메인**: [[교육]] — ner · readme = `curated STEM and Non-STEM educational content` · 신뢰도 medium
- **데이터 용도**: [[평가용]] — ner · readme = `Model evaluation and experimentation` · 신뢰도 medium
