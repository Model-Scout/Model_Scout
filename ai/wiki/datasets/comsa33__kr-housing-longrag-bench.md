---
type: "dataset"
id: "comsa33/kr-housing-longrag-bench"
source: "huggingface"
url: "https://huggingface.co/datasets/comsa33/kr-housing-longrag-bench"
downloads: 205
summary: "KR-Housing-LongRAG-Bench는 한국 공공주택 관련 공식 공고, 표 데이터, 법률 증거를 활용한 장문 LLM 및 RAG 평가용 벤치마크입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[질의응답]]"
  - "[[리랭킹]]"
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
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[행정·민원]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# comsa33/kr-housing-longrag-bench

> dataset · [Hugging Face](https://huggingface.co/datasets/comsa33/kr-housing-longrag-bench)

KR-Housing-LongRAG-Bench는 한국 공공주택 관련 공식 공고, 표 데이터, 법률 증거를 활용한 장문 LLM 및 RAG 평가용 벤치마크입니다.

## 분류

- **작업**: [[질의응답]] — metadata · readme, task_categories = `question-answering` · 신뢰도 high
- **작업**: [[리랭킹]] — ner · readme = `evaluating long-context LLMs, RAG systems, and table/tool pipelines` · 신뢰도 low
- **작업**: [[문서 검색]] — metadata · readme, tags, task_categories = `text-retrieval` · 신뢰도 high
- **작업**: [[표 질의응답]] — tag_match · tags = `table-question-answering` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — ner · modality, readme, task:table_qa = `public tabular data` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:question_answering, task:reranking, task:retrieval, task:table_qa = `no raw PDF/HWP/HWPX documents, extracted document text, bundle text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering, task:table_qa = `The `data/*.jsonl` QA files are byte-identical to v0.9.1; the gold changes are published only in `gold_fixes`.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `173` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[행정·민원]] — ner · readme = `Korean public-housing benchmark for evaluating long-context LLMs, RAG systems, and table/tool pipelines on official housing announcements, public tabular data, ` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · dataset_id/tags, readme = `KR-Housing-LongRAG-Bench is a Korean public-housing benchmark for evaluating long-context LLMs, RAG systems, and table/tool pipelines` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `note` 열 p90 259자 ≈ 173 토큰 (viewer statistics, errata/errata)
