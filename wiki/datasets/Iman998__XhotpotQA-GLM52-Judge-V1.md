---
type: "dataset"
id: "Iman998/XhotpotQA-GLM52-Judge-V1"
source: "huggingface"
url: "https://huggingface.co/datasets/Iman998/XhotpotQA-GLM52-Judge-V1"
downloads: 72
summary: "XHotpotQA GLM-5.2 Judge 데이터셋은 23개 언어 번역 품질 평가용 점수 데이터입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# Iman998/XhotpotQA-GLM52-Judge-V1

> dataset · [Hugging Face](https://huggingface.co/datasets/Iman998/XhotpotQA-GLM52-Judge-V1)

XHotpotQA GLM-5.2 Judge 데이터셋은 23개 언어 번역 품질 평가용 점수 데이터입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories = `text-classification` · 신뢰도 medium
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `Each row evaluates one translated paragraph, question, or short answer against its English source` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `Each row evaluates one translated paragraph, question, or short answer against its English source on a 0–100 scale.` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `23 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `123` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `XHotpotQA resource analysis` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `AUDIT · V1
ROWS · 2,760
SCORED · 100%` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `judge_explanation` 열 p90 493자 ≈ 123 토큰 (viewer statistics, xhotpotqa_glm52_judge_v1/audit)
