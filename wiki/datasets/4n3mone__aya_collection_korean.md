---
type: "dataset"
id: "4n3mone/aya_collection_korean"
source: "huggingface"
url: "https://huggingface.co/datasets/4n3mone/aya_collection_korean"
downloads: 46
summary: "CohereForAI/aya_collection_language_split에서 한국어 스플릿만 추출한 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
  - "[[질의응답]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
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
  - "[[대규모 데이터]]"
---
# 4n3mone/aya_collection_korean

> dataset · [Hugging Face](https://huggingface.co/datasets/4n3mone/aya_collection_korean)

CohereForAI/aya_collection_language_split에서 한국어 스플릿만 추출한 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `Flan-CoT-submix(T)` · 신뢰도 low
- **작업**: [[질의응답]] — ner · readme = `Adversarial QA(T)` · 신뢰도 medium
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:question_answering = `CohereForAI/aya_collection_language_split 에서 한국어 스플릿만 추출한 데이터셋 입니다.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering = `CohereForAI/aya_collection_language_split 에서 한국어 스플릿만 추출한 데이터셋 입니다.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `148` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `CohereForAI/aya_collection_language_split 에서 한국어 스플릿만 추출한 데이터셋 입니다.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `CohereForAI/aya_collection_language_split 에서 한국어 스플릿만 추출한 데이터셋 입니다.` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high

샘플 길이: `targets` 열 p90 223자 ≈ 148 토큰 (viewer statistics, default/validation)
