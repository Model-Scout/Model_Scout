---
type: "dataset"
id: "squarelike/sharegpt_deepl_ko_translation"
source: "huggingface"
url: "https://huggingface.co/datasets/squarelike/sharegpt_deepl_ko_translation"
downloads: 86
summary: "sharegpt_deepl_ko 데이터를 한-영 번역 데이터로 변환한 데이터셋입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "not_ko"
task:
  - "[[번역]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[이용 조건 미확인]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# squarelike/sharegpt_deepl_ko_translation

> dataset · [Hugging Face](https://huggingface.co/datasets/squarelike/sharegpt_deepl_ko_translation)

sharegpt_deepl_ko 데이터를 한-영 번역 데이터로 변환한 데이터셋입니다.

## 분류

- **작업**: [[번역]] — ner · readme = `sharegpt_deepl_ko를 한-영 번역데이터로 변환한 데이터입니다.` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:translation = `한-영 번역데이터` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:translation = `한-영 번역데이터` · 신뢰도 medium
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `623` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `sharegpt_deepl_ko에서 몇 가지의 데이터 전처리를 진행했습니다.` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `english` 열 p90 2492자 ≈ 623 토큰 (viewer statistics, default/train)

## 이 데이터로 학습한 모델

- [[squarelike__Gugugo-koen-7B-V1.1-GGUF|squarelike/Gugugo-koen-7B-V1.1-GGUF]]
- [[tensorblock__nayohan_llama3-8b-it-translation-sharegpt-en-ko-GGUF|tensorblock/nayohan_llama3-8b-it-translation-sharegpt-en-ko-GGUF]]
