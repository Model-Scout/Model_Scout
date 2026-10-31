---
type: "dataset"
id: "dancinlab/anima-corpus-5lang-unified"
source: "huggingface"
url: "https://huggingface.co/datasets/dancinlab/anima-corpus-5lang-unified"
downloads: 28
summary: "en, fr, de, es, ko 5개 언어의 위키, SNS, 페르소나 텍스트를 통합한 다국어 학습 코퍼스입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[임베딩]]"
  - "[[텍스트 생성]]"
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
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[텍스트 파일]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# dancinlab/anima-corpus-5lang-unified

> dataset · [Hugging Face](https://huggingface.co/datasets/dancinlab/anima-corpus-5lang-unified)

en, fr, de, es, ko 5개 언어의 위키, SNS, 페르소나 텍스트를 통합한 다국어 학습 코퍼스입니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `so a single byte-level model is multilingual across ALL surfaces (wiki + SNS + persona) in en / fr / de / es / ko` · 신뢰도 low
- **작업**: [[텍스트 생성]] — ner · readme = `This corpus feeds a FUTURE 5-lang 7B retrain` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:embedding, task:generation = `wiki + SNS + persona` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `a single byte-level model is multilingual across ALL surfaces (wiki + SNS + persona)` · 신뢰도 medium
- **언어**: [[de]] — metadata · languages = `de` · 신뢰도 high
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[es]] — metadata · languages = `es` · 신뢰도 high
- **언어**: [[fr]] — metadata · languages = `fr` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `5 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `59` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-4.0` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `A UNIFIED 5-language training corpus` · 신뢰도 medium
- **데이터 형식**: [[텍스트 파일]] — metadata · format = `text` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 238자 ≈ 59 토큰 (viewer statistics, default/train)
