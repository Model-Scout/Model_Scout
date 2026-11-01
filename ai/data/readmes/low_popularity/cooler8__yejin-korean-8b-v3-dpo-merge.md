---
language:
- ko
- en
license: apache-2.0
tags:
- yejin
- korean
- causal-lm
- merge
- dpo
- musr
- reasoning
- 8b
base_model: cooler8/yejin-korean-8b-v3-base
pipeline_tag: text-generation
---

# Yejin Korean 8B v3 DPO Merge (DARE-TIES Ensemble Blend)

**Yejin Korean 8B v3 DPO Merge**는 깊은 장문 다단계 연역 추론력(MuSR gen 0.353, 1,450토큰 스크래치패드)을 보유한 `cooler8/yejin-korean-8b-v3-dpo-v4`와 고정밀 한국어 이해 및 최고 포맷 준수율(CLIcK 0.419, MuSR ll 0.413, 파싱률 97.2%)을 보유한 `cooler8/yejin-korean-8b-v3-dpo-musr`의 가중치를 정밀 가중 블렌딩(Weight Blending / DARE-TIES Ensemble)하여 두 모델의 장점만을 결합한 단일 8B 궁극 추론 모델입니다.

## 모델 합성 구성 (Model Blend Composition)
- **Model A (65~70%)**: `cooler8/yejin-korean-8b-v3-dpo-v4` (장문 복합 추론 & DPO 안정성)
- **Model B (30~35%)**: `cooler8/yejin-korean-8b-v3-dpo-musr` (초정밀 정답 출력 & 97.2% 파싱률)
- **Base Architecture**: Qwen3 8B (7.24B Params, digitsplit 64k tokenizer)

## Generation Config
- Greedy Decoding 기본 권장 (`do_sample=False`, `repetition_penalty=1.05`)
- Stop tokens: `<|end|>`, `</s>` (Token ID 7, 2)
