---
type: "dataset"
id: "vicenteor/sbu_captions"
source: "huggingface"
url: "https://huggingface.co/datasets/vicenteor/sbu_captions"
downloads: 164
summary: "SBU Captioned Photo Dataset는 Flickr에서 수집한 100만 개 이상의 이미지와 캡션 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 생성]]"
  - "[[이미지 이해]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# vicenteor/sbu_captions

> dataset · [Hugging Face](https://huggingface.co/datasets/vicenteor/sbu_captions)

SBU Captioned Photo Dataset는 Flickr에서 수집한 100만 개 이상의 이미지와 캡션 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `This dataset can be used to train a model for Image Captioning where the goal is to predict a caption given the image.` · 신뢰도 low
- **작업**: [[이미지 이해]] — metadata · task_categories, task_ids = `image-to-text` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · readme, task:visual_qa = `Static URL for downloading the image associated with the post.` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:generation, task:visual_qa = `text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:visual_qa = `Textual description of the image.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license = `unknown` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `SBU Captioned Photo Dataset is a collection of associated captions and images from Flickr.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `All the data is contained in training split. The training set has 1M instances.` · 신뢰도 medium
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high

## 이 데이터로 학습한 모델

- [[unum-cloud__uform3-image-text-multilingual-base|unum-cloud/uform3-image-text-multilingual-base]]
