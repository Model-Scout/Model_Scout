---
type: "dataset"
id: "ChuGyouk/Asan-AMC-Healthinfo"
source: "huggingface"
url: "https://huggingface.co/datasets/ChuGyouk/Asan-AMC-Healthinfo"
downloads: 24
summary: "서울아산병원 건강정보를 바탕으로 한 의료정보 데이터셋입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
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
  - "[[의료·보건]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# ChuGyouk/Asan-AMC-Healthinfo

> dataset · [Hugging Face](https://huggingface.co/datasets/ChuGyouk/Asan-AMC-Healthinfo)

서울아산병원 건강정보를 바탕으로 한 의료정보 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `서울아산병원 홈페이지의 건강정보-의료정보에서, 인체정보/질환백과/검사시술수술정보/알기쉬운의학용어/식사요법 데이터를 바탕으로` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `alpaca-style로 편집한 데이터입니다.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `322` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[의료·보건]] — tag_match · readme, tags = `medical` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `output` 열 p90 483자 ≈ 322 토큰 (viewer statistics, default/train)
