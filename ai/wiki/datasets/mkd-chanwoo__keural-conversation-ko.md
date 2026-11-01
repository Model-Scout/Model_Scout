---
type: "dataset"
id: "mkd-chanwoo/keural-conversation-ko"
source: "huggingface"
url: "https://huggingface.co/datasets/mkd-chanwoo/keural-conversation-ko"
downloads: 110
summary: "한국어 일상 대화 AI 학습용 합성 데이터셋으로 9개 주제, 191,093개 멀티턴 대화 쌍 포함"
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
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# mkd-chanwoo/keural-conversation-ko

> dataset · [Hugging Face](https://huggingface.co/datasets/mkd-chanwoo/keural-conversation-ko)

한국어 일상 대화 AI 학습용 합성 데이터셋으로 9개 주제, 191,093개 멀티턴 대화 쌍 포함

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:generation = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation = `text` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `253` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `한국어 일상 대화 AI 학습용 합성 데이터셋입니다.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `학습 데이터 보강 용도로 제작되었습니다.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `optimized-parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `conversation` 열 p90 379자 ≈ 253 토큰 (viewer statistics, default/train)
