---
type: "dataset"
id: "CarrotAI/ko-multi-turn-queries"
source: "huggingface"
url: "https://huggingface.co/datasets/CarrotAI/ko-multi-turn-queries"
downloads: 36
summary: "한국어 지시문을 정보 단위로 분해해 자연스러운 다중 턴 대화로 변환하는 데이터셋입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# CarrotAI/ko-multi-turn-queries

> dataset · [Hugging Face](https://huggingface.co/datasets/CarrotAI/ko-multi-turn-queries)

한국어 지시문을 정보 단위로 분해해 자연스러운 다중 턴 대화로 변환하는 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, tags, task_categories = `text-generation` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `원본 복잡한 지시문` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `대화형으로 변환된 질문들 (점진적 공개)` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `이 데이터셋은 한국어 instruction 데이터셋입니다.` · 신뢰도 low
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high
