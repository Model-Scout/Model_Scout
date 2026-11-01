---
type: "dataset"
id: "logitly-ai/flash-coding-sft-v1"
source: "huggingface"
url: "https://huggingface.co/datasets/logitly-ai/flash-coding-sft-v1"
downloads: 148
summary: "Flash Coding은 실제 소스 저장소에서 AI 코딩 에이전트의 작업 기록을 담은 학습용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 생성]]"
input_modality:
  - "[[문서 파일 (입력 형식)|문서 파일]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[ar]]"
  - "[[de]]"
  - "[[영어]]"
  - "[[fr]]"
  - "[[it]]"
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
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# logitly-ai/flash-coding-sft-v1

> dataset · [Hugging Face](https://huggingface.co/datasets/logitly-ai/flash-coding-sft-v1)

Flash Coding은 실제 소스 저장소에서 AI 코딩 에이전트의 작업 기록을 담은 학습용 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **입력 형식**: [[문서 파일 (입력 형식)|문서 파일]] — metadata · modality = `document` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `A trace is a list of messages in the style of the Anthropic Messages API: each message has a `role` (`user` or `assistant`) and a `content`, a list of typed blo` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `A trace is a list of messages in the style of the Anthropic Messages API: each message has a `role` (`user` or `assistant`) and a `content`, a list of typed blo` · 신뢰도 medium
- **언어**: [[ar]] — metadata · languages = `ar` · 신뢰도 high
- **언어**: [[de]] — metadata · languages = `de` · 신뢰도 high
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[fr]] — metadata · languages = `fr` · 신뢰도 high
- **언어**: [[it]] — metadata · languages = `it` · 신뢰도 high
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `8 languages` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `2216` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Flash Coding is a dataset of agentic coding traces: an AI coding agent working on tasks in real source repositories.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Flash Coding is training data: it carries no scores and no task-success labels, so the effect of training on it cannot be read off the data itself.` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `init_md` 열 p90 8862자 ≈ 2216 토큰 (viewer statistics, default/train)

## 같은 데이터의 사본·중복 등록

- `logitly-ai/flash-coding-dpo-v1`
