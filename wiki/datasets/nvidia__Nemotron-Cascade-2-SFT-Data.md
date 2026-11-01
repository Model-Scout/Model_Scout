---
type: "dataset"
id: "nvidia/Nemotron-Cascade-2-SFT-Data"
source: "huggingface"
url: "https://huggingface.co/datasets/nvidia/Nemotron-Cascade-2-SFT-Data"
downloads: 12478
summary: "Nemotron-Cascade-2 학습용 SFT 데이터로 수학, 과학, 대화, 소프트웨어 엔지니어링 등 다양한 분야 포함"
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[학술·논문]]"
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# nvidia/Nemotron-Cascade-2-SFT-Data

> dataset · [Hugging Face](https://huggingface.co/datasets/nvidia/Nemotron-Cascade-2-SFT-Data)

Nemotron-Cascade-2 학습용 SFT 데이터로 수학, 과학, 대화, 소프트웨어 엔지니어링 등 다양한 분야 포함

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `We release the SFT data used for training Nemotron-Cascade-2.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `We pack all SFT samples into sequences of up to 256K tokens` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `We pack all SFT samples into sequences of up to 256K tokens` · 신뢰도 medium
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[학술·논문]] — ner · readme = `Math` · 신뢰도 low
- **도메인**: [[일반]] — ner · readme = `General Chat` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `We release the SFT data used for training Nemotron-Cascade-2.` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `99999999.0` · 신뢰도 high

## 이 데이터로 학습한 모델

- [[ATH-MaaS__Marco-Mini-Instruct|ATH-MaaS/Marco-Mini-Instruct]]
- [[ATH-MaaS__Marco-Nano-Instruct|ATH-MaaS/Marco-Nano-Instruct]]
- [[Abu-Dju__Marco-Mini-Instruct|Abu-Dju/Marco-Mini-Instruct]]
