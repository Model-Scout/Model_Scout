---
type: "dataset"
id: "google/wit"
source: "huggingface"
url: "https://huggingface.co/datasets/google/wit"
downloads: 328
summary: "WIT는 108개 언어의 1,150만 이미지와 텍스트 예제로 구성된 대규모 다중언어 멀티모달 데이터셋입니다."
readme_status: "template"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[임베딩]]"
  - "[[언어 모델링]]"
  - "[[문서 검색]]"
  - "[[이미지 이해]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# google/wit

> dataset · [Hugging Face](https://huggingface.co/datasets/google/wit)

WIT는 108개 언어의 1,150만 이미지와 텍스트 예제로 구성된 대규모 다중언어 멀티모달 데이터셋입니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `multimodal machine learning models` · 신뢰도 low
- **작업**: [[언어 모델링]] — ner · readme = `pretraining dataset for multimodal machine learning models` · 신뢰도 low
- **작업**: [[문서 검색]] — metadata · task_categories = `text-retrieval` · 신뢰도 low
- **작업**: [[이미지 이해]] — metadata · task_categories, task_ids = `image-to-text` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · modality, readme, task:visual_qa = `entity rich image-text examples` · 신뢰도 high
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:embedding, task:language_modeling, task:retrieval, task:visual_qa = `entity rich image-text examples` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:language_modeling, task:visual_qa = `entity rich image-text examples` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `58 languages` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `590` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-3.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Wikipedia-based Image Text (WIT) Dataset is a large multimodal multilingual dataset.` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `Its size enables WIT to be used as a pretraining dataset for multimodal machine learning models.` · 신뢰도 medium
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high

샘플 길이: `context_section_description` 열 p90 2359자 ≈ 590 토큰 (viewer statistics, default/train)
