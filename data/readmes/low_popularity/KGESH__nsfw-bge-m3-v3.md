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

# NSFW BGE-M3 v3 (Collapsed)

NSFW 키워드 임베딩 모델 (bge-m3 파인튜닝) — 임베딩 붕괴 발생

## 학습 설정
- Stage 1: MNR Loss, 25,372 pairs, 3 epochs, lr=2e-5
- Stage 2: OnlineContrastiveLoss, 92 hard negatives, margin=0.5, 2 epochs, lr=1e-5

## 문제: Embedding Collapse
- 모든 단어 쌍의 유사도가 0.96~0.99로 수렴
- std=0.0080, NSFW-General gap=0.0091
- 다의어 구분 불가 (creampie vs dessert 차이 < 0.01)

## 원인
1. 데이터 과다 (25K쌍) + 3에폭 과학습
2. margin=0.5로 너무 작음
3. positive_examples[:5000] 중복 주입
4. co-occurrence 노이즈 (10K x 4소스)

## 참고용
이 모델은 실사용 불가입니다. v1 또는 v4를 사용하세요.
