---
type: "dataset"
id: "K-University-AIED/LearningChat_ai_video_production"
source: "huggingface"
url: "https://huggingface.co/datasets/K-University-AIED/LearningChat_ai_video_production"
downloads: 148
summary: "한림대학교 AI영상제작실습 2025-2 수업에서 조별 제작한 AI 기반 영상 결과물 공개 데이터셋입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[임베딩]]"
  - "[[문서 검색]]"
input_modality:
  - "[[문서 파일 (입력 형식)|문서 파일]]"
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
  - "[[영상 (입력 형식)|영상]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[교육]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[CSV]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# K-University-AIED/LearningChat_ai_video_production

> dataset · [Hugging Face](https://huggingface.co/datasets/K-University-AIED/LearningChat_ai_video_production)

한림대학교 AI영상제작실습 2025-2 수업에서 조별 제작한 AI 기반 영상 결과물 공개 데이터셋입니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `작품 단위 메타데이터를 함께 제공하기 위함이다.` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `AI영상제작실습 수업에서 조별로 제작·제출한 AI 기반 영상 결과물을 공개용 데이터셋 형태로 정리한 것이다.` · 신뢰도 low
- **입력 형식**: [[문서 파일 (입력 형식)|문서 파일]] — metadata · modality = `document` · 신뢰도 high
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:embedding, task:retrieval = `text` · 신뢰도 high
- **입력 형식**: [[영상 (입력 형식)|영상]] — ner · modality, readme = `각 팀 폴더의 원본 MP4 1개` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-nd-4.0` · 신뢰도 high
- **도메인**: [[교육]] — tag_match · readme, tags = `education` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `2025학년도 2학기 AI영상제작실습 수업에서 조별로 제작·제출한 AI 기반 영상 결과물을 공개용 데이터셋 형태로 정리한 것이다.` · 신뢰도 low
- **데이터 형식**: [[CSV]] — metadata · format = `csv` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high
