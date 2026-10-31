---
type: "dataset"
id: "seoulraphaellee/korean-assembly-minutes"
source: "huggingface"
url: "https://huggingface.co/datasets/seoulraphaellee/korean-assembly-minutes"
downloads: 2478
summary: "대한민국 국회 회의록 원문과 AI 요약을 연도별로 모은 아카이브 데이터셋입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
  - "[[문서 검색]]"
  - "[[요약]]"
input_modality:
  - "[[문서 파일 (입력 형식)|문서 파일]]"
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[초장문]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[행정·민원]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# seoulraphaellee/korean-assembly-minutes

> dataset · [Hugging Face](https://huggingface.co/datasets/seoulraphaellee/korean-assembly-minutes)

대한민국 국회 회의록 원문과 AI 요약을 연도별로 모은 아카이브 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `국회 회의록 원문(record.assembly.go.kr) PDF 에서 본문을 뽑아 모은 것이다.` · 신뢰도 low
- **작업**: [[요약]] — metadata · readme, task_categories = `summarization` · 신뢰도 high
- **입력 형식**: [[문서 파일 (입력 형식)|문서 파일]] — ner · readme = `국회 회의록 원문(record.assembly.go.kr) PDF 에서 본문을 뽑아 모은 것이다.` · 신뢰도 medium
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:retrieval, task:summarization = `회의록 본문, 연도별` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:summarization = `회의록 본문, 연도별` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[초장문]] — viewer_stats · viewer_statistics = `104002` · 신뢰도 medium
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[행정·민원]] — tag_match · readme, tags = `government` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `ds = load_dataset("seoulraphaellee/korean-assembly-minutes", split="train")` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 156003자 ≈ 104002 토큰 (viewer statistics, default/train)
