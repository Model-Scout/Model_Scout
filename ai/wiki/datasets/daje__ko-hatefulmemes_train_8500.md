---
type: "dataset"
id: "daje/ko-hatefulmemes_train_8500"
source: "huggingface"
url: "https://huggingface.co/datasets/daje/ko-hatefulmemes_train_8500"
downloads: 29
summary: "한국어와 영어 텍스트 및 이미지를 포함한 혐오 표현 분류용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
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
# daje/ko-hatefulmemes_train_8500

> dataset · [Hugging Face](https://huggingface.co/datasets/daje/ko-hatefulmemes_train_8500)

한국어와 영어 텍스트 및 이미지를 포함한 혐오 표현 분류용 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `- name: label
  dtype:
    class_label:
      names:
      '0': '0'
      '1': '1'` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · modality, readme = `- name: image
  dtype: image` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `- name: text
  dtype: string` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `- name: label
  dtype:
    class_label:` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `76` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `- name: train
  num_bytes: 2964245922.375
  num_examples: 8197` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 114자 ≈ 76 토큰 (viewer statistics, default/train)
