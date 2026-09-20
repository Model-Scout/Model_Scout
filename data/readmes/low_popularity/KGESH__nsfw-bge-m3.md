---
tags:
- sentence-transformers
- sentence-similarity
- feature-extraction
- nsfw
- embedding
- bge-m3
language:
- en
- ko
- ja
base_model: BAAI/bge-m3
---

# NSFW BGE-M3 — Model Index

NSFW 키워드 임베딩 모델 프로젝트 (bge-m3 파인튜닝)

## 버전별 레포

| Version | Repo | 상태 | 특징 |
|---------|------|------|------|
| v1 | [KGESH/nsfw-bge-m3-v1](https://huggingface.co/KGESH/nsfw-bge-m3-v1) | 추천 | MNR only, 다의어 구분 최강 |
| v3 | [KGESH/nsfw-bge-m3-v3](https://huggingface.co/KGESH/nsfw-bge-m3-v3) | 사용불가 | Embedding collapse |
| v4 | [KGESH/nsfw-bge-m3-v4](https://huggingface.co/KGESH/nsfw-bge-m3-v4) | 추천 | Collapse 수정, hard negative 강화 |

## 성능 비교

| Metric | v1 | v3 | v4 |
|--------|------|------|------|
| Sim mean | 0.577 | 0.990 | 0.683 |
| Sim std | 0.212 | 0.008 | 0.201 |
| NSFW-General gap | 0.275 | 0.009 | 0.292 |
| Collapse | 없음 | 심각 | 없음 |
| Overall | ALL PASS | ALL PASS* | ALL PASS |

*v3는 모든 단어가 0.99라서 통과한 것 (실제로는 구분 불가)

## 추천
- 실사용: v1 또는 v4
- GGUF 다운로드: 각 레포에서 nsfw-bge-m3-vN.gguf 파일 사용

## 학습 스크립트
- [KGESH/nsfw-embed-scripts](https://huggingface.co/KGESH/nsfw-embed-scripts)
