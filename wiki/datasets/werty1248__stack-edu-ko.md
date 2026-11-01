---
type: "dataset"
id: "werty1248/stack-edu-ko"
source: "huggingface"
url: "https://huggingface.co/datasets/werty1248/stack-edu-ko"
downloads: 52
summary: "HuggingFaceTB/stack-edu에서 한국어가 포함된 주석, 소스코드, 문서만 추출한 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[언어 모델링]]"
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
  - "[[Parquet]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# werty1248/stack-edu-ko

> dataset · [Hugging Face](https://huggingface.co/datasets/werty1248/stack-edu-ko)

HuggingFaceTB/stack-edu에서 한국어가 포함된 주석, 소스코드, 문서만 추출한 데이터셋입니다.

## 분류

- **작업**: [[언어 모델링]] — ner · readme = `SmolLM2 토크나이저 기준 토큰 수 비교 (총 125B -> 4.1B, 마크다운 제외 시 2.1B)` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:language_modeling = `주석이나 소스코드 내부에 한국어가 포함된 경우
한국어로 작성된 문서(Markdown 등)` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:language_modeling = `주석이나 소스코드 내부에 한국어가 포함된 경우
한국어로 작성된 문서(Markdown 등)` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `22` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[교육]] — ner · readme = `werty1248/stack-edu-ko
[HuggingFaceTB/stack-edu](https://huggingface.co/datasets/HuggingFaceTB/stack-edu) 에서 한국어가 포함된 데이터만 발췌` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `SmolLM2 토크나이저 기준 토큰 수 비교 (총 125B -> 4.1B, 마크다운 제외 시 2.1B)` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high

샘플 길이: `repo_name` 열 p90 33자 ≈ 22 토큰 (viewer statistics, C/train)
