---
type: "dataset"
id: "neuralfoundry-coder/OpenMathReasoning-mini-ko"
source: "huggingface"
url: "https://huggingface.co/datasets/neuralfoundry-coder/OpenMathReasoning-mini-ko"
downloads: 69
summary: "OpenMathReasoning-mini 데이터셋을 한국어로 번역한 수학 문제 및 풀이 데이터셋입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 생성]]"
  - "[[질의응답]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
input_length:
  - "[[장문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[교육]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# neuralfoundry-coder/OpenMathReasoning-mini-ko

> dataset · [Hugging Face](https://huggingface.co/datasets/neuralfoundry-coder/OpenMathReasoning-mini-ko)

OpenMathReasoning-mini 데이터셋을 한국어로 번역한 수학 문제 및 풀이 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **작업**: [[질의응답]] — metadata · readme, task_categories = `question-answering` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:question_answering = `수학 문제` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering = `풀이 과정 (Chain-of-Thought)` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[장문]] — viewer_stats · viewer_statistics = `6793` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[교육]] — ner · readme = `수학 문제 및 풀이` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `학습(가공 후 · 가중치 HF 없음)` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `generated_solution` 열 p90 10189자 ≈ 6793 토큰 (viewer statistics, default/cot)
