---
type: "dataset"
id: "vocabradar/WordTranslation"
source: "huggingface"
url: "https://huggingface.co/datasets/vocabradar/WordTranslation"
downloads: 140
summary: "42개 언어의 단어별 번역을 제공하는 오프라인 단어 번역 팩 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[번역]]"
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
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# vocabradar/WordTranslation

> dataset · [Hugging Face](https://huggingface.co/datasets/vocabradar/WordTranslation)

42개 언어의 단어별 번역을 제공하는 오프라인 단어 번역 팩 데이터셋입니다.

## 분류

- **작업**: [[번역]] — metadata · readme, task_categories = `translation` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:translation = `every word of a language's cleaned vocabulary` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:translation = `paired with its translations` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `42 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `3` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Offline word-translation packs for 42 languages around English and Chinese` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `The vocabulary comes straight from the vocabradar/wordfreq dataset — that dataset is this one's direct source` · 신뢰도 low
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high

샘플 길이: `word` 열 p90 11자 ≈ 3 토큰 (viewer statistics, default/train)
