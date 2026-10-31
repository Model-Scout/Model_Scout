---
type: "dataset"
id: "PatronusAI/financebench"
source: "huggingface"
url: "https://huggingface.co/datasets/PatronusAI/financebench"
downloads: 7271
summary: "FinanceBench는 공개 기업 관련 금융 질의응답 성능 평가용 테스트셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[질의응답]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[금융·경제]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# PatronusAI/financebench

> dataset · [Hugging Face](https://huggingface.co/datasets/PatronusAI/financebench)

FinanceBench는 공개 기업 관련 금융 질의응답 성능 평가용 테스트셋입니다.

## 분류

- **작업**: [[질의응답]] — ner · readme = `FinanceBench is a first-of-its-kind test suite for evaluating the performance of LLMs on open book financial question answering (QA)` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:question_answering = `questions about publicly traded companies, with corresponding answers and evidence strings` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `questions about publicly traded companies, with corresponding answers and evidence strings` · 신뢰도 medium
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `115` · 신뢰도 medium
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-4.0` · 신뢰도 high
- **도메인**: [[금융·경제]] — ner · readme = `questions about publicly traded companies` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · dataset_id/tags, readme = `used in the evaluation and analysis of models assessed in the FinanceBench paper` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — metadata · referenced_by_models = `train` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

샘플 길이: `justification` 열 p90 459자 ≈ 115 토큰 (viewer statistics, default/train)

## 이 데이터로 학습한 모델

- [[PeterAM4__Qwen3-Embedding-0.6B-GGUF|PeterAM4/Qwen3-Embedding-0.6B-GGUF]]
- [[zhiqian99__Qwen3-Embedding-0.6B-GGUF|zhiqian99/Qwen3-Embedding-0.6B-GGUF]]
