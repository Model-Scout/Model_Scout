---
type: "dataset"
id: "heegyu/orca-math-korean-preference-cleaned"
source: "huggingface"
url: "https://huggingface.co/datasets/heegyu/orca-math-korean-preference-cleaned"
downloads: 66
summary: "수학 문제와 답변 데이터에서 수식 띄어쓰기 제거 및 중복 숫자 제거한 한국어 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 분류]]"
  - "[[질의응답]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[교육]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# heegyu/orca-math-korean-preference-cleaned

> dataset · [Hugging Face](https://huggingface.co/datasets/heegyu/orca-math-korean-preference-cleaned)

수학 문제와 답변 데이터에서 수식 띄어쓰기 제거 및 중복 숫자 제거한 한국어 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `question, chosen 칼럼에 대해서 다음과 같은 필터링 수행` · 신뢰도 low
- **작업**: [[질의응답]] — ner · readme = `question, chosen 칼럼에 대해서 다음과 같은 필터링 수행` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:question_answering = `question, chosen 칼럼에 대해서 다음과 같은 필터링 수행` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `question, chosen 칼럼에 대해서 다음과 같은 필터링 수행` · 신뢰도 medium
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `366` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[교육]] — ner · readme = `수학문제 특정상 수식을 작성하는 과정에서 반복되는 n-gram이 많아서` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `원본 데이터: kuotient/orca-math-korean-preference` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `answer_en` 열 p90 1464자 ≈ 366 토큰 (viewer statistics, default/train)

## 이 데이터로 학습한 모델

- [[pathcosmos__frankenstallm|pathcosmos/frankenstallm]]
