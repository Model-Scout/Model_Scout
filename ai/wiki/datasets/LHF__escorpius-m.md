---
type: "dataset"
id: "LHF/escorpius-m"
source: "huggingface"
url: "https://huggingface.co/datasets/LHF/escorpius-m"
downloads: 39
summary: "esCorpius-m은 다국어 웹 크롤링 코퍼스로, 고품질 텍스트 정제와 중복 제거를 포함합니다."
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
  - "[[한국어]]"
  - "[[다국어]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[초대규모 데이터]]"
---
# LHF/escorpius-m

> dataset · [Hugging Face](https://huggingface.co/datasets/LHF/escorpius-m)

esCorpius-m은 다국어 웹 크롤링 코퍼스로, 고품질 텍스트 정제와 중복 제거를 포함합니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[언어 모델링]] — metadata · readme, task_categories, task_ids = `fill-mask` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:generation, task:language_modeling = `web textual content` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:language_modeling = `web textual content` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `32 languages` · 신뢰도 high
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-nd-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `multilingual datasets obtained from automatic web crawling` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `they require a vast amount of data to be (pre-)trained` · 신뢰도 medium
- **데이터 규모**: [[초대규모 데이터]] — metadata · size_categories = `999999999999.0` · 신뢰도 high
