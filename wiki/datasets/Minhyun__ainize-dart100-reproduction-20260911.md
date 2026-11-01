---
type: "dataset"
id: "Minhyun/ainize-dart100-reproduction-20260911"
source: "huggingface"
url: "https://huggingface.co/datasets/Minhyun/ainize-dart100-reproduction-20260911"
downloads: 11
summary: "금융감독원 오픈 DART 기반 100개 태스크 구성 데이터셋으로 질의응답 학습용임"
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[질의응답]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[금융·경제]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# Minhyun/ainize-dart100-reproduction-20260911

> dataset · [Hugging Face](https://huggingface.co/datasets/Minhyun/ainize-dart100-reproduction-20260911)

금융감독원 오픈 DART 기반 100개 태스크 구성 데이터셋으로 질의응답 학습용임

## 분류

- **작업**: [[질의응답]] — tag_match · readme, tags = `question-answering` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:question_answering = `The train split contains the question/answer records` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `The train split contains the question/answer records` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[금융·경제]] — ner · readme = `Source: Financial Supervisory Service Open DART, https://opendart.fss.or.kr/.` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `The train split contains the question/answer records used by Ainize.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high
