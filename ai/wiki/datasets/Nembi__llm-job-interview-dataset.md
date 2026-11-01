---
type: "dataset"
id: "Nembi/llm-job-interview-dataset"
source: "huggingface"
url: "https://huggingface.co/datasets/Nembi/llm-job-interview-dataset"
downloads: 16
summary: "국내 주요 IT 기업 AI/LLM 직무 채용 공고 기반 가상 면접 시나리오 데이터셋으로, LLM 면접관 파인튜닝용입니다."
readme_status: "ok"
readme_language: "ko"
korean_focus: "ko_only"
task:
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
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# Nembi/llm-job-interview-dataset

> dataset · [Hugging Face](https://huggingface.co/datasets/Nembi/llm-job-interview-dataset)

국내 주요 IT 기업 AI/LLM 직무 채용 공고 기반 가상 면접 시나리오 데이터셋으로, LLM 면접관 파인튜닝용입니다.

## 분류

- **작업**: [[질의응답]] — ner · readme = `면접관이 해당 페르소나의 이력서를 바탕으로 던질 법한 심층적이고 날카로운 질문들로 구성되어 있습니다` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:question_answering = `instruction: 질문 생성의 의도
input: resume(이력서 요약)과…` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:question_answering = `text` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `165` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `AI/LLM 관련 직무 채용 공고를 기반으로 생성된 가상 면접 시나리오입니다` · 신뢰도 low
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

샘플 길이: `output` 열 p90 247자 ≈ 165 토큰 (viewer statistics, default/train)
