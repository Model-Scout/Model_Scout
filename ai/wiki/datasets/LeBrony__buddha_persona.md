---
type: "dataset"
id: "LeBrony/buddha_persona"
source: "huggingface"
url: "https://huggingface.co/datasets/LeBrony/buddha_persona"
downloads: 33
summary: "한국 팔만대장경 불교 경전을 기반으로 한 다양한 질문-답변과 추론 대화 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
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
dataset_role:
  - "[[학습용]]"
---
# LeBrony/buddha_persona

> dataset · [Hugging Face](https://huggingface.co/datasets/LeBrony/buddha_persona)

한국 팔만대장경 불교 경전을 기반으로 한 다양한 질문-답변과 추론 대화 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — tag_match · tags = `chat` · 신뢰도 low
- **작업**: [[질의응답]] — tag_match · tags = `qa` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering = `question-answer pairs and reasoning-enhanced conversations` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering = `Korean responses for end-user interaction` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `Fine-tune models for accurate Buddhist Q&A` · 신뢰도 medium
