---
type: "dataset"
id: "drlee1/KoDistill-VL-research-artifacts"
source: "huggingface"
url: "https://huggingface.co/datasets/drlee1/KoDistill-VL-research-artifacts"
downloads: 397
summary: "KoDistill-VL 연구용 코드와 학생 모델 예측 기록을 비상업적 연구 목적으로 제공하는 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
  - "[[임베딩]]"
  - "[[텍스트 생성]]"
  - "[[리랭킹]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[학술·논문]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# drlee1/KoDistill-VL-research-artifacts

> dataset · [Hugging Face](https://huggingface.co/datasets/drlee1/KoDistill-VL-research-artifacts)

KoDistill-VL 연구용 코드와 학생 모델 예측 기록을 비상업적 연구 목적으로 제공하는 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `Auxiliary choice-ranking diagnostic` · 신뢰도 low
- **작업**: [[임베딩]] — ner · readme = `student-model prediction records` · 신뢰도 low
- **작업**: [[텍스트 생성]] — ner · readme = `Model-generated raw outputs are predictions` · 신뢰도 low
- **작업**: [[리랭킹]] — ner · readme = `Auxiliary choice-ranking diagnostic` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:embedding, task:generation, task:reranking = `original research code, configurations, dependency lock, scientific source manifests, and unmodified student-model prediction records` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `Model-generated raw outputs are predictions` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `43` · 신뢰도 medium
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[학술·논문]] — ner · readme = `This repository publishes original research code, configurations, dependency lock, scientific source manifests` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `Training images/targets, teacher answers, benchmark questions/images/gold, authentication, workstation manifests, environments, vendor packages and checkpoints ` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `image_sha256` 열 p90 64자 ≈ 43 토큰 (viewer statistics, default/validation)
