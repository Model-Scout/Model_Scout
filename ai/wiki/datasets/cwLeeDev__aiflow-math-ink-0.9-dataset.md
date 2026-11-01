---
type: "dataset"
id: "cwLeeDev/aiflow-math-ink-0.9-dataset"
source: "huggingface"
url: "https://huggingface.co/datasets/cwLeeDev/aiflow-math-ink-0.9-dataset"
downloads: 34
summary: "AIFlow Math Ink 0.9의 온라인 수식 필기 데이터로 필기 인식 모델 학습·검증용이다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
  - "[[임베딩]]"
  - "[[정보 추출]]"
  - "[[이미지 인식]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
  - "[[시계열 (입력 형식)|시계열]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[교육]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# cwLeeDev/aiflow-math-ink-0.9-dataset

> dataset · [Hugging Face](https://huggingface.co/datasets/cwLeeDev/aiflow-math-ink-0.9-dataset)

AIFlow Math Ink 0.9의 온라인 수식 필기 데이터로 필기 인식 모델 학습·검증용이다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `검수 완료 학습·분석 후보` · 신뢰도 low
- **작업**: [[임베딩]] — ner · readme = `AIFlow 필기 인식 모델 학습·검증` · 신뢰도 low
- **작업**: [[정보 추출]] — ner · readme = `수동 검수된 stroke-to-symbol ownership` · 신뢰도 low
- **작업**: [[이미지 인식]] — metadata · task_categories = `image-classification` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — task_rule · task:vision = `image` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:classification, task:embedding, task:information_extraction = `목표 token/관계, 검수 상태` · 신뢰도 medium
- **입력 형식**: [[시계열 (입력 형식)|시계열]] — ner · readme = `원본 stroke 순서와 point 순서` · 신뢰도 low
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `목표 token/관계, 검수 상태` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[교육]] — ner · readme = `AIFlow Math Ink 0.9의 온라인 수식 필기 데이터다` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `AIFlow 필기 인식 모델 학습·검증과 이번 공개 배포 승인을 함께 기록한다.` · 신뢰도 medium
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high
