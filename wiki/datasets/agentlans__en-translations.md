---
type: "dataset"
id: "agentlans/en-translations"
source: "huggingface"
url: "https://huggingface.co/datasets/agentlans/en-translations"
downloads: 16
summary: "영어와 여러 언어의 병렬 문장과 의미 유사도 점수, 품질 지표를 포함한 데이터셋으로 기계 번역 등에 활용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 분류]]"
  - "[[임베딩]]"
  - "[[번역]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# agentlans/en-translations

> dataset · [Hugging Face](https://huggingface.co/datasets/agentlans/en-translations)

영어와 여러 언어의 병렬 문장과 의미 유사도 점수, 품질 지표를 포함한 데이터셋으로 기계 번역 등에 활용됨.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `Translation Quality Estimation` · 신뢰도 low
- **작업**: [[임베딩]] — metadata · readme, task_categories = `feature-extraction` · 신뢰도 high
- **작업**: [[번역]] — metadata · readme, task_categories = `translation` · 신뢰도 high
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:embedding, task:translation = `parallel sentences in English and various other languages` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:translation = `semantic similarity score calculated using the Language-agnostic BERT Sentence Embedding (LaBSE) model` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `53` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `a diverse collection of parallel sentences in English and various other languages` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `sourced from multiple high-quality datasets` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `english` 열 p90 212자 ≈ 53 토큰 (viewer statistics, default/validation)

## 이 데이터로 학습한 모델

- [[agentlans__multilingual-e5-small-aligned-sentiment|agentlans/multilingual-e5-small-aligned-sentiment]]
