---
type: "dataset"
id: "jaeyong2/ko_math_qwq"
source: "huggingface"
url: "https://huggingface.co/datasets/jaeyong2/ko_math_qwq"
downloads: 21
summary: "한국어 수학 문제 데이터셋으로 수학 문제 해결에 활용됨"
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[질의응답]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[장문]]"
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
# jaeyong2/ko_math_qwq

> dataset · [Hugging Face](https://huggingface.co/datasets/jaeyong2/ko_math_qwq)

한국어 수학 문제 데이터셋으로 수학 문제 해결에 활용됨

## 분류

- **작업**: [[질의응답]] — ner · readme = `question dataset from kuotient/orca-math-word-problems-193k-korean` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:question_answering = `question dataset from kuotient/orca-math-word-problems-193k-korean` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `question dataset from kuotient/orca-math-word-problems-193k-korean` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[장문]] — viewer_stats · viewer_statistics = `13279` · 신뢰도 medium
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[교육]] — ner · readme = `question dataset from kuotient/orca-math-word-problems-193k-korean` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `question dataset from kuotient/orca-math-word-problems-193k-korean` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `answer` 열 p90 19919자 ≈ 13279 토큰 (viewer statistics, default/train)
