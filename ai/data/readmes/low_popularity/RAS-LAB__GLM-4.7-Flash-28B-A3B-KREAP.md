---
license: mit
base_model: zai-org/GLM-4.7-Flash
library_name: transformers
pipeline_tag: text-generation
language:
  - ko
  - en
tags:
  - glm
  - moe
  - pruning
  - reap
  - expert-pruning
  - experimental

  - k-reap
  - korean
---

# GLM-4.7-Flash-28B-A3B-KREAP

Korean-priority one-shot MoE Expert pruning of [zai-org/GLM-4.7-Flash](https://huggingface.co/zai-org/GLM-4.7-Flash), produced with [K-REAP](https://github.com/Chedrian07/K-REAP).

Routed Experts were pruned **64 → 56 per layer (12.5%)** while top-4 routing was kept unchanged.
`28B` rounds the measured 27.75B stored parameters; `A3B` retains the base model's approximate active-parameter class because top-4 routing is unchanged, not a new active-parameter measurement; `KREAP` pruned 12.5% of routed Experts; BF16 is the dominant dtype with 2,640 F32 entries, without quantization

The checkpoint contains **27.75B parameters** (base 31.22B; **11.13% total-parameter reduction**) and occupies **51.71 GiB** (approximately **11.1% smaller** than the base checkpoint),
is stored in BF16/F32 safetensors, and received **no fine-tuning**.

| Status | Result |
|---|---|
| Checkpoint integrity checks | **PASS** |
| Internal release gate | **NOT PASSED** |
| External reproduction | **NOT YET REPORTED** |
| Deployment status | **EXPERIMENTAL** |

**Best tested strict KREAP checkpoint in this GLM grid, but it did not pass the project's internal release criteria.** It is the only checkpoint here whose complete hard-protected set fits every layer budget.

## What this checkpoint shows

- Method: **KREAP**
- Korean MC macro: **66.6** (base 68.8, -2.2 pp)
- Overall non-Korean composite: **62.5** (base 65.5, -3.0 pp)
- Coding 2-benchmark macro: **72.5** (base 76.0, -3.5 pp)
- LiveCodeBench v6 pass@1: **25.1** (base 22.9, +2.3 pp)
- Coding 3-benchmark macro: **56.7** (base 58.3, -1.6 pp)
- Protection budget: Satisfied in all 46 routed MoE layers; no protected Expert was force-dropped.

## Benchmark results

| benchmark | base | **KREAP 12.5% (this checkpoint)** | KREAP force-fit 25% | KREAP force-fit 50% | KREAP-Code 25% |
|---|---:|---:|---:|---:|---:|
| **Korean (held-out harness)** |  |  |  |  |  |
| KMMLU | 49.4 | 48.8 | 42.4 | 23.6 | 35.0 |
| KoBEST BoolQ | 90.2 | 87.7 | 78.8 | 74.3 | 79.6 |
| KoBEST COPA | 70.7 | 69.7 | 65.0 | 55.9 | 51.7 |
| KoBEST SentiNeg | 74.8 | 71.8 | 70.5 | 53.7 | 49.6 |
| KoBEST HellaSwag | 58.8 | 55.0 | 57.4 | 48.8 | 51.6 |
| **English reasoning / knowledge** |  |  |  |  |  |
| ARC-Challenge | 87.1 | 86.1 | 79.9 | 36.9 | 79.1 |
| HellaSwag (en) | 74.2 | 67.4 | 55.3 | 32.6 | 61.7 |
| WinoGrande | 67.4 | 65.6 | 59.2 | 53.1 | 63.5 |
| MMLU-Pro | 41.2 | 36.9 | 34.2 | 14.8 | 33.8 |
| TruthfulQA MC2 | 47.3 | 46.0 | 43.1 | 40.6 | 44.6 |
| MMLU-en | 69.7 | 64.5 | 56.6 | 30.1 | 59.6 |
| **Math** |  |  |  |  |  |
| GSM8K | 86.3 | 86.7 | 81.8 | 61.3 | 86.7 |
| MathQA | 30.5 | 29.1 | 24.8 | 21.3 | 28.7 |
| **Coding** |  |  |  |  |  |
| HumanEval+ | 81.1 | 75.6 | 74.4 | 65.2 | 80.5 |
| MBPP+ | 70.9 | 69.3 | 67.5 | 61.6 | 67.5 |
| LiveCodeBench v6 | 22.9 | 25.1 | 20.6 | 16.6 | 25.1 |
| **Safety / bias** |  |  |  |  |  |
| BBQ | 76.6 | 69.9 | 59.8 | 33.6 | 74.0 |
| SafetyBench | 74.8 | 73.0 | 69.1 | 44.3 | 72.1 |
| **Macro** |  |  |  |  |  |
| Korean MC macro | **68.8** | **66.6** | **62.8** | **51.2** | **53.5** |
| English reasoning / knowledge macro (6) | **64.5** | **61.1** | **54.7** | **34.7** | **57.0** |
| Math macro (2) | **58.4** | **57.9** | **53.3** | **41.3** | **57.7** |
| Safety / bias macro (2) | **75.7** | **71.5** | **64.5** | **39.0** | **73.0** |
| Overall non-Korean composite (10) | **65.5** | **62.5** | **56.4** | **36.9** | **60.4** |
| Coding 2-bench macro | **76.0** | **72.5** | **70.9** | **63.4** | **74.0** |
| Coding 3-bench macro | **58.3** | **56.7** | **54.1** | **47.8** | **57.7** |

Aggregate rows are unweighted arithmetic means. The overall non-Korean composite averages
six English reasoning/knowledge metrics, two math metrics, and two safety/bias metrics. The
coding 3-benchmark macro averages HumanEval+, MBPP+, and LiveCodeBench v6 pass@1. These mixed
summaries are compact internal comparisons, not standardized leaderboard scores.

## Compatibility

| Runtime or feature | Status |
|---|---|
| Transformers 5.0.0, PyTorch/CUDA, eager attention and eager Experts on DGX Spark | **Validated** |
| Native `from_pretrained(..., trust_remote_code=False)` loading | **Validated** |
| Speculative MTP/NextN decoding | **Unsupported (`mtp_compatible=false`)** |
| vLLM | **Untested for this pruned checkpoint** |
| SGLang | **Untested for this pruned checkpoint** |

- Architecture: `Glm4MoeLiteForCausalLM`.
- Model code: native Transformers implementation; no repository-side `modeling_*.py` is
  required, and the checkpoint loads with `trust_remote_code=False`.
- Preserved: first Dense layer, shared Experts, `topk_method=noaux_tc`,
  `norm_topk_prob=true`, router correction bias, and `routed_scaling_factor=1.8`.
- Routing: top-4 remains unchanged; only routed Expert tensors and corresponding router rows/bias
  entries were compacted with one old→new ID map per layer.
- The extra layer-47 MTP/NextN tensors are retained for checkpoint completeness, but runtime
  validation reports `mtp_compatible=false`. Use standard autoregressive generation; speculative
  MTP/NextN decoding is not supported by this release.
- Top-4 routing is unchanged, so the checkpoint-size and resident-weight reduction must not be
  interpreted as a proportional reduction in active Expert compute or latency. Cold-load time,
  TTFT, prefill/decode throughput, batch scaling, power, and 4K/32K/128K serving behavior have not
  been benchmarked.

## How it was made

### Source checkpoint

- Base: [zai-org/GLM-4.7-Flash](https://huggingface.co/zai-org/GLM-4.7-Flash)
- Frozen revision: `7dd20894a642a0aa287e9827cb1a1f7f91386b67`
- Original routed MoE layout: first layer Dense, then 46 routed MoE layers with 64 Experts,
  top-4 routing, plus shared Experts.

### Calibration dataset

| Group | Records | Role |
|---|---:|---|
| Korean/English semantic pairs | 2,752 | Korean↔English routing contrast |
| Common Korean | 2,752 | Korean routing coverage |
| General replay | 1,344 | General-capability retention |
| GLM-specialized | 1,344 | Documents, language retention, reasoning, security, structured output, tool calling |
| **Total** | **8,192** | **5,472 Korean / 2,720 English; 1,376 pairs** |

- 6,848 records contain source teacher responses.
- 1,344 GLM-specialized records use deterministic base-model rollouts.
- Prompt/response observations cover 3,898,756 token memberships.
- The manifest passed a separate internal token-length and exact-prompt contamination validator.
- The exact calibration manifest and deterministic reconstruction script are not included in this
  model repository, so the full GLM experiment is not yet externally reproducible from public
  materials alone.

### Observation and scoring

- Selected-only observer: only routed Expert assignments were measured; no dense
  `[experts, tokens, hidden]` activation tensor was retained.
- REAP contribution: normalized dispatch weight × L2 norm of the unweighted Expert output.
- Router selection and dispatch were checked separately so GLM's correction bias affects selection
  without being mistaken for the actual dispatch weight.
- The observed model remained logit-identical to the uninstrumented eager model in validation.

### Pruning

- Uniform routed Experts per layer: `64 → 56`.
- Shared Experts and the first Dense layer were not pruned.
- Top-4 and routed scaling factor 1.8 were retained.
- Safetensors surgery physically compacted Expert tensors, router rows, and correction-bias entries.
- Protection result: Satisfied in all 46 routed MoE layers; no protected Expert was force-dropped.

## Evaluation scope

These are **internal comparative evaluation results**, not standardized leaderboard numbers:

- KMMLU: deterministic 500-example subset (seed 42).
- KoBEST: declared BoolQ, COPA, SentiNeg, and HellaSwag evaluation splits.
- ARC-Challenge, HellaSwag-en, WinoGrande, MMLU-Pro, TruthfulQA MC2, MMLU-en, GSM8K, MathQA,
  BBQ, and SafetyBench: deterministic 512-example subsets.
- HumanEval+: full 164 tasks; MBPP+: frozen full 378-task revision; greedy pass@1.
- LiveCodeBench: full incremental v6 split (175 problems), n=1 greedy no-thinking generation,
  batch size 1, with official functional tests executed in an isolated ARM64 container. This
  protocol is not directly comparable to the official leaderboard's n=10 sampling protocol.
- The machine-readable field `decision_eligible=true` means that the run passed the project's
  internal screening checks. It is not an external certification. `release_eligible=false`.
- Do not compare these subset scores directly with full-set or few-shot leaderboard values.

Machine-readable results and the exact survivor manifest are included under `evaluation/`.

**Internal release-gate result:** The project plan's 12.5% gate allows at most -1.0 pp Korean macro
and -2.0 pp overall non-Korean composite. This checkpoint measured -2.2 pp and -3.0 pp, so it did
not pass the internal release criteria despite being the best tested GLM candidate. Some losses are
concentrated: HellaSwag-en, MMLU-en, and BBQ decline more than the aggregate suggests.

### Interpretation boundaries

- This grid does not isolate the causal effect of hard protection. KREAP and KREAP-Code differ in
  both calibration data and survivor-selection rules. A same-calibration REAP baseline and
  component ablations are still required.
- Machine-readable results include direct KREAP-48E versus KREAP-Code-48E McNemar tests for 11
  non-Korean binary/pass-fail tasks. Direct paired tests for the Korean benchmark set, aggregate
  bootstrap confidence intervals, multiple-comparison correction, and repeated calibration seeds
  are not included.
- `PASS` in the artifacts refers to checkpoint integrity and internal pipeline validation, not
  external replication.

## Usage

Install a Transformers release that includes `Glm4MoeLiteForCausalLM`:

```bash
pip install "transformers>=5.0.0" accelerate safetensors
```

The checkpoint was validated with Transformers 5.0.0 and NVIDIA PyTorch 25.09.
It uses the native Transformers model implementation and does not execute custom
code from this repository.

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "RAS-LAB/GLM-4.7-Flash-28B-A3B-KREAP"
tokenizer = AutoTokenizer.from_pretrained(
    model_id,
    trust_remote_code=False,
)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    dtype=torch.bfloat16,
    device_map="auto",
    trust_remote_code=False,
    attn_implementation="eager",
    experts_implementation="eager",
)
model.eval()

messages = [{"role": "user", "content": "한국어로 이진 탐색을 설명해줘."}]
prompt = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True,
    enable_thinking=False,
)
inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

with torch.inference_mode():
    output = model.generate(
        **inputs,
        max_new_tokens=256,
        do_sample=False,
        pad_token_id=tokenizer.eos_token_id,
    )

print(tokenizer.decode(output[0, inputs["input_ids"].shape[1]:], skip_special_tokens=True))
```

## Limitations

Expert pruning is irreversible within this checkpoint and can change routing behavior sharply on
tasks not represented by the calibration or evaluation sets. No post-pruning recovery or
fine-tuning was applied. Reported Korean behavior is relative to the tested base checkpoint and
harness; it does not imply universal Korean-language safety or quality preservation. The current
release is not validated for speculative MTP/NextN decoding.

The Korean evaluation is primarily multiple-choice. Korean long-form generation, summarization,
multi-turn dialogue, format-following, code explanation/debugging, factuality, hallucination,
safety, tool calling, JSON output, and long-context retrieval were not comprehensively evaluated.
Chinese capability is inherited from the base model but was not specifically protected or
evaluated after pruning. vLLM/SGLang compatibility and deployment performance remain unverified.

## Included research artifacts

- `evaluation/glm-full-b20-results-with-livecodebench.json`: machine-readable five-model full results
- `evaluation/glm-full-b20-long-scores.csv`: compact long-format B20 scores
- `evaluation/glm-full-b20-independent-validation.json`: independent B20 validation report
- `evaluation/survivor-manifest.json`: exact per-layer old Expert IDs retained
- `artifacts/calibration-validation.json`: separate internal calibration-manifest validation
- `artifacts/observation-validation.json`: selected-only observation validation
- `artifacts/expert-statistics.csv`: per-Expert scoring/features used for this method

- `artifacts/protected-experts.json`: exact KREAP protected set and evidence


## Provenance

- Base model: [zai-org/GLM-4.7-Flash](https://huggingface.co/zai-org/GLM-4.7-Flash), revision
  `7dd20894a642a0aa287e9827cb1a1f7f91386b67`
- Base license: MIT
- General method code: [K-REAP, commit `234666e`](https://github.com/Chedrian07/K-REAP/tree/234666e0dde8714b0c61f36b67f6f9f053c02d07)
- Reproducibility note: the linked repository documents K-REAP and its public adapters, but the
  exact GLM-specific observation pipeline, run configuration, and evaluation manifests used for
  this checkpoint are not yet published there.
- Team: [RAS-LAB](https://huggingface.co/RAS-LAB)
- Benchmark report SHA256: `71ab2ce742bf8a481d90d10c8b8684a918241fd475729b0bf2afe56b44335dd6`
- Model card generated from an internally validated benchmark artifact with zero validation
  failures; this is not an external reproduction claim.

## Citation

Please cite the base checkpoint, REAP, and K-REAP when using this model:

```bibtex
@misc{zai2026glm47flash,
  title        = {GLM-4.7-Flash},
  author       = {{Z.ai}},
  year         = {2026},
  howpublished = {\url{https://huggingface.co/zai-org/GLM-4.7-Flash}},
  note         = {Base revision 7dd20894a642a0aa287e9827cb1a1f7f91386b67}
}

@article{lasby2025reap,
  title   = {REAP the Experts: Why Pruning Prevails for One-Shot MoE Compression},
  author  = {Lasby, Mike and Lazarevich, Ivan and Sinnadurai, Nish and Lie, Sean and Ioannou, Yani and Thangarasa, Vithursan},
  journal = {arXiv preprint arXiv:2510.13999},
  year    = {2025},
  doi     = {10.48550/arXiv.2510.13999}
}

@software{chedrian07_2026_kreap,
  author  = {Chedrian07},
  title   = {K-REAP: Language-preserving one-shot MoE expert pruning},
  year    = {2026},
  url     = {https://github.com/Chedrian07/K-REAP},
  version = {234666e0dde8714b0c61f36b67f6f9f053c02d07}
}
```
