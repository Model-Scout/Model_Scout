---
type: "dataset"
id: "MelissaJ/ProjectLucia_Hera"
source: "huggingface"
url: "https://huggingface.co/datasets/MelissaJ/ProjectLucia_Hera"
downloads: 59
summary: "루시아 페르소나 기반 한국어 단일 턴 및 도구 호출 대화 학습용 데이터셋입니다."
readme_status: "ok"
readme_language: "ko"
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
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# MelissaJ/ProjectLucia_Hera

> dataset · [Hugging Face](https://huggingface.co/datasets/MelissaJ/ProjectLucia_Hera)

루시아 페르소나 기반 한국어 단일 턴 및 도구 호출 대화 학습용 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 high
- **작업**: [[도구 호출]] — tag_match · tags = `tool-calling` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `단일 턴 한국어 페르소나 대화 (`instruction` / `response`)` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `단일 턴 한국어 페르소나 대화 (`instruction` / `response`)` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `79` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `루시아 발렌타인' 페르소나 LoRA 학습용 한국어 데이터셋.` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `eval은 템플릿 단위로 다시 나눴다(근접 중복 군집 통째로)` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `train / eval / probe 5,495 / 322 / —` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `response` 열 p90 118자 ≈ 79 토큰 (viewer statistics, default/train)
