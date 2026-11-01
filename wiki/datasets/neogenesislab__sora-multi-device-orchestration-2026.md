---
type: "dataset"
id: "neogenesislab/sora-multi-device-orchestration-2026"
source: "huggingface"
url: "https://huggingface.co/datasets/neogenesislab/sora-multi-device-orchestration-2026"
downloads: 66
summary: "Sora Multi-Device Orchestration Architecture 2026은 1인 운영자가 여러 디바이스를 하나의 AI 코어로 통합 운영하는 reference 아키텍처 SSOT 코퍼스다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
  - "[[텍스트 생성]]"
input_modality:
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
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# neogenesislab/sora-multi-device-orchestration-2026

> dataset · [Hugging Face](https://huggingface.co/datasets/neogenesislab/sora-multi-device-orchestration-2026)

Sora Multi-Device Orchestration Architecture 2026은 1인 운영자가 여러 디바이스를 하나의 AI 코어로 통합 운영하는 reference 아키텍처 SSOT 코퍼스다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories = `text-classification` · 신뢰도 medium
- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:classification, task:generation = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `train or fine-tune routing agents on which device tier should host which capability` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `454` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **데이터 용도**: [[평가용]] — ner · readme = `suitable as ground-truth for incident-response retrieval evaluation` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `train or fine-tune routing agents` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

샘플 길이: `section_text` 열 p90 681자 ≈ 454 토큰 (viewer statistics, default/train)
