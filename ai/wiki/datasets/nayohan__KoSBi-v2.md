---
type: "dataset"
id: "nayohan/KoSBi-v2"
source: "huggingface"
url: "https://huggingface.co/datasets/nayohan/KoSBi-v2"
downloads: 39
summary: "KoSBi-v2는 안전한 대형 언어 모델 적용을 위한 사회적 편향 위험 완화 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
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
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# nayohan/KoSBi-v2

> dataset · [Hugging Face](https://huggingface.co/datasets/nayohan/KoSBi-v2)

KoSBi-v2는 안전한 대형 언어 모델 적용을 위한 사회적 편향 위험 완화 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `KoSBi: A Dataset for Mitigating Social Bias Risks Towards Safer Large Language Model Application` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `KoSBi: A Dataset for Mitigating Social Bias Risks Towards Safer Large Language Model Application` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `KoSBi: A Dataset for Mitigating Social Bias Risks Towards Safer Large Language Model Application` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `72` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `KoSBi: A Dataset for Mitigating Social Bias Risks Towards Safer Large Language Model Application` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `KoSBi: A Dataset for Mitigating Social Bias Risks Towards Safer Large Language Model Application` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `sentence_en` 열 p90 107자 ≈ 72 토큰 (viewer statistics, default/test)

## 같은 데이터의 사본·중복 등록

- `nayohan/KoSBi`
