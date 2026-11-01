---
language: [ko, en]
license: apache-2.0
library_name: transformers
pipeline_tag: text-generation
tags: [korean, pretrained, from-scratch, qwen3-architecture, causal-lm]
---

# yejin-korean-3b-v2-base

**100% from-scratch** 사전학습된 한국어 3B 파운데이션 모델. 외부 공개 모델 가중치를 전혀 사용하지 않았습니다.

- 파라미터: 3.02B (hidden 3072, 28 layers, 24 heads, 8 KV heads, GQA 3:1)
- 컨텍스트 4096, RoPE theta 500000, QK-Norm, tied embeddings
- 토크나이저: 독자 64K Byte-level BPE (한국어 특화)
- 학습: 8x NVIDIA H200, 34000 steps, 약 73B 토큰 (155GB 한국어 코퍼스: AI Hub, CulturaX, 위키백과, 교과서 등)
- 학습 손실: ~2.0

## HF 아키텍처 클래스에 관하여
학습 모델은 QK-Norm(헤드별 RMSNorm, RoPE 이전) 을 사용합니다. HF `LlamaForCausalLM` 에는 QK-Norm이 없어
동일 구조를 지원하는 `Qwen3ForCausalLM` 클래스로 로드합니다. **가중치는 Qwen 과 무관한 독자 학습 결과**이며,
클래스는 모델 구조(연산 그래프) 호환을 위해서만 사용됩니다. vLLM / llama.cpp 에서 그대로 로드 가능합니다.

## 사용
```python
from transformers import AutoModelForCausalLM, AutoTokenizer
tok = AutoTokenizer.from_pretrained("cooler8/yejin-korean-3b-v2-base")
model = AutoModelForCausalLM.from_pretrained("cooler8/yejin-korean-3b-v2-base", torch_dtype="bfloat16", device_map="auto")
ids = tok("대한민국의 수도는", return_tensors="pt").to(model.device)
print(tok.decode(model.generate(**ids, max_new_tokens=50)[0]))
```

이 모델은 base 모델입니다 (지시문 튜닝 없음). SFT/DPO 버전: `cooler8/yejin-korean-3b-v2-sft`, `cooler8/yejin-korean-3b-v2-dpo`.

변환: step 34000 체크포인트, 2026-09-12 02:27 UTC
