---
type: "dataset"
id: "NCDTech/human-gated-qaqc-knowledge-example"
source: "huggingface"
url: "https://huggingface.co/datasets/NCDTech/human-gated-qaqc-knowledge-example"
downloads: 139
summary: "노후 기계식 설비 예지보전을 위한 셀프 QA/QC 및 온프레미스 LLM 리포팅 기록 형식 시연용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[정보 추출]]"
  - "[[질의응답]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
---
# NCDTech/human-gated-qaqc-knowledge-example

> dataset · [Hugging Face](https://huggingface.co/datasets/NCDTech/human-gated-qaqc-knowledge-example)

노후 기계식 설비 예지보전을 위한 셀프 QA/QC 및 온프레미스 LLM 리포팅 기록 형식 시연용 데이터셋입니다.

## 분류

- **작업**: [[정보 추출]] — ner · readme = `Useful conversations become knowledge, but only under administrator approval, and every approved record keeps its full revision history.` · 신뢰도 low
- **작업**: [[질의응답]] — ner · readme = `Our system lets operators chat with a local LLM about inspection reports.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:information_extraction, task:question_answering = `All records here are synthetic examples that show the data structures we use in our self QA/QC + on-premise LLM reporting system.` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `Useful conversations become knowledge, but only under administrator approval, and every approved record keeps its full revision history.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `This is a format demonstration, not real operational data.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `All records here are synthetic examples that show the data structures we use in our self QA/QC + on-premise LLM reporting system.` · 신뢰도 low
