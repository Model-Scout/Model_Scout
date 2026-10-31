---
type: "dataset"
id: "zhiyuan-ning/linguasafe"
source: "huggingface"
url: "https://huggingface.co/datasets/zhiyuan-ning/linguasafe"
downloads: 101
summary: "다국어 언어 학습용 데이터셋으로 다양한 언어와 레벨의 프롬프트를 포함함"
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
commercial_use:
  - "[[비상업 전용]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# zhiyuan-ning/linguasafe

> dataset · [Hugging Face](https://huggingface.co/datasets/zhiyuan-ning/linguasafe)

다국어 언어 학습용 데이터셋으로 다양한 언어와 레벨의 프롬프트를 포함함

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `prompt` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:generation = `- name: prompt` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `- name: prompt` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `12 languages` · 신뢰도 high
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-sa-4.0` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `- name: train` · 신뢰도 medium
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
