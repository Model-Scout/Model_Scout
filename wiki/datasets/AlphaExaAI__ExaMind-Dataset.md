---
type: "dataset"
id: "AlphaExaAI/ExaMind-Dataset"
source: "huggingface"
url: "https://huggingface.co/datasets/AlphaExaAI/ExaMind-Dataset"
downloads: 55
summary: "AlphaExaAI가 개발한 LLM 학습용 대규모 합성 데이터셋으로, 프로그래밍, 수학, 보안 등 다양한 AI 역량을 포함합니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 생성]]"
  - "[[질의응답]]"
  - "[[요약]]"
  - "[[번역]]"
input_modality:
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
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# AlphaExaAI/ExaMind-Dataset

> dataset · [Hugging Face](https://huggingface.co/datasets/AlphaExaAI/ExaMind-Dataset)

AlphaExaAI가 개발한 LLM 학습용 대규모 합성 데이터셋으로, 프로그래밍, 수학, 보안 등 다양한 AI 역량을 포함합니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **작업**: [[질의응답]] — metadata · task_categories = `question-answering` · 신뢰도 low
- **작업**: [[요약]] — metadata · task_categories = `summarization` · 신뢰도 low
- **작업**: [[번역]] — metadata · task_categories = `translation` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:question_answering, task:summarization, task:translation = `Single, merged, and fully deduplicated JSONL file` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering, task:summarization, task:translation = `an intelligent AI assistant capable of reasoning, coding, debugging, and communicating in 35+ world languages` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `34 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `146` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `covers a comprehensive range of AI capabilities — from programming and mathematics to cybersecurity, multilingual understanding, and autonomous agent behavior` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `designed for fine-tuning and training large language models (LLMs)` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `output` 열 p90 584자 ≈ 146 토큰 (viewer statistics, default/train)
