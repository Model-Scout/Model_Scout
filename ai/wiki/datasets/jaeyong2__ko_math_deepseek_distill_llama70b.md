---
type: "dataset"
id: "jaeyong2/ko_math_deepseek_distill_llama70b"
source: "huggingface"
url: "https://huggingface.co/datasets/jaeyong2/ko_math_deepseek_distill_llama70b"
downloads: 29
summary: "한국어 수학 문제 데이터셋으로, 딥러닝 모델 학습에 활용됨."
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
# jaeyong2/ko_math_deepseek_distill_llama70b

> dataset · [Hugging Face](https://huggingface.co/datasets/jaeyong2/ko_math_deepseek_distill_llama70b)

한국어 수학 문제 데이터셋으로, 딥러닝 모델 학습에 활용됨.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `question dataset from kuotient/orca-math-word-problems-193k-korean` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `question dataset from kuotient/orca-math-word-problems-193k-korean` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `question dataset from kuotient/orca-math-word-problems-193k-korean` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `2319` · 신뢰도 medium
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[교육]] — ner · readme = `question dataset from kuotient/orca-math-word-problems-193k-korean` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `question dataset from kuotient/orca-math-word-problems-193k-korean` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `answer` 열 p90 3478자 ≈ 2319 토큰 (viewer statistics, default/train)
