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
base_model: KGESH/nsfw-bge-m3-v4
---

# NSFW BGE-M3 v5 (Category-Aware)

NSFW keyword embedding model with category-level discrimination.

## Improvements over v4
- Co-occurrence based tag clustering from 23M+ adult videos (XVideos + Big-Porn)
- Hard negatives: different NSFW categories (creampie vs deepthroat)
- 8557 clusters from 2.1M unique tags
- Multilingual pairs (en/ko/ja) from Danbooru aliases

## Training Data
- 172K training pairs (138K positive, 1.7K hard negative, 1.5K easy negative, 31K multilingual)
- Stage 1: MNR Loss, 2 epochs, lr=1e-5
- Stage 2: OnlineContrastiveLoss, 5 epochs, lr=5e-6, margin=0.85
