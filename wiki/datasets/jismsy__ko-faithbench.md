---
type: "dataset"
id: "jismsy/ko-faithbench"
source: "huggingface"
url: "https://huggingface.co/datasets/jismsy/ko-faithbench"
downloads: 31
summary: "한국어 위키피디아 문단과 생성 답변의 충실성 판별을 위한 벤치마크 데이터셋입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# jismsy/ko-faithbench

> dataset · [Hugging Face](https://huggingface.co/datasets/jismsy/ko-faithbench)

한국어 위키피디아 문단과 생성 답변의 충실성 판별을 위한 벤치마크 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories = `text-classification` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:classification = `given a Wikipedia passage and a generated answer` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `judge whether the answer is fully supported by the passage (SUPPORTED) or contains exactly one subtle factual error (HALLUCINATED)` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `given a Wikipedia passage and a generated answer` · 신뢰도 medium
- **데이터 용도**: [[평가용]] — ner · dataset_id/tags, readme = `봉인셋 평가는 운영자가 대행하고 결과만 게시합니다 — 벤치 과적합·오염 검출이 목적입니다.` · 신뢰도 medium
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high
