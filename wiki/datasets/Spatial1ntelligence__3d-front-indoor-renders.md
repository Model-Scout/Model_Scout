---
type: "dataset"
id: "Spatial1ntelligence/3d-front-indoor-renders"
source: "huggingface"
url: "https://huggingface.co/datasets/Spatial1ntelligence/3d-front-indoor-renders"
downloads: 1553
summary: "3D-FRONT과 3D-FUTURE 기반 20,240개 실내 장면 렌더링 데이터셋으로 인스턴스 분할, 6DoF 객체 위치 포함"
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[임베딩]]"
  - "[[정보 추출]]"
  - "[[이미지 인식]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[이미지 (출력 형식)|이미지]]"
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# Spatial1ntelligence/3d-front-indoor-renders

> dataset · [Hugging Face](https://huggingface.co/datasets/Spatial1ntelligence/3d-front-indoor-renders)

3D-FRONT과 3D-FUTURE 기반 20,240개 실내 장면 렌더링 데이터셋으로 인스턴스 분할, 6DoF 객체 위치 포함

## 분류

- **작업**: [[임베딩]] — ner · readme = `instance segmentation, 6DoF object poses, camera intrinsics and depth` · 신뢰도 low
- **작업**: [[정보 추출]] — ner · readme = `instance segmentation, 6DoF object poses, camera intrinsics and depth` · 신뢰도 low
- **작업**: [[이미지 인식]] — metadata · readme, task_categories = `image-segmentation` · 신뢰도 medium
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · readme, task:vision = `20,240 photo-realistic indoor scene renders` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:embedding, task:information_extraction = `camera intrinsics and depth — rendered from the 3D-FRONT scene layouts and 3D-FUTURE furniture models.` · 신뢰도 medium
- **출력 형식**: [[이미지 (출력 형식)|이미지]] — ner · readme = `20,240 photo-realistic indoor scene renders` · 신뢰도 low
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `instance segmentation, 6DoF object poses, camera intrinsics and depth` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Indoor Scene Renders from 3D-FRONT / 3D-FUTURE` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `This repository provides a render set of the same size, produced with a documented and reproducible pipeline.` · 신뢰도 low
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
