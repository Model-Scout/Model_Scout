---
license: apache-2.0
language:
  - en
  - ko
base_model: skt/A.X-K2
pipeline_tag: text-generation
library_name: vllm
tags:
  - speculative-decoding
  - eagle3
  - draft-model
  - axk2
---

# A.X K2 EAGLE3

<p align="center">
  <a href="https://huggingface.co/collections/skt/ax-k2">🤗 Models</a> |
  <a href="https://github.com/SKT-AI/A.X-K2">🖥️ Github</a> |
  <a href="https://github.com/SKT-AI/A.X-K2/blob/main/A_X_K2_Tech_Report.pdf">📄 Technical Report</a>
</p>

## Model Summary

**A.X K2 EAGLE3** is an EAGLE3 speculative-decoding draft model for [**A.X K2**](https://huggingface.co/skt/A.X-K2), SK Telecom's 688B-total / 33B-active Mixture-of-Experts foundation model.

Paired with A.X K2 at its native 256K context, the draft accelerates decoding by proposing multiple candidate tokens per step that A.X K2 verifies in a single forward pass, without changing what the target model would have generated on its own. In production-traffic serving it delivers up to **1.64× throughput** and **28% lower time-per-output-token**, with the largest gains at low-to-moderate concurrency.

This is a **drafter-only** checkpoint: it has no standalone use and is loaded automatically by vLLM alongside A.X K2 as a `--speculative-config` argument.

## Key Features

- **EAGLE3 Architecture**
  Built on [`Eagle3DeepseekV2ForCausalLM`](https://huggingface.co/docs/transformers/main/en/model_doc/deepseek_v2), a single-layer MLA decoder that consumes three auxiliary hidden states from A.X K2's layers 2, 30, and 58 (early / middle / late signal) and combines them through a per-auxiliary-state RMSNorm (`fc_norm`) before the fusion layer.
- **256K-Native, RoPE-Matched to A.X K2**
  The draft's YaRN RoPE parameters (factor 2.0, original context 131,072, θ = 1e6) are tuned to match A.X K2's 256K configuration exactly. It is intended for use with A.X K2 at 256K and has not been validated against other context-length or RoPE configurations.
- **Full, Unpruned Vocabulary**
  `draft_vocab_size` equals A.X K2's full 163,840-token vocabulary, so no target-to-draft ID remapping is needed at the logits boundary.
- **Lossless by Construction**
  As with any EAGLE-style draft, every proposed token is verified by A.X K2 itself; the draft only changes decoding speed, not the distribution A.X K2 samples from.

## Model Details

| Property | Value |
|----------|-------|
| Architecture | Eagle3DeepseekV2 (1-layer MLA decoder) |
| Target model | [skt/A.X-K2](https://huggingface.co/skt/A.X-K2) (256K, fused attention gate) |
| Hidden size | 7168 |
| Auxiliary hidden-state layers | 2, 30, 58 (of A.X K2's 61 layers) |
| Combine-layer normalization | Per-auxiliary-state RMSNorm before `fc` (`fc_norm: true`) |
| Vocab size | 163,840 (unpruned, matches target) |
| Context length | 262,144 tokens (256K), YaRN factor 2.0 |
| Checkpoint precision | fp16 |
| Checkpoint size | ~5.6 GiB |
| Recommended `num_speculative_tokens` | 3 |

## Evaluation Results

Measured on production-representative mixed traffic (`k=3`, concurrency 16) against A.X K2 serving without a draft:

| Metric | Result |
|---|---|
| Throughput | **1.64×** |
| Time-per-output-token (TPOT) | **−28%** (36.9 → 26.5 ms) |
| Mean accepted length | 2.24 tokens/step |

Speedup is workload-dependent and concentrated in the memory-bandwidth-bound regime:

- **At low-to-moderate concurrency** (roughly 1–4 concurrent sequences), TPOT improves by up to **~2×**.
- **At saturated concurrency**, where decoding is already compute-bound, the extra draft/verify forward passes can cost throughput rather than gain it — expect **up to ~10% lower** throughput in that regime.
- **Per-domain speedup** varies with how much of each response is decode-bound: Korean **2.44×**, math **1.67×**, science **1.51×**, code **1.13×** (code responses tend to be short, leaving less room for the draft to pay off).

## Usage

### vLLM

A.X K2 EAGLE3 is served through the same [SKT-AI/vllm](https://github.com/SKT-AI/vllm) fork used for A.X K2 itself — upstream vLLM **v0.23.0** plus A.X K2 support:

```bash
git clone -b axk2-v0.23.0 https://github.com/SKT-AI/vllm.git
cd vllm
pip install -e .   # see the vLLM docs for build prerequisites
```

Add a single `--speculative-config` argument to your existing A.X K2 serving command — everything else stays the same:

```bash
vllm serve skt/A.X-K2 --tensor-parallel-size <N> \
    --tool-call-parser hermes \
    --reasoning-parser deepseek_v3 \
    --speculative-config '{"method": "eagle3", "model": "skt/A.X-K2-EAGLE3", "num_speculative_tokens": 3}'
```

A few things worth knowing before you turn this on in production:

- **256K target only.** This draft's RoPE is tuned specifically for A.X K2's 256K configuration; don't pair it with a different context-length or RoPE variant of A.X K2 if SKT publishes one later.
- **Data-parallel serving.** Speculative decoding under `--data-parallel-size > 1` with async scheduling has a known upstream vLLM failure mode: if one DP rank's request exceeds the draft's usable context while a peer rank's does not, that rank skips its draft forward and drops the collectives the other ranks still issue, desynchronizing the DP group into a hang (`RPC call to sample_tokens timed out`; tracked upstream at [vllm-project/vllm#44954](https://github.com/vllm-project/vllm/pull/44954)). The `axk2-v0.23.0` branch carries this fix, so DP deployments on the current branch do not need a workaround.

## Intended Use

A.X K2 EAGLE3 is a serving-time accelerator for A.X K2 and is released under Apache-2.0 for the same research and commercial uses as A.X K2 itself. It has no independent function outside of that pairing: use it wherever you serve A.X K2 at 256K and want lower latency at unchanged output quality.

## Out-of-Scope Use

This draft has not been validated with any target other than A.X K2 at 256K, and should not be assumed compatible with future A.X K2 variants at different context lengths or with unrelated models. All intended-use and out-of-scope guidance for [A.X K2](https://huggingface.co/skt/A.X-K2#out-of-scope-use) itself applies equally here, since the draft does not change what A.X K2 generates.

## Contact

For questions about A.X K2 EAGLE3 — including compatibility, deployment, and licensing — contact the A.X team at **[a.x@sk.com](mailto:a.x@sk.com)**. Please send reports of vulnerabilities, harmful outputs, suspected misuse, or copyright infringement claims to the same address.

## Citation

If you use A.X K2 EAGLE3 in your research, please cite the A.X K2 technical report:

```bibtex
@techreport{axk2-2026,
      title={A.X K2 Technical Report},
      author={SK Telecom},
      year={2026},
      institution={SK Telecom},
      url={https://github.com/SKT-AI/A.X-K2/blob/main/A_X_K2_Tech_Report.pdf},
}
```
