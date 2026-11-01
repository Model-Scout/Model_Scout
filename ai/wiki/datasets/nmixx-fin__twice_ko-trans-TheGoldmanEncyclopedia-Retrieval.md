---
type: "dataset"
id: "nmixx-fin/twice_ko-trans-TheGoldmanEncyclopedia-Retrieval"
source: "huggingface"
url: "https://huggingface.co/datasets/nmixx-fin/twice_ko-trans-TheGoldmanEncyclopedia-Retrieval"
downloads: 24
summary: "FinanceMTEB/TheGoldmanEncyclopedia-en의 한국어 번역 데이터로 금융 분야 문서 검색에 활용됨."
readme_status: "ok"
readme_language: "en"
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
  - "[[이용 조건 미확인]]"
domain:
  - "[[금융·경제]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# nmixx-fin/twice_ko-trans-TheGoldmanEncyclopedia-Retrieval

> dataset · [Hugging Face](https://huggingface.co/datasets/nmixx-fin/twice_ko-trans-TheGoldmanEncyclopedia-Retrieval)

FinanceMTEB/TheGoldmanEncyclopedia-en의 한국어 번역 데이터로 금융 분야 문서 검색에 활용됨.

## 분류

- **작업**: [[문서 검색]] — ner · readme = `The Korean translation of FinanceMTEB/TheGoldmanEncyclopedia-en` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:retrieval = `The Korean translation of FinanceMTEB/TheGoldmanEncyclopedia-en` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `The Korean translation of FinanceMTEB/TheGoldmanEncyclopedia-en` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `147` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[금융·경제]] — tag_match · readme, tags = `finance` · 신뢰도 medium
- **데이터 용도**: [[평가용]] — name_rule · dataset_id/tags = `evaluation` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 220자 ≈ 147 토큰 (viewer statistics, default/train)
