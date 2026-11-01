---
type: "dataset"
id: "mkd-hossain/keural-nova-tooluse"
source: "huggingface"
url: "https://huggingface.co/datasets/mkd-hossain/keural-nova-tooluse"
downloads: 93
summary: "Keural Nova v1.2용 도구 호출 데이터로, 단일 및 다중 턴 대화와 긴 문맥 포함"
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 생성]]"
  - "[[도구 호출]]"
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
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# mkd-hossain/keural-nova-tooluse

> dataset · [Hugging Face](https://huggingface.co/datasets/mkd-hossain/keural-nova-tooluse)

Keural Nova v1.2용 도구 호출 데이터로, 단일 및 다중 턴 대화와 긴 문맥 포함

## 분류

- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[도구 호출]] — tag_match · readme, tags = `tool-calling` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `Rendered as Qwen XML tool calls via ms-swift's native agent schema` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `Rendered as Qwen XML tool calls via ms-swift's native agent schema` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `737` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `Tool-calling data used for Keural Nova v1.2. 17,337 rows` · 신뢰도 low
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `tools` 열 p90 1106자 ≈ 737 토큰 (viewer statistics, default/train)
