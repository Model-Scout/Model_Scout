---
type: "dataset"
id: "alchemine/namuwiki-arknights-asr-preview"
source: "huggingface"
url: "https://huggingface.co/datasets/alchemine/namuwiki-arknights-asr-preview"
downloads: 24
summary: "명일방주 나무위키 문서 기반 한국어 음성 인식 모델 훈련용 음성 데이터셋입니다."
readme_status: "ok"
readme_language: "mixed"
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
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# alchemine/namuwiki-arknights-asr-preview

> dataset · [Hugging Face](https://huggingface.co/datasets/alchemine/namuwiki-arknights-asr-preview)

명일방주 나무위키 문서 기반 한국어 음성 인식 모델 훈련용 음성 데이터셋입니다.

## 분류

- **작업**: [[음성 인식]] — metadata · readme, task_categories = `automatic-speech-recognition` · 신뢰도 high
- **입력 형식**: [[음성 (입력 형식)|음성]] — ner · modality, readme, task:speech_recognition = `16kHz 모노 오디오 파일` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:speech_recognition = `한국어 텍스트 전사` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `52` · 신뢰도 medium
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-sa-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `명일방주 - 나무위키 관련 문서를 기반으로` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `검증 데이터 수: 1,909` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `훈련 데이터 수: 7,635` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 78자 ≈ 52 토큰 (viewer statistics, default/test)
