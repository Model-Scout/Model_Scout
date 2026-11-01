---
type: "dataset"
id: "OzoneAsai/4typeCalculation"
source: "huggingface"
url: "https://huggingface.co/datasets/OzoneAsai/4typeCalculation"
downloads: 822
summary: "숫자와 기호만 사용된 계산 데이터셋으로, 대화 및 지시사항 작업에 활용 가능하다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[de]]"
  - "[[영어]]"
  - "[[fr]]"
  - "[[일본어]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[ru]]"
  - "[[중국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[초대규모 데이터]]"
---
# OzoneAsai/4typeCalculation

> dataset · [Hugging Face](https://huggingface.co/datasets/OzoneAsai/4typeCalculation)

숫자와 기호만 사용된 계산 데이터셋으로, 대화 및 지시사항 작업에 활용 가능하다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `conversation, instruction` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `It only used numbers and symbols.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `It only used numbers and symbols.` · 신뢰도 medium
- **언어**: [[de]] — metadata · languages = `de` · 신뢰도 high
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[fr]] — metadata · languages = `fr` · 신뢰도 high
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `7 languages` · 신뢰도 high
- **언어**: [[ru]] — metadata · languages = `ru` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `3` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `wtfpl` · 신뢰도 high
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[초대규모 데이터]] — metadata · size_categories = `999999999.0` · 신뢰도 high

샘플 길이: `instruction` 열 p90 14자 ≈ 3 토큰 (viewer statistics, default/train)
