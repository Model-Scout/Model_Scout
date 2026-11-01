---
type: "dataset"
id: "hyeonmin1/kbo-listen"
source: "huggingface"
url: "https://huggingface.co/datasets/hyeonmin1/kbo-listen"
downloads: 83
summary: "야구 중계 음성을 듣고 질의 시각마다 볼카운트(B-S-O)를 맞히는 음성인식 챌린지 데이터셋입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[음성 인식]]"
input_modality:
  - "[[음성 (입력 형식)|음성]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[미디어 파일]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# hyeonmin1/kbo-listen

> dataset · [Hugging Face](https://huggingface.co/datasets/hyeonmin1/kbo-listen)

야구 중계 음성을 듣고 질의 시각마다 볼카운트(B-S-O)를 맞히는 음성인식 챌린지 데이터셋입니다.

## 분류

- **작업**: [[음성 인식]] — metadata · readme, task_categories = `automatic-speech-recognition` · 신뢰도 medium
- **입력 형식**: [[음성 (입력 형식)|음성]] — ner · modality, readme, task:speech_recognition = `야구 중계 음성을 듣고, 질의 시각마다 볼-스트라이크-아웃(B-S-O)을 맞히는 음성인식 챌린지 데이터셋입니다.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:speech_recognition = `야구 중계 음성을 듣고, 질의 시각마다 볼-스트라이크-아웃(B-S-O)을 맞히는 음성인식 챌린지 데이터셋입니다.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `야구 중계 음성을 듣고, 질의 시각마다 볼-스트라이크-아웃(B-S-O)을 맞히는 음성인식 챌린지 데이터셋입니다.` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `dev
100 (50 / 50)
audio, queries, gt, meta` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `train
1,000 (500 / 500)
audio, queries, gt, scripts, meta` · 신뢰도 medium
- **데이터 형식**: [[미디어 파일]] — metadata · format = `audiofolder` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high
