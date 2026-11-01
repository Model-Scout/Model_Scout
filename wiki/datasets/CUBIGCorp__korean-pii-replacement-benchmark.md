---
type: "dataset"
id: "CUBIGCorp/korean-pii-replacement-benchmark"
source: "huggingface"
url: "https://huggingface.co/datasets/CUBIGCorp/korean-pii-replacement-benchmark"
downloads: 113
summary: "한국어 개인정보 식별자(PII) 대체 방식이 LLM의 식별자 추출 능력에 미치는 영향을 평가하는 벤치마크 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[정보 추출]]"
  - "[[질의응답]]"
  - "[[문서 검색]]"
input_modality:
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
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# CUBIGCorp/korean-pii-replacement-benchmark

> dataset · [Hugging Face](https://huggingface.co/datasets/CUBIGCorp/korean-pii-replacement-benchmark)

한국어 개인정보 식별자(PII) 대체 방식이 LLM의 식별자 추출 능력에 미치는 영향을 평가하는 벤치마크 데이터셋입니다.

## 분류

- **작업**: [[정보 추출]] — ner · readme = `Each item has two questions evaluated under four conditions.` · 신뢰도 low
- **작업**: [[질의응답]] — metadata · task_categories = `question-answering` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `This benchmark measures how the form of replacement affects an LLM's ability to look up and extract identifiers from Korean text.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:information_extraction, task:question_answering, task:retrieval = `This benchmark measures how the form of replacement affects an LLM's ability to look up and extract identifiers from Korean text.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `Each item has two questions evaluated under four conditions.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `328` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `This benchmark measures how the form of replacement affects an LLM's ability to look up and extract identifiers from Korean text.` · 신뢰도 low
- **데이터 용도**: [[평가용]] — name_rule · dataset_id/tags = `evaluation` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `text_hash` 열 p90 492자 ≈ 328 토큰 (viewer statistics, all/test)
