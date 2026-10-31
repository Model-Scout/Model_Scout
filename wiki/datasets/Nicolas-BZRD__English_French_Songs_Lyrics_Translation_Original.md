---
type: "dataset"
id: "Nicolas-BZRD/English_French_Songs_Lyrics_Translation_Original"
source: "huggingface"
url: "https://huggingface.co/datasets/Nicolas-BZRD/English_French_Songs_Lyrics_Translation_Original"
downloads: 93
summary: "원곡 가사와 프랑스어 번역 가사를 포함한 99,289곡의 노래 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 생성]]"
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
  - "[[중문]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# Nicolas-BZRD/English_French_Songs_Lyrics_Translation_Original

> dataset · [Hugging Face](https://huggingface.co/datasets/Nicolas-BZRD/English_French_Songs_Lyrics_Translation_Original)

원곡 가사와 프랑스어 번역 가사를 포함한 99,289곡의 노래 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[번역]] — metadata · readme, task_categories = `translation` · 신뢰도 medium
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:translation = `original lyrics and lyrics translated into French` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:translation = `original lyrics and lyrics translated into French` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `38 languages` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `670` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license = `unknown` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Dataset of 99289 songs containing their metadata (author, album, release date, song number), original lyrics and lyrics translated into French.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Dataset of 99289 songs containing their metadata (author, album, release date, song number), original lyrics and lyrics translated into French.` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `french_version` 열 p90 2680자 ≈ 670 토큰 (viewer statistics, default/train)
