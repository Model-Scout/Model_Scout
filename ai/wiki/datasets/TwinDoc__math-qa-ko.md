---
type: "dataset"
id: "TwinDoc/math-qa-ko"
source: "huggingface"
url: "https://huggingface.co/datasets/TwinDoc/math-qa-ko"
downloads: 5
summary: "AI-HUB에서 받은 경제 분야 숫자연산 기계독해 데이터로, 다양한 수학 문제 유형 포함."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[질의응답]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[금융·경제]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# TwinDoc/math-qa-ko

> dataset · [Hugging Face](https://huggingface.co/datasets/TwinDoc/math-qa-ko)

AI-HUB에서 받은 경제 분야 숫자연산 기계독해 데이터로, 다양한 수학 문제 유형 포함.

## 분류

- **작업**: [[질의응답]] — metadata · readme, task_categories = `question-answering` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:question_answering = `json 파일을 DataFrame 형태로 변형하여 수정 없이 업로드하였습니다.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `숫자연산 기계독해 데이터 입니다.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-sa-4.0` · 신뢰도 high
- **도메인**: [[금융·경제]] — tag_match · readme, tags = `economy` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `경제 > Train > json 파일을 DataFrame 형태로 변형하여 수정 없이 업로드하였습니다.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high
