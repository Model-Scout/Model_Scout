---
type: "dataset"
id: "Mattimax/DATA-AI_Chat"
source: "huggingface"
url: "https://huggingface.co/datasets/Mattimax/DATA-AI_Chat"
downloads: 38
summary: "M.INC.의 ELNS 아키텍처 기반 AI 모델 DATA-AI의 자연어 이해 및 질의응답용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[임베딩]]"
  - "[[텍스트 생성]]"
  - "[[질의응답]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[상업 이용 가능]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[CSV]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# Mattimax/DATA-AI_Chat

> dataset · [Hugging Face](https://huggingface.co/datasets/Mattimax/DATA-AI_Chat)

M.INC.의 ELNS 아키텍처 기반 AI 모델 DATA-AI의 자연어 이해 및 질의응답용 데이터셋입니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `un dataset ottimizzato per la comprensione del linguaggio naturale` · 신뢰도 low
- **작업**: [[텍스트 생성]] — ner · readme = `un'applicazione di chat avanzata` · 신뢰도 medium
- **작업**: [[질의응답]] — ner · readme = `DATA-AI è stato addestrato su un dataset ottimizzato per la comprensione del linguaggio naturale e per rispondere in modo accurato a domande` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:embedding, task:generation, task:question_answering = `dataset ottimizzato per la comprensione del linguaggio naturale` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering = `rispondere in modo accurato a domande sulla sua origine, il suo funzionamento` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `35 languages` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `587` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `DATA-AI è stato addestrato su un dataset ottimizzato per la comprensione del linguaggio naturale` · 신뢰도 low
- **데이터 형식**: [[CSV]] — metadata · format = `csv` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 2347자 ≈ 587 토큰 (viewer statistics, default/train)
