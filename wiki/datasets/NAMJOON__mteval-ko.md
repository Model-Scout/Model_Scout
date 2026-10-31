---
type: "dataset"
id: "NAMJOON/mteval-ko"
source: "huggingface"
url: "https://huggingface.co/datasets/NAMJOON/mteval-ko"
downloads: 36
summary: "MT-Eval 한국어 번역 데이터로, 번역 벤치마크 비교 연구용 멀티턴 대화 168개 포함"
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
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
# NAMJOON/mteval-ko

> dataset · [Hugging Face](https://huggingface.co/datasets/NAMJOON/mteval-ko)

MT-Eval 한국어 번역 데이터로, 번역 벤치마크 비교 연구용 멀티턴 대화 168개 포함

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `recollection_cls 의 분류 라벨(ethics, sports, medicine 등)은 채점기가 문자 그대로 비교하므로 영어로 두었습니다.` · 신뢰도 medium
- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:generation = `멀티턴 대화 168 개.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `멀티턴 대화 168 개.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `MT-Eval (한국어 번역)` · 신뢰도 low
- **데이터 용도**: [[평가용]] — name_rule · dataset_id/tags = `evaluation` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `번역 벤치마크와 한국어로 직접 작성한 벤치마크를 비교하는 연구를 위해 만들었습니다.` · 신뢰도 low
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high
