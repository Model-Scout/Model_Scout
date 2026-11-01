---
type: "dataset"
id: "dancinlab/anima-corpus-5lang-unified-v2"
source: "huggingface"
url: "https://huggingface.co/datasets/dancinlab/anima-corpus-5lang-unified-v2"
downloads: 69
summary: "5개 언어(영어, 프랑스어, 독일어, 스페인어, 한국어) 위키, 페르소나 SNS, 감정·장르 등 다양한 레지스터를 포함한 통합 학습 말뭉치입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[언어 모델링]]"
  - "[[문서 검색]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[de]]"
  - "[[영어]]"
  - "[[es]]"
  - "[[fr]]"
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
  - "[[중규모 데이터]]"
---
# dancinlab/anima-corpus-5lang-unified-v2

> dataset · [Hugging Face](https://huggingface.co/datasets/dancinlab/anima-corpus-5lang-unified-v2)

5개 언어(영어, 프랑스어, 독일어, 스페인어, 한국어) 위키, 페르소나 SNS, 감정·장르 등 다양한 레지스터를 포함한 통합 학습 말뭉치입니다.

## 분류

- **작업**: [[언어 모델링]] — ner · readme = `A UNIFIED 5-language training corpus (en / fr / de / es / ko, byte-vocab V=256) that extends anima-corpus-5lang-unified (v1) by ADDING the register/act/emotion/` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `This corpus feeds a FUTURE 5-lang retrain; the v1 vs v2 difference (register breadth) is itself a pre-registered measurement target` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:language_modeling, task:retrieval = `A UNIFIED 5-language training corpus (en / fr / de / es / ko, byte-vocab V=256)` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:language_modeling = `A UNIFIED 5-language training corpus (en / fr / de / es / ko, byte-vocab V=256)` · 신뢰도 medium
- **언어**: [[de]] — metadata · languages = `de` · 신뢰도 high
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[es]] — metadata · languages = `es` · 신뢰도 high
- **언어**: [[fr]] — metadata · languages = `fr` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `5 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `59` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `A UNIFIED 5-language training corpus (en / fr / de / es / ko, byte-vocab V=256)` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `A UNIFIED 5-language training corpus (en / fr / de / es / ko, byte-vocab V=256) that extends anima-corpus-5lang-unified (v1)` · 신뢰도 medium
- **데이터 형식**: [[텍스트 파일]] — metadata · format = `text` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 236자 ≈ 59 토큰 (viewer statistics, default/train)
