---
type: "dataset"
id: "tellang/yeji-bazi-translated-ko"
source: "huggingface"
url: "https://huggingface.co/datasets/tellang/yeji-bazi-translated-ko"
downloads: 52
summary: "중국어 사주팔자 데이터를 한국어로 번역한 명리학 전문 용어 및 상담 대화 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 생성]]"
  - "[[번역]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
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
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# tellang/yeji-bazi-translated-ko

> dataset · [Hugging Face](https://huggingface.co/datasets/tellang/yeji-bazi-translated-ko)

중국어 사주팔자 데이터를 한국어로 번역한 명리학 전문 용어 및 상담 대화 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[번역]] — metadata · readme, tags, task_categories = `translation` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:translation = `중국어 사주팔자 데이터의 한국어 번역` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:translation = `중국어 사주팔자 데이터의 한국어 번역` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `20` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `중국어 사주팔자 데이터의 한국어 번역` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `중국어 사주팔자 데이터의 한국어 번역` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `question_ko` 열 p90 81자 ≈ 20 토큰 (viewer statistics, default/train)
