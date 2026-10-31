---
type: "dataset"
id: "OpenCoder-LLM/opc-fineweb-code-corpus"
source: "huggingface"
url: "https://huggingface.co/datasets/OpenCoder-LLM/opc-fineweb-code-corpus"
downloads: 7219
summary: "OpenCoder 사전학습에 사용된 Fineweb에서 추출한 코드 관련 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
input_length:
  - "[[장문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[초대규모 데이터]]"
---
# OpenCoder-LLM/opc-fineweb-code-corpus

> dataset · [Hugging Face](https://huggingface.co/datasets/OpenCoder-LLM/opc-fineweb-code-corpus)

OpenCoder 사전학습에 사용된 Fineweb에서 추출한 코드 관련 데이터셋입니다.

## 분류

- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme = `code-related page recalled from fineweb` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `code-related page recalled from fineweb` · 신뢰도 low
- **입력 길이**: [[장문]] — viewer_stats · viewer_statistics = `14164` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `code-related page recalled from fineweb` · 신뢰도 low
- **데이터 용도**: [[학습용]] — metadata · referenced_by_models = `train` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[초대규모 데이터]] — metadata · size_categories = `999999999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 56655자 ≈ 14164 토큰 (viewer statistics, default/train)

## 이 데이터로 학습한 모델

- [[FINAL-Bench__Aether-7B-5Attn|FINAL-Bench/Aether-7B-5Attn]]
- [[FINAL-Bench__Aether-7B-5Attn-it|FINAL-Bench/Aether-7B-5Attn-it]]
