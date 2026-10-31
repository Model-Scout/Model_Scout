---
type: "dataset"
id: "Babelscape/SREDFM"
source: "huggingface"
url: "https://huggingface.co/datasets/Babelscape/SREDFM"
downloads: 550
summary: "18개 언어, 400개 관계 유형을 포함한 다국어 관계 추출 데이터셋으로 다국어 RE 시스템 학습 및 평가에 활용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
  - "[[정보 추출]]"
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
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# Babelscape/SREDFM

> dataset · [Hugging Face](https://huggingface.co/datasets/Babelscape/SREDFM)

18개 언어, 400개 관계 유형을 포함한 다국어 관계 추출 데이터셋으로 다국어 RE 시스템 학습 및 평가에 활용됨.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `enabling the acquisition of relational facts and bridging the gap between natural language and structured knowledge` · 신뢰도 low
- **작업**: [[정보 추출]] — metadata · readme, task_categories = `token-classification` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:information_extraction = `Relation Extraction (RE) is a task that identifies relationships between entities in a text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `extracts triplets, including entity types, in multiple languages` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `18 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `177` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `multilingual RE systems` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `RED\textsuperscript{FM}, a smaller, human-revised dataset for seven languages that allows for the evaluation of multilingual RE systems` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `SRED\textsuperscript{FM}, an automatically annotated dataset covering 18 languages, 400 relation types, 13 entity types, totaling more than 40 million triplet i` · 신뢰도 medium
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `99999999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 710자 ≈ 177 토큰 (viewer statistics, ko/validation)

## 이 데이터로 학습한 모델

- [[Babelscape__mrebel-large|Babelscape/mrebel-large]]
