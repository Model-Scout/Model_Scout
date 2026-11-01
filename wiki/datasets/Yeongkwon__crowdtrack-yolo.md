---
type: "dataset"
id: "Yeongkwon/crowdtrack-yolo"
source: "huggingface"
url: "https://huggingface.co/datasets/Yeongkwon/crowdtrack-yolo"
downloads: 166
summary: "Fudan University CrowdTrack 원본에서 5프레임마다 1장씩 추출한 사람 검출용 YOLO 라벨 데이터셋입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_with_others"
task:
  - "[[정보 추출]]"
  - "[[이미지 인식]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
data_format:
  - "[[미디어 파일]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# Yeongkwon/crowdtrack-yolo

> dataset · [Hugging Face](https://huggingface.co/datasets/Yeongkwon/crowdtrack-yolo)

Fudan University CrowdTrack 원본에서 5프레임마다 1장씩 추출한 사람 검출용 YOLO 라벨 데이터셋입니다.

## 분류

- **작업**: [[정보 추출]] — ner · readme = `사람 검출용 YOLO TXT 라벨을 붙인 데이터셋입니다.` · 신뢰도 low
- **작업**: [[이미지 인식]] — metadata · task_categories = `object-detection` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · modality, readme, task:vision = `이미지 파일은 원본과 바이트까지 같습니다.` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:information_extraction = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `사람 검출용 YOLO TXT 라벨` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Fleyderer/CrowdTrack-MOT(원저: Fu et al., 2025, Fudan University의 CrowdTrack)` · 신뢰도 low
- **데이터 형식**: [[미디어 파일]] — metadata · format = `imagefolder` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high
