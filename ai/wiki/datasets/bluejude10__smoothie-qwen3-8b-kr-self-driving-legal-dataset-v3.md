---
type: "dataset"
id: "bluejude10/smoothie-qwen3-8b-kr-self-driving-legal-dataset-v3"
source: "huggingface"
url: "https://huggingface.co/datasets/bluejude10/smoothie-qwen3-8b-kr-self-driving-legal-dataset-v3"
downloads: 79
summary: "대한민국 자율주행자동차법 관련 750건 한국어 QnA 데이터셋으로 법률 AI 파인튜닝용입니다."
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
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[법률]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# bluejude10/smoothie-qwen3-8b-kr-self-driving-legal-dataset-v3

> dataset · [Hugging Face](https://huggingface.co/datasets/bluejude10/smoothie-qwen3-8b-kr-self-driving-legal-dataset-v3)

대한민국 자율주행자동차법 관련 750건 한국어 QnA 데이터셋으로 법률 AI 파인튜닝용입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `대한민국 자율주행자동차법 파인튜닝을 위한 750건의 한국어 특화 데이터셋입니다.` · 신뢰도 low
- **작업**: [[질의응답]] — metadata · task_categories = `question-answering` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:question_answering = `대한민국 자율주행자동차법 파인튜닝을 위한 750건의 한국어 특화 데이터셋입니다.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering = `대한민국 자율주행자동차법 파인튜닝을 위한 750건의 한국어 특화 데이터셋입니다.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `62` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[법률]] — tag_match · readme, tags = `legal` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `본 데이터셋은 기존 v1, v2 데이터셋 치명적인 "컨텍스트 소실(Context Forgetting)" 문제를 해결하기 위해 DTRO (Direct-To-Response Output) 스타일로 완전히 재구축되었습니다.` · 신뢰도 low
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

샘플 길이: `output` 열 p90 93자 ≈ 62 토큰 (viewer statistics, default/train)
