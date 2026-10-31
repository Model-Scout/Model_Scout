---
type: "dataset"
id: "origindatalab/stereo-imu-egocentric-evaluation"
source: "huggingface"
url: "https://huggingface.co/datasets/origindatalab/stereo-imu-egocentric-evaluation"
downloads: 221
summary: "헤드마운트 스테레오 카메라와 IMU 센서의 기술 평가용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[정보 추출]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[미디어 파일]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# origindatalab/stereo-imu-egocentric-evaluation

> dataset · [Hugging Face](https://huggingface.co/datasets/origindatalab/stereo-imu-egocentric-evaluation)

헤드마운트 스테레오 카메라와 IMU 센서의 기술 평가용 데이터셋입니다.

## 분류

- **작업**: [[정보 추출]] — ner · readme = `A head-mounted stereo egocentric recording of an indoor two-handed workbench assembly task was evaluated for frame correspondence, timing, sensor continuity, im` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · modality, readme = `head-mounted stereo + IMU recording` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:information_extraction = `text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `technical evaluation, measurement figures and documentation only.` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Real-World Data Production for Physical AI` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · dataset_id/tags, readme = `technical evaluation, measurement figures and documentation only.` · 신뢰도 medium
- **데이터 형식**: [[미디어 파일]] — metadata · format = `imagefolder` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high
