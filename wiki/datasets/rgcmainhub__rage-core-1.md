---
type: "dataset"
id: "rgcmainhub/rage-core-1"
source: "huggingface"
url: "https://huggingface.co/datasets/rgcmainhub/rage-core-1"
downloads: 43
summary: "Rage Core Gen 1 모델의 감독 학습용 대화 및 코딩 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 생성]]"
  - "[[정보 추출]]"
  - "[[질의응답]]"
  - "[[도구 호출]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# rgcmainhub/rage-core-1

> dataset · [Hugging Face](https://huggingface.co/datasets/rgcmainhub/rage-core-1)

Rage Core Gen 1 모델의 감독 학습용 대화 및 코딩 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **작업**: [[정보 추출]] — ner · readme = `make precise code edits, operate as a coding agent through explicit tool calls` · 신뢰도 low
- **작업**: [[질의응답]] — ner · readme = `understand user intent and ask clarifying questions when requirements are ambiguous` · 신뢰도 low
- **작업**: [[도구 호출]] — tag_match · tags = `tool-calling` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · readme = `Images reach the model as bracketed metadata` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:information_extraction, task:question_answering = `Each line of the JSONL files is one conversation record` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation, task:question_answering = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `13 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `2` · 신뢰도 medium
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `This dataset teaches the model to: understand user intent and ask clarifying questions when requirements are ambiguous` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Supervised fine-tuning dataset for Rage Core Gen 1` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

샘플 길이: `language` 열 p90 7자 ≈ 2 토큰 (viewer statistics, default/validation)
