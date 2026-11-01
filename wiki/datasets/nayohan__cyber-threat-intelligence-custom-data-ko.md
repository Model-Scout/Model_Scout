---
type: "dataset"
id: "nayohan/cyber-threat-intelligence-custom-data-ko"
source: "huggingface"
url: "https://huggingface.co/datasets/nayohan/cyber-threat-intelligence-custom-data-ko"
downloads: 20
summary: "사이버 위협 인텔리전스 관련 맞춤형 한국어 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
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
  - "[[이용 조건 미확인]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# nayohan/cyber-threat-intelligence-custom-data-ko

> dataset · [Hugging Face](https://huggingface.co/datasets/nayohan/cyber-threat-intelligence-custom-data-ko)

사이버 위협 인텔리전스 관련 맞춤형 한국어 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `cyber-threat-intelligence-custom-data` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:generation = `cyber-threat-intelligence-custom-data` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `cyber-threat-intelligence-custom-data` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `207` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `cyber-threat-intelligence-custom-data` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Translated swaption2009/cyber-threat-intelligence-custom-data using nayohan/llama3-instrucTrans-enko-8b.` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

샘플 길이: `solutions` 열 p90 310자 ≈ 207 토큰 (viewer statistics, default/train)
