---
type: "dataset"
id: "richard-park/aihub-llm-corpora-2024-1113"
source: "huggingface"
url: "https://huggingface.co/datasets/richard-park/aihub-llm-corpora-2024-1113"
downloads: 38
summary: "aihub-llm-corpora-2024-1113 데이터셋은 LLM 학습용 대규모 말뭉치입니다."
readme_status: "template"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[언어 모델링]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[초장문]]"
commercial_use:
  - "[[이용 조건 미확인]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# richard-park/aihub-llm-corpora-2024-1113

> dataset · [Hugging Face](https://huggingface.co/datasets/richard-park/aihub-llm-corpora-2024-1113)

aihub-llm-corpora-2024-1113 데이터셋은 LLM 학습용 대규모 말뭉치입니다.

## 분류

- **작업**: [[언어 모델링]] — ner · readme = `tokenizer: sapie-tokenizer-v2.0

sample #: 2,688,972` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:language_modeling = `tokenizer: sapie-tokenizer-v2.0` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:language_modeling = `tokenizer: sapie-tokenizer-v2.0` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[초장문]] — viewer_stats · viewer_statistics = `59856` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `tokenizer: sapie-tokenizer-v2.0

sample #: 2,688,972` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 89784자 ≈ 59856 토큰 (viewer statistics, default/train)
