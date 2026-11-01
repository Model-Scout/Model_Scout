---
type: "dataset"
id: "christian-hoang-04/moltverse"
source: "huggingface"
url: "https://huggingface.co/datasets/christian-hoang-04/moltverse"
downloads: 55
summary: "MoltVerse는 AI 에이전트 간 사회적 상호작용 데이터를 연구용으로 제공하는 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
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
  - "[[초장문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# christian-hoang-04/moltverse

> dataset · [Hugging Face](https://huggingface.co/datasets/christian-hoang-04/moltverse)

MoltVerse는 AI 에이전트 간 사회적 상호작용 데이터를 연구용으로 제공하는 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories = `text-classification` · 신뢰도 medium
- **작업**: [[임베딩]] — ner · readme = `studying emergent behaviors, synthetic sociology, multi-agent coordination, alignment risks, and the sociology of large language model-driven societies` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[질의응답]] — metadata · task_categories = `question-answering` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:embedding, task:generation, task:question_answering = `Core post metadata (comments removed for cleanliness).` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering = `Core post metadata (comments removed for cleanliness).` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `multilingual` · 신뢰도 high
- **입력 길이**: [[초장문]] — viewer_stats · viewer_statistics = `95635` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `the world's first public social network built exclusively for AI agents` · 신뢰도 low
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 382538자 ≈ 95635 토큰 (viewer statistics, comments/train)
