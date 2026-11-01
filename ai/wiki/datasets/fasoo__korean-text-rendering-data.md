---
type: "dataset"
id: "fasoo/korean-text-rendering-data"
source: "huggingface"
url: "https://huggingface.co/datasets/fasoo/korean-text-rendering-data"
downloads: 2392
summary: "한글 텍스트를 정확히 렌더링하기 위한 합성 이미지-프롬프트 학습 데이터셋입니다."
readme_status: "ok"
readme_language: "ko"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
  - "[[이미지 생성]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[이미지 (출력 형식)|이미지]]"
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# fasoo/korean-text-rendering-data

> dataset · [Hugging Face](https://huggingface.co/datasets/fasoo/korean-text-rendering-data)

한글 텍스트를 정확히 렌더링하기 위한 합성 이미지-프롬프트 학습 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `이미지 안에 정확한 한글 텍스트를 렌더링하는 능력 개선을 위해 만들어진 합성(synthetic) 이미지-프롬프트 데이터셋입니다.` · 신뢰도 low
- **작업**: [[이미지 생성]] — tag_match · tags = `text-to-image` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · modality, readme, task:image_generation = `총 79,460장, 2개 config(콘텐츠 유형)로 구성.` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:image_generation = `이미지 생성에 사용된 전체 프롬프트 (텍스트 인코더 입력)` · 신뢰도 high
- **출력 형식**: [[이미지 (출력 형식)|이미지]] — ner · readme, task:image_generation = `총 79,460장, 2개 config(콘텐츠 유형)로 구성.` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation = `text` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license = `unknown` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `일반적인 text-to-image 모델은 이미지 안에 텍스트(특히 한글)를 그릴 때 글자가 깨지거나, 문맥과 무관한 글자를 생성하거나, 일부만 렌더링하는 문제가 흔합니다.` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `세 차례의 별도 학습 이터레이션에서 나온 데이터를 통합했습니다.` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
