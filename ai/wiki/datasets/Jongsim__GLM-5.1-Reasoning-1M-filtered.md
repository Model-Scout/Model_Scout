---
type: "dataset"
id: "Jongsim/GLM-5.1-Reasoning-1M-filtered"
source: "huggingface"
url: "https://huggingface.co/datasets/Jongsim/GLM-5.1-Reasoning-1M-filtered"
downloads: 80
summary: "GLM-5.1-Reasoning-1M-filtered는 거절 응답을 필터링한 추론 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
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
  - "[[다국어]]"
input_length:
  - "[[초장문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[학술·논문]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# Jongsim/GLM-5.1-Reasoning-1M-filtered

> dataset · [Hugging Face](https://huggingface.co/datasets/Jongsim/GLM-5.1-Reasoning-1M-filtered)

GLM-5.1-Reasoning-1M-filtered는 거절 응답을 필터링한 추론 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **작업**: [[질의응답]] — ner · readme = `mathematics reasoning` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:question_answering = `assistant response field` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering = `assistant response field` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `multilingual` · 신뢰도 high
- **입력 길이**: [[초장문]] — viewer_stats · viewer_statistics = `37762` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[학술·논문]] — ner · readme = `mathematics reasoning` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `full main subset, refusals removed` · 신뢰도 low
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `output` 열 p90 151049자 ≈ 37762 토큰 (viewer statistics, default/train)
