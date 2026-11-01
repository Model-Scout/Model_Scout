---
type: "dataset"
id: "KimTaeHyun1/MAGO_share"
source: "huggingface"
url: "https://huggingface.co/datasets/KimTaeHyun1/MAGO_share"
downloads: 207
summary: "AIHub, Gemini 3개 음성 데이터셋과 라벨을 검증·게시한 음성 데이터셋입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[음성 인식]]"
  - "[[음성 합성]]"
input_modality:
  - "[[음성 (입력 형식)|음성]]"
  - "[[표 (입력 형식)|표]]"
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
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# KimTaeHyun1/MAGO_share

> dataset · [Hugging Face](https://huggingface.co/datasets/KimTaeHyun1/MAGO_share)

AIHub, Gemini 3개 음성 데이터셋과 라벨을 검증·게시한 음성 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = ``caption`은 실제 음성을 기술하는 설명, `instruction_ko/en`은 발화 지시문, `generation_prompt`는 생성 요청입니다.` · 신뢰도 low
- **작업**: [[음성 인식]] — ner · readme = `3개 데이터셋 음성·라벨 게시 완료` · 신뢰도 low
- **작업**: [[음성 합성]] — metadata · task_categories = `text-to-speech` · 신뢰도 low
- **입력 형식**: [[음성 (입력 형식)|음성]] — ner · readme, task:speech_recognition = `원음 WAV/FLAC 및 원본 JSON/instruction/tag sidecar 보존` · 신뢰도 medium
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:text_to_speech = ``caption`은 실제 음성을 기술하는 설명, `instruction_ko/en`은 발화 지시문, `generation_prompt`는 생성 요청입니다.` · 신뢰도 high
- **출력 형식**: [[음성 (출력 형식)|음성]] — task_rule · task:text_to_speech = `audio` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:speech_recognition = ``caption`은 실제 음성을 기술하는 설명, `instruction_ko/en`은 발화 지시문, `generation_prompt`는 생성 요청입니다.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `AIHub 2k, Gemini 4.7k, Gemini 5k KO의 아래 원음 패키지와 공통 라벨이 모두 고정 commit에서 검증됐습니다.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `기존 Gemini_4p7k YAML config는 그대로 유지하고, 두 데이터셋의 완료 검증 후 AIHub_2k·Gemini_5k_KO config를 추가했습니다.` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high
