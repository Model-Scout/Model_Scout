---
type: "dataset"
id: "Minbyul/Ko-widesearch"
source: "huggingface"
url: "https://huggingface.co/datasets/Minbyul/Ko-widesearch"
downloads: 142
summary: "Ko-WideSearch는 한국어 웹 에이전트를 위한 광범위 탐색 벤치마크로, 표의 모든 속성 셀을 채우는 작업을 포함합니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[질의응답]]"
  - "[[문서 검색]]"
  - "[[표 질의응답]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
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
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# Minbyul/Ko-widesearch

> dataset · [Hugging Face](https://huggingface.co/datasets/Minbyul/Ko-widesearch)

Ko-WideSearch는 한국어 웹 에이전트를 위한 광범위 탐색 벤치마크로, 표의 모든 속성 셀을 채우는 작업을 포함합니다.

## 분류

- **작업**: [[질의응답]] — metadata · task_categories = `question-answering` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `each task asks a web agent to exhaustively enumerate a closed set and fill every attribute cell of a table` · 신뢰도 low
- **작업**: [[표 질의응답]] — metadata · readme, task_categories = `table-question-answering` · 신뢰도 medium
- **입력 형식**: [[표 (입력 형식)|표]] — task_rule · task:table_qa = `table` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:question_answering, task:retrieval, task:table_qa = `The question and answer fields are encrypted` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering, task:table_qa = `The expected output for each question is a single markdown table whose columns are the decrypted `columns`` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `3550` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `A Korean breadth-search benchmark` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `To keep this a fair, leakage-aware test of web agents, the gold is not published as plain text` · 신뢰도 low
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

샘플 길이: `answer` 열 p90 5324자 ≈ 3550 토큰 (viewer statistics, default/easy)
