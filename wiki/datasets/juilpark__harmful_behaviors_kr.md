---
type: "dataset"
id: "juilpark/harmful_behaviors_kr"
source: "huggingface"
url: "https://huggingface.co/datasets/juilpark/harmful_behaviors_kr"
downloads: 10
summary: "영어 문장과 한국어 번역을 포함한 유해 행동 관련 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[번역]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[이용 조건 미확인]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# juilpark/harmful_behaviors_kr

> dataset · [Hugging Face](https://huggingface.co/datasets/juilpark/harmful_behaviors_kr)

영어 문장과 한국어 번역을 포함한 유해 행동 관련 데이터셋입니다.

## 분류

- **작업**: [[번역]] — ner · readme = `This dataset keeps the original English prompt in text_en and adds a Korean translation in text_ko.` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:translation = `This dataset keeps the original English prompt in text_en and adds a Korean translation in text_ko.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:translation = `This dataset keeps the original English prompt in text_en and adds a Korean translation in text_ko.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `64` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `The translation source files are stored in translations/train_ko.txt and translations/test_ko.txt.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

샘플 길이: `text_en` 열 p90 96자 ≈ 64 토큰 (viewer statistics, default/test)
