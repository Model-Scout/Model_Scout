---
type: "dataset"
id: "Hikaf143/korean_data_scraper_wikipedia"
source: "huggingface"
url: "https://huggingface.co/datasets/Hikaf143/korean_data_scraper_wikipedia"
downloads: 125
summary: "한국어 위키백과 덤프에서 문서 본문 텍스트를 추출한 코퍼스입니다."
readme_status: "ok"
readme_language: "mixed"
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
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# Hikaf143/korean_data_scraper_wikipedia

> dataset · [Hugging Face](https://huggingface.co/datasets/Hikaf143/korean_data_scraper_wikipedia)

한국어 위키백과 덤프에서 문서 본문 텍스트를 추출한 코퍼스입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[언어 모델링]] — ner · readme = `한국어 위키백과(ko.wikipedia.org) 덤프를 파싱하여 문서 본문 텍스트를 추출한 결과입니다.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:language_modeling = `text는 해당 위키백과 문서의 본문 텍스트입니다.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:language_modeling = `text는 해당 위키백과 문서의 본문 텍스트입니다.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[초장문]] — viewer_stats · viewer_statistics = `41148` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-4.0` · 신뢰도 high
- **도메인**: [[일반]] — tag_match · readme, tags = `wikipedia` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `Korean_data_scraper 프로젝트의 wikipedia_dump 소스가 생성한 코퍼스입니다.` · 신뢰도 low
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 61721자 ≈ 41148 토큰 (viewer statistics, default/train)
