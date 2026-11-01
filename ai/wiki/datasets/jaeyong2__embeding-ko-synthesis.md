---
type: "dataset"
id: "jaeyong2/embeding-ko-synthesis"
source: "huggingface"
url: "https://huggingface.co/datasets/jaeyong2/embeding-ko-synthesis"
downloads: 28
summary: "Cohere miracl-ko-corpus-22-12 데이터셋을 기반으로 한 한국어 임베딩 합성 데이터입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[임베딩]]"
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
  - "[[중규모 데이터]]"
---
# jaeyong2/embeding-ko-synthesis

> dataset · [Hugging Face](https://huggingface.co/datasets/jaeyong2/embeding-ko-synthesis)

Cohere miracl-ko-corpus-22-12 데이터셋을 기반으로 한 한국어 임베딩 합성 데이터입니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `context dataset from Cohere/miracl-ko-corpus-22-12` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:embedding = `context dataset from Cohere/miracl-ko-corpus-22-12` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `context dataset from Cohere/miracl-ko-corpus-22-12` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `444` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `This research is supported by TPU Research Cloud program.` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `context` 열 p90 665자 ≈ 444 토큰 (viewer statistics, default/train)
