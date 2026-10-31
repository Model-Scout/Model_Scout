---
type: "dataset"
id: "thetaone-ai/Korean-Japanese-Code-Switching-Speech"
source: "huggingface"
url: "https://huggingface.co/datasets/thetaone-ai/Korean-Japanese-Code-Switching-Speech"
downloads: 92
summary: "한국어-일본어 코드스위칭 음성 데이터로 ASR 모델 평가용 소규모 데이터셋입니다."
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
  - "[[일본어]]"
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
# thetaone-ai/Korean-Japanese-Code-Switching-Speech

> dataset · [Hugging Face](https://huggingface.co/datasets/thetaone-ai/Korean-Japanese-Code-Switching-Speech)

한국어-일본어 코드스위칭 음성 데이터로 ASR 모델 평가용 소규모 데이터셋입니다.

## 분류

- **작업**: [[음성 인식]] — metadata · readme, task_categories = `automatic-speech-recognition` · 신뢰도 medium
- **입력 형식**: [[음성 (입력 형식)|음성]] — ner · modality, readme, task:speech_recognition = `Audio format: 16 kHz WAV stored in the Hugging Face `Audio` feature` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:speech_recognition = `sentence-level transcriptions` · 신뢰도 medium
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `9` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Since there is an extremely small amount of Korean-Japanese code-switching data available, this dataset was designed to be used as a small-scale evaluation data` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `this dataset was designed to be used as a small-scale evaluation dataset.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 36자 ≈ 9 토큰 (viewer statistics, default/test)
