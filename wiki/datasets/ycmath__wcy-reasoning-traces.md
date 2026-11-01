---
type: "dataset"
id: "ycmath/wcy-reasoning-traces"
source: "huggingface"
url: "https://huggingface.co/datasets/ycmath/wcy-reasoning-traces"
downloads: 56
summary: "WCY 형식의 에이전트 추론 과정 기록 데이터셋으로, 추론 과정 분석에 활용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[임베딩]]"
  - "[[텍스트 생성]]"
  - "[[문서 검색]]"
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
dataset_size:
  - "[[소규모 데이터]]"
---
# ycmath/wcy-reasoning-traces

> dataset · [Hugging Face](https://huggingface.co/datasets/ycmath/wcy-reasoning-traces)

WCY 형식의 에이전트 추론 과정 기록 데이터셋으로, 추론 과정 분석에 활용됨.

## 분류

- **작업**: [[임베딩]] — ner · readme = `Line-oriented, phase-tagged agent reasoning traces in the WCY format.` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `Line-oriented, phase-tagged agent reasoning traces in the WCY format.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:embedding, task:generation, task:retrieval = `Line-oriented, phase-tagged agent reasoning traces in the WCY format.` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `Line-oriented, phase-tagged agent reasoning traces in the WCY format.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Line-oriented, phase-tagged agent reasoning traces in the WCY format.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `original WCY v1 corpus (pipeline-generated; the full 540-trace v1 set incl. 12 hand-crafted traces is at 10.5281/zenodo.19068769 and github.com/ycmath/wcy)` · 신뢰도 low
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high
