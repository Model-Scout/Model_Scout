---
type: "dataset"
id: "akhilvssg/TRACE-MAGMaR-2026"
source: "huggingface"
url: "https://huggingface.co/datasets/akhilvssg/TRACE-MAGMaR-2026"
downloads: 212
summary: "TRACE-MAGMaR 2026 데이터셋은 다중 비디오 이벤트 이해 및 주장 생성 연구를 위한 전처리, 주장 생성, 교차 비디오 집계 결과를 포함합니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[임베딩]]"
  - "[[텍스트 생성]]"
  - "[[문서 인식(OCR)]]"
  - "[[문서 검색]]"
  - "[[음성 인식]]"
  - "[[이미지 인식]]"
  - "[[이미지 이해]]"
input_modality:
  - "[[음성 (입력 형식)|음성]]"
  - "[[문서 파일 (입력 형식)|문서 파일]]"
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
  - "[[영상 (입력 형식)|영상]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[es]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[my]]"
  - "[[ne]]"
  - "[[중국어]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# akhilvssg/TRACE-MAGMaR-2026

> dataset · [Hugging Face](https://huggingface.co/datasets/akhilvssg/TRACE-MAGMaR-2026)

TRACE-MAGMaR 2026 데이터셋은 다중 비디오 이벤트 이해 및 주장 생성 연구를 위한 전처리, 주장 생성, 교차 비디오 집계 결과를 포함합니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `Stage 2 (Qwen3-Embedding-8B greedy single-link clustering at cosine τ = 0.9)` · 신뢰도 medium
- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 high
- **작업**: [[문서 인식(OCR)]] — tag_match · tags = `ocr` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `Evidence Grounding-Guided Multi-Video Event Understanding` · 신뢰도 low
- **작업**: [[음성 인식]] — tag_match · tags = `asr` · 신뢰도 low
- **작업**: [[이미지 인식]] — tag_match · tags = `object-detection` · 신뢰도 low
- **작업**: [[이미지 이해]] — metadata · task_categories = `video-text-to-text` · 신뢰도 low
- **입력 형식**: [[음성 (입력 형식)|음성]] — task_rule · task:speech_recognition = `audio` · 신뢰도 medium
- **입력 형식**: [[문서 파일 (입력 형식)|문서 파일]] — task_rule · task:ocr = `document` · 신뢰도 medium
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — task_rule · task:ocr, task:vision, task:visual_qa = `image` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:embedding, task:generation, task:retrieval, task:visual_qa = `text` · 신뢰도 medium
- **입력 형식**: [[영상 (입력 형식)|영상]] — ner · readme = `90 `.mp4` files packed in a single uncompressed tarball` · 신뢰도 low
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:ocr, task:speech_recognition, task:visual_qa = `claim-generation outputs` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[es]] — metadata · languages = `es` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `6 languages` · 신뢰도 high
- **언어**: [[my]] — metadata · languages = `my` · 신뢰도 high
- **언어**: [[ne]] — metadata · languages = `ne` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `agpl-3.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `multi-video event understanding and claim generation` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `MAGMaR 2026 Oracle Track test set` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `TRACE pipeline on the MAGMaR 2026 Oracle Track test set` · 신뢰도 low
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high
