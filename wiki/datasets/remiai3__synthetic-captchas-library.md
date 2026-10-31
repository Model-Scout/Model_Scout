---
type: "dataset"
id: "remiai3/synthetic-captchas-library"
source: "huggingface"
url: "https://huggingface.co/datasets/remiai3/synthetic-captchas-library"
downloads: 2455
summary: "44개 세계 문자 체계의 4글자 합성 CAPTCHA 이미지로 OCR 및 문자 인식 연구용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
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
  - "[[한국어]]"
  - "[[다국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# remiai3/synthetic-captchas-library

> dataset · [Hugging Face](https://huggingface.co/datasets/remiai3/synthetic-captchas-library)

44개 세계 문자 체계의 4글자 합성 CAPTCHA 이미지로 OCR 및 문자 인식 연구용 데이터셋입니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `Vision-language model pretraining` · 신뢰도 low
- **작업**: [[정보 추출]] — ner · readme = `designed for OCR, multilingual vision models, and script recognition research` · 신뢰도 low
- **작업**: [[이미지 인식]] — ner · readme = `synthetic 4-character CAPTCHA images` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · modality, readme, task:vision = `synthetic 4-character CAPTCHA images` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:embedding, task:information_extraction = `text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `Label file mapping image filename → correct 4-character text` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `26 languages` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `A multilingual dataset of synthetic 4-character CAPTCHA images` · 신뢰도 low
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high
