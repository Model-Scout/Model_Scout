---
type: "dataset"
id: "sappho192/Tatoeba-Challenge-jpn-kor"
source: "huggingface"
url: "https://huggingface.co/datasets/sappho192/Tatoeba-Challenge-jpn-kor"
downloads: 95
summary: "일본어-한국어 문장 쌍 데이터로 일본어 문장을 한국어로 번역하는 모델 학습용입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[번역]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[일본어]]"
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[비상업 전용]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[CSV]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# sappho192/Tatoeba-Challenge-jpn-kor

> dataset · [Hugging Face](https://huggingface.co/datasets/sappho192/Tatoeba-Challenge-jpn-kor)

일본어-한국어 문장 쌍 데이터로 일본어 문장을 한국어로 번역하는 모델 학습용입니다.

## 분류

- **작업**: [[번역]] — metadata · readme, task_categories = `translation` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:translation = `Each dataset has two columns: `sourceString` and `targetString`, which corresponds to Japanese and Korean sentence.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:translation = `Each dataset has two columns: `sourceString` and `targetString`, which corresponds to Japanese and Korean sentence.` · 신뢰도 medium
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `7` · 신뢰도 medium
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-sa-4.0` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `The dataset can be used to train the translation model that translates Japanese sentence to Korean.` · 신뢰도 medium
- **데이터 형식**: [[CSV]] — metadata · format = `csv` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `99999999.0` · 신뢰도 high

샘플 길이: `targetString` 열 p90 27자 ≈ 7 토큰 (viewer statistics, default/test)

## 이 데이터로 학습한 모델

- [[sappho192__ffxiv-ja-ko-translator|sappho192/ffxiv-ja-ko-translator]]
