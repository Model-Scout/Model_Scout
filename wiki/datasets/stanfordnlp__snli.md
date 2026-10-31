---
type: "dataset"
id: "stanfordnlp/snli"
source: "huggingface"
url: "https://huggingface.co/datasets/stanfordnlp/snli"
downloads: 48183
summary: "SNLI는 영어 문장 쌍에 대해 자연어 추론(NLI) 태스크를 위한 라벨링된 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 분류]]"
  - "[[질의응답]]"
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
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# stanfordnlp/snli

> dataset · [Hugging Face](https://huggingface.co/datasets/stanfordnlp/snli)

SNLI는 영어 문장 쌍에 대해 자연어 추론(NLI) 태스크를 위한 라벨링된 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories, task_ids = `text-classification` · 신뢰도 high
- **작업**: [[질의응답]] — ner · readme = `Natural Language Inference (NLI), also known as Recognizing Textual Entailment (RTE), is the task of determining the inference relation between two (short, orde` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:question_answering = `For each instance, there is a string for the premise, a string for the hypothesis` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `an integer for the label` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `30` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `The language in the dataset is English as spoken by users of the website Flickr and as spoken by crowdworkers from Amazon Mechanical Turk.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — metadata · referenced_by_models = `train` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `premise` 열 p90 119자 ≈ 30 토큰 (viewer statistics, plain_text/validation)

## 이 데이터로 학습한 모델

- [[BalaRajesh1__mmbert-small-nli|BalaRajesh1/mmbert-small-nli]]
