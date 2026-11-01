---
type: "dataset"
id: "allganize/rag-ko"
source: "huggingface"
url: "https://huggingface.co/datasets/allganize/rag-ko"
downloads: 20
summary: "금융 도메인 RAG 데이터셋으로, 질문과 답변, 골든 및 네거티브 컨텍스트를 포함합니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
  - "[[문서 검색]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[금융·경제]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# allganize/rag-ko

> dataset · [Hugging Face](https://huggingface.co/datasets/allganize/rag-ko)

금융 도메인 RAG 데이터셋으로, 질문과 답변, 골든 및 네거티브 컨텍스트를 포함합니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `GPT-4를 이용하여 해당 컨텍스트에 대한 질문과 답변을 생성하고 이를 각각, Golden Context, Question, Golden Answer로 삼습니다` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `RAG(Retrieval Augmented Generation, 검색증강생성) 데이터셋입니다` · 신뢰도 medium
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:retrieval = `Golden Context, 2개의 Negative Context, Question과 Instruction을 모두 포함했을때 3K Token(Llama2 tokenizer기준)을 넘지 않도록 Allganize Summerizer(사내 추출형 요약엔진)을 이용해 요약합니다` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `GPT-4를 이용하여 해당 컨텍스트에 대한 질문과 답변을 생성하고 이를 각각, Golden Context, Question, Golden Answer로 삼습니다` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `1152` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[금융·경제]] — ner · readme = `금융 도메인의 RAG(Retrieval Augmented Generation, 검색증강생성) 데이터셋입니다` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `사람이 검수 완료한 200개의 데이터셋입니다` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

샘플 길이: `system` 열 p90 1728자 ≈ 1152 토큰 (viewer statistics, default/test)
