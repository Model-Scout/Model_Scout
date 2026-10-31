---
type: "dataset"
id: "Helsinki-NLP/opus_gnome"
source: "huggingface"
url: "https://huggingface.co/datasets/Helsinki-NLP/opus_gnome"
downloads: 297
summary: "Opus Gnome은 다양한 언어 쌍의 번역 데이터셋으로 번역 작업에 사용됩니다."
readme_status: "template"
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
commercial_use:
  - "[[이용 조건 미확인]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# Helsinki-NLP/opus_gnome

> dataset · [Hugging Face](https://huggingface.co/datasets/Helsinki-NLP/opus_gnome)

Opus Gnome은 다양한 언어 쌍의 번역 데이터셋으로 번역 작업에 사용됩니다.

## 분류

- **작업**: [[번역]] — metadata · readme, task_categories = `translation` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:translation = `To load a language pair which isn't part of the config, all you need to do is specify the language code as pairs.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:translation = `To load a language pair which isn't part of the config, all you need to do is specify the language code as pairs.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `137 languages` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license = `unknown` · 신뢰도 high
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
