---
type: "dataset"
id: "nvidia/HelpSteer2"
source: "huggingface"
url: "https://huggingface.co/datasets/nvidia/HelpSteer2"
downloads: 29395
summary: "HelpSteer2는 모델을 더 유용하고 정확하며 일관되게 조정하기 위한 오픈소스 보상 모델 학습 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 생성]]"
  - "[[리랭킹]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# nvidia/HelpSteer2

> dataset · [Hugging Face](https://huggingface.co/datasets/nvidia/HelpSteer2)

HelpSteer2는 모델을 더 유용하고 정확하며 일관되게 조정하기 위한 오픈소스 보상 모델 학습 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `When used to tune a Llama 3.1 70B Instruct Model, we achieve 94.1% on RewardBench, which makes it the best Reward…` · 신뢰도 low
- **작업**: [[리랭킹]] — ner · readme = `HelpSteer2 is an open-source Helpfulness Dataset (CC-BY-4.0) that supports aligning models to become more helpful, factually correct and coherent` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:reranking = `HelpSteer contains 21, 362 samples, each containing a prompt, a response as well as five human-annotated attributes of the response` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `HelpSteer contains 21, 362 samples, each containing a prompt, a response as well as five human-annotated attributes of the response` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `739` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `HelpSteer2 is an open-source Helpfulness Dataset (CC-BY-4.0) that supports aligning models to become more helpful, factually correct and coherent` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `HelpSteer2 is an open-source Helpfulness Dataset (CC-BY-4.0) that supports aligning models to become more helpful, factually correct and coherent` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `response` 열 p90 2955자 ≈ 739 토큰 (viewer statistics, default/validation)

## 이 데이터로 학습한 모델

- [[blackmallangcow__nari-decision-4b|blackmallangcow/nari-decision-4b]]
