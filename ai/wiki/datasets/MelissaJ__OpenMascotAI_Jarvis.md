---
type: "dataset"
id: "MelissaJ/OpenMascotAI_Jarvis"
source: "huggingface"
url: "https://huggingface.co/datasets/MelissaJ/OpenMascotAI_Jarvis"
downloads: 55
summary: "OpenMascotAI Jarvis는 페르소나 없는 한국어 도구 호출 대화 데이터셋으로, LLM의 도구 호출 학습용입니다."
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
  - "[[중문]]"
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
# MelissaJ/OpenMascotAI_Jarvis

> dataset · [Hugging Face](https://huggingface.co/datasets/MelissaJ/OpenMascotAI_Jarvis)

OpenMascotAI Jarvis는 페르소나 없는 한국어 도구 호출 대화 데이터셋으로, LLM의 도구 호출 학습용입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[도구 호출]] — tag_match · readme, tags = `tool-calling` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `system(페르소나·활동 줄·인적 정보 블록·기억 블록·[자비스 모드]·[웹 검색]), 마지막 user만 [참고 정보] 래퍼` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation = `text` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `3439` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `한국어 function-calling 데이터셋` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `eval은 템플릿 단위로 다시 나눴다` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `tools` 열 p90 5159자 ≈ 3439 토큰 (viewer statistics, tools/train)
