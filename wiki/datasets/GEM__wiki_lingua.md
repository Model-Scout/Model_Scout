---
type: "dataset"
id: "GEM/wiki_lingua"
source: "huggingface"
url: "https://huggingface.co/datasets/GEM/wiki_lingua"
downloads: 100109
summary: "WikiLingua는 18개 언어의 위키하우 문서와 요약 쌍으로 구성된 다국어 추상적 요약 평가용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
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
  - "[[비상업 전용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
---
# GEM/wiki_lingua

> dataset · [Hugging Face](https://huggingface.co/datasets/GEM/wiki_lingua)

WikiLingua는 18개 언어의 위키하우 문서와 요약 쌍으로 구성된 다국어 추상적 요약 평가용 데이터셋입니다.

## 분류

- **작업**: [[요약]] — metadata · readme, task_categories = `summarization` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:summarization = `source -- The source document.` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:summarization = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `18 languages` · 신뢰도 high
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-sa-3.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `a high quality, collaborative resource of how-to guides on a diverse set of topics` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `The data is split into train/dev/test.` · 신뢰도 medium
