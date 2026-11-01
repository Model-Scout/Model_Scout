---
type: "dataset"
id: "taeminlee/Ko-mrtydi"
source: "huggingface"
url: "https://huggingface.co/datasets/taeminlee/Ko-mrtydi"
downloads: 87
summary: "Ko-mrtydi는 Mr.TyDI 한국어 데이터를 BeIR 포맷으로 변환한 검색용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[문서 검색]]"
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
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# taeminlee/Ko-mrtydi

> dataset · [Hugging Face](https://huggingface.co/datasets/taeminlee/Ko-mrtydi)

Ko-mrtydi는 Mr.TyDI 한국어 데이터를 BeIR 포맷으로 변환한 검색용 데이터셋입니다.

## 분류

- **작업**: [[문서 검색]] — metadata · readme, tags, task_categories, task_ids = `text-retrieval` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:retrieval = `This dataset represents a conversion of the Korean (Ko) section from the Mr.TyDI dataset` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `making it compatible for use with mteb` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `1516` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `This dataset represents a conversion of the Korean (Ko) section from the Mr.TyDI dataset` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `This dataset represents a conversion of the Korean (Ko) section from the Mr.TyDI dataset into the BeIR format` · 신뢰도 low
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 2274자 ≈ 1516 토큰 (viewer statistics, corpus/corpus)
