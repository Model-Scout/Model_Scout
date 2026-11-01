---
type: "dataset"
id: "useKled/non-latin-script-text"
source: "huggingface"
url: "https://huggingface.co/datasets/useKled/non-latin-script-text"
downloads: 23
summary: "비라틴 문자로 된 실제 세계의 글자를 촬영한 이미지 데이터셋으로, 다국어 장면 텍스트 인식 및 스크립트 식별에 활용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
  - "[[정보 추출]]"
  - "[[질의응답]]"
  - "[[이미지 인식]]"
  - "[[이미지 이해]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[ar]]"
  - "[[bn]]"
  - "[[hi]]"
  - "[[일본어]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[my]]"
  - "[[ru]]"
  - "[[th]]"
  - "[[중국어]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# useKled/non-latin-script-text

> dataset · [Hugging Face](https://huggingface.co/datasets/useKled/non-latin-script-text)

비라틴 문자로 된 실제 세계의 글자를 촬영한 이미지 데이터셋으로, 다국어 장면 텍스트 인식 및 스크립트 식별에 활용됨.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `Script identification` · 신뢰도 low
- **작업**: [[정보 추출]] — ner · readme = `Multilingual scene-text detection and recognition` · 신뢰도 low
- **작업**: [[질의응답]] — ner · readme = `Text-centric VQA beyond Latin` · 신뢰도 low
- **작업**: [[이미지 인식]] — metadata · task_categories = `object-detection` · 신뢰도 low
- **작업**: [[이미지 이해]] — metadata · task_categories = `image-to-text` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · modality, readme, task:vision, task:visual_qa = `Sharp photos of real-world writing` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:classification, task:information_extraction, task:question_answering, task:visual_qa = `text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering, task:visual_qa = `Labeled (script tag)` · 신뢰도 medium
- **언어**: [[ar]] — metadata · languages = `ar` · 신뢰도 high
- **언어**: [[bn]] — metadata · languages = `bn` · 신뢰도 high
- **언어**: [[hi]] — metadata · languages = `hi` · 신뢰도 high
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `9 languages` · 신뢰도 high
- **언어**: [[my]] — metadata · languages = `my` · 신뢰도 high
- **언어**: [[ru]] — metadata · languages = `ru` · 신뢰도 high
- **언어**: [[th]] — metadata · languages = `th` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Sharp photos of real-world writing in Devanagari, Arabic, Thai, Cyrillic, Han and other non-Latin scripts` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `licensed for commercial training` · 신뢰도 medium
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
