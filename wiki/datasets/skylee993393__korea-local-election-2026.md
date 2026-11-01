---
type: "dataset"
id: "skylee993393/korea-local-election-2026"
source: "huggingface"
url: "https://huggingface.co/datasets/skylee993393/korea-local-election-2026"
downloads: 43
summary: "9회 전국동시지방선거 후보자 정보를 수집·정제한 데이터셋으로 후보자 조회·비교에 활용됨."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
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
  - "[[조건부 이용]]"
domain:
  - "[[행정·민원]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# skylee993393/korea-local-election-2026

> dataset · [Hugging Face](https://huggingface.co/datasets/skylee993393/korea-local-election-2026)

9회 전국동시지방선거 후보자 정보를 수집·정제한 데이터셋으로 후보자 조회·비교에 활용됨.

## 분류

- **작업**: [[문서 검색]] — ner · readme = `유권자가 자기 지역구 후보 정보를 손쉽게 조회·비교할 수 있도록 제공된다.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:retrieval = `후보자 정보, 선거공약 정보, 코드 정보` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `유권자가 자기 지역구 후보 정보를 손쉽게 조회·비교할 수 있도록 제공된다.` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `318` · 신뢰도 medium
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[행정·민원]] — ner · readme = `대한민국 제9회 전국동시지방선거 후보자 정보를 중앙선거관리위원회 공식 데이터에서 수집·정제한 데이터셋.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `본 데이터셋만으로도 분석·연구에 사용 가능하지만, MCP 서버를 통한 Claude·Cursor·Cline 등 AI 클라이언트 연동이 권장된다.` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `optimized-parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `raw_json` 열 p90 477자 ≈ 318 토큰 (viewer statistics, default/all)
