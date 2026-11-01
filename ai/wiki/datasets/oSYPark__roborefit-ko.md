---
type: "dataset"
id: "oSYPark/roborefit-ko"
source: "huggingface"
url: "https://huggingface.co/datasets/oSYPark/roborefit-ko"
downloads: 36
summary: "RoboRefit 로봇 작업대 실사진 기반 referring expression segmentation 어노테이션의 한국어 번역 데이터셋입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_with_others"
task:
  - "[[임베딩]]"
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
  - "[[이용 조건 미확인]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
---
# oSYPark/roborefit-ko

> dataset · [Hugging Face](https://huggingface.co/datasets/oSYPark/roborefit-ko)

RoboRefit 로봇 작업대 실사진 기반 referring expression segmentation 어노테이션의 한국어 번역 데이터셋입니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `이 번역 데이터로 학습한 체크포인트는 oSYPark/VATEX-korean-pnp에 있습니다` · 신뢰도 low
- **작업**: [[정보 추출]] — ner · readme = `referring expression segmentation 데이터셋` · 신뢰도 low
- **작업**: [[이미지 인식]] — metadata · task_categories = `image-segmentation` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — task_rule · task:vision = `image` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:embedding, task:information_extraction = `expressions_ko 필드만 추가한 COCO-format JSON 어노테이션 파일만 올립니다.` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `expressions_ko 필드만 추가한 COCO-format JSON 어노테이션 파일만 올립니다.` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license = `unknown` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `RoboRefit (robot 작업대 위 실사진 기반 referring expression segmentation 데이터셋)` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `testA | 1859 | 8523 | 0` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `train | 7929 | 36915 | 0` · 신뢰도 medium
