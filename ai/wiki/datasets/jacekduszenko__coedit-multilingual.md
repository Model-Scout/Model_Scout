---
type: "dataset"
id: "jacekduszenko/coedit-multilingual"
source: "huggingface"
url: "https://huggingface.co/datasets/jacekduszenko/coedit-multilingual"
downloads: 41
summary: "다국어 텍스트 편집 데이터셋으로 문법 교정, 의역, 단순화 등 편집 모델 평가용입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
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
  - "[[it]]"
  - "[[일본어]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[nl]]"
  - "[[pt]]"
  - "[[중국어]]"
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
  - "[[중규모 데이터]]"
---
# jacekduszenko/coedit-multilingual

> dataset · [Hugging Face](https://huggingface.co/datasets/jacekduszenko/coedit-multilingual)

다국어 텍스트 편집 데이터셋으로 문법 교정, 의역, 단순화 등 편집 모델 평가용입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `A multilingual text-editing dataset for evaluating instruction-following edit models (grammar correction, paraphrase, simplification, neutralization, coherence,` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `A multilingual text-editing dataset for evaluating instruction-following edit models` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `A multilingual text-editing dataset for evaluating instruction-following edit models` · 신뢰도 medium
- **언어**: [[de]] — metadata · languages = `de` · 신뢰도 high
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[es]] — metadata · languages = `es` · 신뢰도 high
- **언어**: [[fr]] — metadata · languages = `fr` · 신뢰도 high
- **언어**: [[it]] — metadata · languages = `it` · 신뢰도 high
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `10 languages` · 신뢰도 high
- **언어**: [[nl]] — metadata · languages = `nl` · 신뢰도 high
- **언어**: [[pt]] — metadata · languages = `pt` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `77` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `A multilingual text-editing dataset for evaluating instruction-following edit models` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `English: the original grammarly/coedit (train + validation).` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `src` 열 p90 306자 ≈ 77 토큰 (viewer statistics, default/validation)
