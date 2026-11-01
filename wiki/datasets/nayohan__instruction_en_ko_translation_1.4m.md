---
type: "dataset"
id: "nayohan/instruction_en_ko_translation_1.4m"
source: "huggingface"
url: "https://huggingface.co/datasets/nayohan/instruction_en_ko_translation_1.4m"
downloads: 62
summary: "9개의 영어-한국어 명령어 병렬 데이터셋을 통합하고 중복 및 긴 문장 제거한 1.4백만 데이터셋입니다."
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
  - "[[대규모 데이터]]"
---
# nayohan/instruction_en_ko_translation_1.4m

> dataset · [Hugging Face](https://huggingface.co/datasets/nayohan/instruction_en_ko_translation_1.4m)

9개의 영어-한국어 명령어 병렬 데이터셋을 통합하고 중복 및 긴 문장 제거한 1.4백만 데이터셋입니다.

## 분류

- **작업**: [[번역]] — ner · readme = `9개의 명령어(영어-한국어) 병렬 데이터셋 통합 후 공백, 중복데이터, 토큰 4096이상 문장 제거` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:translation = `9개의 명령어(영어-한국어) 병렬 데이터셋 통합 후 공백, 중복데이터, 토큰 4096이상 문장 제거` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:translation = `9개의 명령어(영어-한국어) 병렬 데이터셋 통합 후 공백, 중복데이터, 토큰 4096이상 문장 제거` · 신뢰도 medium
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `396` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `9개의 명령어(영어-한국어) 병렬 데이터셋 통합 후 공백, 중복데이터, 토큰 4096이상 문장 제거` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `9개의 명령어(영어-한국어) 병렬 데이터셋 통합 후 공백, 중복데이터, 토큰 4096이상 문장 제거` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high

샘플 길이: `english` 열 p90 1584자 ≈ 396 토큰 (viewer statistics, default/test)

## 이 데이터로 학습한 모델

- [[mradermacher__exaone3-instrucTrans-v2-enko-7.8b-GGUF|mradermacher/exaone3-instrucTrans-v2-enko-7.8b-GGUF]]
- [[mradermacher__exaone3-instrucTrans-v2-enko-7.8b-i1-GGUF|mradermacher/exaone3-instrucTrans-v2-enko-7.8b-i1-GGUF]]
