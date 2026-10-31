---
type: "dataset"
id: "KimTaeHyun1/MAGO_share"
source: "huggingface"
url: "https://huggingface.co/datasets/KimTaeHyun1/MAGO_share"
downloads: 148
summary: "Gemini 4.7k 음성 데이터와 라벨을 포함한 MAGO share 데이터셋으로 음성 인식 및 분석에 활용됨."
readme_status: "ok"
readme_language: "ko"
korean_focus: "ko_only"
task:
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

Gemini 4.7k 음성 데이터와 라벨을 포함한 MAGO share 데이터셋으로 음성 인식 및 분석에 활용됨.

## 분류

- **작업**: [[음성 인식]] — ner · readme = `Gemini 4.7k의 라벨과 새 audio-only TAR40개가 게시·검증됐습니다.` · 신뢰도 low
- **작업**: [[음성 합성]] — metadata · task_categories = `text-to-speech` · 신뢰도 low
- **입력 형식**: [[음성 (입력 형식)|음성]] — ner · readme, task:speech_recognition = `새 audio-only TAR40개420.952135680GB` · 신뢰도 medium
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:text_to_speech = `text` · 신뢰도 high
- **출력 형식**: [[음성 (출력 형식)|음성]] — task_rule · task:text_to_speech = `audio` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:speech_recognition = ``caption`(실제 음성을 기술하는 설명), `instruction_ko/en`(발화 지시문), `generation_prompt`(실제 생성 요청)를 구분합니다.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Gemini 4.7k의 라벨과 새 audio-only TAR40개가 게시·검증됐습니다.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `HF의 data split은 조회용 인덱스 전체를 뜻하고 실제 훈련용 재분할이나 현재 학습 사용을 뜻하지 않습니다.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high
