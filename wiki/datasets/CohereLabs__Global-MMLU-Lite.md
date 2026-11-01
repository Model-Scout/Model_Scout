---
type: "dataset"
id: "CohereLabs/Global-MMLU-Lite"
source: "huggingface"
url: "https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite"
downloads: 13899
summary: "23개 언어로 번역된 다국어 평가용 MMLU Lite 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[질의응답]]"
input_modality:
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
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# CohereLabs/Global-MMLU-Lite

> dataset · [Hugging Face](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite)

23개 언어로 번역된 다국어 평가용 MMLU Lite 데이터셋입니다.

## 분류

- **작업**: [[질의응답]] — ner · readme = `Global-MMLU-Lite is a multilingual evaluation set spanning 23 languages` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:question_answering = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:question_answering = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `23 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `70` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Global-MMLU-Lite is a multilingual evaluation set spanning 23 languages` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `Global-MMLU-Lite is a multilingual evaluation set spanning 23 languages` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `question` 열 p90 282자 ≈ 70 토큰 (viewer statistics, ko/test)
