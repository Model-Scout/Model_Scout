---
type: "dataset"
id: "klue/klue"
source: "huggingface"
url: "https://huggingface.co/datasets/klue/klue"
downloads: 5518
summary: "KLUE는 한국어 자연어 이해 능력 평가를 위한 8개 작업 데이터셋 모음입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[임베딩]]"
  - "[[텍스트 생성]]"
  - "[[정보 추출]]"
  - "[[언어 모델링]]"
  - "[[질의응답]]"
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
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# klue/klue

> dataset · [Hugging Face](https://huggingface.co/datasets/klue/klue)

KLUE는 한국어 자연어 이해 능력 평가를 위한 8개 작업 데이터셋 모음입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories, task_ids = `text-classification` · 신뢰도 high
- **작업**: [[임베딩]] — metadata · readme, task_ids = `semantic-similarity-scoring` · 신뢰도 high
- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[정보 추출]] — metadata · readme, task_categories, task_ids = `token-classification` · 신뢰도 high
- **작업**: [[언어 모델링]] — metadata · task_categories = `fill-mask` · 신뢰도 low
- **작업**: [[질의응답]] — metadata · readme, task_categories, task_ids = `question-answering` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:embedding, task:generation, task:information_extraction, task:language_modeling, task:question_answering = `sentence` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:language_modeling, task:question_answering = `label` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `59` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `KLUE is a collection of 8 tasks to evaluate natural language understanding capability of Korean language models.` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `validation: 9,107` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `train: 45,678` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `sentence` 열 p90 89자 ≈ 59 토큰 (viewer statistics, dp/validation)

## 이 데이터로 학습한 모델

- [[Huffon__klue-roberta-base-nli|Huffon/klue-roberta-base-nli]]
- [[SECUFIBRE__klue-roberta-base-klue-sts|SECUFIBRE/klue-roberta-base-klue-sts]]
- [[bespin-global__klue-sentence-roberta-base|bespin-global/klue-sentence-roberta-base]]
- [[bespin-global__klue-sroberta-base-continue-learning-by-mnr|bespin-global/klue-sroberta-base-continue-learning-by-mnr]]
- [[blackmallangcow__nari-decision-4b|blackmallangcow/nari-decision-4b]]
- [[blueapple8259__TinyKo|blueapple8259/TinyKo]]
- [[jhgan__ko-sroberta-nli-mrl|jhgan/ko-sroberta-nli-mrl]]
- [[snumin44__simcse-ko-bert-supervised|snumin44/simcse-ko-bert-supervised]]
- [[snumin44__simcse-ko-roberta-supervised|snumin44/simcse-ko-roberta-supervised]]
- [[snumin44__simcse-ko-roberta-unsupervised|snumin44/simcse-ko-roberta-unsupervised]]
- [[snunlp__KR-SBERT-Medium-extended-klueNLItriplet_PARpair_QApair-klueSTS|snunlp/KR-SBERT-Medium-extended-klueNLItriplet_PARpair_QApair-klueSTS]]
- [[snunlp__KR-SBERT-Medium-klueNLI-klueSTS|snunlp/KR-SBERT-Medium-klueNLI-klueSTS]]
- [[sorryhyun__sentence-embedding-klue-large|sorryhyun/sentence-embedding-klue-large]]
