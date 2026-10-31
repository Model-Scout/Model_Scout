---
type: "dataset"
id: "cfpark00/KoreanSAT"
source: "huggingface"
url: "https://huggingface.co/datasets/cfpark00/KoreanSAT"
downloads: 127
summary: "KoreanSAT 벤치마크로 수학 영역의 연도별 출제 주제를 분석한 데이터입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
  - "[[질의응답]]"
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
  - "[[비상업 전용]]"
domain:
  - "[[교육]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# cfpark00/KoreanSAT

> dataset · [Hugging Face](https://huggingface.co/datasets/cfpark00/KoreanSAT)

KoreanSAT 벤치마크로 수학 영역의 연도별 출제 주제를 분석한 데이터입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `KoreanSAT Benchmark` · 신뢰도 low
- **작업**: [[질의응답]] — metadata · tags, task_categories = `question-answering` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `Current Topics over years` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:question_answering, task:retrieval = `Current Topics over years` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `Current Topics over years` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `443` · 신뢰도 medium
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-sa-4.0` · 신뢰도 high
- **도메인**: [[교육]] — ner · readme = `KoreanSAT Benchmark` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `KoreanSAT Benchmark` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

샘플 길이: `problem` 열 p90 665자 ≈ 443 토큰 (viewer statistics, default/2022_math)
