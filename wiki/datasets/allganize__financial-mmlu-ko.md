---
type: "dataset"
id: "allganize/financial-mmlu-ko"
source: "huggingface"
url: "https://huggingface.co/datasets/allganize/financial-mmlu-ko"
downloads: 34
summary: "금융 도메인의 한국어 다중 선택 객관식 문제 데이터셋으로 금융 지식 평가용입니다."
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
  - "[[이용 조건 미확인]]"
domain:
  - "[[금융·경제]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# allganize/financial-mmlu-ko

> dataset · [Hugging Face](https://huggingface.co/datasets/allganize/financial-mmlu-ko)

금융 도메인의 한국어 다중 선택 객관식 문제 데이터셋으로 금융 지식 평가용입니다.

## 분류

- **작업**: [[질의응답]] — ner · readme = `금융 도메인의 다중 선택(Multiple Choice) 데이터셋입니다. 질문과 선택지가 주어졌을 때, 답을 찾는 객관식 문제입니다.` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:question_answering = `입력값은 text이며` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `답을 찾는 객관식 문제입니다.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[금융·경제]] — ner · readme = `financial-mmlu-ko 데이터는 금융 도메인의 다중 선택(Multiple Choice) 데이터셋입니다.` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `한국어 데이터를 생성하기 위해, 여러 금융 문제가 있는 공공 사이트의 문제들을 크롤링하여 수집, 검수(104건)하였습니다. 그리고 Wikipedia와 공공사이트들의 금융사전/보고서들을 기반으로 GPT-4로 문제를 생성하고 사람이 검수하였습니다.(315건)` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high
