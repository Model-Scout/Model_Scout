---
type: "dataset"
id: "seastar105/emilia-yodas-ko-filtered-pocket-tts"
source: "huggingface"
url: "https://huggingface.co/datasets/seastar105/emilia-yodas-ko-filtered-pocket-tts"
downloads: 389
summary: "Emilia-YODAS 한국어 음성 데이터로 음성 합성 학습용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[음성 인식]]"
  - "[[음성 합성]]"
input_modality:
  - "[[음성 (입력 형식)|음성]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[음성 (출력 형식)|음성]]"
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# seastar105/emilia-yodas-ko-filtered-pocket-tts

> dataset · [Hugging Face](https://huggingface.co/datasets/seastar105/emilia-yodas-ko-filtered-pocket-tts)

Emilia-YODAS 한국어 음성 데이터로 음성 합성 학습용 데이터셋입니다.

## 분류

- **작업**: [[음성 인식]] — ner · readme = `Qwen3-forced-aligned Korean data` · 신뢰도 low
- **작업**: [[음성 합성]] — metadata · readme, task_categories = `text-to-speech` · 신뢰도 high
- **입력 형식**: [[음성 (입력 형식)|음성]] — ner · readme, task:speech_recognition = `verifies every referenced audio file.` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:text_to_speech = `The training transcript is the source JSON text field` · 신뢰도 medium
- **출력 형식**: [[음성 (출력 형식)|음성]] — task_rule · task:text_to_speech = `audio` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:speech_recognition = `The training transcript is the source JSON text field` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `The training transcript is the source JSON text field after NFC and whitespace normalization.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Train-ready, Qwen3-forced-aligned Korean data derived from seastar105/Emilia-YODAS-KO-filtered.` · 신뢰도 medium
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high
