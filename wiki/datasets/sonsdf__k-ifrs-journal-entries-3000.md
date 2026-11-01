---
type: "dataset"
id: "sonsdf/k-ifrs-journal-entries-3000"
source: "huggingface"
url: "https://huggingface.co/datasets/sonsdf/k-ifrs-journal-entries-3000"
downloads: 19
summary: "한국 회계기준 거래 입력으로 계산 과정과 복식부기 분개를 생성하는 한국어 합성 데이터셋입니다."
readme_status: "ok"
readme_language: "ko"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[금융·경제]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# sonsdf/k-ifrs-journal-entries-3000

> dataset · [Hugging Face](https://huggingface.co/datasets/sonsdf/k-ifrs-journal-entries-3000)

한국 회계기준 거래 입력으로 계산 과정과 복식부기 분개를 생성하는 한국어 합성 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `Alpaca 스타일의 instruction / input / output 3개 필드.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation = `text` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[금융·경제]] — tag_match · readme, tags = `finance` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `로컬 소형 언어모델(Qwen2.5-Coder-7B)의 LoRA 파인튜닝 연구에 사용되었습니다.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `optimized-parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high
