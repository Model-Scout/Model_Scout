---
type: "dataset"
id: "jojo0217/korean_safe_conversation"
source: "huggingface"
url: "https://huggingface.co/datasets/jojo0217/korean_safe_conversation"
downloads: 321
summary: "성균관대와 VAIV COMPANY가 구축한 윤리적 일상대화 챗봇 학습용 데이터셋입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
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
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# jojo0217/korean_safe_conversation

> dataset · [Hugging Face](https://huggingface.co/datasets/jojo0217/korean_safe_conversation)

성균관대와 VAIV COMPANY가 구축한 윤리적 일상대화 챗봇 학습용 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `일상대화 데이터셋` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `자연스럽고 윤리적인 챗봇 구축을 위한 데이터셋 입니다.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `439` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `일상대화에 중점을 두면서 혐오표현, 편향적인 대답을 지양하면서 일상대화를 하는 것에 중점을 두었습니다.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `성균관대 - VAIV COMPANY 산학협력을 위해 구축한 일상대화 데이터입니다.` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `output` 열 p90 658자 ≈ 439 토큰 (viewer statistics, default/train)

## 같은 데이터의 사본·중복 등록

- `Eri4nder/korean_safe_conversation`

## 이 데이터로 학습한 모델

- [[shopkeeper__kor-finewiki-1b-chat|shopkeeper/kor-finewiki-1b-chat]]
