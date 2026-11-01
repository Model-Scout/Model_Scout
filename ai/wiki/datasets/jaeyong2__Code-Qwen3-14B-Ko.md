---
type: "dataset"
id: "jaeyong2/Code-Qwen3-14B-Ko"
source: "huggingface"
url: "https://huggingface.co/datasets/jaeyong2/Code-Qwen3-14B-Ko"
downloads: 11
summary: "nayohan/CodeFeedback-Filtered-Instruction-ko 질문 데이터셋과 Qwen3-14B 모델 평가용 데이터셋입니다."
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
  - "[[초장문]]"
commercial_use:
  - "[[조건부 이용]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# jaeyong2/Code-Qwen3-14B-Ko

> dataset · [Hugging Face](https://huggingface.co/datasets/jaeyong2/Code-Qwen3-14B-Ko)

nayohan/CodeFeedback-Filtered-Instruction-ko 질문 데이터셋과 Qwen3-14B 모델 평가용 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `We used Qwen/Qwen3-14B to evaluate the appropriateness of those candidates.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `question dataset` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `evaluate the appropriateness of those candidates` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[초장문]] — viewer_stats · viewer_statistics = `24206` · 신뢰도 medium
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `question dataset from nayohan/CodeFeedback-Filtered-Instruction-ko` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 36309자 ≈ 24206 토큰 (viewer statistics, default/train)
