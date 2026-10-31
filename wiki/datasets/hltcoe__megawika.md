---
type: "dataset"
id: "hltcoe/megawika"
source: "huggingface"
url: "https://huggingface.co/datasets/hltcoe/megawika"
downloads: 31818
summary: "MegaWika는 50개 언어 위키피디아 문단과 웹 인용문, 영어 번역, QA 쌍을 포함한 다국어 텍스트 데이터셋입니다."
readme_status: "template"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 생성]]"
  - "[[질의응답]]"
  - "[[요약]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# hltcoe/megawika

> dataset · [Hugging Face](https://huggingface.co/datasets/hltcoe/megawika)

MegaWika는 50개 언어 위키피디아 문단과 웹 인용문, 영어 번역, QA 쌍을 포함한 다국어 텍스트 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[질의응답]] — metadata · readme, task_categories = `question-answering` · 신뢰도 medium
- **작업**: [[요약]] — metadata · task_categories = `summarization` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering, task:summarization = `Wikipedia passages with their scraped and cleaned web citations` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering, task:summarization = `nearly 130 million English question/answer pairs` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `50 languages` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `50 Wikipedias in 50 languages` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `MegaWika is a multi- and crosslingual text dataset containing 30 million Wikipedia passages` · 신뢰도 low
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `99999999.0` · 신뢰도 high
