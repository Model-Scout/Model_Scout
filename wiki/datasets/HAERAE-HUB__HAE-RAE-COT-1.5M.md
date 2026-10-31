---
type: "dataset"
id: "HAERAE-HUB/HAE-RAE-COT-1.5M"
source: "huggingface"
url: "https://huggingface.co/datasets/HAERAE-HUB/HAE-RAE-COT-1.5M"
downloads: 117
summary: "HAE-RAE-COT-1.5M은 한국어 질문과 CoT 추론이 포함된 158만 개 샘플 데이터셋입니다."
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
  - "[[중문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# HAERAE-HUB/HAE-RAE-COT-1.5M

> dataset · [Hugging Face](https://huggingface.co/datasets/HAERAE-HUB/HAE-RAE-COT-1.5M)

HAE-RAE-COT-1.5M은 한국어 질문과 CoT 추론이 포함된 158만 개 샘플 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `HAE-RAE-COT-1.5M is a dataset encompassing 1,586,688 samples of questions paired with CoT (Chain of Thought) rationales.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `samples of questions paired with CoT (Chain of Thought) rationales` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `samples of questions paired with CoT (Chain of Thought) rationales` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `1104` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `HAE-RAE-COT-1.5M represents the largest available CoT or instruction data in the Korean language.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `HAE-RAE-COT-1.5M is a dataset encompassing 1,586,688 samples of questions paired with CoT (Chain of Thought) rationales.` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high

샘플 길이: `Question` 열 p90 1655자 ≈ 1104 토큰 (viewer statistics, default/train)
