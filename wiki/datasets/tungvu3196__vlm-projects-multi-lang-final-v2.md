---
type: "dataset"
id: "tungvu3196/vlm-projects-multi-lang-final-v2"
source: "huggingface"
url: "https://huggingface.co/datasets/tungvu3196/vlm-projects-multi-lang-final-v2"
downloads: 89
summary: "다국어 의료 시각 질의응답 데이터셋으로 의료 이미지와 질문-답변 쌍을 포함합니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[질의응답]]"
  - "[[이미지 이해]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[의료·보건]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# tungvu3196/vlm-projects-multi-lang-final-v2

> dataset · [Hugging Face](https://huggingface.co/datasets/tungvu3196/vlm-projects-multi-lang-final-v2)

다국어 의료 시각 질의응답 데이터셋으로 의료 이미지와 질문-답변 쌍을 포함합니다.

## 분류

- **작업**: [[질의응답]] — metadata · readme, task_categories = `question-answering` · 신뢰도 high
- **작업**: [[이미지 이해]] — metadata · task_categories = `visual-question-answering` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — metadata · modality, task:visual_qa = `image` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:question_answering, task:visual_qa = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:question_answering, task:visual_qa = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `16 languages` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[의료·보건]] — ner · readme = `My Final Multilingual Medical VQA Dataset` · 신뢰도 medium
- **데이터 용도**: [[평가용]] — ner · readme = `# Load the English testing data
en_test = load_dataset("tungvu3196/vlm-projects-multi-lang-final-v2", "English", split="test")` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `# Load the Vietnamese training data
vi_train = load_dataset("tungvu3196/vlm-projects-multi-lang-final-v2", "Vietnamese", split="train")` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high
