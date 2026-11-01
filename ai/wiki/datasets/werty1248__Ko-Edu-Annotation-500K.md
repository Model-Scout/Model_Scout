---
type: "dataset"
id: "werty1248/Ko-Edu-Annotation-500K"
source: "huggingface"
url: "https://huggingface.co/datasets/werty1248/Ko-Edu-Annotation-500K"
downloads: 115
summary: "한국어 사전학습 데이터의 퀄리티 평가를 위한 어노테이션 학습 데이터셋입니다."
readme_status: "ok"
readme_language: "ko"
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
  - "[[초장문]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[학술·논문]]"
  - "[[교육]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# werty1248/Ko-Edu-Annotation-500K

> dataset · [Hugging Face](https://huggingface.co/datasets/werty1248/Ko-Edu-Annotation-500K)

한국어 사전학습 데이터의 퀄리티 평가를 위한 어노테이션 학습 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `quality_score: 최종 어노테이션 점수` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `어노테이션 모델은 텍스트의 앞부분 2,048토큰을 보고 평가를 수행했습니다.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `quality_score: 최종 어노테이션 점수` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[초장문]] — viewer_stats · viewer_statistics = `113127` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[학술·논문]] — ner · readme = `논문 초록/사업보고서/법률 정보/국민 청원 등의 데이터를 추가할 수 있었습니다.` · 신뢰도 medium
- **도메인**: [[교육]] — ner · readme = `한국어 사전학습 데이터 퀄리티 평가 모델 학습 데이터 셋` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `한국어 사전학습 데이터 퀄리티 평가 모델 학습 데이터 셋` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 169691자 ≈ 113127 토큰 (viewer statistics, default/test)
