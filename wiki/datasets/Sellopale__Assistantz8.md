---
type: "dataset"
id: "Sellopale/Assistantz8"
source: "huggingface"
url: "https://huggingface.co/datasets/Sellopale/Assistantz8"
downloads: 95
summary: "OpenAssistant Conversations는 35개 언어로 된 어시스턴트 대화 코퍼스로, 대규모 정렬 연구를 위한 데이터입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
  - "[[텍스트 생성]]"
  - "[[표 질의응답]]"
  - "[[음성 합성]]"
  - "[[번역]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[음성 (출력 형식)|음성]]"
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# Sellopale/Assistantz8

> dataset · [Hugging Face](https://huggingface.co/datasets/Sellopale/Assistantz8)

OpenAssistant Conversations는 35개 언어로 된 어시스턴트 대화 코퍼스로, 대규모 정렬 연구를 위한 데이터입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `annotated with 461,292 quality ratings` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **작업**: [[표 질의응답]] — metadata · task_categories = `table-question-answering` · 신뢰도 low
- **작업**: [[음성 합성]] — metadata · task_categories = `text-to-audio` · 신뢰도 low
- **작업**: [[번역]] — metadata · task_categories = `translation` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality, task:table_qa = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:generation, task:table_qa, task:text_to_speech, task:translation = `assistant-style conversation corpus consisting of 161,443 messages` · 신뢰도 high
- **출력 형식**: [[음성 (출력 형식)|음성]] — task_rule · task:text_to_speech = `audio` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:table_qa, task:translation = `assistant-style conversation corpus consisting of 161,443 messages` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `35 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `375` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `assistant-style conversation corpus consisting of 161,443 messages in 35 different languages` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `oasst_ready-trees file usually is sufficient for supervised fine-tuning (SFT) & reward model (RM) training` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 1499자 ≈ 375 토큰 (viewer statistics, default/validation)
