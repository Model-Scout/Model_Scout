---
type: "dataset"
id: "franktheglock/temp-guard-data-20260722"
source: "huggingface"
url: "https://huggingface.co/datasets/franktheglock/temp-guard-data-20260722"
downloads: 37
summary: "NVIDIA Nemotron-Safety-Guard-Dataset-v3의 5만 샘플로 LLM 안전 가드 모델 미세조정용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[상업 이용 가능]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# franktheglock/temp-guard-data-20260722

> dataset · [Hugging Face](https://huggingface.co/datasets/franktheglock/temp-guard-data-20260722)

NVIDIA Nemotron-Safety-Guard-Dataset-v3의 5만 샘플로 LLM 안전 가드 모델 미세조정용 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `Determine if the following is safe or unsafe. If unsafe, identify the category.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `Each line is a JSON object with a messages array` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `assistant response includes the category` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `12 languages` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `1530` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 6122자 ≈ 1530 토큰 (viewer statistics, default/train)
