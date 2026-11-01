---
type: "dataset"
id: "princeton-nlp/SWE-bench_Verified"
source: "huggingface"
url: "https://huggingface.co/datasets/princeton-nlp/SWE-bench_Verified"
downloads: 167527
summary: "SWE-bench Verified는 GitHub 이슈 자동 해결 능력을 평가하는 데이터셋 SWE-bench의 인간 검증된 500개 샘플 하위집합입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[질의응답]]"
  - "[[문서 검색]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
input_length:
  - "[[장문]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# princeton-nlp/SWE-bench_Verified

> dataset · [Hugging Face](https://huggingface.co/datasets/princeton-nlp/SWE-bench_Verified)

SWE-bench Verified는 GitHub 이슈 자동 해결 능력을 평가하는 데이터셋 SWE-bench의 인간 검증된 500개 샘플 하위집합입니다.

## 분류

- **작업**: [[질의응답]] — ner · readme = `SWE-bench is a dataset that tests systems’ ability to solve GitHub issues automatically.` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `SWE-bench proposes a new task: issue resolution provided a full repository and GitHub issue.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:question_answering, task:retrieval = `This dataset only contains the problem_statement (i.e. issue text) and the base_commit which represents the state of the codebase before the issue has been reso` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `Evaluation is performed by unit test verification using post-PR behavior as the reference solution.` · 신뢰도 medium
- **입력 길이**: [[장문]] — viewer_stats · viewer_statistics = `6523` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `The text of the dataset is primarily English, but we make no effort to filter or otherwise clean based on language type.` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · dataset_id/tags, readme = `SWE-bench Verified is a subset of 500 samples from the SWE-bench test set, which have been human-validated for quality.` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — metadata · referenced_by_models = `train` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

샘플 길이: `PASS_TO_PASS` 열 p90 26093자 ≈ 6523 토큰 (viewer statistics, default/test)

## 이 데이터로 학습한 모델

- [[mradermacher__next-70b-GGUF|mradermacher/next-70b-GGUF]]
- [[mradermacher__next-70b-i1-GGUF|mradermacher/next-70b-i1-GGUF]]
- [[thelamapi__next-70b-GGUF|thelamapi/next-70b-GGUF]]
- [[thelamapi__next-70b-i1-GGUF|thelamapi/next-70b-i1-GGUF]]
