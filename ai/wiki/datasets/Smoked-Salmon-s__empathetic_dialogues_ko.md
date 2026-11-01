---
type: "dataset"
id: "Smoked-Salmon-s/empathetic_dialogues_ko"
source: "huggingface"
url: "https://huggingface.co/datasets/Smoked-Salmon-s/empathetic_dialogues_ko"
downloads: 58
summary: "일상 상황에서 사용자와 챗봇 간 공감형 대화 데이터셋으로 GPT 기반 합성 데이터입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# Smoked-Salmon-s/empathetic_dialogues_ko

> dataset · [Hugging Face](https://huggingface.co/datasets/Smoked-Salmon-s/empathetic_dialogues_ko)

일상 상황에서 사용자와 챗봇 간 공감형 대화 데이터셋으로 GPT 기반 합성 데이터입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `일상 속 다양한 상황에서 사용자와 챗봇 간의 대화를 담은 데이터셋 입니다.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `답변은 [공감적 표현 - 일반적인 대화 - 관련된 질문] 의 형태를 가집니다.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `259` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `일상 속 다양한 상황에서 사용자와 챗봇 간의 대화를 담은 데이터셋 입니다.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `boostCamp AI Tech 5기 과정 중 NLP 12조 훈제연어들 팀의 최종 프로젝트에서 제작한 데이터입니다.` · 신뢰도 low
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `instruction` 열 p90 389자 ≈ 259 토큰 (viewer statistics, default/train)
