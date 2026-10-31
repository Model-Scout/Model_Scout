---
type: "dataset"
id: "developer-lunark/kaidol-character-dataset"
source: "huggingface"
url: "https://huggingface.co/datasets/developer-lunark/kaidol-character-dataset"
downloads: 657
summary: "41개 고유 캐릭터의 한국어 롤플레이 대화 데이터셋으로 캐릭터별 음성 프로필 기반 대화 모델 학습용입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# developer-lunark/kaidol-character-dataset

> dataset · [Hugging Face](https://huggingface.co/datasets/developer-lunark/kaidol-character-dataset)

41개 고유 캐릭터의 한국어 롤플레이 대화 데이터셋으로 캐릭터별 음성 프로필 기반 대화 모델 학습용입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `음성 프로필 평가 시스템으로 검증되었습니다.` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · readme, tags, task_categories = `text-generation` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:generation = `한국어 캐릭터 롤플레이 대화 데이터셋` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `롤플레이 대화 데이터셋` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `SFT, DPO, Multiturn 학습 지원` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high
