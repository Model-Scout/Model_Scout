---
type: "dataset"
id: "werty1248/s1k-1.1-Ko-ReGenerated-Formatted"
source: "huggingface"
url: "https://huggingface.co/datasets/werty1248/s1k-1.1-Ko-ReGenerated-Formatted"
downloads: 23
summary: "simplescaling/s1K-1.1 질문 데이터를 GPT-4o로 번역하고 Deepseek-R1으로 한국어 추론 및 답변 재생성한 데이터셋입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
  - "[[질의응답]]"
  - "[[번역]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[장문]]"
commercial_use:
  - "[[상업 이용 가능]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# werty1248/s1k-1.1-Ko-ReGenerated-Formatted

> dataset · [Hugging Face](https://huggingface.co/datasets/werty1248/s1k-1.1-Ko-ReGenerated-Formatted)

simplescaling/s1K-1.1 질문 데이터를 GPT-4o로 번역하고 Deepseek-R1으로 한국어 추론 및 답변 재생성한 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[질의응답]] — ner · readme = `Deepseek-R1 (fp8, Provider: fireworks.ai)을 사용하여 한국어로 추론 및 답하게 함` · 신뢰도 low
- **작업**: [[번역]] — ner · readme = `simplescaling/s1K-1.1 에서 question 데이터만 GPT-4o를 이용하여 번역` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:question_answering, task:translation = `question 데이터만 GPT-4o를 이용하여 번역` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering, task:translation = `한국어로 추론 및 답하게 함` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[장문]] — viewer_stats · viewer_statistics = `15227` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `1차 정제` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 22841자 ≈ 15227 토큰 (viewer statistics, default/train)
