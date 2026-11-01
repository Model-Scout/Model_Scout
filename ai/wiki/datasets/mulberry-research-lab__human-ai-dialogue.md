---
type: "dataset"
id: "mulberry-research-lab/human-ai-dialogue"
source: "huggingface"
url: "https://huggingface.co/datasets/mulberry-research-lab/human-ai-dialogue"
downloads: 9
summary: "Mulberry Research Lab의 인간과 AI 간 질문과 답변 기록 데이터셋으로 AI-Human 상호작용 연구에 활용됨."
readme_status: "ok"
readme_language: "mixed"
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
  - "[[비상업 전용]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# mulberry-research-lab/human-ai-dialogue

> dataset · [Hugging Face](https://huggingface.co/datasets/mulberry-research-lab/human-ai-dialogue)

Mulberry Research Lab의 인간과 AI 간 질문과 답변 기록 데이터셋으로 AI-Human 상호작용 연구에 활용됨.

## 분류

- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[질의응답]] — metadata · readme, task_categories = `question-answering` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering = `질문 내용` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering = `답변 (또는 '대기 중')` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-4.0` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `지속적 대화 기록의 공개적 축적` · 신뢰도 low
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high
