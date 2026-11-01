---
type: "dataset"
id: "OLAIR/numina_math_ko_verifiable_540k"
source: "huggingface"
url: "https://huggingface.co/datasets/OLAIR/numina_math_ko_verifiable_540k"
downloads: 39
summary: "수학 문제와 검증 가능한 답변의 쌍으로 구성된 RL 학습용 한국어 번역 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[교육]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# OLAIR/numina_math_ko_verifiable_540k

> dataset · [Hugging Face](https://huggingface.co/datasets/OLAIR/numina_math_ko_verifiable_540k)

수학 문제와 검증 가능한 답변의 쌍으로 구성된 RL 학습용 한국어 번역 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `Intended for RL training (e.g., GRPO) and mathematical reasoning tasks.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `A paired dataset of math questions (translated into Korean using GPT-4o-mini) and verifiable answers.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `A paired dataset of math questions (translated into Korean using GPT-4o-mini) and verifiable answers.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `1396` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[교육]] — ner · readme = `A paired dataset of math questions (translated into Korean using GPT-4o-mini) and verifiable answers.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Suitable for RL and language model training in math-related tasks.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `reference` 열 p90 2094자 ≈ 1396 토큰 (viewer statistics, default/train)
