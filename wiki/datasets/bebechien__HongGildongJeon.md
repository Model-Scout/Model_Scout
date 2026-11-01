---
type: "dataset"
id: "bebechien/HongGildongJeon"
source: "huggingface"
url: "https://huggingface.co/datasets/bebechien/HongGildongJeon"
downloads: 43
summary: "홍길동전을 원문과 현대어 번역으로 제공하는 공개 도메인 문학 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
  - "[[번역]]"
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
  - "[[일반]]"
dataset_role:
  - "[[서비스 데이터]]"
data_format:
  - "[[CSV]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# bebechien/HongGildongJeon

> dataset · [Hugging Face](https://huggingface.co/datasets/bebechien/HongGildongJeon)

홍길동전을 원문과 현대어 번역으로 제공하는 공개 도메인 문학 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[번역]] — ner · readme = `modern translation : https://ko.wikisource.org/wiki/%ED%99%8D%EA%B8%B8%EB%8F%99%EC%A0%84_36%EC%9E%A5_%EC%99%84%ED%8C%90%EB%B3%B8/%ED%98%84%EB%8C%80%EC%96%B4_%ED` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:translation = `original : https://ko.wikisource.org/wiki/%ED%99%8D%EA%B8%B8%EB%8F%99%EC%A0%84_36%EC%9E%A5_%EC%99%84%ED%8C%90%EB%B3%B8` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:translation = `modern translation : https://ko.wikisource.org/wiki/%ED%99%8D%EA%B8%B8%EB%8F%99%EC%A0%84_36%EC%9E%A5_%EC%99%84%ED%8C%90%EB%B3%B8/%ED%98%84%EB%8C%80%EC%96%B4_%ED` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `278` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `pddl` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `https://ko.wikisource.org/wiki/%ED%99%8D%EA%B8%B8%EB%8F%99%EC%A0%84_36%EC%9E%A5_%EC%99%84%ED%8C%90%EB%B3%B8` · 신뢰도 low
- **데이터 용도**: [[서비스 데이터]] — ner · readme = `original : https://ko.wikisource.org/wiki/%ED%99%8D%EA%B8%B8%EB%8F%99%EC%A0%84_36%EC%9E%A5_%EC%99%84%ED%8C%90%EB%B3%B8` · 신뢰도 low
- **데이터 형식**: [[CSV]] — metadata · format = `csv` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

샘플 길이: `modern translation` 열 p90 417자 ≈ 278 토큰 (viewer statistics, default/train)
