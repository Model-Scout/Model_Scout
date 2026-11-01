---
type: "dataset"
id: "msw-ai-tf/maplestory-worlds-creator-code-instruct"
source: "huggingface"
url: "https://huggingface.co/datasets/msw-ai-tf/maplestory-worlds-creator-code-instruct"
downloads: 22
summary: "MapleStory Worlds의 mlua 스크립트 언어용 명령형 코드 데이터셋으로 게임 스크립트 작성 학습용입니다."
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
  - "[[중문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[문화·관광]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# msw-ai-tf/maplestory-worlds-creator-code-instruct

> dataset · [Hugging Face](https://huggingface.co/datasets/msw-ai-tf/maplestory-worlds-creator-code-instruct)

MapleStory Worlds의 mlua 스크립트 언어용 명령형 코드 데이터셋으로 게임 스크립트 작성 학습용입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `each example is grounded in its source document and paired with a natural-language task` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `commented mlua code` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `1128` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[문화·관광]] — ner · readme = `the scripting language of MapleStory Worlds` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Instruction-style code dataset for mlua` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `code` 열 p90 1692자 ≈ 1128 토큰 (viewer statistics, ko/train)
