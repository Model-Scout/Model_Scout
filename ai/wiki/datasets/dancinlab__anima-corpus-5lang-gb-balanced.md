---
type: "dataset"
id: "dancinlab/anima-corpus-5lang-gb-balanced"
source: "huggingface"
url: "https://huggingface.co/datasets/dancinlab/anima-corpus-5lang-gb-balanced"
downloads: 39
summary: "영어, 프랑스어, 독일어, 스페인어, 한국어 5개 언어의 균형 잡힌 0.35GB KOSMOS 계층 훈련 코퍼스입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[언어 모델링]]"
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
  - "[[대규모 데이터]]"
---
# dancinlab/anima-corpus-5lang-gb-balanced

> dataset · [Hugging Face](https://huggingface.co/datasets/dancinlab/anima-corpus-5lang-gb-balanced)

영어, 프랑스어, 독일어, 스페인어, 한국어 5개 언어의 균형 잡힌 0.35GB KOSMOS 계층 훈련 코퍼스입니다.

## 분류

- **작업**: [[언어 모델링]] — ner · readme = `A KOSMOS-tier-BALANCED, ~0.35 GB default-lane training corpus (en / fr / de / es / ko, byte-vocab V=256)` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:language_modeling = `training corpus (en / fr / de / es / ko, byte-vocab V=256)` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:language_modeling = `training corpus (en / fr / de / es / ko, byte-vocab V=256)` · 신뢰도 medium
- **언어**: [[de]] — metadata · languages = `de` · 신뢰도 high
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[es]] — metadata · languages = `es` · 신뢰도 high
- **언어**: [[fr]] — metadata · languages = `fr` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `5 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `153` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-4.0` · 신뢰도 high
- **도메인**: [[일반]] — tag_match · tags = `wikipedia` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `default-lane training corpus` · 신뢰도 medium
- **데이터 형식**: [[텍스트 파일]] — metadata · format = `text` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 610자 ≈ 153 토큰 (viewer statistics, default/train)
