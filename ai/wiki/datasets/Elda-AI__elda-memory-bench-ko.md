---
type: "dataset"
id: "Elda-AI/elda-memory-bench-ko"
source: "huggingface"
url: "https://huggingface.co/datasets/Elda-AI/elda-memory-bench-ko"
downloads: 30
summary: "한국어 대화에서 사용자가 자신에 대해 말한 내용을 규칙대로 집어내는 규칙준수 평가 벤치입니다."
readme_status: "ok"
readme_language: "ko"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[정보 추출]]"
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
  - "[[평가용]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# Elda-AI/elda-memory-bench-ko

> dataset · [Hugging Face](https://huggingface.co/datasets/Elda-AI/elda-memory-bench-ko)

한국어 대화에서 사용자가 자신에 대해 말한 내용을 규칙대로 집어내는 규칙준수 평가 벤치입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `발화 한 턴에서 사용자가 자기에 대해 말한 것을 규칙대로 집어내는지 재는 벤치입니다.` · 신뢰도 low
- **작업**: [[정보 추출]] — metadata · task_categories = `token-classification` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:classification, task:information_extraction = `발화 한 턴에서 사용자가 자기에 대해 말한 것` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `규칙대로 집어내는지 재는 벤치입니다.` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `한국어 대화 기억 규칙준수 벤치` · 신뢰도 low
- **데이터 용도**: [[평가용]] — name_rule · dataset_id/tags = `evaluation` · 신뢰도 medium
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high
