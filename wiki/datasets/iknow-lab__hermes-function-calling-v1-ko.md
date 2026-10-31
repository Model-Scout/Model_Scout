---
type: "dataset"
id: "iknow-lab/hermes-function-calling-v1-ko"
source: "huggingface"
url: "https://huggingface.co/datasets/iknow-lab/hermes-function-calling-v1-ko"
downloads: 33
summary: "문서에서 구조화된 정보 추출을 위한 함수 호출 형태의 JSON 스키마 데이터를 제공하는 한국어 데이터셋입니다."
readme_status: "ok"
readme_language: "ko"
korean_focus: "ko_with_others"
task:
  - "[[정보 추출]]"
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
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# iknow-lab/hermes-function-calling-v1-ko

> dataset · [Hugging Face](https://huggingface.co/datasets/iknow-lab/hermes-function-calling-v1-ko)

문서에서 구조화된 정보 추출을 위한 함수 호출 형태의 JSON 스키마 데이터를 제공하는 한국어 데이터셋입니다.

## 분류

- **작업**: [[정보 추출]] — ner · readme = `당신은 전문가로서 구조화된 정보 추출 AI 모델입니다. 정보 추출을 위해 문서를 제공받습니다.` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:information_extraction = `문서를 제공받습니다.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `추출된 정보를 XML 태그 <tools></tools> 내의 함수 서명 형태로 출력할 json 스키마도 제공받습니다.` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `40` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `문서에서 개념이나 정보가 실제 상황에 어떻게 적용될 수 있는지를 묻는…` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `GPT-4o-mini로 번역했으나, 길이가 너무 길거나 에러가 난 경우가 1300 건 가량 제외됨.` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `task` 열 p90 59자 ≈ 40 토큰 (viewer statistics, default/train)
