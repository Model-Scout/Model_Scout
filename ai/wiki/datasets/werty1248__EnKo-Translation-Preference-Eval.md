---
type: "dataset"
id: "werty1248/EnKo-Translation-Preference-Eval"
source: "huggingface"
url: "https://huggingface.co/datasets/werty1248/EnKo-Translation-Preference-Eval"
downloads: 21
summary: "한국어-영어 번역 품질 평가를 위한 오역 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[이용 조건 미확인]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# werty1248/EnKo-Translation-Preference-Eval

> dataset · [Hugging Face](https://huggingface.co/datasets/werty1248/EnKo-Translation-Preference-Eval)

한국어-영어 번역 품질 평가를 위한 오역 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `evaluating the performance of reward models or filtering methods used in assessing the quality of Korean to English translations` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `Korean to English translations` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `Korean to English translations` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `191` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **데이터 용도**: [[평가용]] — ner · dataset_id/tags, readme = `57 records is too small to evaluate something` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

샘플 길이: `source_text` 열 p90 286자 ≈ 191 토큰 (viewer statistics, default/test)
