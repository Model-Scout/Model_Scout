---
type: "dataset"
id: "0xDing/wikipedia-cn-20230720-filtered"
source: "huggingface"
url: "https://huggingface.co/datasets/0xDing/wikipedia-cn-20230720-filtered"
downloads: 3756
summary: "중국 대륙 지역 맞춤어로 정제한 2023년 7월 20일자 중국어 위키피디아 고품질 문서 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 생성]]"
  - "[[언어 모델링]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[중국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# 0xDing/wikipedia-cn-20230720-filtered

> dataset · [Hugging Face](https://huggingface.co/datasets/0xDing/wikipedia-cn-20230720-filtered)

중국 대륙 지역 맞춤어로 정제한 2023년 7월 20일자 중국어 위키피디아 고품질 문서 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[언어 모델링]] — ner · readme = `本数据集基于中文维基2023年7月20日的dump存档。作为一项以数据为中心的工作，本数据集仅保留了 254,547条 质量较高的词条内容。` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:language_modeling = `本数据集基于中文维基2023年7月20日的dump存档。` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:language_modeling = `本数据集基于中文维基2023年7月20日的dump存档。` · 신뢰도 medium
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `1921` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-3.0` · 신뢰도 high
- **도메인**: [[일반]] — tag_match · readme, tags = `wikipedia` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `作为一项以数据为中心的工作，本数据集仅保留了 254,547条 质量较高的词条内容。` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `completion` 열 p90 7683자 ≈ 1921 토큰 (viewer statistics, default/train)

## 이 데이터로 학습한 모델

- [[Q1ngMang__LFM2.5-350M-PT-zh_CN|Q1ngMang/LFM2.5-350M-PT-zh_CN]]
