---
type: "dataset"
id: "junyeong-nero/kin_med_2M_filtered"
source: "huggingface"
url: "https://huggingface.co/datasets/junyeong-nero/kin_med_2M_filtered"
downloads: 70
summary: "mncai/kin_med_2M 데이터셋을 필터링한 의료 데이터셋으로, instruction, input, output 포함."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[의료·보건]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# junyeong-nero/kin_med_2M_filtered

> dataset · [Hugging Face](https://huggingface.co/datasets/junyeong-nero/kin_med_2M_filtered)

mncai/kin_med_2M 데이터셋을 필터링한 의료 데이터셋으로, instruction, input, output 포함.

## 분류

- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality = `text` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `821` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[의료·보건]] — ner · readme = `This dataset is a filtered dataset of the mncai/kin_med_2M dataset.` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `output` 열 p90 1231자 ≈ 821 토큰 (viewer statistics, default/train)
