---
type: "dataset"
id: "hltcoe/megawika-report-generation"
source: "huggingface"
url: "https://huggingface.co/datasets/hltcoe/megawika-report-generation"
downloads: 388
summary: "MegaWika는 50개 언어 위키피디아 구절과 인용문으로 구성된 다국어 보고서 생성용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 생성]]"
  - "[[문서 검색]]"
  - "[[요약]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[장문]]"
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
# hltcoe/megawika-report-generation

> dataset · [Hugging Face](https://huggingface.co/datasets/hltcoe/megawika-report-generation)

MegaWika는 50개 언어 위키피디아 구절과 인용문으로 구성된 다국어 보고서 생성용 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 high
- **작업**: [[문서 검색]] — metadata · readme, task_categories = `text-retrieval` · 신뢰도 high
- **작업**: [[요약]] — metadata · readme, task_categories = `summarization` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:retrieval, task:summarization = `MegaWika is a multi- and crosslingual text dataset containing 30 million Wikipedia passages with their scraped and cleaned web citations.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:summarization = `Given the rest of the fields (except for the ID) the goals is to produce the `gold_section_text` (e.g. given the title, intro, section name, and citations).` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `50 languages` · 신뢰도 high
- **입력 길이**: [[장문]] — viewer_stats · viewer_statistics = `5950` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `MegaWika is a multi- and crosslingual text dataset containing 30 million Wikipedia passages with their scraped and cleaned web citations.` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `text drawn from Wikipedia citations are meant for research use in algorithmic design and model training.` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `gold_section_text` 열 p90 23802자 ≈ 5950 토큰 (viewer statistics, default/validation)
