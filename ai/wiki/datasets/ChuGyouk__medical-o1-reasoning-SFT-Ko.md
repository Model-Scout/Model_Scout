---
type: "dataset"
id: "ChuGyouk/medical-o1-reasoning-SFT-Ko"
source: "huggingface"
url: "https://huggingface.co/datasets/ChuGyouk/medical-o1-reasoning-SFT-Ko"
downloads: 53
summary: "의료 문제 해결을 위한 고급 의료 추론에 특화된 HuatuoGPT-o1 모델의 한국어 미세조정 데이터셋입니다."
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
domain:
  - "[[의료·보건]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# ChuGyouk/medical-o1-reasoning-SFT-Ko

> dataset · [Hugging Face](https://huggingface.co/datasets/ChuGyouk/medical-o1-reasoning-SFT-Ko)

의료 문제 해결을 위한 고급 의료 추론에 특화된 HuatuoGPT-o1 모델의 한국어 미세조정 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 high
- **작업**: [[질의응답]] — metadata · task_categories = `question-answering` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:question_answering = `Your task is to translate the following three categories (Question, Reasoning, Final_answer) into Korean` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering = `Your task is to translate the following three categories (Question, Reasoning, Final_answer) into Korean` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `946` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[의료·보건]] — tag_match · readme, tags = `medical` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `The original data was used to fine-tune HuatuoGPT-o1` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `Complex_Cot` 열 p90 1420자 ≈ 946 토큰 (viewer statistics, default/train)
