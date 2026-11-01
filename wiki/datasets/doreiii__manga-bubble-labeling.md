---
type: "dataset"
id: "doreiii/manga-bubble-labeling"
source: "huggingface"
url: "https://huggingface.co/datasets/doreiii/manga-bubble-labeling"
downloads: 24
summary: "만화 말풍선 감지를 위한 YOLO 학습용 라벨링 준비 데이터셋입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
  - "[[정보 추출]]"
  - "[[이미지 인식]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[일본어]]"
  - "[[한국어]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[문화·관광]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# doreiii/manga-bubble-labeling

> dataset · [Hugging Face](https://huggingface.co/datasets/doreiii/manga-bubble-labeling)

만화 말풍선 감지를 위한 YOLO 학습용 라벨링 준비 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `클래스: 4개 (speech_bubble, thought_bubble, narration_box, sound_effect)` · 신뢰도 low
- **작업**: [[정보 추출]] — ner · readme = `만화 말풍선 감지를 위한 YOLO 학습 데이터셋` · 신뢰도 low
- **작업**: [[이미지 인식]] — metadata · tags, task_categories = `object-detection` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · readme, task:vision = `총 이미지: 200개` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:classification, task:information_extraction = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `클래스: 4개 (speech_bubble, thought_bubble, narration_box, sound_effect)` · 신뢰도 low
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[문화·관광]] — ner · readme = `만화 말풍선 감지를 위한 YOLO 학습 데이터셋` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `YOLO 모델 학습` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high
