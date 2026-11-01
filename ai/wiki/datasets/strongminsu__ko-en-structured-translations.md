---
type: "dataset"
id: "strongminsu/ko-en-structured-translations"
source: "huggingface"
url: "https://huggingface.co/datasets/strongminsu/ko-en-structured-translations"
downloads: 62
summary: "한국어 사용자에게 익숙한 표현 기반의 다도메인·다문체 한–영 병렬 번역 데이터셋입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 생성]]"
  - "[[번역]]"
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
  - "[[교육]]"
  - "[[일반]]"
data_format:
  - "[[CSV]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# strongminsu/ko-en-structured-translations

> dataset · [Hugging Face](https://huggingface.co/datasets/strongminsu/ko-en-structured-translations)

한국어 사용자에게 익숙한 표현 기반의 다도메인·다문체 한–영 병렬 번역 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `langchain을 사용하여 직접 고품질 병렬 데이터를 자동으로 생성·정제하여 구성한 데이터셋` · 신뢰도 low
- **작업**: [[번역]] — metadata · readme, tags, task_categories = `translation` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:translation = `한국어(ko) – 영어(en)` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:translation = `한국어(ko) – 영어(en)` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `50` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[교육]] — tag_match · tags = `education` · 신뢰도 medium
- **도메인**: [[일반]] — ner · readme = `한국어 사용자에게 익숙한 표현을 중심으로 다양한 문체, 문장 구조를 포함해 교육용·연구용·실습용으로 바로 사용 가능한 실용적 번역 코퍼스를 목표로 합니다.` · 신뢰도 low
- **데이터 형식**: [[CSV]] — metadata · format = `csv` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `en` 열 p90 75자 ≈ 50 토큰 (viewer statistics, default/validation)
