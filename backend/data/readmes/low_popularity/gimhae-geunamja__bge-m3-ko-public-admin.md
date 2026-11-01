---
license: apache-2.0
language:
- ko
library_name: sentence-transformers
pipeline_tag: sentence-similarity
base_model: dragonkue/bge-m3-ko
tags:
- sentence-transformers
- sentence-similarity
- feature-extraction
- bge-m3
- korean
- retrieval
- public-administration
---

# bge-m3-ko-public-admin

한국 지자체 **행정 문서·행정법 도메인 검색(RAG)** 에 특화되도록 `dragonkue/bge-m3-ko` 를 파인튜닝한 한국어 임베딩 모델입니다.

- **베이스 모델**: [`dragonkue/bge-m3-ko`](https://huggingface.co/dragonkue/bge-m3-ko) (Apache-2.0) → [`BAAI/bge-m3`](https://huggingface.co/BAAI/bge-m3) 계열
- **모델 종류**: Sentence Transformer (XLM-RoBERTa, 1024차원)
- **언어**: 한국어
- **용도**: 행정 문서 검색, 질의-문서 유사도, RAG 리트리버

## 라이선스

본 모델은 베이스 모델의 라이선스를 승계하여 **Apache-2.0** 으로 배포합니다. 학습에 사용된 AI Hub 데이터의 이용조건(아래 "학습 데이터 및 출처표기" 참고)도 함께 준수해야 합니다.

## 학습 데이터 및 출처표기

본 모델은 과학기술정보통신부의 재원으로 **한국지능정보사회진흥원(NIA)** 의 지원을 받아 구축된 아래 AI Hub **개방데이터**를 활용하여 학습되었습니다.

- **016. 행정 문서 대상 기계독해 데이터** — 질문(question)과 지문(context)의 정답 쌍을 positive 예시로 사용
- **03. 행정법 LLM 사전학습 및 Instruction Tuning 데이터** (개방데이터) — instruction과 output 쌍을 positive 예시로 사용

> 본 학습에 활용된 데이터는 AI 허브([aihub.or.kr](https://www.aihub.or.kr))에서 다운로드할 수 있습니다.
> 이 데이터의 저작권 및 이용조건은 한국지능정보사회진흥원 및 각 수행기관에 있으며, 원본 데이터 자체의 재배포는 금지됩니다. 본 저장소는 학습된 모델 가중치만 배포하며 원본 데이터는 포함하지 않습니다.

- 총 학습 쌍: 약 373,410개 (질문–문서 positive 쌍), 이 중 5%를 평가용으로 분리
- 데이터에서 정답이 없는 항목(`is_impossible`)은 제외

## 사용법

```python
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("gimhae-geunamja/bge-m3-ko-public-admin")

queries = ["출산 지원금 신청은 어디서 하나요?"]
documents = [
    "출산 지원금은 관할 읍·면·동 행정복지센터에서 신청할 수 있습니다.",
    "주민등록등본은 정부24에서 온라인 발급이 가능합니다.",
]

query_emb = model.encode(queries, normalize_embeddings=True)
doc_emb = model.encode(documents, normalize_embeddings=True)

scores = query_emb @ doc_emb.T
print(scores)
```

## 학습 상세

| 항목 | 값 |
|------|-----|
| 손실 함수 | `MultipleNegativesRankingLoss` |
| Epoch | 3 |
| max_seq_length | 1024 |
| 물리 배치 / GPU | 16 |
| Gradient Accumulation | 4 |
| 글로벌 배치 | 128 (16 × 2 GPU × 4) |
| Learning rate | 2e-5 |
| Precision | bf16 |
| 하드웨어 | RTX 5090 × 2 (DDP) |

> `bge-m3` 의 기본 max_seq_length(8192)를 행정문서 RAG에 맞춰 1024로 제한했습니다. 배치 내 anchor 중복 방지를 위해 `BatchSamplers.NO_DUPLICATES` 를 사용했습니다.

## 평가

5% hold-out 테스트셋으로 `InformationRetrievalEvaluator`(MRR@10, nDCG@10, Accuracy@1/5/10)를 사용해 베이스 모델 대비 검색 성능을 측정했습니다. 상세 수치는 저장소 이용자가 자체 도메인 데이터로 재검증할 것을 권장합니다.

## 제한 사항

- 한국 행정/법령 도메인에 특화되어 있어 일반 도메인·타 언어 성능은 베이스 모델과 다를 수 있습니다.
- 학습 데이터가 공공 행정 문서에 편중되어 있어 도메인 밖 질의에는 편향이 있을 수 있습니다.

## 인용 및 출처

- 베이스 모델: `dragonkue/bge-m3-ko`, `BAAI/bge-m3`
- 학습 데이터: 「행정 문서 대상 기계독해 데이터」, 「행정법 LLM 사전학습 및 Instruction Tuning 데이터」, AI 허브(aihub.or.kr), 한국지능정보사회진흥원
- Sentence-Transformers (Reimers & Gurevych, 2019, arXiv:1908.10084)

## 알려진 한계 (2026-08 갱신)

- **시퀀스 상한 1,024 토큰**: 아키텍처는 8,192 포지션(max_position_embeddings 8194)을 지원하지만, 파인튜닝을 max_seq_length=1024로 수행했고 저장된 `tokenizer_config.json`의 `model_max_length`도 1024입니다. 그대로 로드하면 1,024 토큰 초과분은 **조용히 잘립니다.** 상한을 늘려 쓸 수는 있으나 그 길이 구간은 학습 분포 밖이라 품질이 미검증입니다.
- **CLS 풀링**: 문장 벡터는 mean pooling이 아니라 **CLS 토큰 표현**입니다(`1_Pooling/config.json: pooling_mode="cls"`). late chunking 등 토큰 임베딩의 스팬 평균을 전제로 하는 기법과는 벡터 공간이 달라 직접 호환되지 않습니다.
- **체크포인트 dtype은 bfloat16**: `config.json`의 dtype이 bfloat16이라 자동 로드 시 bf16 추론이 됩니다. CPU에서는 fp32보다 느릴 수 있고, 저장 벡터와의 정밀도 일관성이 중요한 서빙에서는 fp32 명시 로드를 권장합니다: `SentenceTransformer(..., model_kwargs={"dtype": torch.float32})`.
