---
type: "dataset"
id: "TwinDoc/math-qa-sample_ext-ko"
source: "huggingface"
url: "https://huggingface.co/datasets/TwinDoc/math-qa-sample_ext-ko"
downloads: 6
summary: "AI-HUB 숫자연산 기계독해 데이터를 활용해 경제 분야 질의응답용으로 만든 한국어 단서추출 데이터입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[질의응답]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
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
  - "[[소규모 데이터]]"
---
# TwinDoc/math-qa-sample_ext-ko

> dataset · [Hugging Face](https://huggingface.co/datasets/TwinDoc/math-qa-sample_ext-ko)

AI-HUB 숫자연산 기계독해 데이터를 활용해 경제 분야 질의응답용으로 만든 한국어 단서추출 데이터입니다.

## 분류

- **작업**: [[질의응답]] — metadata · readme, task_categories = `question-answering` · 신뢰도 high
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:question_answering = `json 파일을 DataFrame 형태로 변형하여 전처리 및 답변 생성을 하였습니다.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `Raw 데이터의 answer 정보를 참고하여 답변을 생성하였습니다.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-sa-4.0` · 신뢰도 high
- **도메인**: [[금융·경제]] — tag_match · readme, tags = `economy` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `경제 > Train > json 파일을 DataFrame 형태로 변형하여 전처리 및 답변 생성을 하였습니다.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high
