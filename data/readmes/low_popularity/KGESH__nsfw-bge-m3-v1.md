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

# NSFW BGE-M3 v1

NSFW 키워드 임베딩 모델 (bge-m3 파인튜닝)

## 학습 설정
- Loss: MultipleNegativesRankingLoss
- Data: 10,008 positive pairs
- Epochs: 5
- LR: 2e-5
- Batch: 32

## 특징
- 다의어 구분: creampie(성인) vs dessert(디저트) 구분 가능
- 다국어: 한국어(질싸, 보지, 자지), 일본어(中出し, フェラチオ)
- Collapse 없음: std=0.2115, NSFW-General gap=0.2749

## 평가
- Pearson: 0.9075, Spearman: 0.8496
- ALL PASS (20 test cases)
