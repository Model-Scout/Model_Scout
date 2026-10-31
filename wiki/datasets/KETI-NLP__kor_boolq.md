---
type: "dataset"
id: "KETI-NLP/kor_boolq"
source: "huggingface"
url: "https://huggingface.co/datasets/KETI-NLP/kor_boolq"
downloads: 198
summary: "kor_boolq는 자연어 예/아니오 질문에 대한 한국어 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[질의응답]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# KETI-NLP/kor_boolq

> dataset · [Hugging Face](https://huggingface.co/datasets/KETI-NLP/kor_boolq)

kor_boolq는 자연어 예/아니오 질문에 대한 한국어 데이터셋입니다.

## 분류

- **작업**: [[질의응답]] — ner · readme = `BoolQ: Exploring the Surprising Difficulty of Natural Yes/No Questions` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:question_answering = `natural Yes/No Questions` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `natural Yes/No Questions` · 신뢰도 medium
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `117` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-3.0` · 신뢰도 high
- **데이터 용도**: [[학습용]] — metadata · referenced_by_models = `train` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `passage` 열 p90 468자 ≈ 117 토큰 (viewer statistics, default/validation)

## 이 데이터로 학습한 모델

- [[tensorblock__ft-solar-10.7b-v2.1-dpo-GGUF|tensorblock/ft-solar-10.7b-v2.1-dpo-GGUF]]
