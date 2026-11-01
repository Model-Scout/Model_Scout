---
type: "dataset"
id: "ENSEONG/ko-math-500-test"
source: "huggingface"
url: "https://huggingface.co/datasets/ENSEONG/ko-math-500-test"
downloads: 21
summary: "한국어 수학 문제 해결을 위한 ko-math-500 데이터셋의 테스트 분할 데이터입니다."
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
  - "[[중문]]"
commercial_use:
  - "[[이용 조건 미확인]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# ENSEONG/ko-math-500-test

> dataset · [Hugging Face](https://huggingface.co/datasets/ENSEONG/ko-math-500-test)

한국어 수학 문제 해결을 위한 ko-math-500 데이터셋의 테스트 분할 데이터입니다.

## 분류

- **작업**: [[질의응답]] — metadata · readme, task_categories = `question-answering` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:question_answering = `Language: Korean` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `Task: Math problem solving` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `628` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license = `unknown` · 신뢰도 high
- **데이터 용도**: [[평가용]] — ner · readme = `The original 'train' split has been changed to 'test' split` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `optimized-parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

샘플 길이: `solution` 열 p90 942자 ≈ 628 토큰 (viewer statistics, default/test)
