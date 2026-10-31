---
type: "dataset"
id: "lianghsun/tw-judgment-gist-chat"
source: "huggingface"
url: "https://huggingface.co/datasets/lianghsun/tw-judgment-gist-chat"
downloads: 9
summary: "판결서 전문을 입력으로 하여 핵심 법률 견해를 요약하는 법률 요약 대화 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 생성]]"
  - "[[요약]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[중국어]]"
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
# lianghsun/tw-judgment-gist-chat

> dataset · [Hugging Face](https://huggingface.co/datasets/lianghsun/tw-judgment-gist-chat)

판결서 전문을 입력으로 하여 핵심 법률 견해를 요약하는 법률 요약 대화 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[요약]] — metadata · task_categories = `summarization` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:summarization = `完整判決書文本（含裁判字號、日期、案由、當事人、論理段落等）` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:summarization = `以 gpt-4o 生成之判決要旨摘要，聚焦於該判決之核心法律見解。` · 신뢰도 medium
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-4.0` · 신뢰도 high
- **도메인**: [[법률]] — tag_match · readme, tags = `legal` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `適合作為法律 LLM 之判決要旨萃取任務之 SFT 素材。` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

## 이 데이터로 학습한 모델

- [[QuantFactory__Llama-3.2-Taiwan-3B-Instruct-GGUF|QuantFactory/Llama-3.2-Taiwan-3B-Instruct-GGUF]]
