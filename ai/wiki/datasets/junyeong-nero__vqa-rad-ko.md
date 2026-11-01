---
type: "dataset"
id: "junyeong-nero/vqa-rad-ko"
source: "huggingface"
url: "https://huggingface.co/datasets/junyeong-nero/vqa-rad-ko"
downloads: 35
summary: "의료 영상과 한국어 질문-답변으로 구성된 의료 VQA 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[이미지 이해]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[의료·보건]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# junyeong-nero/vqa-rad-ko

> dataset · [Hugging Face](https://huggingface.co/datasets/junyeong-nero/vqa-rad-ko)

의료 영상과 한국어 질문-답변으로 구성된 의료 VQA 데이터셋입니다.

## 분류

- **작업**: [[이미지 이해]] — metadata · readme, task_categories = `image-to-text` · 신뢰도 high
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · modality, readme, task:visual_qa = `- name: image
dtype: image` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:visual_qa = `- name: question_ko
dtype: string` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:visual_qa = `- name: answer_ko
dtype: string` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `40` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[의료·보건]] — tag_match · readme, tags = `medical` · 신뢰도 medium
- **데이터 용도**: [[평가용]] — ner · readme = `- name: test
num_bytes: 23850090
num_examples: 451` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `- name: train
num_bytes: 95350706.976
num_examples: 1793` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `question` 열 p90 59자 ≈ 40 토큰 (viewer statistics, default/test)
