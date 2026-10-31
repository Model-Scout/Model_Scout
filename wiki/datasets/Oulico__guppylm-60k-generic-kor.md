---
type: "dataset"
id: "Oulico/guppylm-60k-generic-kor"
source: "huggingface"
url: "https://huggingface.co/datasets/Oulico/guppylm-60k-generic-kor"
downloads: 35
summary: "한국어로 현지화된 GuppyLM의 6만 건 단일 대화 데이터셋으로, 작은 물고기 캐릭터와의 대화용입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# Oulico/guppylm-60k-generic-kor

> dataset · [Hugging Face](https://huggingface.co/datasets/Oulico/guppylm-60k-generic-kor)

한국어로 현지화된 GuppyLM의 6만 건 단일 대화 데이터셋으로, 작은 물고기 캐릭터와의 대화용입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `| `input` | string | 사용자 메시지 |` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `| `output` | string | 구피의 응답 |` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `54` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Guppy speaks in short, casual sentences about water, food, light, and tank life.` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `optimized-parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `output` 열 p90 81자 ≈ 54 토큰 (viewer statistics, default/test)
