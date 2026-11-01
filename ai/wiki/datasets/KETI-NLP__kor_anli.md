---
type: "dataset"
id: "KETI-NLP/kor_anli"
source: "huggingface"
url: "https://huggingface.co/datasets/KETI-NLP/kor_anli"
downloads: 65
summary: "KETI-NLP/kor_anli는 자연어 이해를 위한 적대적 자연어 추론(NLI) 벤치마크 데이터셋입니다."
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
  - "[[비상업 전용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# KETI-NLP/kor_anli

> dataset · [Hugging Face](https://huggingface.co/datasets/KETI-NLP/kor_anli)

KETI-NLP/kor_anli는 자연어 이해를 위한 적대적 자연어 추론(NLI) 벤치마크 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories, task_ids = `text-classification` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `Adversarial NLI: A New Benchmark for Natural Language Understanding` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `Adversarial NLI: A New Benchmark for Natural Language Understanding` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `144` · 신뢰도 medium
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Adversarial NLI: A New Benchmark for Natural Language Understanding` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Adversarial NLI: A New Benchmark for Natural Language Understanding` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `premise` 열 p90 216자 ≈ 144 토큰 (viewer statistics, default/train_r1)
