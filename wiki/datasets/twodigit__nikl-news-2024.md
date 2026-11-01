---
type: "dataset"
id: "twodigit/nikl-news-2024"
source: "huggingface"
url: "https://huggingface.co/datasets/twodigit/nikl-news-2024"
downloads: 334
summary: "2023년 생산된 신문 기사 1,119,753건으로 구성된 모두의말뭉치 신문 말뭉치 2024 데이터셋입니다."
readme_status: "ok"
readme_language: "ko"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[정보 추출]]"
  - "[[문서 검색]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[일반]]"
  - "[[뉴스·미디어]]"
dataset_role:
  - "[[학습용]]"
---
# twodigit/nikl-news-2024

> dataset · [Hugging Face](https://huggingface.co/datasets/twodigit/nikl-news-2024)

2023년 생산된 신문 기사 1,119,753건으로 구성된 모두의말뭉치 신문 말뭉치 2024 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `주제(TOPIC)별 기사 건수` · 신뢰도 low
- **작업**: [[정보 추출]] — ner · readme = `매체 종류 매체 이름` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `신문 기사 1,119,753건` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:classification, task:information_extraction, task:retrieval = `신문 기사` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `신문 기사` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `신문 기사` · 신뢰도 low
- **도메인**: [[뉴스·미디어]] — ner · readme = `신문 말뭉치 2024` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `2023년 생산된 신문 기사 1,119,753건` · 신뢰도 low
