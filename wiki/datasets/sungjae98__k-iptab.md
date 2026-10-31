---
type: "dataset"
id: "sungjae98/k-iptab"
source: "huggingface"
url: "https://huggingface.co/datasets/sungjae98/k-iptab"
downloads: 30
summary: "한국 특허 무효심판 심결문으로 무효 예측, 구성요소 개시, 선행기술 역할귀속 3태스크 벤치마크 데이터셋입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[리랭킹]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[법률]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# sungjae98/k-iptab

> dataset · [Hugging Face](https://huggingface.co/datasets/sungjae98/k-iptab)

한국 특허 무효심판 심결문으로 무효 예측, 구성요소 개시, 선행기술 역할귀속 3태스크 벤치마크 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories = `text-classification` · 신뢰도 medium
- **작업**: [[리랭킹]] — metadata · task_categories = `text-ranking` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:classification, task:reranking = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = ``matrix` (DISCLOSE/DISCLOSE_SUBST/DIFFERENT/NOT_DISCLOSED)` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[법률]] — tag_match · readme, tags = `legal` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `3way split(train/val/test), 그룹분할(trial 누수 없음)` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high
