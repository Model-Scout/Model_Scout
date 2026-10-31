---
type: "dataset"
id: "SALT-NLP/SWE-chat"
source: "huggingface"
url: "https://huggingface.co/datasets/SALT-NLP/SWE-chat"
downloads: 14732
summary: "SWE-chat은 실제 개발자들이 AI 코딩 어시스턴트와 주고받은 대화와 코드 변경 기록을 담은 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[임베딩]]"
  - "[[텍스트 생성]]"
  - "[[문서 검색]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[일본어]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[pt]]"
  - "[[ru]]"
  - "[[중국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# SALT-NLP/SWE-chat

> dataset · [Hugging Face](https://huggingface.co/datasets/SALT-NLP/SWE-chat)

SWE-chat은 실제 개발자들이 AI 코딩 어시스턴트와 주고받은 대화와 코드 변경 기록을 담은 데이터셋입니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `Each session includes the full conversation transcript, tool calls, thinking traces, code changes, and attribution of human vs. agent-authored code.` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **작업**: [[문서 검색]] — ner · readme = `SWE-chat captures real-world AI coding sessions from developers using AI coding assistants` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:embedding, task:generation, task:retrieval = `Each session includes the full conversation transcript, tool calls, thinking traces, code changes, and attribution of human vs. agent-authored code.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `Each session includes the full conversation transcript, tool calls, thinking traces, code changes, and attribution of human vs. agent-authored code.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `6 languages` · 신뢰도 high
- **언어**: [[pt]] — metadata · languages = `pt` · 신뢰도 high
- **언어**: [[ru]] — metadata · languages = `ru` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `odc-by` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `SWE-chat captures real-world AI coding sessions from developers using AI coding assistants` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `SWE-chat captures real-world AI coding sessions from developers using AI coding assistants` · 신뢰도 low
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `99999999.0` · 신뢰도 high
