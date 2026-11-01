---
type: "dataset"
id: "lianghsun/tw-legal-nlp"
source: "huggingface"
url: "https://huggingface.co/datasets/lianghsun/tw-legal-nlp"
downloads: 81
summary: "tw-legal-nlp는 대만 법률 분야의 명명 개체 인식, 법률 텍스트 이해, 구조화, 조문 표기 변환을 위한 소규모 다중 작업 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 분류]]"
  - "[[텍스트 생성]]"
  - "[[정보 추출]]"
  - "[[질의응답]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[중국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[법률]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# lianghsun/tw-legal-nlp

> dataset · [Hugging Face](https://huggingface.co/datasets/lianghsun/tw-legal-nlp)

tw-legal-nlp는 대만 법률 분야의 명명 개체 인식, 법률 텍스트 이해, 구조화, 조문 표기 변환을 위한 소규모 다중 작업 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `語意理解 / 文本分類：理解判決書內容並進行分類或摘要；` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[정보 추출]] — metadata · readme, tags, task_categories = `token-classification` · 신뢰도 high
- **작업**: [[질의응답]] — metadata · task_categories = `question-answering` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:generation, task:information_extraction, task:question_answering = `命名實體識別（NER）：從判決書中抽取當事人、法條、日期等關鍵實體；` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering = `命名實體識別（NER）：從判決書中抽取當事人、法條、日期等關鍵實體；` · 신뢰도 medium
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `30` · 신뢰도 medium
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-4.0` · 신뢰도 high
- **도메인**: [[법률]] — tag_match · readme, tags = `legal` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — metadata · referenced_by_models = `train` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

샘플 길이: `output` 열 p90 118자 ≈ 30 토큰 (viewer statistics, default/train)

## 이 데이터로 학습한 모델

- [[QuantFactory__Llama-3.2-Taiwan-3B-Instruct-GGUF|QuantFactory/Llama-3.2-Taiwan-3B-Instruct-GGUF]]
