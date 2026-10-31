---
type: "dataset"
id: "seyoungsong/Open-Korean-Historical-Corpus"
source: "huggingface"
url: "https://huggingface.co/datasets/seyoungsong/Open-Korean-Historical-Corpus"
downloads: 908
summary: "한국어 역사 말뭉치로, 한국어 NLP와 역사언어학 연구에 활용되는 대규모 공개 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[언어 모델링]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[일본어]]"
  - "[[한국어]]"
  - "[[lzh]]"
  - "[[다국어]]"
commercial_use:
  - "[[비상업 전용]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# seyoungsong/Open-Korean-Historical-Corpus

> dataset · [Hugging Face](https://huggingface.co/datasets/seyoungsong/Open-Korean-Historical-Corpus)

한국어 역사 말뭉치로, 한국어 NLP와 역사언어학 연구에 활용되는 대규모 공개 데이터셋입니다.

## 분류

- **작업**: [[언어 모델링]] — ner · readme = `Pre-training or fine-tuning Large Language Models (LLMs) on historical and diverse Korean scripts.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:language_modeling = `It contains 17.7 million documents (5.1 billion tokens) compiled from 19 distinct archives` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:language_modeling = `Pre-training or fine-tuning Large Language Models (LLMs) on historical and diverse Korean scripts.` · 신뢰도 medium
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[lzh]] — metadata · languages = `lzh` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `3 languages` · 신뢰도 high
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-4.0` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `Pre-training or fine-tuning Large Language Models (LLMs) on historical and diverse Korean scripts.` · 신뢰도 medium
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `99999999.0` · 신뢰도 high

## 이 데이터로 학습한 모델

- [[cadazar__han2han-it|cadazar/han2han-it]]
