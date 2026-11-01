---
type: "dataset"
id: "Seungjun/Korean-DeepMath-with-Difficulty"
source: "huggingface"
url: "https://huggingface.co/datasets/Seungjun/Korean-DeepMath-with-Difficulty"
downloads: 20
summary: "Korean-DeepMath 데이터에 난이도와 주제 메타데이터를 추가한 수학 추론용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[텍스트 생성]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[교육]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# Seungjun/Korean-DeepMath-with-Difficulty

> dataset · [Hugging Face](https://huggingface.co/datasets/Seungjun/Korean-DeepMath-with-Difficulty)

Korean-DeepMath 데이터에 난이도와 주제 메타데이터를 추가한 수학 추론용 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `Prepared for controlled Korean mathematical reasoning SFT experiments, including difficulty-aware sampling such as TDCS.` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:generation = `Korean mathematical reasoning` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `Korean mathematical reasoning` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[교육]] — ner · readme = `Prepared for controlled Korean mathematical reasoning SFT experiments` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Prepared for controlled Korean mathematical reasoning SFT experiments` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `optimized-parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high
