---
type: "dataset"
id: "amphora/Open-R1-Mulitlingual-SFT"
source: "huggingface"
url: "https://huggingface.co/datasets/amphora/Open-R1-Mulitlingual-SFT"
downloads: 80
summary: "Open-R1-Mulitlingual-SFT는 14개 언어로 번역된 다국어 감독 학습용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[장문]]"
commercial_use:
  - "[[상업 이용 가능]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# amphora/Open-R1-Mulitlingual-SFT

> dataset · [Hugging Face](https://huggingface.co/datasets/amphora/Open-R1-Mulitlingual-SFT)

Open-R1-Mulitlingual-SFT는 14개 언어로 번역된 다국어 감독 학습용 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `Open-R1-Mulitlingual-SFT is a curated dataset designed for multilingual supervised fine-tuning.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `The source data comprises multiple datasets containing original prompts and responses` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `The source data comprises multiple datasets containing original prompts and responses` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `14 languages` · 신뢰도 high
- **입력 길이**: [[장문]] — viewer_stats · viewer_statistics = `11586` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `Open-R1-Mulitlingual-SFT is a curated dataset designed for multilingual supervised fine-tuning.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `response` 열 p90 46343자 ≈ 11586 토큰 (viewer statistics, default/train)
