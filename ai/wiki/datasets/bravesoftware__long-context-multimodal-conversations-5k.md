---
type: "dataset"
id: "bravesoftware/long-context-multimodal-conversations-5k"
source: "huggingface"
url: "https://huggingface.co/datasets/bravesoftware/long-context-multimodal-conversations-5k"
downloads: 350
summary: "long-context-multimodal-conversations-5k는 긴 멀티턴 대화를 구조화된 요약으로 압축하는 합성 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 생성]]"
  - "[[언어 모델링]]"
  - "[[요약]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[극장문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# bravesoftware/long-context-multimodal-conversations-5k

> dataset · [Hugging Face](https://huggingface.co/datasets/bravesoftware/long-context-multimodal-conversations-5k)

long-context-multimodal-conversations-5k는 긴 멀티턴 대화를 구조화된 요약으로 압축하는 합성 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 high
- **작업**: [[언어 모델링]] — ner · readme = `Long-context modeling, compaction input, multimodal chat research` · 신뢰도 low
- **작업**: [[요약]] — metadata · task_categories = `summarization` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · readme = `text and optional `image_url` blocks` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:language_modeling, task:summarization = `Raw synthetic chat logs` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:language_modeling, task:summarization = `structured summary from a strong teacher` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `13 languages` · 신뢰도 high
- **입력 길이**: [[극장문]] — viewer_stats · viewer_statistics = `2349376` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Synthetic Conversation & Compaction Dataset` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `training models to compact long multi-turn chat histories into structured, LLM-facing summaries` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `prompt` 열 p90 9397504자 ≈ 2349376 토큰 (viewer statistics, default/validation)
