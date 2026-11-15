---
license: apache-2.0
base_model: ThakiCloud/Qwen3.8-27B-Human-KO-Safety
language:
- ko
- en
pipeline_tag: text-generation
tags:
- korean
- safety
- bias
- kobbq
- nvfp4
- fp8
- gptq
- qwen
base_model_relation: quantized
library_name: transformers
---

# Qwen3.8-27B-Human-KO-Safety-NVFP4

This is the **Blackwell-only quantized version** of
[`ThakiCloud/Qwen3.8-27B-Human-KO-Safety`](https://huggingface.co/ThakiCloud/Qwen3.8-27B-Human-KO-Safety).
MLP weights are NVFP4, attention (self_attn·linear_attn) is FP8 dynamic, and embeddings,
lm_head, the recurrent input projection (`in_proj_a/b`), and the vision tower are left as
bf16. Disk size 21.4GiB (38% of bf16's 55.6GB).

## What was re-measured for this version (2026-09-07, temperature 0, thinking off, same serving config as bf16)

Quantization changes abstention behavior. So instead of copying over the bf16 card's
figures, we re-measured them on this checkpoint.

| Axis | bf16 original | **This model (NVFP4)** | How to read it |
|---|---|---|---|
| KoBBQ ambiguous-context abstention (8,139) | 92.8% | **89.5%** | 3.3pp lower. Misses the pre-registered target of 93%, +23.8pp over EXAONE 4.5's 65.7% |
| Change in disambiguated-context accuracy (vs. base 90.66) | −2.1pp | **−0.9pp** | Less over-abstention (within the −3pp threshold) |
| Conditional bias (among answered items) | 0.861 | 0.848 | Both miss the pre-registered target of 0.60 (structural — see the bf16 card) |
| Identity probe (8-language holdout, n=240) | 96.2% | 95.8% | 1-item difference |
| MMLU English 1,000 (thinking off) | 80.9% | 80.0% | Within detection limit |
| Thinking-mode empty responses (100) | 0 | 0 | No format defect |
| Korean human-likeness pairwise win rate (n=175) | +14.3pp | +10.3pp | Judge uncalibrated, direction only |
| HumanEval (executed, same run, n=148) | 97.1% | 94.6% | −2.5pp, 4-item difference, within detection limit |
| KMMLU 1,000 (same run) | 52.3% | 54.4% | +2.1pp |
| Instruction following 100 (deterministic checker) | 79% | 81% | Equivalent |

In one line: **it abstains slightly less and also over-abstains slightly less — behavior
similar to shifting β a bit toward 0.2.** If abstention rate is the top priority, use
bf16 or W4A16; if memory and speed on Blackwell come first, use this version. Capability
gates (coding·KMMLU·instruction) were re-measured in the same run with bf16 as the
reference arm and entered into the table above. The difference from the bf16 card's
absolute values is because the runs differ; read the comparison only within the same
run.

## Quantization recipe

llm-compressor 0.13.0 GPTQ · calibration 1,024 samples × 2,048 tokens (chat format, 25%
Korean) · dampening 0.01 · actorder static · scheme NVFP4 (MLP) + FP8_DYNAMIC (attention)
· ignore: vision/visual, `lm_head`, `embed_tokens`, `linear_attn.in_proj_a/b`. Took 46
minutes (1x B200). Metadata is in `quantize_meta.json`; the actual group and ignore lists
are in `config.json`'s `quantization_config`, verbatim.

## Serving

Blackwell (SM100+: B200·GB200·RTX 50) only. There is no NVFP4 kernel on Hopper or below.

```bash
vllm serve ThakiCloud/Qwen3.8-27B-Human-KO-Safety-NVFP4 \
  --max-model-len 32768 --kv-cache-dtype fp8 --enable-prefix-caching
```

vLLM ≥ 0.28 auto-detects the scheme from `config.json`, so there is no need to pass
`--quantization` separately. DFlash drafter speculative decoding is not recommended on
NVFP4, since a single-stream penalty (0.71-0.82x) has been measured.

## Limitations

- The safety axis was measured with KoBBQ alone, and the table above is from a single
  build of this quantized checkpoint. Given the noise between requantization builds (our
  measured GSM8K figure is 3.56pp), a difference within 3pp is not attributed to the
  treatment.
- The abstention rate of 89.5% differs from the bf16 card's 92.8%. Do not cite the bf16
  figure for this model.
- Other limitations and data provenance are the same as the bf16 card and
  `DATA_PROVENANCE.md`.

## License

Apache-2.0 (same as `Qwen/Qwen3.8-27B`). See `LICENSE` · `NOTICE`.

## Paper

Off-Target Effects of Response-Style Alignment in a Korean 27B Language Model — [arXiv:2609.11291](https://arxiv.org/abs/2609.11291)

The style alignment behind this line also moved two behaviors nobody trained for: abstention on ambiguous social questions (KoBBQ) and unprompted disclosure in securities guidance. Both moved through the **emission policy** — how often the model answers and how much it says — rather than through what it says when it does answer. Holding prompts, recipe, data volume and serving fixed and changing only the training target, three style seeds moved answer rate one way and three neutral seeds moved it the other (observed ranges do not overlap). Read this card's numbers with that in mind.
