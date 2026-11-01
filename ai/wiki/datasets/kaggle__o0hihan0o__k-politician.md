---
type: "dataset"
id: "kaggle/o0hihan0o/k-politician"
source: "kaggle"
url: "https://www.kaggle.com/datasets/o0hihan0o/k-politician"
downloads: 69
summary: "한국 정치인 얼굴 이미지 데이터셋으로, 얼굴 인상이 투표 행동에 미치는 영향 연구용입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[이미지 인식]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/o0hihan0o/k-politician

> dataset · [Kaggle](https://www.kaggle.com/datasets/o0hihan0o/k-politician)

한국 정치인 얼굴 이미지 데이터셋으로, 얼굴 인상이 투표 행동에 미치는 영향 연구용입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `image classification` · 신뢰도 medium
- **작업**: [[이미지 인식]] — tag_match · tags = `image classification` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · readme, task:vision = `image label [45,850]` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:classification = `text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `annotated with evaluations for facial impressions (competence, dominance, trustworthiness, sex-typicality) via surveys` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[비상업 전용]] — metadata · license = `Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Korean Politician Facial Image Dataset` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `PoliticGAN is a dataset of K-Politicians built with electoral poster images, annotated with evaluations for facial impressions` · 신뢰도 low
