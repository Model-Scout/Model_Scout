---
type: "dataset"
id: "arimm/yeoncheon-market-info-official"
source: "huggingface"
url: "https://huggingface.co/datasets/arimm/yeoncheon-market-info-official"
downloads: 4
summary: "경기도 연천군 전통시장 현황 데이터로 LLM 환각 방지 및 정확한 정보 제공용입니다."
readme_status: "ok"
readme_language: "ko"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
  - "[[질의응답]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[지리·위치]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# arimm/yeoncheon-market-info-official

> dataset · [Hugging Face](https://huggingface.co/datasets/arimm/yeoncheon-market-info-official)

경기도 연천군 전통시장 현황 데이터로 LLM 환각 방지 및 정확한 정보 제공용입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `output: 공공데이터에 근거한 정확한 답변` · 신뢰도 low
- **작업**: [[질의응답]] — metadata · readme, task_categories = `question-answering` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:question_answering = `instruction: 연천군 시장 관련 질문 (대화체 및 정보 요청 포함)` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering = `output: 공공데이터에 근거한 정확한 답변` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `150` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[지리·위치]] — ner · readme = `한국 로컬 지리 및 행정 정보에 대한 AI 학습 및 검증용` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `이 데이터셋은 대형 언어 모델(LLM)이 경기도 연천군과 같은 소규모 지역 정보에 대해 일으키는 환각(Hallucination) 현상을 방지하고, 정확한 정보를 제공하기 위해 제작되었습니다.` · 신뢰도 low
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

샘플 길이: `source` 열 p90 225자 ≈ 150 토큰 (viewer statistics, default/train)
