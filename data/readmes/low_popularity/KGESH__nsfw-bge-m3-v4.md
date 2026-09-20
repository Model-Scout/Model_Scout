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

# NSFW BGE-M3 v4 (Collapse Fixed)

NSFW 키워드 임베딩 모델 (bge-m3 파인튜닝) — v3 붕괴 문제 해결

## 학습 설정
- Stage 1: MNR Loss, 18,816 pairs, 2 epochs, lr=1e-5
- Stage 2: OnlineContrastiveLoss, 199 hard negatives, margin=0.85, 5 epochs, lr=5e-6
- co-occurrence: 3,000 per source (v3의 10,000에서 감소)

## 개선 사항 (v3 대비)
- 데이터 축소: 25K → 18K (노이즈 감소)
- Stage 1 에폭: 3 → 2 (과학습 방지)
- Stage 1 LR: 2e-5 → 1e-5
- Stage 2 margin: 0.5 → 0.85 (강한 구분)
- Stage 2 에폭: 2 → 5 (hard negative 학습 강화)
- Hard negatives: 92 → 199 (포지션, 신체, 페티시, 은어 추가)
- positive_examples 주입 제거 (collapse 원인 제거)

## 평가
- Collapse Detection: OK (std=0.2005, gap=0.2915)
- ALL PASS (20 test cases)
- NSFW avg=0.7995, General avg=0.5080

## 다운로드
- GGUF: nsfw-bge-m3-v4.gguf (1.08GB F16)
- eval_results.json 참고
