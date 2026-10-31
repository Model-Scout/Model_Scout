---
type: "dataset"
id: "KRAFTON/KMMAU"
source: "huggingface"
url: "https://huggingface.co/datasets/KRAFTON/KMMAU"
downloads: 211
summary: "KMMAU는 한국어 음성 모델 평가를 위한 다양한 오디오 이해 벤치마크입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[질의응답]]"
  - "[[음성 인식]]"
input_modality:
  - "[[음성 (입력 형식)|음성]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# KRAFTON/KMMAU

> dataset · [Hugging Face](https://huggingface.co/datasets/KRAFTON/KMMAU)

KMMAU는 한국어 음성 모델 평가를 위한 다양한 오디오 이해 벤치마크입니다.

## 분류

- **작업**: [[질의응답]] — metadata · readme, task_categories = `question-answering` · 신뢰도 medium
- **작업**: [[음성 인식]] — metadata · task_categories = `automatic-speech-recognition` · 신뢰도 low
- **입력 형식**: [[음성 (입력 형식)|음성]] — metadata · modality, task:speech_recognition = `audio` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:question_answering = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:question_answering, task:speech_recognition = `text` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `60` · 신뢰도 medium
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-sa-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `KMMAU is a Korean Multi-Modal Audio Understanding benchmark for evaluating speech models on diverse audio comprehension tasks.` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `Evaluation code for KVoiceBench, KOpenAudioBench, and KMMAU is available in Raon-Eval.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `question` 열 p90 91자 ≈ 60 토큰 (viewer statistics, age/test)
