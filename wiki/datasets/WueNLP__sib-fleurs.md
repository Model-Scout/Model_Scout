---
type: "dataset"
id: "WueNLP/sib-fleurs"
source: "huggingface"
url: "https://huggingface.co/datasets/WueNLP/sib-fleurs"
downloads: 817
summary: "SIB-Fleurs는 다국어 음성 언어 이해 평가용 데이터셋으로, 발화의 주제를 분류하는 데 사용됩니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[음성 분류]]"
  - "[[텍스트 분류]]"
  - "[[문서 인식(OCR)]]"
  - "[[질의응답]]"
  - "[[음성 인식]]"
  - "[[음성 합성]]"
input_modality:
  - "[[음성 (입력 형식)|음성]]"
  - "[[문서 파일 (입력 형식)|문서 파일]]"
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[음성 (출력 형식)|음성]]"
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# WueNLP/sib-fleurs

> dataset · [Hugging Face](https://huggingface.co/datasets/WueNLP/sib-fleurs)

SIB-Fleurs는 다국어 음성 언어 이해 평가용 데이터셋으로, 발화의 주제를 분류하는 데 사용됩니다.

## 분류

- **작업**: [[음성 분류]] — metadata · task_categories = `audio-classification` · 신뢰도 low
- **작업**: [[텍스트 분류]] — ner · readme = `For each utterance in Fleurs, the task is to determine the topic the utterance belongs to.` · 신뢰도 low
- **작업**: [[문서 인식(OCR)]] — metadata · task_categories = `document-question-answering` · 신뢰도 low
- **작업**: [[질의응답]] — metadata · task_categories = `question-answering` · 신뢰도 low
- **작업**: [[음성 인식]] — metadata · task_categories = `audio-text-to-text` · 신뢰도 low
- **작업**: [[음성 합성]] — metadata · task_categories = `text-to-speech` · 신뢰도 low
- **입력 형식**: [[음성 (입력 형식)|음성]] — ner · modality, readme, task:audio_classification, task:speech_recognition = `Each sentence in Flores has ~2.3 utterances in Fleurs, on average. That is why each instance comprises the aligned Fleurs data as `list[str, audio, ...]`.` · 신뢰도 high
- **입력 형식**: [[문서 파일 (입력 형식)|문서 파일]] — task_rule · task:ocr = `document` · 신뢰도 medium
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — task_rule · task:ocr = `image` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:question_answering, task:text_to_speech = `We select the best checkpoint by maximizing performance on the English validation set. For evaluation, we test zero-shot cross-lingual transfer across all avail` · 신뢰도 high
- **출력 형식**: [[음성 (출력 형식)|음성]] — task_rule · task:text_to_speech = `audio` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:ocr, task:question_answering, task:speech_recognition = `For each utterance in Fleurs, the task is to determine the topic the utterance belongs to.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `198 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `25` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `SIB-Fleurs is a dataset suitable to evaluate Multilingual Spoken Language Understanding.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `This dataset retains the training, validation, and test splits of Fleurs and not SIB.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `raw_transcription` 열 p90 99자 ≈ 25 토큰 (viewer statistics, kor_Hang/validation)
