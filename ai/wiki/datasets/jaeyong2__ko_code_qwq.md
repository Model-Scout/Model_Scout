---
type: "dataset"
id: "jaeyong2/ko_code_qwq"
source: "huggingface"
url: "https://huggingface.co/datasets/jaeyong2/ko_code_qwq"
downloads: 21
summary: "nayohan/CodeFeedback-Filtered-Instruction-ko의 질문 데이터셋으로 Qwen/QwQ-32B 모델에 사용됨"
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[질의응답]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[초장문]]"
commercial_use:
  - "[[상업 이용 가능]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# jaeyong2/ko_code_qwq

> dataset · [Hugging Face](https://huggingface.co/datasets/jaeyong2/ko_code_qwq)

nayohan/CodeFeedback-Filtered-Instruction-ko의 질문 데이터셋으로 Qwen/QwQ-32B 모델에 사용됨

## 분류

- **작업**: [[질의응답]] — ner · readme = `question dataset from nayohan/CodeFeedback-Filtered-Instruction-ko` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:question_answering = `question dataset from nayohan/CodeFeedback-Filtered-Instruction-ko` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `question dataset from nayohan/CodeFeedback-Filtered-Instruction-ko` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[초장문]] — viewer_stats · viewer_statistics = `25474` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `question dataset from nayohan/CodeFeedback-Filtered-Instruction-ko` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `answer` 열 p90 38211자 ≈ 25474 토큰 (viewer statistics, default/train)
