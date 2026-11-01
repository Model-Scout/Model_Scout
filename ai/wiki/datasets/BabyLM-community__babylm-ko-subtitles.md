---
type: "dataset"
id: "BabyLM-community/babylm-ko-subtitles"
source: "huggingface"
url: "https://huggingface.co/datasets/BabyLM-community/babylm-ko-subtitles"
downloads: 36
summary: "BabyLM 다국어 컬렉션의 한국어 자막 데이터셋으로, 7,909개 문서와 3,447만 토큰으로 구성됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
  - "[[언어 모델링]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[초장문]]"
commercial_use:
  - "[[이용 조건 미확인]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# BabyLM-community/babylm-ko-subtitles

> dataset · [Hugging Face](https://huggingface.co/datasets/BabyLM-community/babylm-ko-subtitles)

BabyLM 다국어 컬렉션의 한국어 자막 데이터셋으로, 7,909개 문서와 3,447만 토큰으로 구성됨.

## 분류

- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[언어 모델링]] — ner · readme = `This dataset is part of the BabyLM multilingual collection.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:language_modeling = `text: The document text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:language_modeling = `text: The document text` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[초장문]] — viewer_stats · viewer_statistics = `18937` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license = `unknown` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `This dataset is part of the BabyLM multilingual collection.` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 28406자 ≈ 18937 토큰 (viewer statistics, default/train)
