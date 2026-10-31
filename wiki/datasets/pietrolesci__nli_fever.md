---
type: "dataset"
id: "pietrolesci/nli_fever"
source: "huggingface"
url: "https://huggingface.co/datasets/pietrolesci/nli_fever"
downloads: 8490
summary: "FEVER 데이터셋을 변형해 주장과 증거 문장 쌍에 라벨을 부여한 NLI 연구용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
input_length:
  - "[[단문]]"
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
  - "[[중규모 데이터]]"
---
# pietrolesci/nli_fever

> dataset · [Hugging Face](https://huggingface.co/datasets/pietrolesci/nli_fever)

FEVER 데이터셋을 변형해 주장과 증거 문장 쌍에 라벨을 부여한 NLI 연구용 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `the expected output is a label` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `pair the claims in the FEVER dataset with the textual evidence` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `expected output is a label` · 신뢰도 low
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `155` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `claim from Wikipedia` · 신뢰도 medium
- **데이터 용도**: [[평가용]] — ner · readme = `no label is available for the "test" split` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `3 instances in common between `dev` and `train` splits` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `hypothesis` 열 p90 622자 ≈ 155 토큰 (viewer statistics, default/test)

## 이 데이터로 학습한 모델

- [[BalaRajesh1__mmbert-small-nli|BalaRajesh1/mmbert-small-nli]]
