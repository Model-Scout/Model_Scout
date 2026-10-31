---
type: "dataset"
id: "ekgP115/campusvoice-rt-eval"
source: "huggingface"
url: "https://huggingface.co/datasets/ekgP115/campusvoice-rt-eval"
downloads: 65
summary: "CampusVoice-RT 평가용 데이터셋으로 한국어 읽기 음성에 다양한 잡음을 섞은 음성 데이터입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[음성 인식]]"
input_modality:
  - "[[음성 (입력 형식)|음성]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[미디어 파일]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# ekgP115/campusvoice-rt-eval

> dataset · [Hugging Face](https://huggingface.co/datasets/ekgP115/campusvoice-rt-eval)

CampusVoice-RT 평가용 데이터셋으로 한국어 읽기 음성에 다양한 잡음을 섞은 음성 데이터입니다.

## 분류

- **작업**: [[음성 인식]] — metadata · readme, task_categories = `automatic-speech-recognition` · 신뢰도 medium
- **입력 형식**: [[음성 (입력 형식)|음성]] — ner · modality, readme, task:speech_recognition = `audio.tar.gz (all audio in one archive; download this), audio/<condition>/<id>.wav` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:speech_recognition = `Korean read speech (Zeroth-Korean test, FLEURS ko_kr test; both CC BY 4.0)` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Korean read speech (Zeroth-Korean test, FLEURS ko_kr test; both CC BY 4.0) mixed with outdoor noise from FSD50K` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · dataset_id/tags, readme = `CampusVoice-RT evaluation set` · 신뢰도 medium
- **데이터 형식**: [[미디어 파일]] — metadata · format = `audiofolder` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high
