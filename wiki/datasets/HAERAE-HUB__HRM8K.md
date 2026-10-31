---
type: "dataset"
id: "HAERAE-HUB/HRM8K"
source: "huggingface"
url: "https://huggingface.co/datasets/HAERAE-HUB/HRM8K"
downloads: 5898
summary: "한국어와 영어 이중언어 수학 추론 벤치마크 HRM8K, 평가용 8,011문제 포함"
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
  - "[[질의응답]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[교육]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[CSV]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# HAERAE-HUB/HRM8K

> dataset · [Hugging Face](https://huggingface.co/datasets/HAERAE-HUB/HRM8K)

한국어와 영어 이중언어 수학 추론 벤치마크 HRM8K, 평가용 8,011문제 포함

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `challenging mathematical problems from Korean sources` · 신뢰도 low
- **작업**: [[질의응답]] — ner · readme = `a bilingual math reasoning benchmark for Korean and English` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · readme = `manually capture the problems as screenshots` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:question_answering = `mathematical problems` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `numeric answers` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `249` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[교육]] — ner · readme = `Korean math exams` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `8,011 instances for evaluation` · 신뢰도 medium
- **데이터 형식**: [[CSV]] — metadata · format = `csv` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `original` 열 p90 373자 ≈ 249 토큰 (viewer statistics, GSM8K/test)
