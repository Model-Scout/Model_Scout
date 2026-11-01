---
type: "dataset"
id: "ahuseynli-17683/pii-masking-openpii-finance"
source: "huggingface"
url: "https://huggingface.co/datasets/ahuseynli-17683/pii-masking-openpii-finance"
downloads: 62
summary: "한국어·영어 금융 도메인 개인정보(PII) 탐지용 토큰 분류 학습 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[정보 추출]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[금융·경제]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# ahuseynli-17683/pii-masking-openpii-finance

> dataset · [Hugging Face](https://huggingface.co/datasets/ahuseynli-17683/pii-masking-openpii-finance)

한국어·영어 금융 도메인 개인정보(PII) 탐지용 토큰 분류 학습 데이터셋입니다.

## 분류

- **작업**: [[정보 추출]] — metadata · tags, task_categories = `token-classification` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:information_extraction = `Train a token classifier on `(tokens, token_classes)`` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `Train a token classifier on `(tokens, token_classes)`` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `281` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[금융·경제]] — tag_match · tags = `finance` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `optimized-parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `source_text` 열 p90 421자 ≈ 281 토큰 (viewer statistics, default/validation)
