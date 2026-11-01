---
type: "dataset"
id: "bong9513/nationalpension_textmining_crawled_rawdata"
source: "huggingface"
url: "https://huggingface.co/datasets/bong9513/nationalpension_textmining_crawled_rawdata"
downloads: 4
summary: "국민연금 관련 네이버 뉴스, 블로그, 카페 원본 텍스트 데이터로 여론 분석에 활용됨."
readme_status: "ok"
readme_language: "ko"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[임베딩]]"
  - "[[언어 모델링]]"
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
  - "[[행정·민원]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[텍스트 파일]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# bong9513/nationalpension_textmining_crawled_rawdata

> dataset · [Hugging Face](https://huggingface.co/datasets/bong9513/nationalpension_textmining_crawled_rawdata)

국민연금 관련 네이버 뉴스, 블로그, 카페 원본 텍스트 데이터로 여론 분석에 활용됨.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `시계열에 따른 여론의 감성 변화 추이 분석` · 신뢰도 low
- **작업**: [[임베딩]] — ner · readme = `텍스트 마이닝, 감성 분석, 토픽 모델링 등 다양한 자연어 처리(NLP) 연구의 기초 자료로 활용될 수 있습니다.` · 신뢰도 low
- **작업**: [[언어 모델링]] — ner · readme = `한국어 텍스트 데이터 전처리 및 자연어 처리 모델 학습` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:classification, task:embedding, task:language_modeling = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:language_modeling = `텍스트 마이닝, 감성 분석, 토픽 모델링 등 다양한 자연어 처리(NLP) 연구의 기초 자료로 활용될 수 있습니다.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `27` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-4.0` · 신뢰도 high
- **도메인**: [[행정·민원]] — ner · readme = `국민연금에 대한 대중의 인식을 파악하기 위해 네이버(Naver)의 뉴스, 블로그, 카페에서 수집한 원본 텍스트 데이터의 모음입니다.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `텍스트 마이닝, 감성 분석, 토픽 모델링 등 다양한 자연어 처리(NLP) 연구의 기초 자료로 활용될 수 있습니다.` · 신뢰도 low
- **데이터 형식**: [[텍스트 파일]] — metadata · format = `text` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 40자 ≈ 27 토큰 (viewer statistics, default/train)
