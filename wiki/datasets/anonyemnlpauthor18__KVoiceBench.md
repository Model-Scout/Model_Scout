---
type: "dataset"
id: "anonyemnlpauthor18/KVoiceBench"
source: "huggingface"
url: "https://huggingface.co/datasets/anonyemnlpauthor18/KVoiceBench"
downloads: 19
summary: "KVoiceBench는 한국어 음성 질문응답 벤치마크로, 다양한 QA 유형 평가용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
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
# anonyemnlpauthor18/KVoiceBench

> dataset · [Hugging Face](https://huggingface.co/datasets/anonyemnlpauthor18/KVoiceBench)

KVoiceBench는 한국어 음성 질문응답 벤치마크로, 다양한 QA 유형 평가용 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `open-ended generation, instruction following, and safety behavior under Korean speech input` · 신뢰도 medium
- **작업**: [[질의응답]] — metadata · readme, task_categories = `question-answering` · 신뢰도 high
- **작업**: [[음성 인식]] — metadata · task_categories = `automatic-speech-recognition` · 신뢰도 low
- **입력 형식**: [[음성 (입력 형식)|음성]] — ner · modality, readme, task:speech_recognition = `Synthesized Korean speech audio` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:question_answering = `Korean text transcription of the audio` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering, task:speech_recognition = `Reference answer, if applicable` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `31` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `KVoiceBench is a Korean spoken question answering (SpokenQA) benchmark derived from VoiceBench.` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · dataset_id/tags, readme = `KVoiceBench is a Korean spoken question answering (SpokenQA) benchmark derived from VoiceBench.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `transcription` 열 p90 47자 ≈ 31 토큰 (viewer statistics, advbench-test/test)
