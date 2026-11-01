---
type: "dataset"
id: "Iman998/XhotpotQA-GLM52-Judge-V2"
source: "huggingface"
url: "https://huggingface.co/datasets/Iman998/XhotpotQA-GLM52-Judge-V2"
downloads: 108
summary: "XHotpotQA V2 RC1 번역 평가 데이터셋으로 23개 언어의 문단, 질문, 답변 품질 점수를 제공함."
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
# Iman998/XhotpotQA-GLM52-Judge-V2

> dataset · [Hugging Face](https://huggingface.co/datasets/Iman998/XhotpotQA-GLM52-Judge-V2)

XHotpotQA V2 RC1 번역 평가 데이터셋으로 23개 언어의 문단, 질문, 답변 품질 점수를 제공함.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories = `text-classification` · 신뢰도 medium
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `Paragraphs, questions, and short answers are scored against their English source` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `Paragraphs, questions, and short answers are scored against their English source on a 0–100 scale.` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `23 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `110` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `This release provides the clean final 2,760-row translation audit for XHotpotQA V2 RC1.` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `This release provides the clean final 2,760-row translation audit for XHotpotQA V2 RC1.` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `judge_explanation` 열 p90 439자 ≈ 110 토큰 (viewer statistics, xhotpotqa_glm52_judge_v2/audit)
