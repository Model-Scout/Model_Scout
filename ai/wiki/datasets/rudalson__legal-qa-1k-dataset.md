---
type: "dataset"
id: "rudalson/legal-qa-1k-dataset"
source: "huggingface"
url: "https://huggingface.co/datasets/rudalson/legal-qa-1k-dataset"
downloads: 21
summary: "한국 민사법 분야 법률 질문과 전문가 답변으로 구성된 1,000개 QA 데이터셋입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
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
  - "[[비상업 전용]]"
domain:
  - "[[법률]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# rudalson/legal-qa-1k-dataset

> dataset · [Hugging Face](https://huggingface.co/datasets/rudalson/legal-qa-1k-dataset)

한국 민사법 분야 법률 질문과 전문가 답변으로 구성된 1,000개 QA 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `한국어 법률 도메인 파인튜닝(SFT) 실습` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **작업**: [[질의응답]] — metadata · readme, task_categories = `question-answering` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:generation, task:question_answering = `원본 법률 질문 텍스트` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering = `법률 전문가 스타일의 답변 텍스트` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `152` · 신뢰도 medium
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-sa-4.0` · 신뢰도 high
- **도메인**: [[법률]] — tag_match · readme, tags = `legal` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `Llama 3.x 모델의 한국어 법률 도메인 파인튜닝(SFT) 실습을 목적으로 합니다.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `answer` 열 p90 228자 ≈ 152 토큰 (viewer statistics, default/train)
