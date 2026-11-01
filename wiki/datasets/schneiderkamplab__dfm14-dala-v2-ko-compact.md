---
type: "dataset"
id: "schneiderkamplab/dfm14-dala-v2-ko-compact"
source: "huggingface"
url: "https://huggingface.co/datasets/schneiderkamplab/dfm14-dala-v2-ko-compact"
downloads: 68
summary: "DaLA v2 한국어 DFM14 컴팩트 감사 하위집합으로 교정 및 수용성 평가용 데이터셋입니다."
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
  - "[[중문]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# schneiderkamplab/dfm14-dala-v2-ko-compact

> dataset · [Hugging Face](https://huggingface.co/datasets/schneiderkamplab/dfm14-dala-v2-ko-compact)

DaLA v2 한국어 DFM14 컴팩트 감사 하위집합으로 교정 및 수용성 평가용 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories = `text-classification` · 신뢰도 medium
- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:generation = `Only `messages` are model input, with `target_message_index=1`.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `Other fields expose labels, full original source text, edits, provenance and audit evidence.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `3142` · 신뢰도 medium
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `One language dataset combining all selected base and additive runs.` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `validation_representative` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `train_representative` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high

샘플 길이: `provenance_json` 열 p90 4713자 ≈ 3142 토큰 (viewer statistics, acceptability/train)
