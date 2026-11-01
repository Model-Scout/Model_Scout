---
type: "dataset"
id: "HPLT/hplt_monolingual_v1_2"
source: "huggingface"
url: "https://huggingface.co/datasets/HPLT/hplt_monolingual_v1_2"
downloads: 51
summary: "75개 언어의 대규모 웹 크롤링 단일언어 말뭉치 데이터셋으로 텍스트 분석에 활용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
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
  - "[[다국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_size:
  - "[[초대규모 데이터]]"
---
# HPLT/hplt_monolingual_v1_2

> dataset · [Hugging Face](https://huggingface.co/datasets/HPLT/hplt_monolingual_v1_2)

75개 언어의 대규모 웹 크롤링 단일언어 말뭉치 데이터셋으로 텍스트 분석에 활용됨.

## 분류

- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[언어 모델링]] — ner · readme = `These large-scale web-crawled corpora based on CommonCrawl and the Internet Archive are accessible in 75 languages.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:generation, task:language_modeling = `- `text`: The document's text (a concatenation of newline-separated paragraphs).` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:language_modeling = `- `text`: The document's text (a concatenation of newline-separated paragraphs).` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `75 languages` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc0-1.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `These large-scale web-crawled corpora based on CommonCrawl and the Internet Archive are accessible in 75 languages.` · 신뢰도 medium
- **데이터 규모**: [[초대규모 데이터]] — metadata · size_categories = `inf` · 신뢰도 high
