---
type: "dataset"
id: "suchirsalhan/Phonemized-UD"
source: "huggingface"
url: "https://huggingface.co/datasets/suchirsalhan/Phonemized-UD"
downloads: 1803
summary: "34개 이상의 언어에 대해 Universal Dependencies를 음소화한 다국어 음소화 코퍼스입니다."
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
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[텍스트 파일]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# suchirsalhan/Phonemized-UD

> dataset · [Hugging Face](https://huggingface.co/datasets/suchirsalhan/Phonemized-UD)

34개 이상의 언어에 대해 Universal Dependencies를 음소화한 다국어 음소화 코퍼스입니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `We use G2P+ to phonemize Universal Dependencies.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:embedding = `We use G2P+ to phonemize Universal Dependencies.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `We use G2P+ to phonemize Universal Dependencies.` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `36 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `89` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Phoneme-UD: A Multilingual Phonemized Universal Dependencies Corpus for 34+ Languages` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Phoneme-UD: A Multilingual Phonemized Universal Dependencies Corpus for 34+ Languages` · 신뢰도 low
- **데이터 형식**: [[텍스트 파일]] — metadata · format = `text` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 357자 ≈ 89 토큰 (viewer statistics, ko/train)
