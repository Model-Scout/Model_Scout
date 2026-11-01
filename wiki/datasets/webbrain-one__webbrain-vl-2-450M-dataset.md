---
type: "dataset"
id: "webbrain-one/webbrain-vl-2-450M-dataset"
source: "huggingface"
url: "https://huggingface.co/datasets/webbrain-one/webbrain-vl-2-450M-dataset"
downloads: 645
summary: "웹브레인 VL 2 450M 데이터셋은 브라우저 스크린샷과 여섯 섹션 설명을 매칭한 스크린샷-설명 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 생성]]"
  - "[[이미지 이해]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[ar]]"
  - "[[de]]"
  - "[[영어]]"
  - "[[es]]"
  - "[[fr]]"
  - "[[일본어]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[tr]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# webbrain-one/webbrain-vl-2-450M-dataset

> dataset · [Hugging Face](https://huggingface.co/datasets/webbrain-one/webbrain-vl-2-450M-dataset)

웹브레인 VL 2 450M 데이터셋은 브라우저 스크린샷과 여섯 섹션 설명을 매칭한 스크린샷-설명 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `It is a screenshot-to-description dataset.` · 신뢰도 low
- **작업**: [[이미지 이해]] — metadata · task_categories = `image-to-text` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · modality, readme, task:visual_qa = `50,000 browser viewport screenshots` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:generation, task:visual_qa = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:visual_qa = `one six-section text observation out` · 신뢰도 medium
- **언어**: [[ar]] — metadata · languages = `ar` · 신뢰도 high
- **언어**: [[de]] — metadata · languages = `de` · 신뢰도 high
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[es]] — metadata · languages = `es` · 신뢰도 high
- **언어**: [[fr]] — metadata · languages = `fr` · 신뢰도 high
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `8 languages` · 신뢰도 high
- **언어**: [[tr]] — metadata · languages = `tr` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `647` · 신뢰도 medium
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `It is a screenshot-to-description dataset.` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `messages_json` 열 p90 2586자 ≈ 647 토큰 (viewer statistics, default/validation)
