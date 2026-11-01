---
type: "dataset"
id: "BASF-AI/PubChemWikiKOPC"
source: "huggingface"
url: "https://huggingface.co/datasets/BASF-AI/PubChemWikiKOPC"
downloads: 12
summary: "PubChem과 Wikipedia의 영어-한국어 문단 쌍 분류 데이터셋으로, 동일 엔티티 여부를 판단합니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# BASF-AI/PubChemWikiKOPC

> dataset · [Hugging Face](https://huggingface.co/datasets/BASF-AI/PubChemWikiKOPC)

PubChem과 Wikipedia의 영어-한국어 문단 쌍 분류 데이터셋으로, 동일 엔티티 여부를 판단합니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories = `text-classification` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `pairs of paragraphs in English and Korean (sent1 and sent2)` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `a binary labels column indicating whether the paragraphs describe the same entity (1) or different entities (0)` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `643` · 신뢰도 medium
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-sa-4.0` · 신뢰도 high
- **도메인**: [[일반]] — tag_match · readme, tags = `wikipedia` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `This dataset is a multilingual extension of the PubChem & Wikipedia Paragraphs Pair Classification dataset.` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

샘플 길이: `sent1` 열 p90 965자 ≈ 643 토큰 (viewer statistics, default/test)
