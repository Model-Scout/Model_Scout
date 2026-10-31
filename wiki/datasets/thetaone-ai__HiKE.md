---
type: "dataset"
id: "thetaone-ai/HiKE"
source: "huggingface"
url: "https://huggingface.co/datasets/thetaone-ai/HiKE"
downloads: 381
summary: "한국어-영어 코드스위칭 음성인식 평가를 위한 고품질 데이터셋과 평가 프레임워크입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[음성 인식]]"
input_modality:
  - "[[음성 (입력 형식)|음성]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# thetaone-ai/HiKE

> dataset · [Hugging Face](https://huggingface.co/datasets/thetaone-ai/HiKE)

한국어-영어 코드스위칭 음성인식 평가를 위한 고품질 데이터셋과 평가 프레임워크입니다.

## 분류

- **작업**: [[음성 인식]] — metadata · readme, task_categories = `automatic-speech-recognition` · 신뢰도 high
- **입력 형식**: [[음성 (입력 형식)|음성]] — ner · modality, readme, task:speech_recognition = `Korean-English Code-Switching (CS) Automatic Speech Recognition (ASR) benchmark` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:speech_recognition = `evaluate the models' CS ASR capability` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `105` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `HiKE is the first Korean-English Code-Switching (CS) Automatic Speech Recognition (ASR) benchmark composed of high-quality, natural CS data across various topic` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `HiKE is the first Korean-English Code-Switching (CS) Automatic Speech Recognition (ASR) benchmark` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `text_pier_labeled` 열 p90 157자 ≈ 105 토큰 (viewer statistics, default/test)
