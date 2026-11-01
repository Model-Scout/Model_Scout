---
type: "dataset"
id: "EinicherAI/nemotron-agentic-judgments"
source: "huggingface"
url: "https://huggingface.co/datasets/EinicherAI/nemotron-agentic-judgments"
downloads: 9
summary: "Nemotron-SFT-Agentic-v2의 interactive_agent와 tool_calling 분할에 대한 에이전트 도구 사용 실패 모드 평가용 시드 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
  - "[[리랭킹]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[de]]"
  - "[[영어]]"
  - "[[일본어]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[pt]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
---
# EinicherAI/nemotron-agentic-judgments

> dataset · [Hugging Face](https://huggingface.co/datasets/EinicherAI/nemotron-agentic-judgments)

Nemotron-SFT-Agentic-v2의 interactive_agent와 tool_calling 분할에 대한 에이전트 도구 사용 실패 모드 평가용 시드 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `full-prefix semantic judgments` · 신뢰도 low
- **작업**: [[리랭킹]] — ner · readme = `Useful as an evaluation/audit set for agentic tool-use failure modes` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:classification, task:reranking = `full-prefix semantic judgments` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `full-prefix semantic judgments` · 신뢰도 low
- **언어**: [[de]] — metadata · languages = `de` · 신뢰도 high
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `5 languages` · 신뢰도 high
- **언어**: [[pt]] — metadata · languages = `pt` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `full-prefix semantic judgments` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `Useful as an evaluation/audit set for agentic tool-use failure modes` · 신뢰도 medium
