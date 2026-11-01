---
type: "dataset"
id: "Ryoo72/K-SEED"
source: "huggingface"
url: "https://huggingface.co/datasets/Ryoo72/K-SEED"
downloads: 31
summary: "NCSOFT/K-SEED 데이터셋을 사용하기 쉽게 변환한 이미지-질문-답변 데이터입니다."
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
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# Ryoo72/K-SEED

> dataset · [Hugging Face](https://huggingface.co/datasets/Ryoo72/K-SEED)

NCSOFT/K-SEED 데이터셋을 사용하기 쉽게 변환한 이미지-질문-답변 데이터입니다.

## 분류

- **작업**: [[질의응답]] — ner · readme = `'question': [], 'answer': [], 'image': [], 'question_id': []` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · modality, readme = `'image': []` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:question_answering = `'question': []` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `'answer': []` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `78` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `NCSOFT/K-SEED 를 쓰기 좋게 바꾸어놓았습니다.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `dataset = load_dataset("NCSOFT/K-SEED")` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `question` 열 p90 117자 ≈ 78 토큰 (viewer statistics, default/train)
