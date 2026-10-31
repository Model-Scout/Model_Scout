---
type: "dataset"
id: "izlley2/llm0to1-sft-synth-ko"
source: "huggingface"
url: "https://huggingface.co/datasets/izlley2/llm0to1-sft-synth-ko"
downloads: 148
summary: "한국어 도서 재작성문과 자체 합성으로 만든 한국어 SFT 데이터로, QA와 지시이행 태스크에 활용됨."
readme_status: "ok"
readme_language: "ko"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
  - "[[질의응답]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
---
# izlley2/llm0to1-sft-synth-ko

> dataset · [Hugging Face](https://huggingface.co/datasets/izlley2/llm0to1-sft-synth-ko)

한국어 도서 재작성문과 자체 합성으로 만든 한국어 SFT 데이터로, QA와 지시이행 태스크에 활용됨.

## 분류

- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[질의응답]] — ner · readme = `1. 지식 QA (qa_*.jsonl)` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering = `한국어 도서 재작성문(자체 사전학습 합성물)에서 QA 를 생성했다.` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering = `질문은 자기완결적으로 요구했다` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `한국어 도서 재작성문(자체 사전학습 합성물)에서 QA 를 생성했다.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `한국어 채팅 모델을 `Qwen/Qwen3.5-9B-Base` 에서 사후학습(SFT)하기 위해 만든 데이터다.` · 신뢰도 medium
