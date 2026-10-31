---
type: "dataset"
id: "yoh/modular-sentence-encoders-paraphrase"
source: "huggingface"
url: "https://huggingface.co/datasets/yoh/modular-sentence-encoders-paraphrase"
downloads: 118
summary: "23개 언어로 번역된 다중 병렬 패러프레이즈 말뭉치로 문장 인코더 학습용 데이터입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
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
input_length:
  - "[[단문]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# yoh/modular-sentence-encoders-paraphrase

> dataset · [Hugging Face](https://huggingface.co/datasets/yoh/modular-sentence-encoders-paraphrase)

23개 언어로 번역된 다중 병렬 패러프레이즈 말뭉치로 문장 인코더 학습용 데이터입니다.

## 분류

- **작업**: [[임베딩]] — metadata · readme, task_categories = `feature-extraction` · 신뢰도 medium
- **작업**: [[번역]] — tag_match · tags = `machine-translation` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:embedding, task:translation = `Five English paraphrase datasets, each translated into 22 further languages` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:translation = `Five English paraphrase datasets, each translated into 22 further languages` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `23 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `65` · 신뢰도 medium
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Multi-parallel paraphrase corpus (23 languages)` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `The contrastive training data of Modular Sentence Encoders` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `anchor_rw` 열 p90 260자 ≈ 65 토큰 (viewer statistics, altlex/train)
