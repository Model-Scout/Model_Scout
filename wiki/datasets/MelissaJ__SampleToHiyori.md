---
type: "dataset"
id: "MelissaJ/SampleToHiyori"
source: "huggingface"
url: "https://huggingface.co/datasets/MelissaJ/SampleToHiyori"
downloads: 58
summary: "모모세 히요리 페르소나 기반 한국어 도구 호출 및 대화 학습 데이터셋입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
  - "[[도구 호출]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[이용 조건 미확인]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# MelissaJ/SampleToHiyori

> dataset · [Hugging Face](https://huggingface.co/datasets/MelissaJ/SampleToHiyori)

모모세 히요리 페르소나 기반 한국어 도구 호출 및 대화 학습 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 high
- **작업**: [[도구 호출]] — tag_match · tags = `tool-calling` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `system(페르소나·활동 줄·인적 정보 블록·기억 블록·[자비스 모드]·[웹 검색]), 마지막 user만 [참고 정보] 래퍼` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `마지막 user만 [참고 정보] 래퍼` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `42` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **데이터 용도**: [[평가용]] — ner · readme = `eval은 템플릿 단위로 다시 나눴다(근접 중복 군집 통째로) — train↔eval 근접 중복 0.` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `train / eval / probe 5,495 / 322 / —` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `response` 열 p90 63자 ≈ 42 토큰 (viewer statistics, default/train)
