---
type: "dataset"
id: "didi0di/finance-legal-mrc-with-images"
source: "huggingface"
url: "https://huggingface.co/datasets/didi0di/finance-legal-mrc-with-images"
downloads: 12
summary: "금융·법률 분야 테이블 이미지 데이터셋으로 TIG 입력용, VLM 활용 가능"
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[임베딩]]"
  - "[[텍스트 생성]]"
  - "[[문서 검색]]"
  - "[[표 질의응답]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
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
  - "[[금융·경제]]"
  - "[[법률]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# didi0di/finance-legal-mrc-with-images

> dataset · [Hugging Face](https://huggingface.co/datasets/didi0di/finance-legal-mrc-with-images)

금융·법률 분야 테이블 이미지 데이터셋으로 TIG 입력용, VLM 활용 가능

## 분류

- **작업**: [[임베딩]] — ner · readme = `- 📊 **Table Structure Understanding**
모델이 테이블 구조, 패턴, 분포를 시각적으로 해석하도록 학습` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **작업**: [[문서 검색]] — ner · readme = `- 🔍 **Multimodal RAG or Retrieval Tasks**
이미지 기반 질의응답 또는 검색(RAG) 프레임워크 테스트` · 신뢰도 medium
- **작업**: [[표 질의응답]] — metadata · task_categories = `table-question-answering` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · modality, readme = `원본 HTML 테이블을 PNG 이미지로 렌더링` · 신뢰도 high
- **입력 형식**: [[표 (입력 형식)|표]] — task_rule · task:table_qa = `table` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:embedding, task:generation, task:retrieval, task:table_qa = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation, task:table_qa = `text` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `308` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-4.0` · 신뢰도 high
- **도메인**: [[금융·경제]] — tag_match · readme, tags = `finance` · 신뢰도 medium
- **도메인**: [[법률]] — tag_match · readme, tags = `legal` · 신뢰도 medium
- **데이터 용도**: [[평가용]] — ner · readme = `tableqa / test 스플릿` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `context` 열 p90 462자 ≈ 308 토큰 (viewer statistics, tableqa/test)
