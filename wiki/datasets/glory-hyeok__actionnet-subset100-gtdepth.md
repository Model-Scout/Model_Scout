---
type: "dataset"
id: "glory-hyeok/actionnet-subset100-gtdepth"
source: "huggingface"
url: "https://huggingface.co/datasets/glory-hyeok/actionnet-subset100-gtdepth"
downloads: 249
summary: "ActionNet 데이터셋의 100개 에피소드 서브셋으로, 원본 RGB와 무손실 깊이 정보를 포함하여 로봇 행동 인식 연구에 활용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
  - "[[영상 (입력 형식)|영상]]"
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
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[CSV]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# glory-hyeok/actionnet-subset100-gtdepth

> dataset · [Hugging Face](https://huggingface.co/datasets/glory-hyeok/actionnet-subset100-gtdepth)

ActionNet 데이터셋의 100개 에피소드 서브셋으로, 원본 RGB와 무손실 깊이 정보를 포함하여 로봇 행동 인식 연구에 활용됨.

## 분류

- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality = `text` · 신뢰도 high
- **입력 형식**: [[영상 (입력 형식)|영상]] — ner · readme = `rgb.mp4 (1280x800 fisheye)` · 신뢰도 low
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `the filter that decides whether a video is consistent with the action stream that goes with it` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `12` · 신뢰도 medium
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `This is a 100-episode subset redistribution of a third-party dataset, plus our derived artifacts.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `This is a 100-episode subset redistribution of a third-party dataset, plus our derived artifacts.` · 신뢰도 low
- **데이터 형식**: [[CSV]] — metadata · format = `csv` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

샘플 길이: `ulid` 열 p90 18자 ≈ 12 토큰 (viewer statistics, manifest/train)
