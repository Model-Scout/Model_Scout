---
type: "dataset"
id: "ispras-crawlers/newsxlm-mhtml"
source: "huggingface"
url: "https://huggingface.co/datasets/ispras-crawlers/newsxlm-mhtml"
downloads: 163
summary: "NewsXLM 데이터셋을 위한 MHTML 웹페이지 스냅샷 데이터입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[문서 검색]]"
input_modality:
  - "[[문서 파일 (입력 형식)|문서 파일]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
language:
  - "[[ar]]"
  - "[[de]]"
  - "[[영어]]"
  - "[[es]]"
  - "[[fr]]"
  - "[[hr]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[pt]]"
  - "[[ru]]"
  - "[[중국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[일반]]"
  - "[[뉴스·미디어]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# ispras-crawlers/newsxlm-mhtml

> dataset · [Hugging Face](https://huggingface.co/datasets/ispras-crawlers/newsxlm-mhtml)

NewsXLM 데이터셋을 위한 MHTML 웹페이지 스냅샷 데이터입니다.

## 분류

- **작업**: [[문서 검색]] — ner · readme = `MHTML snapshots of pages where wtl-uid and wtl-parent-uid attributes have been added to every element in <body>, following the WTL algorithm.` · 신뢰도 low
- **입력 형식**: [[문서 파일 (입력 형식)|문서 파일]] — ner · readme = `MHTML snapshots of pages` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:retrieval = `text` · 신뢰도 high
- **언어**: [[ar]] — metadata · languages = `ar` · 신뢰도 high
- **언어**: [[de]] — metadata · languages = `de` · 신뢰도 high
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[es]] — metadata · languages = `es` · 신뢰도 high
- **언어**: [[fr]] — metadata · languages = `fr` · 신뢰도 high
- **언어**: [[hr]] — metadata · languages = `hr` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `10 languages` · 신뢰도 high
- **언어**: [[pt]] — metadata · languages = `pt` · 신뢰도 high
- **언어**: [[ru]] — metadata · languages = `ru` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `9` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[일반]] — tag_match · tags = `web` · 신뢰도 medium
- **도메인**: [[뉴스·미디어]] — tag_match · readme, tags = `news` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `MHTML Sources for NewsXLM dataset` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `optimized-parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `uuid` 열 p90 36자 ≈ 9 토큰 (viewer statistics, default/train)
