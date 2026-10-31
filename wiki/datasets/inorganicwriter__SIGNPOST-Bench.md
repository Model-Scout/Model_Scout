---
type: "dataset"
id: "inorganicwriter/SIGNPOST-Bench"
source: "huggingface"
url: "https://huggingface.co/datasets/inorganicwriter/SIGNPOST-Bench"
downloads: 117
summary: "SIGNPOST-Bench는 멀티모달 대형 언어 모델의 텍스트-비전 충돌 해결 평가용 벤치마크 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[리랭킹]]"
  - "[[이미지 이해]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
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
dataset_size:
  - "[[중규모 데이터]]"
---
# inorganicwriter/SIGNPOST-Bench

> dataset · [Hugging Face](https://huggingface.co/datasets/inorganicwriter/SIGNPOST-Bench)

SIGNPOST-Bench는 멀티모달 대형 언어 모델의 텍스트-비전 충돌 해결 평가용 벤치마크 데이터셋입니다.

## 분류

- **작업**: [[리랭킹]] — ner · readme = `Benchmarking Text--Vision Conflict Resolution in Multimodal Large Language Models` · 신뢰도 low
- **작업**: [[이미지 이해]] — metadata · task_categories = `image-to-text` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · readme, task:visual_qa = `image variants` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:reranking, task:visual_qa = `attack texts, ground-truth labels, taxonomy, and human annotations` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:visual_qa = `ground-truth labels, taxonomy, and human annotations` · 신뢰도 medium
- **언어**: [[de]] — metadata · languages = `de` · 신뢰도 high
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[es]] — metadata · languages = `es` · 신뢰도 high
- **언어**: [[fr]] — metadata · languages = `fr` · 신뢰도 high
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `7 languages` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `multimodal large language models` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · dataset_id/tags, readme = `SIGNPOST-Bench is a benchmark evaluation resource, not a training dataset` · 신뢰도 medium
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
