---
type: "dataset"
id: "Hibiki12y/yukbimsource"
source: "huggingface"
url: "https://huggingface.co/datasets/Hibiki12y/yukbimsource"
downloads: 24
summary: "선급 규정과 해사 웹 문서 기반 한국어 질의응답 데이터셋으로 QA 학습과 평가에 사용됨"
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
  - "[[텍스트 생성]]"
  - "[[질의응답]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# Hibiki12y/yukbimsource

> dataset · [Hugging Face](https://huggingface.co/datasets/Hibiki12y/yukbimsource)

선급 규정과 해사 웹 문서 기반 한국어 질의응답 데이터셋으로 QA 학습과 평가에 사용됨

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `난이도 1/2/3 = 350/433/217` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[질의응답]] — metadata · readme, task_categories = `question-answering` · 신뢰도 high
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:generation, task:question_answering = `한국어 질의응답 데이터입니다` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering = `답변 형식: 한국어 설명 + 원문 영어 인용 + 출처(문서·조항·쪽)` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `해사 규정·웹 문서 기반 한국어 QA` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `평가셋을 함께 담고 있습니다` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `학습 후보 QA` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high
