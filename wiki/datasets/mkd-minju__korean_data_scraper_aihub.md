---
type: "dataset"
id: "mkd-minju/korean_data_scraper_aihub"
source: "huggingface"
url: "https://huggingface.co/datasets/mkd-minju/korean_data_scraper_aihub"
downloads: 443
summary: "AI-Hub에서 수집한 여러 한국어 데이터셋의 본문 텍스트를 추출한 코퍼스입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
  - "[[문서 검색]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[극장문]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[뉴스·미디어]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# mkd-minju/korean_data_scraper_aihub

> dataset · [Hugging Face](https://huggingface.co/datasets/mkd-minju/korean_data_scraper_aihub)

AI-Hub에서 수집한 여러 한국어 데이터셋의 본문 텍스트를 추출한 코퍼스입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `국립정보화진흥원 AI-Hub(aihub.or.kr)에서 내려받은 여러 데이터셋의 로컬 zip 압축 파일을 압축 해제하고, 그 안의 json 파일에서 본문 텍스트를 추출한 결과입니다.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:retrieval = `그 안의 json 파일에서 본문 텍스트를 추출한 결과입니다.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `그 안의 json 파일에서 본문 텍스트를 추출한 결과입니다.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[극장문]] — viewer_stats · viewer_statistics = `146470` · 신뢰도 medium
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[뉴스·미디어]] — ner · readme = `샘플로 확인한 내용 중에는 뉴스 기사(신문기사) 카테고리의 AI-Hub 데이터셋에서 추출된 텍스트가 포함되어 있습니다.` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `Korean_data_scraper 프로젝트의 aihub_local 소스가 생성한 코퍼스입니다.` · 신뢰도 low
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 219705자 ≈ 146470 토큰 (viewer statistics, default/train)
