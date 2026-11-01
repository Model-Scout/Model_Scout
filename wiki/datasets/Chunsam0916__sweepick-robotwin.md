---
type: "dataset"
id: "Chunsam0916/sweepick-robotwin"
source: "huggingface"
url: "https://huggingface.co/datasets/Chunsam0916/sweepick-robotwin"
downloads: 214
summary: "SWEEPICK RoboTwin 시뮬레이션 로봇 동작 영상 및 센서 데이터셋으로 로봇 제어 학습용입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
  - "[[임베딩]]"
  - "[[리랭킹]]"
  - "[[문서 검색]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
  - "[[영상 (입력 형식)|영상]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
  - "[[영상 (출력 형식)|영상]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[일반]]"
  - "[[교통·모빌리티]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# Chunsam0916/sweepick-robotwin

> dataset · [Hugging Face](https://huggingface.co/datasets/Chunsam0916/sweepick-robotwin)

SWEEPICK RoboTwin 시뮬레이션 로봇 동작 영상 및 센서 데이터셋으로 로봇 제어 학습용입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `Expert annotations, for analysis/labels; not policy observations` · 신뢰도 low
- **작업**: [[임베딩]] — ner · readme = `Simulation uses raytraced wrist RGB. Head is depth/IR only: depth and derived PointCloud` · 신뢰도 low
- **작업**: [[리랭킹]] — ner · readme = `Variants rerender at the same physics tick; head depth/PointCloud geometry is reused` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `These are demonstrations used for training/evaluation splits` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · readme = `Simulation uses raytraced wrist RGB. Head is depth/IR only: depth and derived PointCloud` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:embedding, task:reranking, task:retrieval = `Files are custom episodic HDF5; load with h5py` · 신뢰도 high
- **입력 형식**: [[영상 (입력 형식)|영상]] — ner · modality, readme = `Each MP4 shows head depth (fixed0–1.5m color scale), left wrist RGB and right wrist RGB` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `Expert annotations, for analysis/labels; not policy observations` · 신뢰도 low
- **출력 형식**: [[영상 (출력 형식)|영상]] — ner · readme = `Each MP4 shows head depth (fixed0–1.5m color scale), left wrist RGB and right wrist RGB` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Simulation uses raytraced wrist RGB. Head is depth/IR only` · 신뢰도 low
- **도메인**: [[교통·모빌리티]] — ner · readme = `SWEEPICK dual SO101 P-gripper on TurtleBot; 40x40x40mm cube, fixed yaw` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `Val/Test must not be used for gradient updates; reserve Test for independent final evaluation` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `These are demonstrations used for training/evaluation splits` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high
