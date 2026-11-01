---
type: "dataset"
id: "datumo/DATA-Feedback-Bench"
source: "huggingface"
url: "https://huggingface.co/datasets/datumo/DATA-Feedback-Bench"
downloads: 32
summary: "LLM 평가자의 루브릭 준수 능력 측정을 위한 한국어·영어 평가 벤치마크 데이터셋입니다."
readme_status: "ok"
readme_language: "ko"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
  - "[[질의응답]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# datumo/DATA-Feedback-Bench

> dataset · [Hugging Face](https://huggingface.co/datasets/datumo/DATA-Feedback-Bench)

LLM 평가자의 루브릭 준수 능력 측정을 위한 한국어·영어 평가 벤치마크 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `LLM evaluator의 루브릭 준수 능력(rubric following)을 측정하기 위한 평가 벤치마크` · 신뢰도 low
- **작업**: [[질의응답]] — ner · readme = `evaluator의 5점 척도 판정 성능 비교` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:question_answering = `instruction, rubric 및 response를 한국어로 변환한 벤치마크` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `1~5점 레이블` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `2415` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `한국어 및 영어 환경에서 evaluator의 5점 척도 판정 성능 비교` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · dataset_id/tags, readme = `LLM evaluator의 루브릭 준수 능력(rubric following)을 측정하기 위한 평가 벤치마크` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `user` 열 p90 3622자 ≈ 2415 토큰 (viewer statistics, default/feedback_bench)
