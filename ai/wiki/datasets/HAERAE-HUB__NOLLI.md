---
type: "dataset"
id: "HAERAE-HUB/NOLLI"
source: "huggingface"
url: "https://huggingface.co/datasets/HAERAE-HUB/NOLLI"
downloads: 211
summary: "NOLLI는 한국어와 영어로 된 난이도 조절 가능한 논리 퍼즐 벤치마크 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[질의응답]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# HAERAE-HUB/NOLLI

> dataset · [Hugging Face](https://huggingface.co/datasets/HAERAE-HUB/NOLLI)

NOLLI는 한국어와 영어로 된 난이도 조절 가능한 논리 퍼즐 벤치마크 데이터셋입니다.

## 분류

- **작업**: [[질의응답]] — metadata · readme, task_categories = `question-answering` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:question_answering = ``question` | str | full prompt for the model` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = ``answer` | str | gold answer` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `1471` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `NOLLI (논리) is a benchmark of rule-based logical puzzles in Korean and English` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `All configs share a single `test` split and the same schema` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `solution` 열 p90 2206자 ≈ 1471 토큰 (viewer statistics, korean_units/test)
