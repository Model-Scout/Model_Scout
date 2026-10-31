---
type: "dataset"
id: "bluejude10/KR-Self-Driving-Legal-QA"
source: "huggingface"
url: "https://huggingface.co/datasets/bluejude10/KR-Self-Driving-Legal-QA"
downloads: 599
summary: "한국 자율주행자동차 법령 및 가이드라인 기반 고품질 질의응답 데이터셋입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
  - "[[질의응답]]"
  - "[[문서 검색]]"
input_modality:
  - "[[문서 파일 (입력 형식)|문서 파일]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[법률]]"
  - "[[교통·모빌리티]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[텍스트 파일]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# bluejude10/KR-Self-Driving-Legal-QA

> dataset · [Hugging Face](https://huggingface.co/datasets/bluejude10/KR-Self-Driving-Legal-QA)

한국 자율주행자동차 법령 및 가이드라인 기반 고품질 질의응답 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `LLM Fine-Tuning 및 RAG(Retrieval-Augmented Generation) 시스템 구축을 위해 최적화되었습니다.` · 신뢰도 medium
- **작업**: [[질의응답]] — ner · readme = `고품질 질의응답(Q&A) 데이터셋입니다.` · 신뢰도 medium
- **작업**: [[문서 검색]] — tag_match · tags = `rag` · 신뢰도 low
- **입력 형식**: [[문서 파일 (입력 형식)|문서 파일]] — metadata · modality = `document` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:question_answering, task:retrieval = `고품질 질의응답(Q&A) 데이터셋입니다.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering = `고품질 질의응답(Q&A) 데이터셋입니다.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `57` · 신뢰도 medium
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[법률]] — tag_match · readme, tags = `legal` · 신뢰도 medium
- **도메인**: [[교통·모빌리티]] — ner · readme = `자율주행자동차 관련 법령, 규칙, 가이드라인` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `LLM Fine-Tuning 및 RAG(Retrieval-Augmented Generation) 시스템 구축을 위해 최적화되었습니다.` · 신뢰도 medium
- **데이터 형식**: [[텍스트 파일]] — metadata · format = `text` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 85자 ≈ 57 토큰 (viewer statistics, default/validation)
