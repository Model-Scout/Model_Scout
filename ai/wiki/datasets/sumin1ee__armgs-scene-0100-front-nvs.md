---
type: "dataset"
id: "sumin1ee/armgs-scene-0100-front-nvs"
source: "huggingface"
url: "https://huggingface.co/datasets/sumin1ee/armgs-scene-0100-front-nvs"
downloads: 25
summary: "ArmGS scene-0100 FRONT NVS 비디오 데이터로, 원본과 렌더링 영상 비교용입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[이미지 이해]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
  - "[[영상 (입력 형식)|영상]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
  - "[[영상 (출력 형식)|영상]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
commercial_use:
  - "[[이용 조건 미확인]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# sumin1ee/armgs-scene-0100-front-nvs

> dataset · [Hugging Face](https://huggingface.co/datasets/sumin1ee/armgs-scene-0100-front-nvs)

ArmGS scene-0100 FRONT NVS 비디오 데이터로, 원본과 렌더링 영상 비교용입니다.

## 분류

- **작업**: [[이미지 이해]] — ner · readme = `왼쪽: GT · 오른쪽: ArmGS 렌더링` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — metadata · modality, task:visual_qa = `image` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:visual_qa = `text` · 신뢰도 medium
- **입력 형식**: [[영상 (입력 형식)|영상]] — ner · modality, readme = `scene-0100-front-nvs.mp4` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:visual_qa = `text` · 신뢰도 medium
- **출력 형식**: [[영상 (출력 형식)|영상]] — ner · readme = `왼쪽: GT · 오른쪽: ArmGS 렌더링` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **데이터 용도**: [[평가용]] — ner · readme = `FRONT held-out 114프레임, 원본 촬영 시간순` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `학습 프레임은 포함하지 않았습니다.` · 신뢰도 medium
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high
