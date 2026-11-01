---
type: "dataset"
id: "GEM/xlsum"
source: "huggingface"
url: "https://huggingface.co/datasets/GEM/xlsum"
downloads: 5959
summary: "BBC 뉴스 기사 135만 쌍의 다국어 요약 데이터셋으로, 45개 언어를 포함합니다."
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
  - "[[뉴스·미디어]]"
dataset_role:
  - "[[학습용]]"
---
# GEM/xlsum

> dataset · [Hugging Face](https://huggingface.co/datasets/GEM/xlsum)

BBC 뉴스 기사 135만 쌍의 다국어 요약 데이터셋으로, 45개 언어를 포함합니다.

## 분류

- **작업**: [[요약]] — metadata · readme, task_categories = `summarization` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:summarization = `article-summary pairs from BBC` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:summarization = `article-summary pairs` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `44 languages` · 신뢰도 high
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-sa-4.0` · 신뢰도 high
- **도메인**: [[뉴스·미디어]] — ner · readme = `The data stems from BBC news articles.` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `It is intended to be used for both multilingual and per-language summarization tasks.` · 신뢰도 medium

## 이 데이터로 학습한 모델

- [[mskayacioglu__mbart50-xlsum|mskayacioglu/mbart50-xlsum]]
