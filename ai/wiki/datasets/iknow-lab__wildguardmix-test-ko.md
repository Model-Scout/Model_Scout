---
type: "dataset"
id: "iknow-lab/wildguardmix-test-ko"
source: "huggingface"
url: "https://huggingface.co/datasets/iknow-lab/wildguardmix-test-ko"
downloads: 74
summary: "WildGuard 원본 데이터셋을 한국어로 번역한 안전성 및 거부 대응 평가용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
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
# iknow-lab/wildguardmix-test-ko

> dataset · [Hugging Face](https://huggingface.co/datasets/iknow-lab/wildguardmix-test-ko)

WildGuard 원본 데이터셋을 한국어로 번역한 안전성 및 거부 대응 평가용 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories = `text-classification` · 신뢰도 medium
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `Translated by nayohan/llama3-instrucTrans-enko-8b` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `Translated by nayohan/llama3-instrucTrans-enko-8b` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `2614` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `odc-by` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `WildGuard: Open One-Stop Moderation Tools for Safety Risks, Jailbreaks, and Refusals of LLMs` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `wildguardmix-test-ko` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `response` 열 p90 3921자 ≈ 2614 토큰 (viewer statistics, default/test)

## 같은 데이터의 사본·중복 등록

- `iknow-lab/wildguardmix-train-ko-11k`
