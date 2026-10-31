---
type: "dataset"
id: "BCCard/bc-finance-llm-benchmark"
source: "huggingface"
url: "https://huggingface.co/datasets/BCCard/bc-finance-llm-benchmark"
downloads: 55
summary: "한국 금융 도메인 특화 LLM 성능 평가용 벤치마크 데이터셋입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[질의응답]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[금융·경제]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[CSV]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# BCCard/bc-finance-llm-benchmark

> dataset · [Hugging Face](https://huggingface.co/datasets/BCCard/bc-finance-llm-benchmark)

한국 금융 도메인 특화 LLM 성능 평가용 벤치마크 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `문제 유형 (단일추론, 다중추론 등)` · 신뢰도 low
- **작업**: [[질의응답]] — metadata · readme, task_categories = `question-answering` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:question_answering = `Question / Ground Truth` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `정답 (참조 답변)` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `84` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[금융·경제]] — tag_match · readme, tags = `finance` · 신뢰도 medium
- **데이터 용도**: [[평가용]] — ner · dataset_id/tags, readme = `LLM 성능 평가를 위한 벤치마크 데이터셋입니다.` · 신뢰도 medium
- **데이터 형식**: [[CSV]] — metadata · format = `csv` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

샘플 길이: `ground_truth` 열 p90 126자 ≈ 84 토큰 (viewer statistics, default/train)
