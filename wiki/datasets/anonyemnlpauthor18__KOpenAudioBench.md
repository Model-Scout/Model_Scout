---
type: "dataset"
id: "anonyemnlpauthor18/KOpenAudioBench"
source: "huggingface"
url: "https://huggingface.co/datasets/anonyemnlpauthor18/KOpenAudioBench"
downloads: 11
summary: "KOpenAudioBench는 한국어 음성 질의응답 벤치마크로, SpeechLM 평가용입니다."
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
# anonyemnlpauthor18/KOpenAudioBench

> dataset · [Hugging Face](https://huggingface.co/datasets/anonyemnlpauthor18/KOpenAudioBench)

KOpenAudioBench는 한국어 음성 질의응답 벤치마크로, SpeechLM 평가용입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `614 | Open-ended generation` · 신뢰도 medium
- **작업**: [[질의응답]] — metadata · readme, task_categories = `question-answering` · 신뢰도 high
- **작업**: [[음성 인식]] — metadata · task_categories = `automatic-speech-recognition` · 신뢰도 low
- **입력 형식**: [[음성 (입력 형식)|음성]] — metadata · modality, task:speech_recognition = `audio` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:generation, task:question_answering = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation, task:question_answering, task:speech_recognition = `text` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `66` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `KOpenAudioBench is a Korean spoken question answering (SpokenQA) benchmark derived from OpenAudioBench.` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · dataset_id/tags, readme = `KOpenAudioBench is a Korean spoken question answering (SpokenQA) benchmark derived from OpenAudioBench.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `transcription` 열 p90 99자 ≈ 66 토큰 (viewer statistics, alpacaeval_full-test/test)
