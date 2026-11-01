---
type: "dataset"
id: "werty1248/Magpie-Ko-Qwen2.5-Reasoning-Raw"
source: "huggingface"
url: "https://huggingface.co/datasets/werty1248/Magpie-Ko-Qwen2.5-Reasoning-Raw"
downloads: 33
summary: "한국어 다단계 추론 문제와 단계적 풀이를 포함한 Qwen 모델용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
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
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# werty1248/Magpie-Ko-Qwen2.5-Reasoning-Raw

> dataset · [Hugging Face](https://huggingface.co/datasets/werty1248/Magpie-Ko-Qwen2.5-Reasoning-Raw)

한국어 다단계 추론 문제와 단계적 풀이를 포함한 Qwen 모델용 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `question` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `answer` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `1234` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `당신은 알리바바 클라우드에서 만든 Qwen입니다. 당신은 유용한 어시스턴트입니다.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Data Generation` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `answer` 열 p90 1851자 ≈ 1234 토큰 (viewer statistics, default/train)
