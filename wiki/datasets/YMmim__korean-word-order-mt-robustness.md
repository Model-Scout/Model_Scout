---
type: "dataset"
id: "YMmim/korean-word-order-mt-robustness"
source: "huggingface"
url: "https://huggingface.co/datasets/YMmim/korean-word-order-mt-robustness"
downloads: 37
summary: "한국어 어순 변형에 따른 대형 언어 모델 번역 강건성 평가용 메타모픽 테스팅 데이터셋입니다."
readme_status: "ok"
readme_language: "ko"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
  - "[[번역]]"
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
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# YMmim/korean-word-order-mt-robustness

> dataset · [Hugging Face](https://huggingface.co/datasets/YMmim/korean-word-order-mt-robustness)

한국어 어순 변형에 따른 대형 언어 모델 번역 강건성 평가용 메타모픽 테스팅 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `gold_mr_violated — 모델 번역 시 변형 관계 위반 여부(사람 판정)` · 신뢰도 low
- **작업**: [[번역]] — metadata · tags, task_categories = `translation` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:translation = `각 세트는 한국어 원문(src_orig)과 어순 변형문(src_trans) 한 쌍` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:translation = `gold_mr_violated — 모델 번역 시 변형 관계 위반 여부(사람 판정)` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `한국어 어순 변형에 대한 대형 언어 모델(LLM) 번역의 강건성을 평가하기 위한 메타모픽 테스팅 데이터셋입니다.` · 신뢰도 low
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high
