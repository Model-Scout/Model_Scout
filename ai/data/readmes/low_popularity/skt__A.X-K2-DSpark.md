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
  - dspark
  - draft-model
  - axk2
---

# A.X K2 DSpark

<p align="center">
  <a href="https://huggingface.co/collections/skt/ax-k2">🤗 Models</a> |
  <a href="https://github.com/SKT-AI/A.X-K2">🖥️ Github</a> |
  <a href="https://github.com/SKT-AI/A.X-K2/blob/main/A_X_K2_Tech_Report.pdf">📄 Technical Report</a>
</p>

## Model Summary

**A.X K2 DSpark** is a [DSpark](https://arxiv.org/abs/2607.05147) speculative-decoding draft model for [**A.X K2**](https://huggingface.co/skt/A.X-K2), SK Telecom's 688B-total / 33B-active Mixture-of-Experts foundation model.

DSpark accelerates decoding through semi-autoregressive drafting: it proposes multiple candidate tokens in parallel using hidden representations from A.X K2 together with lightweight local dependency modeling. The proposed tokens are then verified by A.X K2 before being committed.

When paired with A.X K2, the draft is designed to improve decoding throughput and latency without changing the target model's output distribution.

This is a **drafter-only** checkpoint: it has no standalone use and is intended to be loaded by vLLM alongside A.X K2 through speculative decoding.

## Key Features

* **DSpark Semi-Autoregressive Drafting**
  Proposes multiple candidate tokens in parallel rather than generating the entire draft sequence strictly autoregressively, reducing proposal latency for large target models.

* **Target Hidden-State Conditioning**
  Uses intermediate representations from the frozen A.X K2 target model to produce draft features closely aligned with the target distribution.

* **Local Dependency Modeling**
  Introduces lightweight dependencies between candidate positions (a Markov head) to improve draft consistency while preserving parallel proposal generation.

* **Adaptive Verification**
  Supports confidence-aware speculative verification so the serving runtime can reduce unnecessary verification work for low-confidence draft positions.

* **A.X K2 Native Integration**
  Designed specifically for A.X K2's MoE architecture and attention structure, and developed for A.X K2's 256K configuration.

* **Lossless by Construction**
  Every speculative candidate is verified by A.X K2 before being committed. The draft changes decoding efficiency, not the target model's sampling distribution.

## Model Details

| Property                              | Value                                                                                   |
| ------------------------------------- | --------------------------------------------------------------------------------------- |
| Architecture                          | DSpark (3-layer Qwen3-style draft + Markov head + confidence head)                      |
| Target model                          | [skt/A.X-K2](https://huggingface.co/skt/A.X-K2)                                         |
| Target size                           | 688B total / 33B active                                                                 |
| Context length                        | 262,144 tokens (256K)                                                                    |
| Draft vocabulary                      | 32,768 (reduced; mapped back to A.X K2's 163,840 vocab)                                 |
| Block size (num_speculative_tokens)   | 5                                                                                        |
| Checkpoint precision                  | BF16                                                                                     |
| Checkpoint size                       | ~6.8 GB                                                                                  |
| Recommended speculative configuration | `{"method": "dspark", "model": "skt/A.X-K2-DSpark", "num_speculative_tokens": 5}`       |

## Evaluation Results

Measured against A.X K2 served **without** speculative decoding, on an internal evaluation suite spanning Korean, English, math, science, and code (20 samples per task, greedy decoding, single-stream / batch = 1). A multimodal task and a long-context task are excluded from the aggregate (a text-only draft yields little benefit on multimodal inputs).

| Metric                       | Result (vs. no speculative decoding) |
| ---------------------------- | ------------------------------------ |
| Throughput (single-stream)   | ~1.8×                                |
| Time-per-output-token (TPOT) | ~−44%                                |
| Mean accepted length         | 2.42                                 |

At higher concurrency, confidence-scheduled verification trims low-confidence draft positions and further improves **aggregate throughput** (≈ +40% over fixed-block drafting in internal batched runs).

Per-task acceptance length and single-stream speedup:

| Task           | Accepted length | Speedup |
| -------------- | --------------- | ------- |
| aime (math)    | 2.95            | 1.78×   |
| apex-shortlist | 2.52            | 1.91×   |
| apex           | 2.70            | 2.04×   |
| click          | 1.97            | 1.49×   |
| gpqa           | 2.44            | 1.85×   |
| hle            | 2.44            | 1.84×   |
| ifbench        | 1.93            | 1.44×   |
| kmmlu-pro      | 2.11            | 1.61×   |
| kmo (math)     | 2.83            | 2.13×   |
| kobalt         | 2.20            | 1.67×   |
| livecodebench  | 2.58            | 1.89×   |
| scicode        | 2.38            | 1.74×   |

Speedup is workload-dependent and varies with concurrency, output length, and draft acceptance; acceptance is strongest on structured outputs (math/code) and lower on short multiple-choice answers.

**Output quality is unaffected when exact speculative verification is used**, because every committed token is verified by A.X K2 itself.

## Usage

### vLLM

A.X K2 DSpark is served through the same [SKT-AI/vllm](https://github.com/SKT-AI/vllm) fork used for A.X K2.

```bash
git clone -b axk2-v0.23.0 https://github.com/SKT-AI/vllm.git
cd vllm
pip install -e .
```

Add a `--speculative-config` argument to the existing A.X K2 serving command:

```bash
vllm serve skt/A.X-K2 \
    --trust-remote-code \
    --tensor-parallel-size 8 \
    --tool-call-parser hermes \
    --reasoning-parser deepseek_v3 \
    --no-async-scheduling \
    --speculative-config '{
        "method": "dspark",
        "model": "skt/A.X-K2-DSpark",
        "num_speculative_tokens": 5
    }'
```

A few things worth knowing before deployment:

* **`--no-async-scheduling` is required.** Confidence-scheduled (dynamic-length) drafting proposes a variable number of tokens per request, which is incompatible with async scheduling in this vLLM version.
* **Confidence threshold.** The draft truncates block positions whose predicted acceptance probability falls below a threshold (default `0.3`, carried in this repo's `config.json`). Override at serve time with the `DSPARK_CONF_THRESHOLD` environment variable; set it to `0` to disable dynamic truncation (fixed-block drafting).
* **256K target configuration.** This draft is developed for A.X K2's native 256K context configuration.
* **Workload-dependent speedup.** Gains depend on concurrency, output length, acceptance rate, and the relative cost of drafting and verification.

## Intended Use

A.X K2 DSpark is a serving-time accelerator for A.X K2 and is released under Apache-2.0 for the same research and commercial uses as A.X K2 itself.

It has no independent function outside of that pairing: use it wherever you serve A.X K2 and want faster decoding at unchanged output quality.

## Out-of-Scope Use

This draft has not been validated with any target other than A.X K2 and should not be assumed compatible with unrelated models or incompatible A.X K2 variants.

All intended-use and out-of-scope guidance for [A.X K2](https://huggingface.co/skt/A.X-K2#out-of-scope-use) itself applies equally here, since the draft does not change what A.X K2 generates.

## Limitations

* **Target-specific.** Trained specifically for A.X K2 and not intended as a standalone model.
* **Workload-dependent speedup.** Benefits depend on draft acceptance, output length, concurrency, and serving configuration.
* **Modality.** As a text draft, it provides little benefit on multimodal inputs.

## Contact

For questions about A.X K2 DSpark — including compatibility, deployment, and licensing — contact the A.X team at **[a.x@sk.com](mailto:a.x@sk.com)**.

Please send reports of vulnerabilities, harmful outputs, suspected misuse, or copyright infringement claims to the same address.

## Citation

If you use A.X K2 DSpark in your research, please cite the A.X K2 technical report:

```bibtex
@techreport{axk2-2026,
      title={A.X K2 Technical Report},
      author={SK Telecom},
      year={2026},
      institution={SK Telecom},
      url={https://github.com/SKT-AI/A.X-K2/blob/main/A_X_K2_Tech_Report.pdf},
}
```
