---
type: "dataset"
id: "Nagase-Kotono/img-latex-ko"
source: "huggingface"
url: "https://huggingface.co/datasets/Nagase-Kotono/img-latex-ko"
downloads: 98
summary: "IM2LATEX-230k 데이터를 LLaVA 형식에 맞게 수정한 이미지-라텍스 변환용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
  - "[[이미지 인식]]"
  - "[[이미지 이해]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[이용 조건 미확인]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[미디어 파일]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# Nagase-Kotono/img-latex-ko

> dataset · [Hugging Face](https://huggingface.co/datasets/Nagase-Kotono/img-latex-ko)

IM2LATEX-230k 데이터를 LLaVA 형식에 맞게 수정한 이미지-라텍스 변환용 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `IMG2LaTeX` · 신뢰도 low
- **작업**: [[이미지 인식]] — ner · readme = `IMG2LaTeX` · 신뢰도 low
- **작업**: [[이미지 이해]] — metadata · task_categories = `visual-question-answering` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · modality, readme, task:vision, task:visual_qa = `IMG2LaTeX` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:generation, task:visual_qa = `text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:visual_qa = `IMG2LaTeX` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license = `cc` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `IM2LATEX-230k 을 LLaVA 형식에 맞게 수정한 데이터셋 입니다.` · 신뢰도 low
- **데이터 형식**: [[미디어 파일]] — metadata · format = `imagefolder` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high
