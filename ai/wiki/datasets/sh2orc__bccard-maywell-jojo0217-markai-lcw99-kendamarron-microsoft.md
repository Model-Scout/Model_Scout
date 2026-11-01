---
type: "dataset"
id: "sh2orc/bccard-maywell-jojo0217-markai-lcw99-kendamarron-microsoft"
source: "huggingface"
url: "https://huggingface.co/datasets/sh2orc/bccard-maywell-jojo0217-markai-lcw99-kendamarron-microsoft"
downloads: 41
summary: "여러 한국어 및 영어 데이터셋을 통합한 질문응답 및 지식 학습용 데이터셋입니다."
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
input_length:
  - "[[장문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[교육]]"
  - "[[금융·경제]]"
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# sh2orc/bccard-maywell-jojo0217-markai-lcw99-kendamarron-microsoft

> dataset · [Hugging Face](https://huggingface.co/datasets/sh2orc/bccard-maywell-jojo0217-markai-lcw99-kendamarron-microsoft)

여러 한국어 및 영어 데이터셋을 통합한 질문응답 및 지식 학습용 데이터셋입니다.

## 분류

- **작업**: [[질의응답]] — ner · readme = `maywell/ko_wikidata_QA` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:question_answering = `maywell/ko_wikidata_QA` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `maywell/ko_wikidata_QA` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[장문]] — viewer_stats · viewer_statistics = `7482` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[교육]] — ner · readme = `microsoft/orca-math-word-problems-200k` · 신뢰도 low
- **도메인**: [[금융·경제]] — ner · readme = `BCCard/BCCard-Finance-Kor-QnA` · 신뢰도 medium
- **도메인**: [[일반]] — ner · readme = `maywell/ko_wikidata_QA` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `[Dataset merged]` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `[Dataset merged]` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high

샘플 길이: `output` 열 p90 11223자 ≈ 7482 토큰 (viewer statistics, default/train)
