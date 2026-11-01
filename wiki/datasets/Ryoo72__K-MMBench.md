---
type: "dataset"
id: "Ryoo72/K-MMBench"
source: "huggingface"
url: "https://huggingface.co/datasets/Ryoo72/K-MMBench"
downloads: 26
summary: "NCSOFT/K-MMBench 데이터셋을 사용하기 쉽게 변환한 데이터입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
  - "[[질의응답]]"
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
  - "[[이용 조건 미확인]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# Ryoo72/K-MMBench

> dataset · [Hugging Face](https://huggingface.co/datasets/Ryoo72/K-MMBench)

NCSOFT/K-MMBench 데이터셋을 사용하기 쉽게 변환한 데이터입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `'answer': []` · 신뢰도 low
- **작업**: [[질의응답]] — ner · readme = `'question': []` · 신뢰도 low
- **작업**: [[이미지 이해]] — ner · readme = `'image': []` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · modality, readme, task:visual_qa = `'image': []` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:question_answering, task:visual_qa = `'question': []` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering, task:visual_qa = `'answer': []` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `221` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **데이터 용도**: [[평가용]] — name_rule · dataset_id/tags = `evaluation` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `NCSOFT/K-MMBench 를 쓰기 좋게 바꾸어놓았습니다.` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `question` 열 p90 332자 ≈ 221 토큰 (viewer statistics, default/dev)
