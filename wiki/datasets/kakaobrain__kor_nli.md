---
type: "dataset"
id: "kakaobrain/kor_nli"
source: "huggingface"
url: "https://huggingface.co/datasets/kakaobrain/kor_nli"
downloads: 604
summary: "한국어 자연어 추론(NLI) 데이터셋으로 자연어 추론 모델 학습에 사용됨."
readme_status: "template"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# kakaobrain/kor_nli

> dataset · [Hugging Face](https://huggingface.co/datasets/kakaobrain/kor_nli)

한국어 자연어 추론(NLI) 데이터셋으로 자연어 추론 모델 학습에 사용됨.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories, task_ids = `text-classification` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `Korean Natural Language Inference datasets.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `Korean Natural Language Inference datasets.` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `81` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-4.0` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `An example of 'train' looks as follows.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `premise` 열 p90 121자 ≈ 81 토큰 (viewer statistics, multi_nli/train)

## 이 데이터로 학습한 모델

- [[blackmallangcow__nari-decision-4b|blackmallangcow/nari-decision-4b]]
- [[jhgan__ko-sroberta-nli-mrl|jhgan/ko-sroberta-nli-mrl]]
- [[snumin44__simcse-ko-bert-supervised|snumin44/simcse-ko-bert-supervised]]
- [[snumin44__simcse-ko-roberta-supervised|snumin44/simcse-ko-roberta-supervised]]
- [[snumin44__simcse-ko-roberta-unsupervised|snumin44/simcse-ko-roberta-unsupervised]]
