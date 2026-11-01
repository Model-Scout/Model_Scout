---
type: "dataset"
id: "nayohan/translate_corpus_uniform_313k"
source: "huggingface"
url: "https://huggingface.co/datasets/nayohan/translate_corpus_uniform_313k"
downloads: 28
summary: "10개의 영어-한국어 명령어 병렬 데이터셋을 통합하고 전처리한 313k 문장 번역 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[번역]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# nayohan/translate_corpus_uniform_313k

> dataset · [Hugging Face](https://huggingface.co/datasets/nayohan/translate_corpus_uniform_313k)

10개의 영어-한국어 명령어 병렬 데이터셋을 통합하고 전처리한 313k 문장 번역 데이터셋입니다.

## 분류

- **작업**: [[번역]] — ner · readme = `10개의 명령어(영어-한국어) 병렬 데이터셋 통합 후 공백, 중복데이터, 토큰 4096이상 문장 제거` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:translation = `10개의 명령어(영어-한국어) 병렬 데이터셋 통합 후 공백, 중복데이터, 토큰 4096이상 문장 제거` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:translation = `10개의 명령어(영어-한국어) 병렬 데이터셋 통합 후 공백, 중복데이터, 토큰 4096이상 문장 제거` · 신뢰도 medium
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `378` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `10개의 명령어(영어-한국어) 병렬 데이터셋 통합 후 공백, 중복데이터, 토큰 4096이상 문장 제거` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `10개의 명령어(영어-한국어) 병렬 데이터셋 통합 후 공백, 중복데이터, 토큰 4096이상 문장 제거` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `english` 열 p90 1513자 ≈ 378 토큰 (viewer statistics, default/test)

## 이 데이터로 학습한 모델

- [[afrideva__llama3-instrucTrans-enko-8b-GGUF|afrideva/llama3-instrucTrans-enko-8b-GGUF]]
- [[tensorblock__llama3-instrucTrans-enko-8b-GGUF|tensorblock/llama3-instrucTrans-enko-8b-GGUF]]
