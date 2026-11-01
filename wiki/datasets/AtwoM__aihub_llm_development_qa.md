---
type: "dataset"
id: "AtwoM/aihub_llm_development_qa"
source: "huggingface"
url: "https://huggingface.co/datasets/AtwoM/aihub_llm_development_qa"
downloads: 12
summary: "AIHUB의 한국어 초거대AI 언어모델 개발용 SFT 라벨 데이터 하위셋입니다."
readme_status: "ok"
readme_language: "en"
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
input_length:
  - "[[중문]]"
commercial_use:
  - "[[상업 이용 가능]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[CSV]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# AtwoM/aihub_llm_development_qa

> dataset · [Hugging Face](https://huggingface.co/datasets/AtwoM/aihub_llm_development_qa)

AIHUB의 한국어 초거대AI 언어모델 개발용 SFT 라벨 데이터 하위셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `It contains extracted SFT label data, formatted for supervised fine-tuning.` · 신뢰도 low
- **작업**: [[질의응답]] — metadata · task_categories = `question-answering` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:question_answering = `It contains extracted SFT label data` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering = `It contains extracted SFT label data` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `622` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `It contains extracted SFT label data, formatted for supervised fine-tuning.` · 신뢰도 medium
- **데이터 형식**: [[CSV]] — metadata · format = `csv` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `completion` 열 p90 933자 ≈ 622 토큰 (viewer statistics, default/validation)
