---
type: "dataset"
id: "LLM-OS-Models/korean-embedding-performance-v1-sionic-squad-train-60k"
source: "huggingface"
url: "https://huggingface.co/datasets/LLM-OS-Models/korean-embedding-performance-v1-sionic-squad-train-60k"
downloads: 12
summary: "KorQuAD v1.0 원본 train split을 질문-정답 문맥 검색 형식으로 변환한 6만 행 임베딩 학습 데이터입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[임베딩]]"
  - "[[문서 검색]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# LLM-OS-Models/korean-embedding-performance-v1-sionic-squad-train-60k

> dataset · [Hugging Face](https://huggingface.co/datasets/LLM-OS-Models/korean-embedding-performance-v1-sionic-squad-train-60k)

KorQuAD v1.0 원본 train split을 질문-정답 문맥 검색 형식으로 변환한 6만 행 임베딩 학습 데이터입니다.

## 분류

- **작업**: [[임베딩]] — metadata · readme, task_categories = `feature-extraction` · 신뢰도 high
- **작업**: [[문서 검색]] — ner · readme = `KorQuAD v1.0의 원본 train split만 질문→정답 문맥 retrieval 형식으로 변환한 60,000-row target-adaptation 데이터다.` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:embedding, task:retrieval = `질문→정답 문맥 retrieval 형식으로 변환한 60,000-row target-adaptation 데이터다.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `질문→정답 문맥 retrieval 형식으로 변환한 60,000-row target-adaptation 데이터다.` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `KorQuAD source를 CC-BY-ND-4.0으로 표시하고, upstream dataset card 본문은 CC BY-ND 2.0 KR도 명시한다.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `KorQuAD v1.0의 원본 train split만 질문→정답 문맥 retrieval 형식으로 변환한 60,000-row target-adaptation 데이터다.` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
