---
type: "dataset"
id: "CaveduckAI/steer-personality-rudeness-ko"
source: "huggingface"
url: "https://huggingface.co/datasets/CaveduckAI/steer-personality-rudeness-ko"
downloads: 40
summary: "매우 무례한 성격 특성을 추출하기 위한 1000개 샘플의 한국어 대화 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[임베딩]]"
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# CaveduckAI/steer-personality-rudeness-ko

> dataset · [Hugging Face](https://huggingface.co/datasets/CaveduckAI/steer-personality-rudeness-ko)

매우 무례한 성격 특성을 추출하기 위한 1000개 샘플의 한국어 대화 데이터셋입니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `This dataset contains 1000 samples designed for extracting personality steering vectors using the Contrastive Activation Addition (CAA) method.` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:embedding, task:generation = `Each sample presents a scenario with two response options: one exhibiting the target personality trait and one neutral.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `Each sample presents a scenario with two response options: one exhibiting the target personality trait and one neutral.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `124` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Each sample presents a scenario with two response options: one exhibiting the target personality trait and one neutral.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `This dataset contains 1000 samples designed for extracting personality steering vectors using the Contrastive Activation Addition (CAA) method.` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `situation` 열 p90 185자 ≈ 124 토큰 (viewer statistics, default/train)
