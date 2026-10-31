---
type: "dataset"
id: "1-800-SHARED-TASKS/xlsum-subset"
source: "huggingface"
url: "https://huggingface.co/datasets/1-800-SHARED-TASKS/xlsum-subset"
downloads: 511
summary: "BBC 기사와 요약문 135만 쌍으로 구성된 45개 언어 다국어 요약 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 생성]]"
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
  - "[[단문]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[미디어 파일]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# 1-800-SHARED-TASKS/xlsum-subset

> dataset · [Hugging Face](https://huggingface.co/datasets/1-800-SHARED-TASKS/xlsum-subset)

BBC 기사와 요약문 135만 쌍으로 구성된 45개 언어 다국어 요약 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[요약]] — metadata · readme, task_categories = `summarization` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:summarization = `article-summary pairs from BBC` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:summarization = `article-summary pairs from BBC` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `43 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `47` · 신뢰도 medium
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-sa-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `The dataset covers 45 languages ranging from low to high-resource` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `We used a 80%-10%-10% split for all languages with a few exceptions.` · 신뢰도 low
- **데이터 형식**: [[미디어 파일]] — metadata · format = `webdataset` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

샘플 길이: `__url__` 열 p90 187자 ≈ 47 토큰 (viewer statistics, default/train)
