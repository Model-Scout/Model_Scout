---
type: "dataset"
id: "passing2961/KorEmpatheticDialogues"
source: "huggingface"
url: "https://huggingface.co/datasets/passing2961/KorEmpatheticDialogues"
downloads: 49
summary: "KorEmpatheticDialogues는 원본 EmpatheticDialogues를 한국어로 번역한 공감 대화 데이터셋입니다."
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
  - "[[단문]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# passing2961/KorEmpatheticDialogues

> dataset · [Hugging Face](https://huggingface.co/datasets/passing2961/KorEmpatheticDialogues)

KorEmpatheticDialogues는 원본 EmpatheticDialogues를 한국어로 번역한 공감 대화 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_ids = `conversational` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `the dialogue where each dict entry includes {utter_idx, utter, user_id}` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `the emotion category (e.g., guilty, caring, etc)` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `57` · 신뢰도 medium
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `KorEmpatheticDialogues is a publicly available Korean empathetic dialogue dataset translated from the original EmpatheticDialogues dataset` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `All models and datasets are intended for research purposes only.` · 신뢰도 low
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `situation` 열 p90 86자 ≈ 57 토큰 (viewer statistics, default/validation)
