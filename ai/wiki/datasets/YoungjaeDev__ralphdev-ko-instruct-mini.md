---
type: "dataset"
id: "YoungjaeDev/ralphdev-ko-instruct-mini"
source: "huggingface"
url: "https://huggingface.co/datasets/YoungjaeDev/ralphdev-ko-instruct-mini"
downloads: 18
summary: "한국어 문단과 질문을 대화 형식으로 바꾼 짧은 답변 학습용 소규모 SFT 데이터입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
  - "[[질의응답]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# YoungjaeDev/ralphdev-ko-instruct-mini

> dataset · [Hugging Face](https://huggingface.co/datasets/YoungjaeDev/ralphdev-ko-instruct-mini)

한국어 문단과 질문을 대화 형식으로 바꾼 짧은 답변 학습용 소규모 SFT 데이터입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[질의응답]] — metadata · readme, task_categories = `question-answering` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:question_answering = `한국어 문단과 질문을 대화 형식으로 바꾼 소규모 SFT 실습 자료다.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering = `모델이 주어진 문단에서 답을 찾아 짧게 쓰도록 학습하는 과정을 재현하는 데 쓴다.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `이 데이터는 한국어 문단과 질문을 대화 형식으로 바꾼 소규모 SFT 실습 자료다.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `두 config 모두 train split만 공개한다.` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high
