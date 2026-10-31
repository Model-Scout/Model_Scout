---
type: "dataset"
id: "kresnik/zeroth_korean"
source: "huggingface"
url: "https://huggingface.co/datasets/kresnik/zeroth_korean"
downloads: 2775
summary: "한국어 음성 인식 연구를 위한 공개 음성 데이터셋으로, 약 51.6시간 훈련 데이터 포함."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[음성 인식]]"
input_modality:
  - "[[음성 (입력 형식)|음성]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# kresnik/zeroth_korean

> dataset · [Hugging Face](https://huggingface.co/datasets/kresnik/zeroth_korean)

한국어 음성 인식 연구를 위한 공개 음성 데이터셋으로, 약 51.6시간 훈련 데이터 포함.

## 분류

- **작업**: [[음성 인식]] — ner · readme = `한국어 음성 인식 연구와 개발을 위해 제작된 공개 음성 데이터셋입니다.` · 신뢰도 medium
- **입력 형식**: [[음성 (입력 형식)|음성]] — ner · modality, readme, task:speech_recognition = `오디오 데이터 (`datasets.Audio` 타입으로 관리, 샘플링 레이트 16kHz)` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:speech_recognition = `발화된 문장 (string)` · 신뢰도 medium
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `21` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `The Zeroth-Korean dataset is a publicly available speech dataset created for Korean automatic speech recognition (ASR) research and development.` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `1.2시간의 발화 데이터로, 총 457개의 발화로 구성되어 있으며, 모델 성능 검증에 사용됩니다.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `51.6시간의 한국어 발화 데이터로 구성되며, 발화 수는 총 22,263개입니다. 이 데이터는 음성 인식 모델의 훈련에 사용됩니다.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 85자 ≈ 21 토큰 (viewer statistics, default/test)

## 이 데이터로 학습한 모델

- [[Kkonjeong__wav2vec2-base-korean|Kkonjeong/wav2vec2-base-korean]]
- [[kresnik__wav2vec2-large-xlsr-korean|kresnik/wav2vec2-large-xlsr-korean]]
- [[seastar105__whisper-medium-ko-zeroth|seastar105/whisper-medium-ko-zeroth]]
- [[w11wo__wav2vec2-xls-r-300m-korean|w11wo/wav2vec2-xls-r-300m-korean]]
