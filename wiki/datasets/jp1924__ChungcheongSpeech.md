---
type: "dataset"
id: "jp1924/ChungcheongSpeech"
source: "huggingface"
url: "https://huggingface.co/datasets/jp1924/ChungcheongSpeech"
downloads: 45
summary: "충청도 방언 음성 데이터로 음성 인식 모델 학습에 사용됨"
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[음성 인식]]"
input_modality:
  - "[[음성 (입력 형식)|음성]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[이용 조건 미확인]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# jp1924/ChungcheongSpeech

> dataset · [Hugging Face](https://huggingface.co/datasets/jp1924/ChungcheongSpeech)

충청도 방언 음성 데이터로 음성 인식 모델 학습에 사용됨

## 분류

- **작업**: [[음성 인식]] — metadata · readme, task_categories = `automatic-speech-recognition` · 신뢰도 high
- **입력 형식**: [[음성 (입력 형식)|음성]] — ner · modality, readme, task:speech_recognition = `- name: audio
dtype:
audio:
sampling_rate: 16000` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:speech_recognition = `- name: sentence
dtype: string` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `- name: train
num_bytes: 49453451858.24
num_examples: 100545` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high
