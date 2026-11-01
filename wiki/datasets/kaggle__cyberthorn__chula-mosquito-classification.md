---
type: "dataset"
id: "kaggle/cyberthorn/chula-mosquito-classification"
source: "kaggle"
url: "https://www.kaggle.com/datasets/cyberthorn/chula-mosquito-classification"
downloads: 728
summary: "태국에서 촬영한 6종 모기 이미지로 모기 분류를 위한 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 분류]]"
  - "[[이미지 인식]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[환경·기상]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/cyberthorn/chula-mosquito-classification

> dataset · [Kaggle](https://www.kaggle.com/datasets/cyberthorn/chula-mosquito-classification)

태국에서 촬영한 6종 모기 이미지로 모기 분류를 위한 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `6 Species Mosquito in Thailand for Classification` · 신뢰도 medium
- **작업**: [[이미지 인식]] — tag_match · tags = `image classification` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · readme, task:vision = `taken by smart phone camera. Image augmentation using Albumentations libraries.` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:classification = `text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `classification of mosquito vectors` · 신뢰도 low
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `Community Data License Agreement - Permissive - Version 1.0` · 신뢰도 high
- **도메인**: [[환경·기상]] — ner · readme = `Mosquitoes transmit pathogens that can cause numerous significant infectious diseases in humans and animals such as malaria, dengue fever, chikungunya fever, an` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `The microscopy dataset contains 6 species of mosquito and one miscellaneous.` · 신뢰도 low
