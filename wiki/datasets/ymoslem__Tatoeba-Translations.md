---
type: "dataset"
id: "ymoslem/Tatoeba-Translations"
source: "huggingface"
url: "https://huggingface.co/datasets/ymoslem/Tatoeba-Translations"
downloads: 170
summary: "Tatoeba 번역 데이터셋으로 414개 언어, 약 5900개 언어쌍의 문장 번역 쌍을 포함합니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[번역]]"
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
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# ymoslem/Tatoeba-Translations

> dataset · [Hugging Face](https://huggingface.co/datasets/ymoslem/Tatoeba-Translations)

Tatoeba 번역 데이터셋으로 414개 언어, 약 5900개 언어쌍의 문장 번역 쌍을 포함합니다.

## 분류

- **작업**: [[번역]] — metadata · readme, task_categories = `translation` · 신뢰도 high
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:translation = `source (sentence_src) and target (sentence_tgt) sentences` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:translation = `source (sentence_src) and target (sentence_tgt) sentences` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `152 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `34` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `The sentences are downloaded from the Tatoeba collection website.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `The dataset is processed through mapping sentences.tar.bz2 using sentences_base.tar.bz2 to find source (sentence_src) and target (sentence_tgt) sentences.` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high

샘플 길이: `sentence_tgt` 열 p90 137자 ≈ 34 토큰 (viewer statistics, default/train)
