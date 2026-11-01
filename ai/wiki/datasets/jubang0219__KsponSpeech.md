---
type: "dataset"
id: "jubang0219/KsponSpeech"
source: "huggingface"
url: "https://huggingface.co/datasets/jubang0219/KsponSpeech"
downloads: 71
summary: "KsponSpeech는 한국어 자발적 대화 음성 데이터셋으로 음성 인식 평가에 사용됨."
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
# jubang0219/KsponSpeech

> dataset · [Hugging Face](https://huggingface.co/datasets/jubang0219/KsponSpeech)

KsponSpeech는 한국어 자발적 대화 음성 데이터셋으로 음성 인식 평가에 사용됨.

## 분류

- **작업**: [[음성 인식]] — ner · readme = `KsponSpeech: Korean Spontaneous Speech Corpus for Automatic Speech Recognition` · 신뢰도 medium
- **입력 형식**: [[음성 (입력 형식)|음성]] — ner · modality, readme, task:speech_recognition = `audio: A dictionary containing the path to the downloaded audio file, the decoded audio array, and the sampling rate.` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:speech_recognition = `transcription: The transcription of the audio file, equivalent to the orthographic transcription.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `39` · 신뢰도 medium
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-nd-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `general open-domain dialog utterances` · 신뢰도 medium
- **데이터 용도**: [[평가용]] — ner · readme = `Please note that we are only sharing the evaluation set of KsponSpeech` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `raw_transcription` 열 p90 59자 ≈ 39 토큰 (viewer statistics, default/eval_clean)
