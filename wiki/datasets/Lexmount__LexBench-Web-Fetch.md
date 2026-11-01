---
type: "dataset"
id: "Lexmount/LexBench-Web-Fetch"
source: "huggingface"
url: "https://huggingface.co/datasets/Lexmount/LexBench-Web-Fetch"
downloads: 445
summary: "LexBench-Web-Fetch는 URL에서 AI 에이전트가 필요한 콘텐츠를 반환하는지 평가하는 웹 콘텐츠 추출 벤치마크입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[문서 검색]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
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
# Lexmount/LexBench-Web-Fetch

> dataset · [Hugging Face](https://huggingface.co/datasets/Lexmount/LexBench-Web-Fetch)

LexBench-Web-Fetch는 URL에서 AI 에이전트가 필요한 콘텐츠를 반환하는지 평가하는 웹 콘텐츠 추출 벤치마크입니다.

## 분류

- **작업**: [[문서 검색]] — ner · readme = `LexBench-Web-Fetch evaluates whether a browser, extraction tool or hosted fetch service returns the content an AI agent needs from a URL.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:retrieval = `Its 430 task entries cover page bodies, structured records with usable links, resource discovery and file delivery.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `Each task declares what the returned answer must contain, so the same acceptance rules apply to every participant.` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `13 languages` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `711` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Its 430 task entries cover page bodies, structured records with usable links, resource discovery and file delivery.` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · dataset_id/tags, readme = `The viewer contains the 430 current task entries.` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

샘플 길이: `task` 열 p90 2842자 ≈ 711 토큰 (viewer statistics, access-restrictions/test)
