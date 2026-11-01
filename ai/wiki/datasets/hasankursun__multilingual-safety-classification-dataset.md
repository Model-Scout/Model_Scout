---
type: "dataset"
id: "hasankursun/multilingual-safety-classification-dataset"
source: "huggingface"
url: "https://huggingface.co/datasets/hasankursun/multilingual-safety-classification-dataset"
downloads: 637
summary: "60개 언어로 된 안전성 분류 데이터셋으로 다국어 콘텐츠 검열 모델 학습에 사용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
  - "[[임베딩]]"
  - "[[번역]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[일반]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# hasankursun/multilingual-safety-classification-dataset

> dataset · [Hugging Face](https://huggingface.co/datasets/hasankursun/multilingual-safety-classification-dataset)

60개 언어로 된 안전성 분류 데이터셋으로 다국어 콘텐츠 검열 모델 학습에 사용됨.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories = `text-classification` · 신뢰도 high
- **작업**: [[임베딩]] — ner · readme = `Cross-lingual safety classification research` · 신뢰도 low
- **작업**: [[번역]] — tag_match · tags = `machine-translation` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:embedding, task:translation = `English safety prompts` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:translation = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `60 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `97` · 신뢰도 medium
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-sa-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `A multilingual dataset for safety classification across 60 languages` · 신뢰도 low
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `prompt` 열 p90 389자 ≈ 97 토큰 (viewer statistics, default/train)
