---
type: "dataset"
id: "Nexdata-kr/1.5-million-Korean-Test-Questions-Structured-Analysis-Processing-Data-Sample"
source: "huggingface"
url: "https://huggingface.co/datasets/Nexdata-kr/1.5-million-Korean-Test-Questions-Structured-Analysis-Processing-Data-Sample"
downloads: 10
summary: "한국어 K12 시험 문제 150만 개로 구성된 구조화 분석·가공 데이터셋입니다."
readme_status: "ok"
readme_language: "ko"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[언어 모델링]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[교육]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# Nexdata-kr/1.5-million-Korean-Test-Questions-Structured-Analysis-Processing-Data-Sample

> dataset · [Hugging Face](https://huggingface.co/datasets/Nexdata-kr/1.5-million-Korean-Test-Questions-Structured-Analysis-Processing-Data-Sample)

한국어 K12 시험 문제 150만 개로 구성된 구조화 분석·가공 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `문제 유형, 문제, 정답, 해설 등의 정보를 포함하며` · 신뢰도 low
- **작업**: [[언어 모델링]] — ner · readme = `본 데이터셋은 대규모 교과 지식 강화 및 학습 데이터 구축 등의 작업에 활용할 수 있습니다.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:language_modeling = `문제 유형, 문제, 정답, 해설 등의 정보를 포함하며` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:language_modeling = `문제 유형, 문제, 정답, 해설 등의 정보를 포함하며` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `540` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[교육]] — ner · readme = `한국어 시험 문제 구조화 분석·가공 데이터로, 약 150만 개의 시험 문제를 포함하고 있습니다.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `본 데이터셋은 대규모 교과 지식 강화 및 학습 데이터 구축 등의 작업에 활용할 수 있습니다.` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

샘플 길이: `parse` 열 p90 810자 ≈ 540 토큰 (viewer statistics, default/train)
