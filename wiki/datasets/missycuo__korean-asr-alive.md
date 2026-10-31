---
type: "dataset"
id: "missycuo/korean-asr-alive"
source: "huggingface"
url: "https://huggingface.co/datasets/missycuo/korean-asr-alive"
downloads: 26
summary: "Alive 영화에서 추출한 한국어 음성 및 베트남어 자막 데이터셋으로 ASR에 활용."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[음성 인식]]"
input_modality:
  - "[[음성 (입력 형식)|음성]]"
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
  - "[[vi]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# missycuo/korean-asr-alive

> dataset · [Hugging Face](https://huggingface.co/datasets/missycuo/korean-asr-alive)

Alive 영화에서 추출한 한국어 음성 및 베트남어 자막 데이터셋으로 ASR에 활용.

## 분류

- **작업**: [[음성 인식]] — metadata · readme, task_categories = `automatic-speech-recognition` · 신뢰도 high
- **입력 형식**: [[음성 (입력 형식)|음성]] — ner · modality, readme, task:speech_recognition = `audio: Dữ liệu âm thanh (binary bytes hoặc dictionary path/bytes)` · 신뢰도 high
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:speech_recognition = `korean_text: Nội dung thoại tiếng Hàn` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[vi]] — metadata · languages = `vi` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Dataset ASR trích xuất thoại tiếng Hàn và phụ đề tiếng Việt từ phim/tập: Alive.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Dataset ASR trích xuất thoại tiếng Hàn và phụ đề tiếng Việt từ phim/tập: Alive.` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high
