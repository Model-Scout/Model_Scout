---
type: "dataset"
id: "neuralfoundry-coder/finance-instructions-ko-sample"
source: "huggingface"
url: "https://huggingface.co/datasets/neuralfoundry-coder/finance-instructions-ko-sample"
downloads: 48
summary: "한국어 금융 분야 지시학습용 샘플 데이터셋으로 데이터 구조 확인 및 테스트용입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 생성]]"
  - "[[질의응답]]"
  - "[[번역]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[id]]"
  - "[[일본어]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[vi]]"
  - "[[중국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[금융·경제]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# neuralfoundry-coder/finance-instructions-ko-sample

> dataset · [Hugging Face](https://huggingface.co/datasets/neuralfoundry-coder/finance-instructions-ko-sample)

한국어 금융 분야 지시학습용 샘플 데이터셋으로 데이터 구조 확인 및 테스트용입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **작업**: [[질의응답]] — metadata · tags, task_categories = `question-answering` · 신뢰도 low
- **작업**: [[번역]] — metadata · tags, task_categories = `translation` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:generation, task:question_answering, task:translation = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation, task:question_answering, task:translation = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[id]] — metadata · languages = `id` · 신뢰도 high
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `6 languages` · 신뢰도 high
- **언어**: [[vi]] — metadata · languages = `vi` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `638` · 신뢰도 medium
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[금융·경제]] — tag_match · readme, tags = `finance` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `input` 열 p90 2553자 ≈ 638 토큰 (viewer statistics, default/test)
