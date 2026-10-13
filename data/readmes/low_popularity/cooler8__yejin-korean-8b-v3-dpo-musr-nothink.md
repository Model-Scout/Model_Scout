---
language:
- ko
- en
license: apache-2.0
tags:
- yejin
- korean
- causal-lm
- musr
- nothink
- 8b
base_model: cooler8/yejin-korean-8b-v3-dpo-musr
pipeline_tag: text-generation
---

# Yejin Korean 8B v3 DPO MuSR (no-think)

`cooler8/yejin-korean-8b-v3-dpo-musr` 가중치에 K-AI Leaderboard 최적화 no-think 템플릿(`<think> </think>`)을 적용한 모델입니다.

## Chat Template
```
<s><|user|>\n{instruction}<|end|>\n<|assistant|>\n<think> </think>{response}<|end|>\n</s>
```
