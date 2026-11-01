---
type: "dataset"
id: "jaeyong2/Qwen3-06B-Ko-DPO-2"
source: "huggingface"
url: "https://huggingface.co/datasets/jaeyong2/Qwen3-06B-Ko-DPO-2"
downloads: 21
summary: "한국어 수학 문제 질문 데이터셋으로 답변 후보 생성 및 평가에 사용됨"
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
  - "[[리랭킹]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[교육]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# jaeyong2/Qwen3-06B-Ko-DPO-2

> dataset · [Hugging Face](https://huggingface.co/datasets/jaeyong2/Qwen3-06B-Ko-DPO-2)

한국어 수학 문제 질문 데이터셋으로 답변 후보 생성 및 평가에 사용됨

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `We used Qwen/Qwen3-0.6B to generate the answer candidates (n=32).` · 신뢰도 low
- **작업**: [[리랭킹]] — ner · readme = `We used Qwen/Qwen3-14B to evaluate the appropriateness of those candidates.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:reranking = `question dataset from kuotient/orca-math-word-problems-193k-korean` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `We used Qwen/Qwen3-0.6B to generate the answer candidates (n=32).` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[교육]] — ner · readme = `question dataset from kuotient/orca-math-word-problems-193k-korean` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `question dataset from kuotient/orca-math-word-problems-193k-korean` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

## 같은 데이터의 사본·중복 등록

- `jaeyong2/Qwen3-06B-Ko-DPO`
- `jaeyong2/Qwen3-06B-Ko-DPO-3`
- `jaeyong2/Qwen3-06B-Ko-KTO`
