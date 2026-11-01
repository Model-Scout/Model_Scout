---
type: "dataset"
id: "JaeJiMin/korean_chat_friendly"
source: "huggingface"
url: "https://huggingface.co/datasets/JaeJiMin/korean_chat_friendly"
downloads: 68
summary: "친근한 대화 톤으로 요약·번역된 한국어 상담 및 안전 대화 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
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
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
---
# JaeJiMin/korean_chat_friendly

> dataset · [Hugging Face](https://huggingface.co/datasets/JaeJiMin/korean_chat_friendly)

친근한 대화 톤으로 요약·번역된 한국어 상담 및 안전 대화 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — tag_match · tags = `chat` · 신뢰도 low
- **작업**: [[질의응답]] — metadata · task_categories = `question-answering` · 신뢰도 low
- **작업**: [[요약]] — metadata · task_categories = `summarization` · 신뢰도 low
- **작업**: [[번역]] — metadata · task_categories = `translation` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering, task:summarization, task:translation = `- `short_question`: The input questions or conversational prompts.` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering, task:summarization, task:translation = `- `short_answer`: The corresponding friendly responses.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `It is ideal for applications related to conversational AI, natural language understanding, and empathetic dialogue modeling in Korean.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `The dataset currently has only a `train` split.` · 신뢰도 medium
