---
type: "dataset"
id: "david9dragon9/shp_translations"
source: "huggingface"
url: "https://huggingface.co/datasets/david9dragon9/shp_translations"
downloads: 414
summary: "Stanford Human Preference 데이터셋 세 가지 분할본을 번역한 데이터로 도메인 불변 보상 모델 학습용입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 생성]]"
  - "[[질의응답]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[th]]"
  - "[[중국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[법률]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# david9dragon9/shp_translations

> dataset · [Hugging Face](https://huggingface.co/datasets/david9dragon9/shp_translations)

Stanford Human Preference 데이터셋 세 가지 분할본을 번역한 데이터로 도메인 불변 보상 모델 학습용입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `used for training domain-invariant reward models` · 신뢰도 low
- **작업**: [[질의응답]] — metadata · task_categories = `question-answering` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:question_answering = `This dataset contains translations of three splits` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering = `This dataset contains translations of three splits` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `4 languages` · 신뢰도 high
- **언어**: [[th]] — metadata · languages = `th` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `426` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[법률]] — tag_match · tags = `legal` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `used for training domain-invariant reward models` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `prompt` 열 p90 1704자 ≈ 426 토큰 (viewer statistics, default/validation)
