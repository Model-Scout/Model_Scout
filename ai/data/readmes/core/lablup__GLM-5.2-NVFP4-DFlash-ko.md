---
license: mit
base_model: nvidia/GLM-5.2-NVFP4
tags:
- dflash
- speculative-decoding
- draft-model
- korean
- agentic
- tool-calling
- vllm
language:
- ko
- en
library_name: transformers
pipeline_tag: text-generation
---

# GLM-5.2-NVFP4-DFlash-ko

A [DFlash](https://arxiv.org/abs/2602.06036) block-diffusion **draft model** for
speculative decoding, paired with the **`nvidia/GLM-5.2-NVFP4`** target (753B-param
MoE, 40B active). Specialized for **Korean-query agentic (tool-calling) and coding
traffic** — trained on captured multi-turn agent trajectories, not benchmark suites.

Load with `trust_remote_code=True`; the draft is a 1.05B `DFlashDraftModel`
(5 layers, block size 16) that consumes concatenated hidden states from target
layers `[1, 20, 38, 56, 75]` and predicts a block of masked tokens in parallel.

## Serving (vLLM, TP8 + expert parallel)

```bash
vllm serve nvidia/GLM-5.2-NVFP4 \
  --tensor-parallel-size 8 --enable-expert-parallel \
  --max-model-len 262144 \
  --tool-call-parser glm47 --enable-auto-tool-choice \
  --reasoning-parser glm45 \
  --speculative-config '{"method": "dflash", "model": "lablup/GLM-5.2-NVFP4-DFlash-ko", "num_speculative_tokens": 15, "attention_backend": "triton_attn"}'
```

Serve with CUDA graphs (not `--enforce-eager`) for full throughput. `k=15` is optimal
on this stack — a k-sweep confirmed shorter blocks lose despite higher accept ratio.

## Results (checkpoint at 33,971 steps)

Measured on vLLM TP8, CUDA graphs, against **`nvidia/GLM-5.2-NVFP4`**. MAL = mean
acceptance length (1 + accepted/drafts); speedup is measured decode tok/s vs the same
server with speculation off (~118 tok/s baseline, batch-1).

**Paper suites** (greedy, non-thinking):

| suite | MAL | decode tok/s | speedup |
|---|---|---|---|
| HumanEval | 4.87 | 400 | 3.38× |
| MATH-500 | 2.88 | 242 | 2.07× |
| MBPP | 2.65 | 224 | 1.90× |
| GSM8K | 2.50 | 212 | 1.79× |
| MT-Bench | 1.94 | 167 | 1.42× |

**Production traffic** (temperature 1.0 / top-p 0.95, the serving distribution):

| workload | MAL | decode tok/s | speedup |
|---|---|---|---|
| Agentic multi-turn (tool-calling) | 2.71 | 198 | 1.72× |
| Korean coding queries | 2.77 | 220 | 1.92× |

On real Korean agentic traffic this draft holds MAL flat across agentic and Korean
(2.71 / 2.77), where an English-trained draft drops ~0.6 MAL between the two.

## Training

- **Warm-started** from a preview draft, then trained on **135,887 captured agentic
  pairs** at 16K context (1 epoch, 33,971 steps, lr 7e-5 cosine).
- Data: real coding-agent sessions (OpenCode / Codex / Claude Code harnesses) driving
  a GLM-5.2-NVFP4 endpoint over **17.6K Korean-localized GitHub issues** across 619
  permissive-license repos, with responses captured server-side (exact target token ids).
- 4 nodes × 8 B200, ~6.9 days.

## License

MIT, following the `nvidia/GLM-5.2-NVFP4` target. The draft weights are original
(HF random init, trained from scratch). Verify upstream dataset/target licenses for
your own redistribution.
