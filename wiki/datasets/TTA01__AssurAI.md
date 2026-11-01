---
type: "dataset"
id: "TTA01/AssurAI"
source: "huggingface"
url: "https://huggingface.co/datasets/TTA01/AssurAI"
downloads: 594
summary: "AssurAI는 생성형 AI 출력의 안전 위험 평가를 위한 다중모달 벤치마크 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[음성 (입력 형식)|음성]]"
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
  - "[[영상 (입력 형식)|영상]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# TTA01/AssurAI

> dataset · [Hugging Face](https://huggingface.co/datasets/TTA01/AssurAI)

AssurAI는 생성형 AI 출력의 안전 위험 평가를 위한 다중모달 벤치마크 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `human-annotated risk scores (1–5)` · 신뢰도 low
- **입력 형식**: [[음성 (입력 형식)|음성]] — ner · readme = `It covers four modalities (text, image, audio, video)` · 신뢰도 medium
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · modality, readme = `It covers four modalities (text, image, audio, video)` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `It covers four modalities (text, image, audio, video)` · 신뢰도 high
- **입력 형식**: [[영상 (입력 형식)|영상]] — ner · readme = `It covers four modalities (text, image, audio, video)` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `human-annotated risk scores (1–5)` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `366` · 신뢰도 medium
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `multimodal benchmark dataset for evaluating safety risks in generative AI outputs` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `benchmark dataset for evaluating safety risks` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `candidate_4_answer` 열 p90 549자 ≈ 366 토큰 (viewer statistics, default/eval)

## 같은 데이터의 사본·중복 등록

- `sd1098/AssurAI`
