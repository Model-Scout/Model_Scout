---
type: "dataset"
id: "omneity-labs/ipa-dict"
source: "huggingface"
url: "https://huggingface.co/datasets/omneity-labs/ipa-dict"
downloads: 49
summary: "여러 언어의 단어 발음을 국제 음성 기호(IPA)로 수집한 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[임베딩]]"
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
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# omneity-labs/ipa-dict

> dataset · [Hugging Face](https://huggingface.co/datasets/omneity-labs/ipa-dict)

여러 언어의 단어 발음을 국제 음성 기호(IPA)로 수집한 데이터셋입니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `This dataset is a comprehensive collection of word pronunciations in the International Phonetic Alphabet (IPA) for multiple languages.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:embedding = `text: The written word or phrase.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `ipa: The corresponding IPA pronunciation.` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `25 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `5` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `This dataset is a comprehensive collection of word pronunciations in the International Phonetic Alphabet (IPA) for multiple languages.` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high

샘플 길이: `ipa` 열 p90 21자 ≈ 5 토큰 (viewer statistics, default/train)
