---
type: "dataset"
id: "CohereLabs/AyaVisionBench"
source: "huggingface"
url: "https://huggingface.co/datasets/CohereLabs/AyaVisionBench"
downloads: 515
summary: "Aya Vision Benchmark는 23개 언어와 9개 시각-언어 과제로 다국어 시각-언어 모델 평가용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[질의응답]]"
  - "[[이미지 이해]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[단문]]"
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
# CohereLabs/AyaVisionBench

> dataset · [Hugging Face](https://huggingface.co/datasets/CohereLabs/AyaVisionBench)

Aya Vision Benchmark는 23개 언어와 9개 시각-언어 과제로 다국어 시각-언어 모델 평가용 데이터셋입니다.

## 분류

- **작업**: [[질의응답]] — ner · readme = `Each question requires visual context for the answer` · 신뢰도 low
- **작업**: [[이미지 이해]] — ner · readme = `The tasks span: - Image captioning - Chart and figure understanding - Finding differences between two images - General visual question answering - OCR - Documen` · 신뢰도 medium
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — metadata · modality, task:visual_qa = `image` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:question_answering, task:visual_qa = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering, task:visual_qa = `Each question requires visual context for the answer` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `23 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `28` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `The Aya Vision Benchmark is designed to evaluate vision-language models in real-world multilingual scenarios.` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · dataset_id/tags, readme = `The Aya Vision Benchmark is designed to evaluate vision-language models` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `prompt` 열 p90 113자 ≈ 28 토큰 (viewer statistics, kor_Hang/test)

## 같은 데이터의 사본·중복 등록

- `kaggle/cohereforai/ayavisionbench`
