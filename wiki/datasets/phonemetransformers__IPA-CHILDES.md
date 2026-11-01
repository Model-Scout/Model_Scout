---
type: "dataset"
id: "phonemetransformers/IPA-CHILDES"
source: "huggingface"
url: "https://huggingface.co/datasets/phonemetransformers/IPA-CHILDES"
downloads: 890
summary: "CHILDES에서 수집한 아동 대상 발화를 음소 표기로 변환한 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[임베딩]]"
  - "[[언어 모델링]]"
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
  - "[[이용 조건 미확인]]"
domain:
  - "[[교육]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[CSV]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# phonemetransformers/IPA-CHILDES

> dataset · [Hugging Face](https://huggingface.co/datasets/phonemetransformers/IPA-CHILDES)

CHILDES에서 수집한 아동 대상 발화를 음소 표기로 변환한 데이터셋입니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `This dataset contains utterances downloaded from CHILDES which have been pre-processed and converted to a phonemic representation.` · 신뢰도 low
- **작업**: [[언어 모델링]] — tag_match · readme, tags = `language modeling` · 신뢰도 medium
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:embedding, task:language_modeling = `This dataset contains utterances downloaded from CHILDES which have been pre-processed and converted to a phonemic representation.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:language_modeling = ``ipa_transcription`| A phonemic transcription of the utterance, space-separated with word boundaries marked with the `WORD_BOUNDARY` token.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `28 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `30` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[교육]] — ner · readme = `This dataset contains utterances downloaded from CHILDES which have been pre-processed and converted to a phonemic representation.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = ``character_split_utterance` and `ipa_transcription` are designed for training character-based (phoneme-based) language models` · 신뢰도 medium
- **데이터 형식**: [[CSV]] — metadata · format = `csv` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `99999999.0` · 신뢰도 high

샘플 길이: `character_split_utterance` 열 p90 121자 ≈ 30 토큰 (viewer statistics, Korean/train)

## 같은 데이터의 사본·중복 등록

- `superBigPigeon/IPA-CHILDES`
