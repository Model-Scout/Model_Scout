---
type: "dataset"
id: "fdemelo/ipa-childes-split"
source: "huggingface"
url: "https://huggingface.co/datasets/fdemelo/ipa-childes-split"
downloads: 80
summary: "IPA-CHILDES 데이터셋을 후처리하여 언어 태그와 IPA 전사 정보를 포함한 학습용 분할 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[임베딩]]"
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
  - "[[CSV]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# fdemelo/ipa-childes-split

> dataset · [Hugging Face](https://huggingface.co/datasets/fdemelo/ipa-childes-split)

IPA-CHILDES 데이터셋을 후처리하여 언어 태그와 IPA 전사 정보를 포함한 학습용 분할 데이터셋입니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `columns `ipa_espeak` and `ipa_epitran` added, containing IPA transcriptions of `sentence` by the phonemizers` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:embedding = `column `gloss` renamed as `sentence`` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `columns `ipa_espeak` and `ipa_epitran` added, containing IPA transcriptions of `sentence`` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `29 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `40` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `This dataset is a postprocessed version of the IPA-CHILDES dataset.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `a train/test split is now provided` · 신뢰도 medium
- **데이터 형식**: [[CSV]] — metadata · format = `csv` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `99999999.0` · 신뢰도 high

샘플 길이: `character_split_utterance` 열 p90 161자 ≈ 40 토큰 (viewer statistics, default/test)
