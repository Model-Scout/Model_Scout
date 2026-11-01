---
type: "dataset"
id: "nayohan/finance-alpaca-ko"
source: "huggingface"
url: "https://huggingface.co/datasets/nayohan/finance-alpaca-ko"
downloads: 25
summary: "nayohan/finance-alpaca-ko는 금융 분야 Alpaca 데이터셋을 한국어로 번역한 원시 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
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
  - "[[중문]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[금융·경제]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# nayohan/finance-alpaca-ko

> dataset · [Hugging Face](https://huggingface.co/datasets/nayohan/finance-alpaca-ko)

nayohan/finance-alpaca-ko는 금융 분야 Alpaca 데이터셋을 한국어로 번역한 원시 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `Translated gbharti/finance-alpaca using nayohan/llama3-instrucTrans-enko-8b.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `Translated gbharti/finance-alpaca` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `Translated gbharti/finance-alpaca` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `1208` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[금융·경제]] — tag_match · readme, tags = `finance` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `This dataset is a raw translated dataset` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `output` 열 p90 1812자 ≈ 1208 토큰 (viewer statistics, default/train)
