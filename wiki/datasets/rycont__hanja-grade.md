---
type: "dataset"
id: "rycont/hanja-grade"
source: "huggingface"
url: "https://huggingface.co/datasets/rycont/hanja-grade"
downloads: 121
summary: "한국어문회에서 분류한 급수별 한자 데이터셋으로 학습자료용입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[교육]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[CSV]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# rycont/hanja-grade

> dataset · [Hugging Face](https://huggingface.co/datasets/rycont/hanja-grade)

한국어문회에서 분류한 급수별 한자 데이터셋으로 학습자료용입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `한국어문회에서 분류한 급수별 한자 데이터셋입니다.` · 신뢰도 medium
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `CSV 데이터셋` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `CSV 데이터셋` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `15` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license = `unknown` · 신뢰도 high
- **도메인**: [[교육]] — ner · readme = `한국어문회에서 분류한 급수별 한자 데이터셋입니다.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `공식 홈페이지의 학습자료 / 기타자료에 업로드된 Xls 파일을 CSV 파일로 변환하여 제공합니다.` · 신뢰도 medium
- **데이터 형식**: [[CSV]] — metadata · format = `csv` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `meaning` 열 p90 23자 ≈ 15 토큰 (viewer statistics, default/train)
