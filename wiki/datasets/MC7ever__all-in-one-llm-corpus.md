---
type: "dataset"
id: "MC7ever/all-in-one-llm-corpus"
source: "huggingface"
url: "https://huggingface.co/datasets/MC7ever/all-in-one-llm-corpus"
downloads: 372
summary: "대화형 언어 모델 학습을 위한 SFT, DPO, RL, 페르소나 스타일 데이터 포함 코퍼스입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
  - "[[임베딩]]"
  - "[[텍스트 생성]]"
  - "[[질의응답]]"
  - "[[리랭킹]]"
  - "[[요약]]"
  - "[[번역]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[cs]]"
  - "[[de]]"
  - "[[영어]]"
  - "[[일본어]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[ru]]"
  - "[[sk]]"
  - "[[uk]]"
  - "[[중국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# MC7ever/all-in-one-llm-corpus

> dataset · [Hugging Face](https://huggingface.co/datasets/MC7ever/all-in-one-llm-corpus)

대화형 언어 모델 학습을 위한 SFT, DPO, RL, 페르소나 스타일 데이터 포함 코퍼스입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories = `text-classification` · 신뢰도 medium
- **작업**: [[임베딩]] — ner · readme = `model-agnostic chat format (LFM2.5, Qwen, Llama, Gemma, Mistral, …)` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · readme, tags, task_categories = `text-generation` · 신뢰도 high
- **작업**: [[질의응답]] — metadata · task_categories = `multiple-choice` · 신뢰도 low
- **작업**: [[리랭킹]] — metadata · readme, task_categories = `text-ranking` · 신뢰도 medium
- **작업**: [[요약]] — metadata · task_categories = `summarization` · 신뢰도 low
- **작업**: [[번역]] — metadata · task_categories = `translation` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:embedding, task:generation, task:question_answering, task:reranking, task:summarization, task:translation = `One repo. Four training stages. Everything a chat model needs` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering, task:summarization, task:translation = `target text is screened against a combined bot/corporo phrase list` · 신뢰도 medium
- **언어**: [[cs]] — metadata · languages = `cs` · 신뢰도 high
- **언어**: [[de]] — metadata · languages = `de` · 신뢰도 high
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `9 languages` · 신뢰도 high
- **언어**: [[ru]] — metadata · languages = `ru` · 신뢰도 high
- **언어**: [[sk]] — metadata · languages = `sk` · 신뢰도 high
- **언어**: [[uk]] — metadata · languages = `uk` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `779` · 신뢰도 medium
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `langdetect-tagged on every row of every subset/split; filter to any language in one line.` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · dataset_id/tags, readme = `benchmark, with clean splits for each step` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `train · validation · test · benchmark (all four in every subset)` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `optimized-parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high

샘플 길이: `prompt` 열 p90 3116자 ≈ 779 토큰 (viewer statistics, ct/validation)
