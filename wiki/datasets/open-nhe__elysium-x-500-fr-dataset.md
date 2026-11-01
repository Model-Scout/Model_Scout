---
type: "dataset"
id: "open-nhe/elysium-x-500-fr-dataset"
source: "huggingface"
url: "https://huggingface.co/datasets/open-nhe/elysium-x-500-fr-dataset"
downloads: 100
summary: "12,000개의 대화에서 감정 좌표를 라벨링한 감정 인식 학습용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
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
# open-nhe/elysium-x-500-fr-dataset

> dataset · [Hugging Face](https://huggingface.co/datasets/open-nhe/elysium-x-500-fr-dataset)

12,000개의 대화에서 감정 좌표를 라벨링한 감정 인식 학습용 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories = `text-classification` · 신뢰도 medium
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `Each row has: `example_id`, `split`, `language`, `style`, `topic`, `target_text` (the line to classify), `gold_dimensions` (the labels), `coordinate`, and the s` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `labelled with one or two of 500 emotion coordinates` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `11 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `18` · 신뢰도 medium
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-sa-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `12 x 1,000 rows: English, Hindi (written mostly as romanised Hinglish), Hinglish, Spanish, French, German, Portuguese, Bengali, Japanese, Korean, Mandarin Chine` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Rows | 12,000 (train 9,000 / dev 1,500 / test 1,500)` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `target_text` 열 p90 71자 ≈ 18 토큰 (viewer statistics, default/validation)
