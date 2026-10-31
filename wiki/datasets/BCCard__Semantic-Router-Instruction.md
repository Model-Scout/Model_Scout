---
type: "dataset"
id: "BCCard/Semantic-Router-Instruction"
source: "huggingface"
url: "https://huggingface.co/datasets/BCCard/Semantic-Router-Instruction"
downloads: 108
summary: "5개 언어로 된 300만 행 규모의 다국어 명령어 데이터셋으로, 14개 축에 따른 발화 분류용입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[일본어]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[vi]]"
  - "[[중국어]]"
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
  - "[[대규모 데이터]]"
---
# BCCard/Semantic-Router-Instruction

> dataset · [Hugging Face](https://huggingface.co/datasets/BCCard/Semantic-Router-Instruction)

5개 언어로 된 300만 행 규모의 다국어 명령어 데이터셋으로, 14개 축에 따른 발화 분류용입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `a model that classifies one utterance along 14 axes simultaneously` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `Every row's `instruction` actually contains the content signal its axis/value label depends on.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `Label strings (`category`, `value`) are English snake_case in **all** blocks, including the non-English ones — they are the router's target vocabulary` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `5 languages` · 신뢰도 high
- **언어**: [[vi]] — metadata · languages = `vi` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `64` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `A multilingual instruction dataset for training and evaluating the semantic-turn router` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `A multilingual instruction dataset for training and evaluating the semantic-turn router` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high

샘플 길이: `instruction` 열 p90 256자 ≈ 64 토큰 (viewer statistics, default/train)
