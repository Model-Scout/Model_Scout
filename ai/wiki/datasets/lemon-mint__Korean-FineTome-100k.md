---
type: "dataset"
id: "lemon-mint/Korean-FineTome-100k"
source: "huggingface"
url: "https://huggingface.co/datasets/lemon-mint/Korean-FineTome-100k"
downloads: 50
summary: "arcee-ai/The-Tome 하위 집합을 한국어로 번역한 FineTome-100k 데이터셋입니다."
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
commercial_use:
  - "[[이용 조건 미확인]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# lemon-mint/Korean-FineTome-100k

> dataset · [Hugging Face](https://huggingface.co/datasets/lemon-mint/Korean-FineTome-100k)

arcee-ai/The-Tome 하위 집합을 한국어로 번역한 FineTome-100k 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `시스템 프롬프트와 질문의 성격에 따라서 나누어진 데이터 세트가 나왔어요!` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `시스템 프롬프트와 질문의 성격에 따라서 나누어진 데이터 세트가 나왔어요!` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `시스템 프롬프트와 질문의 성격에 따라서 나누어진 데이터 세트가 나왔어요!` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `HuggingFaceFW/fineweb-edu-classifier 를 사용하여 다시 필터링된 데이터셋 mlabonne/FineTome-100k 을 한국어로 번역했어요.` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high
