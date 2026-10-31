---
type: "dataset"
id: "naruto-soop/CharacterRAG"
source: "huggingface"
url: "https://huggingface.co/datasets/naruto-soop/CharacterRAG"
downloads: 153
summary: "15명의 가상 캐릭터 페르소나 문서와 450개의 질의응답 쌍으로 구성된 RAG 기반 역할극 에이전트용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[질의응답]]"
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
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[텍스트 파일]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# naruto-soop/CharacterRAG

> dataset · [Hugging Face](https://huggingface.co/datasets/naruto-soop/CharacterRAG)

15명의 가상 캐릭터 페르소나 문서와 450개의 질의응답 쌍으로 구성된 RAG 기반 역할극 에이전트용 데이터셋입니다.

## 분류

- **작업**: [[질의응답]] — ner · readme = `450 question–answer pairs` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `CharacterRAG is a high-quality dataset for RAG-based role-playing agents` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:question_answering, task:retrieval = `persona documents for 15 distinct fictional characters` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `450 question–answer pairs` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `149` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `15 distinct fictional characters` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `CharacterRAG is a high-quality dataset for RAG-based role-playing agents` · 신뢰도 low
- **데이터 형식**: [[텍스트 파일]] — metadata · format = `text` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 224자 ≈ 149 토큰 (viewer statistics, default/train)
