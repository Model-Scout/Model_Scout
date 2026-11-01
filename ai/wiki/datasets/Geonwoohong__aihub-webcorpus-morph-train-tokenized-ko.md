---
type: "dataset"
id: "Geonwoohong/aihub-webcorpus-morph-train-tokenized-ko"
source: "huggingface"
url: "https://huggingface.co/datasets/Geonwoohong/aihub-webcorpus-morph-train-tokenized-ko"
downloads: 8
summary: "AIHub 한국어 웹 코퍼스를 형태소 단위로 분석하여 의미 및 문체 정보로 분류한 학습용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
  - "[[정보 추출]]"
  - "[[언어 모델링]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# Geonwoohong/aihub-webcorpus-morph-train-tokenized-ko

> dataset · [Hugging Face](https://huggingface.co/datasets/Geonwoohong/aihub-webcorpus-morph-train-tokenized-ko)

AIHub 한국어 웹 코퍼스를 형태소 단위로 분석하여 의미 및 문체 정보로 분류한 학습용 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[정보 추출]] — metadata · readme, task_categories = `token-classification` · 신뢰도 medium
- **작업**: [[언어 모델링]] — ner · readme = `morphologically annotated with the word identifier` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:information_extraction, task:language_modeling = `Original sentence reconstructed from morphemes` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:language_modeling = `morphologically annotated with the word identifier` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `1116` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `AIHub Korean Web Corpus cleaned and morphologically annotated` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `arrow` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 1673자 ≈ 1116 토큰 (viewer statistics, default/train)
