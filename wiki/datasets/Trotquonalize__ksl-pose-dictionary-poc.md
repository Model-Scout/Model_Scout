---
type: "dataset"
id: "Trotquonalize/ksl-pose-dictionary-poc"
source: "huggingface"
url: "https://huggingface.co/datasets/Trotquonalize/ksl-pose-dictionary-poc"
downloads: 59
summary: "한국수어(KSL) text-to-pose 시제품용 키포인트 데이터셋으로, KSL 수어 표현 학습에 활용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
  - "[[이미지 생성]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[이미지 (출력 형식)|이미지]]"
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[일반]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# Trotquonalize/ksl-pose-dictionary-poc

> dataset · [Hugging Face](https://huggingface.co/datasets/Trotquonalize/ksl-pose-dictionary-poc)

한국수어(KSL) text-to-pose 시제품용 키포인트 데이터셋으로, KSL 수어 표현 학습에 활용됨.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **작업**: [[이미지 생성]] — metadata · task_categories = `text-to-image` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — task_rule · task:image_generation = `image` · 신뢰도 medium
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:image_generation = `(한국어 문장, KSL gloss 시퀀스)` · 신뢰도 high
- **출력 형식**: [[이미지 (출력 형식)|이미지]] — task_rule · task:image_generation = `image` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `(한국어 문장, KSL gloss 시퀀스)` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `50` · 신뢰도 medium
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-sa-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `한국수어(KSL) text-to-pose 시제품용 keypoint 데이터셋.` · 신뢰도 low
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `korean_text` 열 p90 76자 ≈ 50 토큰 (viewer statistics, default/validation)
