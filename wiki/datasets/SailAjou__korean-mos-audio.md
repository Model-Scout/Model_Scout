---
type: "dataset"
id: "SailAjou/korean-mos-audio"
source: "huggingface"
url: "https://huggingface.co/datasets/SailAjou/korean-mos-audio"
downloads: 18
summary: "AIHub 발화문 기반 한국어 합성 음성 평가용 WAV 데이터셋입니다."
readme_status: "ok"
readme_language: "ko"
korean_focus: "ko_only"
task:
  - "[[음성 분류]]"
  - "[[텍스트 분류]]"
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
  - "[[평가용]]"
data_format:
  - "[[미디어 파일]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# SailAjou/korean-mos-audio

> dataset · [Hugging Face](https://huggingface.co/datasets/SailAjou/korean-mos-audio)

AIHub 발화문 기반 한국어 합성 음성 평가용 WAV 데이터셋입니다.

## 분류

- **작업**: [[음성 분류]] — ner · readme = `한국어 합성 음성 평가 자료` · 신뢰도 low
- **작업**: [[텍스트 분류]] — ner · readme = `모델별 평가 항목은 MOS 관리자 화면에서 선택합니다.` · 신뢰도 low
- **작업**: [[음성 합성]] — metadata · task_categories = `text-to-speech` · 신뢰도 low
- **입력 형식**: [[음성 (입력 형식)|음성]] — ner · modality, readme, task:audio_classification = `평가용 WAV입니다.` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:classification, task:text_to_speech = `text` · 신뢰도 medium
- **출력 형식**: [[음성 (출력 형식)|음성]] — task_rule · task:text_to_speech = `audio` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `모델별 평가 항목은 MOS 관리자 화면에서 선택합니다.` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `한국어 합성 음성 평가 자료` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `평가용 WAV입니다.` · 신뢰도 medium
- **데이터 형식**: [[미디어 파일]] — metadata · format = `audiofolder` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
