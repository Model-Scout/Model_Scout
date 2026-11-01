---
type: "dataset"
id: "Hikaf143/korean_data_scraper_kakaotalk"
source: "huggingface"
url: "https://huggingface.co/datasets/Hikaf143/korean_data_scraper_kakaotalk"
downloads: 71
summary: "KakaoTalk 그룹 채팅 내보내기 데이터를 가명처리 및 정제한 사내 전용 코퍼스입니다."
readme_status: "ok"
readme_language: "ko"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 생성]]"
  - "[[언어 모델링]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# Hikaf143/korean_data_scraper_kakaotalk

> dataset · [Hugging Face](https://huggingface.co/datasets/Hikaf143/korean_data_scraper_kakaotalk)

KakaoTalk 그룹 채팅 내보내기 데이터를 가명처리 및 정제한 사내 전용 코퍼스입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · tags, task_categories = `text-generation` · 신뢰도 low
- **작업**: [[언어 모델링]] — ner · readme = `Korean_data_scraper 프로젝트의 kakaotalk_export 소스가 생성한 코퍼스입니다.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:language_modeling = `가명처리·정제된 전체 대화 본문 (`"SPEAKER_N: 메시지"` 줄바꿈으로 연결)` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:language_modeling = `가명처리·정제된 전체 대화 본문 (`"SPEAKER_N: 메시지"` 줄바꿈으로 연결)` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Korean Data Scraper — KakaoTalk Export Corpus` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `본 데이터셋은 주식회사 MKD(MKD Inc.)가 자체적으로 생성·소유한 내부 데이터이며` · 신뢰도 low
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

## 같은 데이터의 사본·중복 등록

- `mkd-minju/korean_data_scraper_kakaotalk`
