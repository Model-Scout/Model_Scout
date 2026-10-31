---
type: "dataset"
id: "Skywork/Skywork-OR1-RL-Data"
source: "huggingface"
url: "https://huggingface.co/datasets/Skywork/Skywork-OR1-RL-Data"
downloads: 1676
summary: "수학과 코딩 문제로 구성된 RL 학습용 데이터셋으로 Skywork-OR1 모델 학습에 사용됨"
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 분류]]"
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
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
# Skywork/Skywork-OR1-RL-Data

> dataset · [Hugging Face](https://huggingface.co/datasets/Skywork/Skywork-OR1-RL-Data)

수학과 코딩 문제로 구성된 RL 학습용 데이터셋으로 Skywork-OR1 모델 학습에 사용됨

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `We conduct **model-aware difficulty estimation** for each problem and model and conduct **rigorous quality assessment prior to training** via both human and LLM` · 신뢰도 low
- **작업**: [[텍스트 생성]] — ner · readme = `This dataset is used to train the **`Skywork-OR1`** (Open Reasoner 1) model series, which consists of powerful math and code reasoning models trained using larg` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:generation = `a dataset of verifiable, challenging, and diverse math problems (105K) and coding questions (14K)` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `This dataset is used to train the **`Skywork-OR1`** (Open Reasoner 1) model series, which consists of powerful math and code reasoning models trained using larg` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[교육]] — ner · readme = `a dataset of verifiable, challenging, and diverse math problems (105K) and coding questions (14K)` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `We are excited to release our RL training dataset Skywork-OR1-RL-Data` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

## 이 데이터로 학습한 모델

- [[ATH-MaaS__Marco-Mini-Instruct|ATH-MaaS/Marco-Mini-Instruct]]
- [[ATH-MaaS__Marco-Nano-Instruct|ATH-MaaS/Marco-Nano-Instruct]]
- [[Abu-Dju__Marco-Mini-Instruct|Abu-Dju/Marco-Mini-Instruct]]
