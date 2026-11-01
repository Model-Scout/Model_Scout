---
type: "dataset"
id: "yahma/alpaca-cleaned"
source: "huggingface"
url: "https://huggingface.co/datasets/yahma/alpaca-cleaned"
downloads: 20629
summary: "Stanford Alpaca 데이터셋의 오류를 수정한 정제된 버전으로, 텍스트 생성에 활용됨."
readme_status: "template"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# yahma/alpaca-cleaned

> dataset · [Hugging Face](https://huggingface.co/datasets/yahma/alpaca-cleaned)

Stanford Alpaca 데이터셋의 오류를 수정한 정제된 버전으로, 텍스트 생성에 활용됨.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `Many instructions in the original dataset had instructions referencing data on the internet` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `Many instructions in the original dataset had instructions referencing data on the internet, which just caused GPT3 to hallucinate an answer.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `423` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `This is a cleaned version of the original Alpaca Dataset released by Stanford.` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `output` 열 p90 1693자 ≈ 423 토큰 (viewer statistics, default/train)

## 이 데이터로 학습한 모델

- [[martinsu__tildeopen-30b-mu-instruct|martinsu/tildeopen-30b-mu-instruct]]
