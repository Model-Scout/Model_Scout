---
type: "dataset"
id: "ggfox00000/dia-Notsofar-test"
source: "huggingface"
url: "https://huggingface.co/datasets/ggfox00000/dia-Notsofar-test"
downloads: 30
summary: "NOTSOFAR-1은 다중 화자 회의 음성 인식 및 화자 분리 평가용 벤치마크 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[음성 분류]]"
  - "[[음성 인식]]"
input_modality:
  - "[[음성 (입력 형식)|음성]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[de]]"
  - "[[영어]]"
  - "[[es]]"
  - "[[fr]]"
  - "[[it]]"
  - "[[일본어]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[중국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[미디어 파일]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# ggfox00000/dia-Notsofar-test

> dataset · [Hugging Face](https://huggingface.co/datasets/ggfox00000/dia-Notsofar-test)

NOTSOFAR-1은 다중 화자 회의 음성 인식 및 화자 분리 평가용 벤치마크 데이터셋입니다.

## 분류

- **작업**: [[음성 분류]] — metadata · task_categories = `voice-activity-detection` · 신뢰도 low
- **작업**: [[음성 인식]] — metadata · task_categories = `automatic-speech-recognition` · 신뢰도 low
- **입력 형식**: [[음성 (입력 형식)|음성]] — metadata · modality, task:audio_classification, task:speech_recognition = `audio` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:speech_recognition = `Métriques de référence : DER, tcpWER (time-constrained permutation-invariant), SA-WER.` · 신뢰도 medium
- **언어**: [[de]] — metadata · languages = `de` · 신뢰도 high
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[es]] — metadata · languages = `es` · 신뢰도 high
- **언어**: [[fr]] — metadata · languages = `fr` · 신뢰도 high
- **언어**: [[it]] — metadata · languages = `it` · 신뢰도 high
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `8 languages` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cdla-permissive-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `réunions naturelles multi-locuteurs en bureau` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `NOTSOFAR-1 — eval splits (mirror)` · 신뢰도 medium
- **데이터 형식**: [[미디어 파일]] — metadata · format = `audiofolder` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
