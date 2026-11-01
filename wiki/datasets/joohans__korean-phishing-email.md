---
type: "dataset"
id: "joohans/korean-phishing-email"
source: "huggingface"
url: "https://huggingface.co/datasets/joohans/korean-phishing-email"
downloads: 48
summary: "한국어 및 영어 피싱 이메일 탐지용 데이터셋으로, 스팸과 정상 이메일 분류에 활용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[상업 이용 가능]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# joohans/korean-phishing-email

> dataset · [Hugging Face](https://huggingface.co/datasets/joohans/korean-phishing-email)

한국어 및 영어 피싱 이메일 탐지용 데이터셋으로, 스팸과 정상 이메일 분류에 활용됨.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories = `text-classification` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `English spam/legitimate emails` · 신뢰도 high
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `828` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **데이터 용도**: [[평가용]] — ner · readme = `test email_test.jsonl 17 English spam/legitimate test set` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `train email_train.jsonl 67 English spam/legitimate emails (Enron-based)` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 1243자 ≈ 828 토큰 (viewer statistics, default/test)
