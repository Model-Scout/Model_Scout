---
type: "dataset"
id: "aborasheed/Multilingual-Core-Vocabulary"
source: "huggingface"
url: "https://huggingface.co/datasets/aborasheed/Multilingual-Core-Vocabulary"
downloads: 76
summary: "19개 언어의 빈도 정렬된 핵심 어휘 데이터셋으로 다국어 응용과 번역 모델에 활용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
  - "[[임베딩]]"
  - "[[번역]]"
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
---
# aborasheed/Multilingual-Core-Vocabulary

> dataset · [Hugging Face](https://huggingface.co/datasets/aborasheed/Multilingual-Core-Vocabulary)

19개 언어의 빈도 정렬된 핵심 어휘 데이터셋으로 다국어 응용과 번역 모델에 활용됨.

## 분류

- **작업**: [[텍스트 분류]] — metadata · task_categories = `text-classification` · 신뢰도 low
- **작업**: [[임베딩]] — ner · readme = `It is designed to be the ultimate resource for building cross-lingual applications, AI similarity agents, and translation models.` · 신뢰도 low
- **작업**: [[번역]] — metadata · readme, task_categories = `translation` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:classification, task:embedding, task:translation = `This dataset contains millions of frequency-sorted, highly accurate words across 19 languages.` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:translation = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `19 languages` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `This dataset contains millions of frequency-sorted, highly accurate words across 19 languages.` · 신뢰도 low

## 같은 데이터의 사본·중복 등록

- `mustafaalkanxgmail/Multilingual-Core-Vocabulary`
