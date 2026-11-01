---
type: "dataset"
id: "blueapple8259/TinyStories-korean-edu"
source: "huggingface"
url: "https://huggingface.co/datasets/blueapple8259/TinyStories-korean-edu"
downloads: 19
summary: "TinyStories와 TinyStories-Korean, fineweb-edu-classifier를 이용해 만든 교육용 한국어 데이터셋입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[교육]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# blueapple8259/TinyStories-korean-edu

> dataset · [Hugging Face](https://huggingface.co/datasets/blueapple8259/TinyStories-korean-edu)

TinyStories와 TinyStories-Korean, fineweb-edu-classifier를 이용해 만든 교육용 한국어 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `fineweb-edu-classifier로 평가를 한 뒤 int_score가 3 이상이면` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:generation = `TinyStories를 fineweb-edu-classifier로 평가` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `int_score가 3 이상이면 이에 해당되는 TinyStories-Korean을 데이터에 추가하는 방식` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `537` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cdla-sharing-1.0` · 신뢰도 high
- **도메인**: [[교육]] — ner · readme = `fineweb-edu-classifier` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `만든 데이터입니다` · 신뢰도 low
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 805자 ≈ 537 토큰 (viewer statistics, default/train)
