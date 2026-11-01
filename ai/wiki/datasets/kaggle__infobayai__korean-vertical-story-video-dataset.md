---
type: "dataset"
id: "kaggle/infobayai/korean-vertical-story-video-dataset"
source: "kaggle"
url: "https://www.kaggle.com/datasets/infobayai/korean-vertical-story-video-dataset"
downloads: 11
summary: "한국어 세로형 스토리라인 영상 데이터셋으로 AI 학습용으로 활용됨"
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[임베딩]]"
  - "[[텍스트 생성]]"
  - "[[음성 인식]]"
input_modality:
  - "[[음성 (입력 형식)|음성]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
  - "[[영상 (입력 형식)|영상]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/infobayai/korean-vertical-story-video-dataset

> dataset · [Kaggle](https://www.kaggle.com/datasets/infobayai/korean-vertical-story-video-dataset)

한국어 세로형 스토리라인 영상 데이터셋으로 AI 학습용으로 활용됨

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `video classification` · 신뢰도 medium
- **작업**: [[임베딩]] — ner · readme = `multimodal learning, storytelling analysis, and next-generation content intelligence` · 신뢰도 low
- **작업**: [[텍스트 생성]] — ner · readme = `Video captioning and summarization` · 신뢰도 low
- **작업**: [[음성 인식]] — ner · readme = `Speech-to-text and subtitle generation` · 신뢰도 medium
- **입력 형식**: [[음성 (입력 형식)|음성]] — task_rule · task:speech_recognition = `audio` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:classification, task:embedding, task:generation = `text` · 신뢰도 medium
- **입력 형식**: [[영상 (입력 형식)|영상]] — ner · readme = `Modality: Video (Audio + Visual)` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:speech_recognition = `Video captioning and summarization` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `Attribution 4.0 International (CC BY 4.0)` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Large-scale Korean Vertical Storyline Video Dataset for AI training` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `designed to support the development of advanced AI systems for short-form video understanding` · 신뢰도 low
