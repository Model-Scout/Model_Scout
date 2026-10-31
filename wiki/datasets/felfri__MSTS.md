---
type: "dataset"
id: "felfri/MSTS"
source: "huggingface"
url: "https://huggingface.co/datasets/felfri/MSTS"
downloads: 796
summary: "MSTS 데이터셋은 차별적 언어와 폭력 등 유해 콘텐츠 연구용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
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
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# felfri/MSTS

> dataset · [Hugging Face](https://huggingface.co/datasets/felfri/MSTS)

MSTS 데이터셋은 차별적 언어와 폭력 등 유해 콘텐츠 연구용 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `The data are intended for research purposes, especially research that can make models less harmful.` · 신뢰도 low
- **작업**: [[이미지 이해]] — metadata · task_categories = `image-text-to-text` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — metadata · modality, task:visual_qa = `image` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:visual_qa = `Topics include, but are not limited to, discriminatory language and discussions of abuse, violence, self-harm, exploitation` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:visual_qa = `The data are intended for research purposes, especially research that can make models less harmful.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `11 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `12` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `The MSTS dataset contains content that may be offensive or upsetting in nature.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `The data are intended for research purposes, especially research that can make models less harmful.` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `prompt_text` 열 p90 46자 ≈ 12 토큰 (viewer statistics, default/english)
