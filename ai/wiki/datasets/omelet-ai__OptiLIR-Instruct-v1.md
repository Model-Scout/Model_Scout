---
type: "dataset"
id: "omelet-ai/OptiLIR-Instruct-v1"
source: "huggingface"
url: "https://huggingface.co/datasets/omelet-ai/OptiLIR-Instruct-v1"
downloads: 36
summary: "OptiLIR-Instruct-v1은 차량 경로, 간호사 스케줄링, 소매 재고 최적화 요청과 중간 표현을 쌍으로 제공하는 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# omelet-ai/OptiLIR-Instruct-v1

> dataset · [Hugging Face](https://huggingface.co/datasets/omelet-ai/OptiLIR-Instruct-v1)

OptiLIR-Instruct-v1은 차량 경로, 간호사 스케줄링, 소매 재고 최적화 요청과 중간 표현을 쌍으로 제공하는 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:generation = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `235` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Requests are in Korean, English, or a mix of the two.` · 신뢰도 low
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `ir` 열 p90 352자 ≈ 235 토큰 (viewer statistics, default/validation)
