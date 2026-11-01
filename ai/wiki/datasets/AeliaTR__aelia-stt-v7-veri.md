---
type: "dataset"
id: "AeliaTR/aelia-stt-v7-veri"
source: "huggingface"
url: "https://huggingface.co/datasets/AeliaTR/aelia-stt-v7-veri"
downloads: 69
summary: "12개 언어 음성 데이터와 텍스트로 구성된 음성 인식 학습용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
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
  - "[[다국어]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# AeliaTR/aelia-stt-v7-veri

> dataset · [Hugging Face](https://huggingface.co/datasets/AeliaTR/aelia-stt-v7-veri)

12개 언어 음성 데이터와 텍스트로 구성된 음성 인식 학습용 데이터셋입니다.

## 분류

- **작업**: [[음성 인식]] — metadata · readme, task_categories = `automatic-speech-recognition` · 신뢰도 high
- **입력 형식**: [[음성 (입력 형식)|음성]] — ner · readme, task:speech_recognition = `toplam ses 70.18 saat` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme = `veri/STT_MASTER_TEMIZ.jsonl tum satirlar` · 신뢰도 low
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:speech_recognition = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `12 languages` · 신뢰도 high
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Aelia STT v7 - KUMULATIF egitim havuzu (12 dil)` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Aelia STT v7 - KUMULATIF egitim havuzu (12 dil)` · 신뢰도 low
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
