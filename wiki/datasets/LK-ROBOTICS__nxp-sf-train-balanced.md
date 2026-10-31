---
type: "dataset"
id: "LK-ROBOTICS/nxp-sf-train-balanced"
source: "huggingface"
url: "https://huggingface.co/datasets/LK-ROBOTICS/nxp-sf-train-balanced"
downloads: 50
summary: "NXP SF Balanced Fire/Smoke Dataset는 화재 및 연기 인식을 위한 균형 잡힌 학습용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[이미지 인식]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
---
# LK-ROBOTICS/nxp-sf-train-balanced

> dataset · [Hugging Face](https://huggingface.co/datasets/LK-ROBOTICS/nxp-sf-train-balanced)

NXP SF Balanced Fire/Smoke Dataset는 화재 및 연기 인식을 위한 균형 잡힌 학습용 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `NXP SF Balanced Fire/Smoke Dataset` · 신뢰도 low
- **작업**: [[이미지 인식]] — metadata · task_categories = `object-detection` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · modality, readme, task:vision = `polygon->bbox` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:classification = `text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `cleaned labels` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `NXP SF Balanced Fire/Smoke Dataset` · 신뢰도 low
