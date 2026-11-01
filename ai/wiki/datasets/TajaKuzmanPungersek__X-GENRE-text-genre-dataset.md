---
type: "dataset"
id: "TajaKuzmanPungersek/X-GENRE-text-genre-dataset"
source: "huggingface"
url: "https://huggingface.co/datasets/TajaKuzmanPungersek/X-GENRE-text-genre-dataset"
downloads: 238
summary: "영어와 슬로베니아어로 된 수동 주석 다국어 X-GENRE 장르 데이터셋으로 장르 분류기 학습 및 평가용입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[sl]]"
input_length:
  - "[[장문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# TajaKuzmanPungersek/X-GENRE-text-genre-dataset

> dataset · [Hugging Face](https://huggingface.co/datasets/TajaKuzmanPungersek/X-GENRE-text-genre-dataset)

영어와 슬로베니아어로 된 수동 주석 다국어 X-GENRE 장르 데이터셋으로 장르 분류기 학습 및 평가용입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories = `text-classification` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `The dataset is in JSONL format. It has the following attributes: - text: text instance` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `- labels: genre label` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[sl]] — metadata · languages = `sl` · 신뢰도 high
- **입력 길이**: [[장문]] — viewer_stats · viewer_statistics = `4680` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Multilingual (English-Slovenian) manually-annotated X-GENRE genre dataset` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `for training genre classifiers (on the training split)` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 18720자 ≈ 4680 토큰 (viewer statistics, dev/train)

## 이 데이터로 학습한 모델

- [[classla__xlm-roberta-base-multilingual-text-genre-classifier|classla/xlm-roberta-base-multilingual-text-genre-classifier]]
