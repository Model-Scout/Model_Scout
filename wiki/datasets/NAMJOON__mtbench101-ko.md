---
type: "dataset"
id: "NAMJOON/mtbench101-ko"
source: "huggingface"
url: "https://huggingface.co/datasets/NAMJOON/mtbench101-ko"
downloads: 50
summary: "MT-Bench-101 영어 벤치를 한국어로 기계 번역한 대화형 평가 데이터셋입니다."
readme_status: "ok"
readme_language: "ko"
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
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# NAMJOON/mtbench101-ko

> dataset · [Hugging Face](https://huggingface.co/datasets/NAMJOON/mtbench101-ko)

MT-Bench-101 영어 벤치를 한국어로 기계 번역한 대화형 평가 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `1,388 대화, 13개 과제. 원본 구조(task, id, history[{user, bot}])를 유지합니다.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `1,388 대화, 13개 과제. 원본 구조(task, id, history[{user, bot}])를 유지합니다.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `MT-Bench-101 (Bai et al., ACL 2024) 를 한국어로 기계 번역한 자료입니다.` · 신뢰도 low
- **데이터 용도**: [[평가용]] — name_rule · dataset_id/tags = `evaluation` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `번역 벤치마크와 한국어로 직접 작성한 벤치마크를 비교하는 연구를 위해 만들었습니다.` · 신뢰도 low
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high
