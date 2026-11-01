---
type: "dataset"
id: "SungJoo/KoTox"
source: "huggingface"
url: "https://huggingface.co/datasets/SungJoo/KoTox"
downloads: 40
summary: "KoTox는 한국어로 된 3.9만 개의 유해한 지시문-출력 쌍으로 구성된 자동 생성 독성 지시문 데이터셋입니다."
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
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[CSV]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# SungJoo/KoTox

> dataset · [Hugging Face](https://huggingface.co/datasets/SungJoo/KoTox)

KoTox는 한국어로 된 3.9만 개의 유해한 지시문-출력 쌍으로 구성된 자동 생성 독성 지시문 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **작업**: [[질의응답]] — metadata · task_categories = `question-answering` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:question_answering = `KoTox is an automatically generated toxic instruction dataset in Korean, comprising 39K unethical instruction-output pairs.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering = `KoTox is an automatically generated toxic instruction dataset in Korean, comprising 39K unethical instruction-output pairs.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `24` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `KoTox is an automatically generated toxic instruction dataset in Korean` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `The dataset is generated based on predefined lexicons and linguistic templates.` · 신뢰도 low
- **데이터 형식**: [[CSV]] — metadata · format = `csv` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `instruction` 열 p90 36자 ≈ 24 토큰 (viewer statistics, default/train)
