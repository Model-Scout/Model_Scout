---
type: "dataset"
id: "CohereLabs/m-WildVision"
source: "huggingface"
url: "https://huggingface.co/datasets/CohereLabs/m-WildVision"
downloads: 523
summary: "23개 언어로 번역된 멀티모달 LLM 평가용 데이터셋으로, 시각-언어 모델의 다국어 일반화 평가에 사용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[질의응답]]"
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
  - "[[중규모 데이터]]"
---
# CohereLabs/m-WildVision

> dataset · [Hugging Face](https://huggingface.co/datasets/CohereLabs/m-WildVision)

23개 언어로 번역된 멀티모달 LLM 평가용 데이터셋으로, 시각-언어 모델의 다국어 일반화 평가에 사용됨.

## 분류

- **작업**: [[질의응답]] — ner · readme = `500 challenging user queries sourced from the WildVision-Arena platform` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · modality, readme = `image: The raw image data in .jpg format` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:question_answering = `instruction: text of the prompt (question or instruction)` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `instruction: text of the prompt (question or instruction)` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `23 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `48` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `multilingual multimodal LLM evaluation set covering 23 languages` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `LLM evaluation set` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `instruction` 열 p90 193자 ≈ 48 토큰 (viewer statistics, kor_Hang/test)

## 같은 데이터의 사본·중복 등록

- `kaggle/cohereforai/m-wildvision`
