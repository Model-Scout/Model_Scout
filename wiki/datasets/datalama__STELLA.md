---
type: "dataset"
id: "datalama/STELLA"
source: "huggingface"
url: "https://huggingface.co/datasets/datalama/STELLA"
downloads: 59
summary: "NASA NTRS 문서 기반 항공우주 도메인 다국어 정보검색 벤치마크 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[문서 검색]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[fr]]"
  - "[[id]]"
  - "[[일본어]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[th]]"
  - "[[중국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# datalama/STELLA

> dataset · [Hugging Face](https://huggingface.co/datasets/datalama/STELLA)

NASA NTRS 문서 기반 항공우주 도메인 다국어 정보검색 벤치마크 데이터셋입니다.

## 분류

- **작업**: [[문서 검색]] — metadata · readme, task_categories = `text-retrieval` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:retrieval = `Queries: 영어 원본 + 6개 번역 언어` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `Queries: 영어 원본 + 6개 번역 언어` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[fr]] — metadata · languages = `fr` · 신뢰도 high
- **언어**: [[id]] — metadata · languages = `id` · 신뢰도 high
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `7 languages` · 신뢰도 high
- **언어**: [[th]] — metadata · languages = `th` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `9` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `STELLA는 NASA Technical Reports Server (NTRS) 문서 기반 항공우주 도메인 Cross-lingual IR 벤치마크입니다.` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `corpus = load_dataset("datalama/STELLA", "corpus", split="test")` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high

샘플 길이: `corpus-id` 열 p90 36자 ≈ 9 토큰 (viewer statistics, ko-qrels/test)
