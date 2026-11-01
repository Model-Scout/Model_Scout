---
type: "dataset"
id: "Mkd-Yonas/keural-SFT-rebuilt"
source: "huggingface"
url: "https://huggingface.co/datasets/Mkd-Yonas/keural-SFT-rebuilt"
downloads: 30
summary: "Keural SFT 재구성 데이터셋으로, 코드 블록 들여쓰기 오류를 수정한 혼합 영어/한국어 지침 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# Mkd-Yonas/keural-SFT-rebuilt

> dataset · [Hugging Face](https://huggingface.co/datasets/Mkd-Yonas/keural-SFT-rebuilt)

Keural SFT 재구성 데이터셋으로, 코드 블록 들여쓰기 오류를 수정한 혼합 영어/한국어 지침 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:generation = `text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `mixed EN/KO instruction dataset` · 신뢰도 low
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high
