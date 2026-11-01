---
type: "dataset"
id: "bong-9/terminal-bench-task-changelog"
source: "huggingface"
url: "https://huggingface.co/datasets/bong-9/terminal-bench-task-changelog"
downloads: 131
summary: "Terminal-Bench의 모든 작업 변경 내역과 이유, 관련 커밋 및 이슈를 기록한 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[문서 검색]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
  - "[[서비스 데이터]]"
data_format:
  - "[[CSV]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# bong-9/terminal-bench-task-changelog

> dataset · [Hugging Face](https://huggingface.co/datasets/bong-9/terminal-bench-task-changelog)

Terminal-Bench의 모든 작업 변경 내역과 이유, 관련 커밋 및 이슈를 기록한 데이터셋입니다.

## 분류

- **작업**: [[문서 검색]] — ner · readme = `Every task in every Terminal-Bench version, what changed between versions, and why, with a link to the commit, pull request or issue that shows it.` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:retrieval = `Every task in every Terminal-Bench version, what changed between versions, and why, with a link to the commit, pull request or issue that shows it.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `Every task in every Terminal-Bench version, what changed between versions, and why, with a link to the commit, pull request or issue that shows it.` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `130` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Every task in every Terminal-Bench version, what changed between versions, and why, with a link to the commit, pull request or issue that shows it.` · 신뢰도 low
- **데이터 용도**: [[평가용]] — name_rule · dataset_id/tags = `evaluation` · 신뢰도 medium
- **데이터 용도**: [[서비스 데이터]] — ner · readme = `Every task in every Terminal-Bench version, what changed between versions, and why, with a link to the commit, pull request or issue that shows it.` · 신뢰도 low
- **데이터 형식**: [[CSV]] — metadata · format = `csv` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `problem_en` 열 p90 194자 ≈ 130 토큰 (viewer statistics, changes/train)
