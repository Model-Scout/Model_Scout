---
type: "dataset"
id: "phnyxlab/klue-nli-simcse"
source: "huggingface"
url: "https://huggingface.co/datasets/phnyxlab/klue-nli-simcse"
downloads: 26
summary: "KLUENLI 데이터셋을 SimCSE 대비 학습용으로 변환한 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[임베딩]]"
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
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# phnyxlab/klue-nli-simcse

> dataset · [Hugging Face](https://huggingface.co/datasets/phnyxlab/klue-nli-simcse)

KLUENLI 데이터셋을 SimCSE 대비 학습용으로 변환한 데이터셋입니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `This dataset was prepared by converting KLUENLI dataset to use it for contrastive training (SimCSE)` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:embedding = `This dataset was prepared by converting KLUENLI dataset to use it for contrastive training (SimCSE)` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `This dataset was prepared by converting KLUENLI dataset to use it for contrastive training (SimCSE)` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `51` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `This dataset was prepared by converting KLUENLI dataset to use it for contrastive training (SimCSE)` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `premise` 열 p90 77자 ≈ 51 토큰 (viewer statistics, default/validation)
