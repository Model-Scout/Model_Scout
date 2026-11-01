---
type: "dataset"
id: "syntaxsynth/reasoning-conversations"
source: "huggingface"
url: "https://huggingface.co/datasets/syntaxsynth/reasoning-conversations"
downloads: 30
summary: "다국어 추론 대화 데이터셋으로 여러 언어의 추론 과정을 포함함"
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 생성]]"
  - "[[질의응답]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[de]]"
  - "[[영어]]"
  - "[[es]]"
  - "[[fr]]"
  - "[[일본어]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[중국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# syntaxsynth/reasoning-conversations

> dataset · [Hugging Face](https://huggingface.co/datasets/syntaxsynth/reasoning-conversations)

다국어 추론 대화 데이터셋으로 여러 언어의 추론 과정을 포함함

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `Reasoning traces from Deepseek-v3-R1, Deepseek-v3-R1-Zero` · 신뢰도 low
- **작업**: [[질의응답]] — ner · readme = `Multilingual Reasoning Dataset` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:question_answering = `Multilingual Reasoning Dataset` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering = `Multilingual Reasoning Dataset` · 신뢰도 medium
- **언어**: [[de]] — metadata · languages = `de` · 신뢰도 high
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[es]] — metadata · languages = `es` · 신뢰도 high
- **언어**: [[fr]] — metadata · languages = `fr` · 신뢰도 high
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `7 languages` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `3452` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Multilingual Reasoning Dataset` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Reasoning traces from Deepseek-v3-R1, Deepseek-v3-R1-Zero` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `reasoning` 열 p90 13807자 ≈ 3452 토큰 (viewer statistics, deepseek-v3-r1/train)
