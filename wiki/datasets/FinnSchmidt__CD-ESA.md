---
type: "dataset"
id: "FinnSchmidt/CD-ESA"
source: "huggingface"
url: "https://huggingface.co/datasets/FinnSchmidt/CD-ESA"
downloads: 334
summary: "CD-ESA는 기계번역 품질 평가를 위한 교차 도메인 오류 구간 주석 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
  - "[[번역]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[de]]"
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[중국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# FinnSchmidt/CD-ESA

> dataset · [Hugging Face](https://huggingface.co/datasets/FinnSchmidt/CD-ESA)

CD-ESA는 기계번역 품질 평가를 위한 교차 도메인 오류 구간 주석 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `CD-ESA was created to study how well reference-free machine translation evaluation metrics, i.e. quality estimation (QE) metrics, generalize to unseen domains.` · 신뢰도 low
- **작업**: [[번역]] — metadata · tags, task_categories = `translation` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:translation = `Each row contains the following top-level fields: - `src`: source sentence - `tgt`: machine translation - `system`: MT system that produced the translation - `l` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:translation = `The `ESA_scores` and `annotations` fields store multiple human annotations for each translation.` · 신뢰도 medium
- **언어**: [[de]] — metadata · languages = `de` · 신뢰도 high
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `4 languages` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `58` · 신뢰도 medium
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `CD-ESA was created to study how well reference-free machine translation evaluation metrics, i.e. quality estimation (QE) metrics, generalize to unseen domains.` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `This dataset contains the publicly releasable WMT23 and Emea portions of CD-ESA` · 신뢰도 low
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `tgt` 열 p90 231자 ≈ 58 토큰 (viewer statistics, default/train)
