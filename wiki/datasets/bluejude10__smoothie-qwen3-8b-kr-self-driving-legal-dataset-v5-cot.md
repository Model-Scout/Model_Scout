---
type: "dataset"
id: "bluejude10/smoothie-qwen3-8b-kr-self-driving-legal-dataset-v5-cot"
source: "huggingface"
url: "https://huggingface.co/datasets/bluejude10/smoothie-qwen3-8b-kr-self-driving-legal-dataset-v5-cot"
downloads: 94
summary: "대한민국 자율주행자동차 법령 관련 CoT 파인튜닝 데이터셋으로 법률 질의응답 성능 향상용입니다."
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
  - "[[일반]]"
  - "[[법률]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# bluejude10/smoothie-qwen3-8b-kr-self-driving-legal-dataset-v5-cot

> dataset · [Hugging Face](https://huggingface.co/datasets/bluejude10/smoothie-qwen3-8b-kr-self-driving-legal-dataset-v5-cot)

대한민국 자율주행자동차 법령 관련 CoT 파인튜닝 데이터셋으로 법률 질의응답 성능 향상용입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **작업**: [[질의응답]] — ner · readme = `750개 QnA 쌍` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:question_answering = `JSON (`instruction` / `output`)` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering = `JSON (`instruction` / `output`)` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `200` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Qwen3의 추론(Chain-of-Thought) 능력이 전혀 활성화되지 않음` · 신뢰도 low
- **도메인**: [[법률]] — tag_match · readme, tags = `legal` · 신뢰도 medium
- **데이터 용도**: [[평가용]] — ner · readme = `6개 모델 종합 벤치마크 결과` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `CoT 파인튜닝 데이터셋 v5` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

샘플 길이: `output` 열 p90 301자 ≈ 200 토큰 (viewer statistics, default/train)
