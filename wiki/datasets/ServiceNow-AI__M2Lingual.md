---
type: "dataset"
id: "ServiceNow-AI/M2Lingual"
source: "huggingface"
url: "https://huggingface.co/datasets/ServiceNow-AI/M2Lingual"
downloads: 413
summary: "다국어 다중턴 대화 데이터셋으로 대화형 AI 모델 학습과 평가에 활용됨"
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 생성]]"
  - "[[질의응답]]"
  - "[[요약]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# ServiceNow-AI/M2Lingual

> dataset · [Hugging Face](https://huggingface.co/datasets/ServiceNow-AI/M2Lingual)

다국어 다중턴 대화 데이터셋으로 대화형 AI 모델 학습과 평가에 활용됨

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `The M2Lingual dataset is a comprehensive multi-turn multilingual resource designed to facilitate research and development in conversational AI.` · 신뢰도 medium
- **작업**: [[질의응답]] — ner · readme = `The dataset includes diverse tasks such as question answering, task completion, summarization and more.` · 신뢰도 medium
- **작업**: [[요약]] — ner · readme = `The dataset includes diverse tasks such as question answering, task completion, summarization and more.` · 신뢰도 medium
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:question_answering, task:summarization = `The M2Lingual dataset is a comprehensive multi-turn multilingual resource designed to facilitate research and development in conversational AI.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering, task:summarization = `The M2Lingual dataset is a comprehensive multi-turn multilingual resource designed to facilitate research and development in conversational AI.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `58 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `481` · 신뢰도 medium
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-sa-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `The M2Lingual dataset is a comprehensive multi-turn multilingual resource designed to facilitate research and development in conversational AI.` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `making it an invaluable asset for training, evaluating, and benchmarking conversational models.` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `making it an invaluable asset for training, evaluating, and benchmarking conversational models.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `output_assistant_reply` 열 p90 1925자 ≈ 481 토큰 (viewer statistics, full_data/train)
