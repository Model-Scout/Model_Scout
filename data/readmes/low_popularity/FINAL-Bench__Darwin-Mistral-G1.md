---
license: apache-2.0
base_model:
  - mistralai/Devstral-2-123B-Instruct-2512
  - mistralai/Mistral-Medium-3.5-128B
tags:
  - darwin
  - darwin-v7
  - mistral
  - merge
  - mri-merge
  - layer-band-asymmetric
language:
  - en
  - ko
pipeline_tag: text-generation
inference: false
---

# Darwin-Mistral-G1

**Darwin × Mistral 진화적 머지 1세대 (G1)** — Devstral-2-123B(코딩) × Mistral-Medium-3.5-128B(추론·범용) 의 **Darwin V7+ MRI-only Linear merge** 결과물.

> VIDRAFT R&D · 2026-05-16
> 작업지시서 v1.0 (김태봉 CAIO) 옵션 A 채택 결과

## 주요 결과 (Quick)

| Benchmark | Score | Note |
|---|---|---|
| GPQA Diamond 20 (seed 42) | **45.0%** (9/20) | Mother 수준 회복 — Devstral 50% / MM3.5 45% 사이 |
| HumanEval 20 pass@1 (seed 42) | **🔥 90.0%** (18/20) | Devstral 코딩 능력 완벽 보존 |
| Sanity (수학·코드·한국어) | ✅ 3/3 | 17×23=391, fibonacci code, 한국어 번역 정상 |

## 머지 사양

### 부모
- **Father (코딩)**: `mistralai/Devstral-2-123B-Instruct-2512` — Ministral3ForCausalLM, hidden 12288, layers 88, vocab 131072, FP8 + BF16
- **Mother (추론·멀티모달 베이스)**: `mistralai/Mistral-Medium-3.5-128B` — Mistral3ForConditionalGeneration text branch (vision 제외), 동일 spec

### 방법
- **Engine**: Darwin V7+ MRI-only (Linear blend, no SLERP)
- **Blend**: `(1 - r_mother) * Father + r_mother * Mother` per tensor
- **Prefix remap**: Mother `model.language_model.X` → `model.X` (Ministral3 namespace 통일)
- **Vision exclusion**: G1에서 Pixtral vision_tower + multi_modal_projector 제외 (G2에서 통합 예정)

### Layer-band 비대칭 (작업지시서 v1.0 §3-2)
| Layer 구간 | r_mother | 의도 |
|---|---|---|
| 0~29 (low) | 0.25 | Father(Devstral) 우세 — 토큰 표현·코드 구문 보존 |
| 30~59 (mid) | 0.70 | Mother 우세 — 추론 체인 강화 |
| 60~87 (high) | 0.50 | 균등 — 출력 품질·인스트럭션 |

### Category ratio (Mother bias)
| Category | r_mother | 비고 |
|---|---|---|
| **embedding** | **0.00** | Father 100% — 토큰 매핑 보존 (v1 1.00 시 random 손상 확인) |
| **lm_head** | **0.00** | Father 100% — 출력 매핑 보존 |
| attention | 0.50 | 균등 — Devstral reasoning 회복 |
| norm | 0.50 | 균등 — LayerNorm 통계 |
| router/shared_expert/routed_expert | n/a | Mistral dense라 해당 없음 |

### 머지 통계
- Total tensors merged: 2,027 (Father + Mother 공통)
- Mother vision skipped: 438 (vision_tower + multi_modal_projector + patch_merger)
- Output: 32 shards / 128.2 GB (FP8 + BF16 dtype 유지)
- Elapsed: 5.0 min (CPU bound, single-thread safetensors I/O)

## 평가 결과 (전체)

### GPQA Diamond 20 (seed 42, transformers + finegrained-fp8 kernel)
| 모델 | 정답/총 | 정확도 |
|---|---|---|
| Devstral-2-123B (Father) | 10/20 | 50.0% |
| Mistral-Medium-3.5-128B (Mother) | 9/20 | 45.0% |
| Darwin-Mistral-G1 v1 (failed) | 5/20 | 25.0% (random) |
| **Darwin-Mistral-G1 v2 (this)** | **9/20** | **45.0%** ✅ |

### HumanEval 20 pass@1 (seed 42)
- **G1 v2: 18/20 = 90.0%** (284초)
- Devstral baseline 유지 (Devstral 공개 85-90%)
- Linear merge로 코딩 SOTA 보존 사례

## V1 → V2 진단 (재발 방지)

V1 실패 원인 (GPQA 25% random level):
1. **embedding/lm_head Mother 100% → Father 토큰·출력 매핑 완전 소실**
2. layer-band × category ratio 곱셈 보정으로 attention 항상 Mother 쪽으로 끌림

V2 fix:
1. embedding/lm_head Father 100%
2. attention 0.90 → 0.50
3. layer-band 단순 적용 (곱셈 보정 제거)

## 사용

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# 의존성: pip install --user kernels  (transformers 5.5.x finegrained-fp8 kernel)
model = AutoModelForCausalLM.from_pretrained(
    "FINAL-Bench/Darwin-Mistral-G1",
    torch_dtype=torch.bfloat16,
    device_map="auto",
    trust_remote_code=True,
)
tok = AutoTokenizer.from_pretrained("FINAL-Bench/Darwin-Mistral-G1")
messages = [{"role": "user", "content": "Write a Python function to compute Fibonacci."}]
text = tok.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
inp = tok(text, return_tensors="pt").to(model.device)
out = model.generate(**inp, max_new_tokens=256, do_sample=False)
print(tok.decode(out[0][inp.input_ids.shape[1]:], skip_special_tokens=True))
```

**환경 요구사항**:
- `transformers >= 5.5.0`
- `kernels >= 0.14.0` (finegrained-fp8 kernel 자동 다운로드)
- `torch >= 2.10` (FP8 E4M3 지원)
- GPU: 단일 H100/B200 80GB+ (FP8 inference 시 약 128GB → 다중 GPU 권장)

## 한계

- **GPQA 80% 목표 미달**: 작업지시서 §4-3 GPQA >80%는 원래 Darwin-36B-Opus 86.9% baseline 가정. 옵션 A에서 Mother를 Mistral-3.5 (45%)로 변경했기에 도달 불가.
- **G2 진행**: Pixtral 비전 인코더 통합 + Darwin-36B-Opus cross-arch 통합은 별도 트랙 (G2/G3).
- **SWE-Bench 미측정**: 별도 평가 환경 필요.

## License & Attribution

Apache-2.0 (Devstral-2-123B-Instruct-2512와 Mistral-Medium-3.5-128B 모두 Apache 2.0).
머지 엔진은 VIDRAFT Darwin V7+ MRI-only (proprietary).

## 인용

```bibtex
@misc{darwin-mistral-g1-2026,
  title = {Darwin-Mistral-G1: Linear MRI Merge of Devstral-2-123B and Mistral-Medium-3.5-128B},
  author = {VIDRAFT R&D},
  year = {2026},
  url = {https://huggingface.co/FINAL-Bench/Darwin-Mistral-G1}
}
```

---
**VIDRAFT Inc.** | 김태봉 CAIO | CONFIDENTIAL (private repo until publication)
