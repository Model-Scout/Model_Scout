---
type: "dataset"
id: "jaeyong2/RAG-COT-En_KO"
source: "huggingface"
url: "https://huggingface.co/datasets/jaeyong2/RAG-COT-En_KO"
downloads: 19
summary: "Qwen2-72B-Instruct 모델로 COT 답변을 생성한 영어-한국어 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
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
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# jaeyong2/RAG-COT-En_KO

> dataset · [Hugging Face](https://huggingface.co/datasets/jaeyong2/RAG-COT-En_KO)

Qwen2-72B-Instruct 모델로 COT 답변을 생성한 영어-한국어 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `We used Qwen/Qwen2-72B-Instruct model to generate answer with COT.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `source dataset from ohsuz/fineweb-edu-2024-10-1M and roneneldan/TinyStories` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `We used Qwen/Qwen2-72B-Instruct model to generate answer with COT.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `3253` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cdla-sharing-1.0` · 신뢰도 high
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `context` 열 p90 4880자 ≈ 3253 토큰 (viewer statistics, default/train)
