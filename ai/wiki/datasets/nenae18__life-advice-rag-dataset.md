---
type: "dataset"
id: "nenae18/life-advice-rag-dataset"
source: "huggingface"
url: "https://huggingface.co/datasets/nenae18/life-advice-rag-dataset"
downloads: 32
summary: "성경, 불교 경전, 논어 등 인문학 명언을 RAG 검색용 chunk로 변환한 인생조언 데이터셋입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_with_others"
task:
  - "[[임베딩]]"
  - "[[질의응답]]"
  - "[[문서 검색]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[문화·관광]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# nenae18/life-advice-rag-dataset

> dataset · [Hugging Face](https://huggingface.co/datasets/nenae18/life-advice-rag-dataset)

성경, 불교 경전, 논어 등 인문학 명언을 RAG 검색용 chunk로 변환한 인생조언 데이터셋입니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `SentenceTransformer 임베딩 생성` · 신뢰도 medium
- **작업**: [[질의응답]] — metadata · readme, task_categories = `question-answering` · 신뢰도 high
- **작업**: [[문서 검색]] — metadata · readme, tags, task_categories = `text-retrieval` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:embedding, task:question_answering, task:retrieval = `텍스트 chunk` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `답변 생성` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `1061` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[문화·관광]] — ner · readme = `성경, 불교 경전/해설, 논어, 인문학 명언 자료` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `시연용 질문 예시` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `RAG 검색용 chunk 본문` · 신뢰도 low
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 1592자 ≈ 1061 토큰 (viewer statistics, default/train)
