---
type: "dataset"
id: "Ryoo72/K-DTCBench"
source: "huggingface"
url: "https://huggingface.co/datasets/Ryoo72/K-DTCBench"
downloads: 29
summary: "NCSOFT/K-DTCBench 데이터셋을 사용하기 쉽게 변환한 다지선다형 질문 데이터입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[질의응답]]"
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
domain:
  - "[[교육]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# Ryoo72/K-DTCBench

> dataset · [Hugging Face](https://huggingface.co/datasets/Ryoo72/K-DTCBench)

NCSOFT/K-DTCBench 데이터셋을 사용하기 쉽게 변환한 다지선다형 질문 데이터입니다.

## 분류

- **작업**: [[질의응답]] — ner · readme = `주어진 선택지 중 해당 옵션의 문자로 직접 답하세요.` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — metadata · modality = `image` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:question_answering = `question` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `해당 옵션의 문자로 직접 답하세요.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `64` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[교육]] — ner · readme = `NCSOFT/K-DTCBench` · 신뢰도 low
- **데이터 용도**: [[평가용]] — name_rule · dataset_id/tags = `evaluation` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `아래 코드를 이용하였습니다.` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

샘플 길이: `question` 열 p90 96자 ≈ 64 토큰 (viewer statistics, default/test)
