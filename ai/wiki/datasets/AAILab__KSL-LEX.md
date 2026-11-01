---
type: "dataset"
id: "AAILab/KSL-LEX"
source: "huggingface"
url: "https://huggingface.co/datasets/AAILab/KSL-LEX"
downloads: 35
summary: "한국수어 사전 기반의 한국수어 어휘 데이터베이스로, 언어 연구와 기술 개발에 활용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[텍스트 생성]]"
  - "[[정보 추출]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
data_format:
  - "[[CSV]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# AAILab/KSL-LEX

> dataset · [Hugging Face](https://huggingface.co/datasets/AAILab/KSL-LEX)

한국수어 사전 기반의 한국수어 어휘 데이터베이스로, 언어 연구와 기술 개발에 활용됨.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `part-of-speech distinctions` · 신뢰도 low
- **작업**: [[텍스트 생성]] — ner · readme = `Sign language recognition and generation systems` · 신뢰도 medium
- **작업**: [[정보 추출]] — ner · readme = `providing detailed linguistic information including part-of-speech data` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:classification, task:generation, task:information_extraction = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `providing detailed linguistic information including part-of-speech data` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `23` · 신뢰도 medium
- **상업 이용**: [[조건부 이용]] — metadata · license = `gpl-3.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Korean Sign Language (KSL)` · 신뢰도 low
- **데이터 형식**: [[CSV]] — metadata · format = `csv` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `Same_Sign_Words` 열 p90 34자 ≈ 23 토큰 (viewer statistics, default/train)
