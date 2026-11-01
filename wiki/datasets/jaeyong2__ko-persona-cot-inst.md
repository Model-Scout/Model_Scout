---
type: "dataset"
id: "jaeyong2/ko-persona-cot-inst"
source: "huggingface"
url: "https://huggingface.co/datasets/jaeyong2/ko-persona-cot-inst"
downloads: 20
summary: "한국어 페르소나 질문 데이터에 대해 Qwen 모델로 COT 답변을 생성한 데이터셋입니다."
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
  - "[[이용 조건 미확인]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# jaeyong2/ko-persona-cot-inst

> dataset · [Hugging Face](https://huggingface.co/datasets/jaeyong2/ko-persona-cot-inst)

한국어 페르소나 질문 데이터에 대해 Qwen 모델로 COT 답변을 생성한 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `We used Qwen/Qwen2-72B-Instruct model to generate answer with COT.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `features: ['content', 'text']` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `features: ['content', 'text']` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `1557` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `ds = load_dataset("jaeyong2/ko-persona-cot-inst", split="train")` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 2336자 ≈ 1557 토큰 (viewer statistics, default/train)
