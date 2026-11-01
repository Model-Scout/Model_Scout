---
type: "dataset"
id: "dancinlab/anima-agent-lane-argcopy-corpus"
source: "huggingface"
url: "https://huggingface.co/datasets/dancinlab/anima-agent-lane-argcopy-corpus"
downloads: 45
summary: "agent-lane 도구 사용 시 정확한 인자 복사를 강제하는 바이트 수준 데모 코퍼스입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[도구 호출]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[de]]"
  - "[[영어]]"
  - "[[es]]"
  - "[[fr]]"
  - "[[한국어]]"
  - "[[다국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
dataset_role:
  - "[[학습용]]"
---
# dancinlab/anima-agent-lane-argcopy-corpus

> dataset · [Hugging Face](https://huggingface.co/datasets/dancinlab/anima-agent-lane-argcopy-corpus)

agent-lane 도구 사용 시 정확한 인자 복사를 강제하는 바이트 수준 데모 코퍼스입니다.

## 분류

- **작업**: [[도구 호출]] — tag_match · readme, tags = `tool-use` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme = `Byte-level (vocab256) agent-lane tool-USE demo corpus` · 신뢰도 low
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `the call arg is a verbatim copy of the prompt key` · 신뢰도 low
- **언어**: [[de]] — metadata · languages = `de` · 신뢰도 high
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[es]] — metadata · languages = `es` · 신뢰도 high
- **언어**: [[fr]] — metadata · languages = `fr` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `5 languages` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `built to close the key-binding residual of the register-matched tool-use grounding fire` · 신뢰도 low
