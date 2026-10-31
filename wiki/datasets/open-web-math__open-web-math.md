---
type: "dataset"
id: "open-web-math/open-web-math"
source: "huggingface"
url: "https://huggingface.co/datasets/open-web-math/open-web-math"
downloads: 32895
summary: "OpenWebMath는 인터넷에서 수집한 고품질 수학 텍스트 데이터셋으로, 대형 언어 모델 사전학습 및 미세조정에 사용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[언어 모델링]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
input_length:
  - "[[초장문]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[학술·논문]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# open-web-math/open-web-math

> dataset · [Hugging Face](https://huggingface.co/datasets/open-web-math/open-web-math)

OpenWebMath는 인터넷에서 수집한 고품질 수학 텍스트 데이터셋으로, 대형 언어 모델 사전학습 및 미세조정에 사용됨.

## 분류

- **작업**: [[언어 모델링]] — ner · readme = `OpenWebMath is intended for use in pretraining and finetuning large language models.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:language_modeling = `OpenWebMath is a dataset containing the majority of the high-quality, mathematical text from the internet.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:language_modeling = `OpenWebMath is intended for use in pretraining and finetuning large language models.` · 신뢰도 medium
- **입력 길이**: [[초장문]] — viewer_stats · viewer_statistics = `23093` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[학술·논문]] — ner · readme = `The dataset contains documents covering mathematics, physics, statistics, computer science, and more.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `OpenWebMath is intended for use in pretraining and finetuning large language models.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 92374자 ≈ 23093 토큰 (viewer statistics, default/train)

## 이 데이터로 학습한 모델

- [[FINAL-Bench__Aether-7B-5Attn|FINAL-Bench/Aether-7B-5Attn]]
- [[FINAL-Bench__Aether-7B-5Attn-it|FINAL-Bench/Aether-7B-5Attn-it]]
