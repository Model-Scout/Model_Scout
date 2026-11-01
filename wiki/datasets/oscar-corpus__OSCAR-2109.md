---
type: "dataset"
id: "oscar-corpus/OSCAR-2109"
source: "huggingface"
url: "https://huggingface.co/datasets/oscar-corpus/OSCAR-2109"
downloads: 62
summary: "OSCAR는 Common Crawl 데이터를 언어별로 분류·필터링한 대규모 다국어 말뭉치로, 언어 모델 사전학습에 사용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
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
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[초대규모 데이터]]"
---
# oscar-corpus/OSCAR-2109

> dataset · [Hugging Face](https://huggingface.co/datasets/oscar-corpus/OSCAR-2109)

OSCAR는 Common Crawl 데이터를 언어별로 분류·필터링한 대규모 다국어 말뭉치로, 언어 모델 사전학습에 사용됨.

## 분류

- **작업**: [[언어 모델링]] — metadata · readme, task_ids = `language-modeling` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:language_modeling = `Data is distributed by language in both original and deduplicated form.` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:language_modeling = `Data is distributed by language in both original and deduplicated form.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `169 languages` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc0-1.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `The Open Super-large Crawled Aggregated coRpus is a huge multilingual corpus obtained by language classification and filtering of the Common Crawl corpus` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `OSCAR is mainly inteded to pretrain language models and word represantations.` · 신뢰도 low
- **데이터 규모**: [[초대규모 데이터]] — metadata · size_categories = `inf` · 신뢰도 high
