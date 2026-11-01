---
type: "dataset"
id: "syp1229/instruct_train_idiom"
source: "huggingface"
url: "https://huggingface.co/datasets/syp1229/instruct_train_idiom"
downloads: 30
summary: "한국어 관용구 문장이 인간 작성인지 AI 작성인지 구분하는 이진 분류 데이터셋입니다."
readme_status: "thin"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
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
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# syp1229/instruct_train_idiom

> dataset · [Hugging Face](https://huggingface.co/datasets/syp1229/instruct_train_idiom)

한국어 관용구 문장이 인간 작성인지 AI 작성인지 구분하는 이진 분류 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories = `text-classification` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `text: 프롬프트 형식 문장` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `labels: 0=ai, 1=human` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `111` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `이 데이터셋은 한국어 관용구 문장에 대해, 해당 문장이 인간이 작성했는지 AI가 작성했는지를 구분하는 이진 분류 태스크에 사용됩니다.` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 167자 ≈ 111 토큰 (viewer statistics, default/validation)
