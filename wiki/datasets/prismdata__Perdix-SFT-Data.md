---
type: "dataset"
id: "prismdata/Perdix-SFT-Data"
source: "huggingface"
url: "https://huggingface.co/datasets/prismdata/Perdix-SFT-Data"
downloads: 116
summary: "Perdix-1.1B-Instruct 모델 지시 미세조정을 위한 공개 대화 데이터셋과 토크나이즈 학습 데이터입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 생성]]"
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
  - "[[비상업 전용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# prismdata/Perdix-SFT-Data

> dataset · [Hugging Face](https://huggingface.co/datasets/prismdata/Perdix-SFT-Data)

Perdix-1.1B-Instruct 모델 지시 미세조정을 위한 공개 대화 데이터셋과 토크나이즈 학습 데이터입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, tags, task_categories = `text-generation` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `대화 데이터` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `loss 마스크를 붙인 결과` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `220` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `공개 대화 데이터셋 세 곳에서 받은 원본 파일` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `실제 학습 입력입니다.` · 신뢰도 medium
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 330자 ≈ 220 토큰 (viewer statistics, OIG-smallchip2-ko/train)

## 이 데이터로 학습한 모델

- [[prismdata__Perdix-1.1B-Instruct|prismdata/Perdix-1.1B-Instruct]]
