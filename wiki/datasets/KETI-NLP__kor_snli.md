---
type: "dataset"
id: "KETI-NLP/kor_snli"
source: "huggingface"
url: "https://huggingface.co/datasets/KETI-NLP/kor_snli"
downloads: 41
summary: "KETI-NLP/kor_snli는 한국어 SNLI 데이터로 자연어 추론(NLI) 작업에 사용됩니다."
readme_status: "ok"
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
  - "[[중규모 데이터]]"
---
# KETI-NLP/kor_snli

> dataset · [Hugging Face](https://huggingface.co/datasets/KETI-NLP/kor_snli)

KETI-NLP/kor_snli는 한국어 SNLI 데이터로 자연어 추론(NLI) 작업에 사용됩니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories, task_ids = `text-classification` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `KETI-NLP/kor_snli` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `KETI-NLP/kor_snli` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `40` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `KETI-NLP/kor_snli` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `KETI-NLP/kor_snli` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `premise` 열 p90 60자 ≈ 40 토큰 (viewer statistics, default/validation)
