---
type: "dataset"
id: "loopin51/relay-ko-s2-shar"
source: "huggingface"
url: "https://huggingface.co/datasets/loopin51/relay-ko-s2-shar"
downloads: 17
summary: "RelayS2S 한국어 재현 연구용 합성 대화 음성 특징 데이터셋입니다."
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
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
---
# loopin51/relay-ko-s2-shar

> dataset · [Hugging Face](https://huggingface.co/datasets/loopin51/relay-ko-s2-shar)

RelayS2S 한국어 재현 연구용 합성 대화 음성 특징 데이터셋입니다.

## 분류

- **작업**: [[음성 인식]] — ner · readme = `RelayS2S(arXiv:2603.23346)의 한국어 재현 연구에 쓰는 lhotse shar 입니다.` · 신뢰도 low
- **입력 형식**: [[음성 (입력 형식)|음성]] — ner · readme, task:speech_recognition = `80차원 fbank 특징과 대본, 전이중 타이밍 주석만 있습니다.` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:speech_recognition = `80차원 fbank 특징과 대본, 전이중 타이밍 주석만 있습니다.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `RelayS2S(arXiv:2603.23346)의 한국어 재현 연구에 쓰는 lhotse shar 입니다.` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `shar/valid · shar/valid_glm 평가용 (각 51 대화)` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `연구용으로 공개하며 품질을 보증하지 않습니다.` · 신뢰도 low
