---
type: "dataset"
id: "saadumar26/lfm25-base-blind-spots"
source: "huggingface"
url: "https://huggingface.co/datasets/saadumar26/lfm25-base-blind-spots"
downloads: 21
summary: "LFM2.5-1.2B-Base 모델의 10가지 실패 사례(블라인드 스팟)를 문서화한 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
  - "[[텍스트 생성]]"
  - "[[번역]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[ar]]"
  - "[[de]]"
  - "[[영어]]"
  - "[[es]]"
  - "[[fr]]"
  - "[[일본어]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[중국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# saadumar26/lfm25-base-blind-spots

> dataset · [Hugging Face](https://huggingface.co/datasets/saadumar26/lfm25-base-blind-spots)

LFM2.5-1.2B-Base 모델의 10가지 실패 사례(블라인드 스팟)를 문서화한 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `This dataset documents 10 diverse failure cases (blind spots) of the LiquidAI/LFM2.5-1.2B-Base model` · 신뢰도 low
- **작업**: [[텍스트 생성]] — ner · readme = `The model wraps simple factual answers inside unnecessary multiple-choice format` · 신뢰도 low
- **작업**: [[번역]] — ner · readme = `When asked to translate into Arabic, French, or Spanish, the model ignores the instruction and responds in English instead.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:generation, task:translation = `The prompt given to the model` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:translation = `The correct answer` · 신뢰도 medium
- **언어**: [[ar]] — metadata · languages = `ar` · 신뢰도 high
- **언어**: [[de]] — metadata · languages = `de` · 신뢰도 high
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[es]] — metadata · languages = `es` · 신뢰도 high
- **언어**: [[fr]] — metadata · languages = `fr` · 신뢰도 high
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `8 languages` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Languages EN, AR, ZH, FR, DE, JA, KO, ES` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `This dataset documents 10 diverse failure cases (blind spots) of the LiquidAI/LFM2.5-1.2B-Base model` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high
