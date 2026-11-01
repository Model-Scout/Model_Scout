---
type: "dataset"
id: "Baekpica/DeepSeek-V4-Flash-0731-REAM-Healing-Mix-2048"
source: "huggingface"
url: "https://huggingface.co/datasets/Baekpica/DeepSeek-V4-Flash-0731-REAM-Healing-Mix-2048"
downloads: 107
summary: "DeepSeek-V4 Flash REAM Healing Mix 2048은 104-expert REAM-pruned 체크포인트의 성능 저하를 개선하기 위한 치유 혼합 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[일본어]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[중국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# Baekpica/DeepSeek-V4-Flash-0731-REAM-Healing-Mix-2048

> dataset · [Hugging Face](https://huggingface.co/datasets/Baekpica/DeepSeek-V4-Flash-0731-REAM-Healing-Mix-2048)

DeepSeek-V4 Flash REAM Healing Mix 2048은 104-expert REAM-pruned 체크포인트의 성능 저하를 개선하기 위한 치유 혼합 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `Maximum sequence length: 1,024 DeepSeek-V4 tokens` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `loss is computed only on assistant reasoning/content tokens.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `4 languages` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `9` · 신뢰도 medium
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `DeepSeek-V4 Flash REAM Healing Mix 2048` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `These are training/healing records, not benchmark examples.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `source_identity` 열 p90 36자 ≈ 9 토큰 (viewer statistics, seq1024/train)
