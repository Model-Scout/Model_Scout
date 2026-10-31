---
type: "dataset"
id: "SpellOnYou/kor_sarcasm"
source: "huggingface"
url: "https://huggingface.co/datasets/SpellOnYou/kor_sarcasm"
downloads: 202
summary: "한국어 트윗에서 빈정거림(sarcasm) 여부를 감지하기 위한 데이터셋입니다."
readme_status: "template"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# SpellOnYou/kor_sarcasm

> dataset · [Hugging Face](https://huggingface.co/datasets/SpellOnYou/kor_sarcasm)

한국어 트윗에서 빈정거림(sarcasm) 여부를 감지하기 위한 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories = `text-classification` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `9319 tweets were collected from Twitter` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `labeled for sarcasm or not_sarcasm` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `69` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `9319 tweets were collected from Twitter` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `9319 tweets were collected from Twitter and labeled for sarcasm or not_sarcasm` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `tokens` 열 p90 104자 ≈ 69 토큰 (viewer statistics, default/test)
