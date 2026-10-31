---
type: "dataset"
id: "neuralfoundry-coder/korean-llm-trustworthiness-benchmark"
source: "huggingface"
url: "https://huggingface.co/datasets/neuralfoundry-coder/korean-llm-trustworthiness-benchmark"
downloads: 70
summary: "AIHub 초거대 언어모델 신뢰성 벤치마크 기반 한국어 LLM 신뢰성 평가용 데이터셋입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
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
  - "[[비상업 전용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# neuralfoundry-coder/korean-llm-trustworthiness-benchmark

> dataset · [Hugging Face](https://huggingface.co/datasets/neuralfoundry-coder/korean-llm-trustworthiness-benchmark)

AIHub 초거대 언어모델 신뢰성 벤치마크 기반 한국어 LLM 신뢰성 평가용 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories = `text-classification` · 신뢰도 medium
- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:generation = `프롬프트/질문 (DPO용)` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `선호 응답 (DPO용)` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `45` · 신뢰도 medium
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `한국어 LLM 지시학습 데이터셋입니다.` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · dataset_id/tags, readme = `평가 전용이다. 학습 · 합성 시드 · few-shot · 하이퍼파라미터 · 임계값 선택(test 분할)에 쓰지 않는다.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `output` 열 p90 67자 ≈ 45 토큰 (viewer statistics, default/train)
