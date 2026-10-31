---
type: "dataset"
id: "HuggingFaceTB/finemath"
source: "huggingface"
url: "https://huggingface.co/datasets/HuggingFaceTB/finemath"
downloads: 49514
summary: "FineMath는 CommonCrawl에서 필터링한 수학 교육 콘텐츠로 수학 문제 해결 학습용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[언어 모델링]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
input_length:
  - "[[초장문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[교육]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# HuggingFaceTB/finemath

> dataset · [Hugging Face](https://huggingface.co/datasets/HuggingFaceTB/finemath)

FineMath는 CommonCrawl에서 필터링한 수학 교육 콘텐츠로 수학 문제 해결 학습용 데이터셋입니다.

## 분류

- **작업**: [[언어 모델링]] — ner · readme = `FineMath consists of 34B tokens (FineMath-3+) and 54B tokens (FineMath-3+ with InfiMM-WebMath-3+) of mathematical educational content filtered from CommonCrawl.` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:language_modeling = `21.4M documents containing mathematical reasoning and problem solving, formatted with Markdown and LaTeX.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:language_modeling = `focusing on clear explanations and step-by-step problem solving` · 신뢰도 medium
- **입력 길이**: [[초장문]] — viewer_stats · viewer_statistics = `23641` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `odc-by` · 신뢰도 high
- **도메인**: [[교육]] — ner · readme = `mathematical educational content filtered from CommonCrawl` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — metadata · referenced_by_models = `train` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `99999999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 94563자 ≈ 23641 토큰 (viewer statistics, finemath-3plus/train)

## 이 데이터로 학습한 모델

- [[ATH-MaaS__Marco-Mini-Base|ATH-MaaS/Marco-Mini-Base]]
- [[ATH-MaaS__Marco-Mini-Global-Base|ATH-MaaS/Marco-Mini-Global-Base]]
- [[ATH-MaaS__Marco-Nano-Base|ATH-MaaS/Marco-Nano-Base]]
- [[FINAL-Bench__Aether-7B-5Attn|FINAL-Bench/Aether-7B-5Attn]]
- [[FINAL-Bench__Aether-7B-5Attn-it|FINAL-Bench/Aether-7B-5Attn-it]]
- [[prismdata__Perdix-1.1B-Base|prismdata/Perdix-1.1B-Base]]
