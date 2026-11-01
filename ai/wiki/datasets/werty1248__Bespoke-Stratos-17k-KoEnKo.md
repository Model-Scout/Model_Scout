---
type: "dataset"
id: "werty1248/Bespoke-Stratos-17k-KoEnKo"
source: "huggingface"
url: "https://huggingface.co/datasets/werty1248/Bespoke-Stratos-17k-KoEnKo"
downloads: 19
summary: "영어 시스템 프롬프트와 한국어 질문, 영어 사고 과정, 한국어 답변으로 구성된 번역 데이터셋입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_with_others"
task:
  - "[[번역]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
input_length:
  - "[[초장문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# werty1248/Bespoke-Stratos-17k-KoEnKo

> dataset · [Hugging Face](https://huggingface.co/datasets/werty1248/Bespoke-Stratos-17k-KoEnKo)

영어 시스템 프롬프트와 한국어 질문, 영어 사고 과정, 한국어 답변으로 구성된 번역 데이터셋입니다.

## 분류

- **작업**: [[번역]] — ner · readme = `- Let them think in English.

- English system prompt + Korean question + English thinking + Korean answer` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:translation = `English system prompt + Korean question + English thinking + Korean answer` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:translation = `English system prompt + Korean question + English thinking + Korean answer` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[초장문]] — viewer_stats · viewer_statistics = `24701` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `English system prompt + Korean question + English thinking + Korean answer` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Filtering
- Latex grammer check (rule-based detection + manual judgment)
- Boxed answer check (rule-based detection + manual judgment)
- 3 data are dropped` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `think` 열 p90 37052자 ≈ 24701 토큰 (viewer statistics, default/train)
