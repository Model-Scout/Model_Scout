---
license: other
license_name: lfm-open-license-v1.0
license_link: LICENSE
library_name: transformers
pipeline_tag: text-generation
base_model:
  - LiquidAI/LFM2.5-2.6B
  - zai-org/GLM-5.3-Flash
base_model_relation: merge
language:
  - en
  - ko
  - code
tags:
  - custom_code
  - lfm2
  - glm
  - mixture-of-experts
  - routed-experts
  - coding
  - code-generation
  - agentic
  - bf16
  - top-k-routing
  - trust-remote-code
---

# RivetCoder-9B-A4B

RivetCoder-9B-A4B is an experimental coding-oriented routed-expert model. It keeps
`LiquidAI/LFM2.5-2.6B` as a frozen 30-layer host and adds 480 frozen FFNs derived
from `zai-org/GLM-5.3-Flash`. Each host layer owns 16 layer-qualified candidates;
four are routed per token.

The model uses custom Transformers code and must be loaded with
`trust_remote_code=True`.

## Model details

| Item | Value |
|---|---:|
| Host | LiquidAI/LFM2.5-2.6B |
| Expert donor | zai-org/GLM-5.3-Flash |
| Router teacher | qwen/qwen3.8-27b via local LM Studio |
| Host layers | 30 |
| Candidate experts | 16 per layer, 480 total |
| Active experts | Top-4 per token |
| Folded expert shape | 2048 → 2048 → 2048 |
| Approx. total parameters | 8.74B |
| Approx. active parameters | 4.21B |
| Stored tensor bytes | 17,478,172,784 |
| Routing-control training | 60 optimizer steps |

The fixed bridge is `P = [I; H] / sqrt(2)`, where `H` is a normalized,
signed, deterministically permuted order-2048 Hadamard matrix. `P_out = P.T`
and `P.T @ P ≈ I`. The bridge is folded into the expert and router weights and
is not present as a runtime module.

The GLM post-sigmoid expert-choice correction is preserved as a frozen buffer.
It affects Top-K selection only; mixture weights are gathered from the
uncorrected sigmoid scores.

## Installation

```bash
pip install "transformers>=5.16.1,<5.17" "torch>=2.12" "accelerate>=1.13" safetensors
```

## Usage

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "HCHs/RivetCoder-9B-A4B"

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    trust_remote_code=True,
    dtype="auto",
    device_map="auto",
)

messages = [
    {
        "role": "user",
        "content": "Implement an LRU cache in Python and include concise tests.",
    }
]
inputs = tokenizer.apply_chat_template(
    messages,
    add_generation_prompt=True,
    return_tensors="pt",
    return_dict=True,
).to(model.device)

with torch.no_grad():
    output = model.generate(
        **inputs,
        max_new_tokens=512,
        temperature=0.2,
        do_sample=True,
    )

print(tokenizer.decode(output[0][inputs["input_ids"].shape[-1]:], skip_special_tokens=True))
```

The BF16/mixed-FP32 checkpoint is about 16.3 GiB. A single 16 GiB GPU generally
requires CPU/disk placement through `device_map="auto"` or another offload
strategy.

To run the unmodified LFM host path for comparison:

```python
model.set_coding_enabled(False)
```

## Expert selection and router training

GLM router behavior was profiled on 4,119 coding tokens covering Python,
TypeScript, Go, Rust, Java, C++, and SQL. For each sparse donor layer, 16 experts
were selected using the deterministic rank score:

```text
2 × frequency_rank + 3 × weighted_route_mass_rank
```

The provisional monotonic-depth mapping assigns one donor layer to every LFM
layer. Selected experts and the LFM host remain frozen.

Routing controls were trained from Qwen-generated assistant responses:

- 20 coding conversations for training;
- 4 held-out coding conversations;
- 8 generic-control conversations;
- assistant-token-only causal loss through the LFM chat template;
- frozen-host self-KL and generic token-gate suppression;
- trainable tensors: router weights, token gates, and bounded residual scales.

On the small held-out set (1,417 assistant tokens), assistant CE changed from
`0.605825` for the expert-off host to `0.601436` for the fused model. This is a
small internal routing check, not a standardized coding benchmark.

The frozen-host expert-off path remained bitwise identical after training.

## Limitations

- This is an experimental custom architecture, not a stock LFM2 checkpoint.
- Evaluation currently consists of a very small held-out routing set; HumanEval,
  MBPP, SWE-bench, and broader regression results have not been reported.
- The bridge is deterministic and untrained, so donor/host representation
  mismatch can limit transferred expertise.
- The layer mapping is normalized-depth based rather than activation-alignment
  based.
- Soft token gating is enabled at inference. Hard thresholding is disabled
  because the learned gates were not calibrated for a `0.5` compute-skip cutoff.
- CPU expert execution is substantially slower than a dedicated grouped-GEMM
  kernel.

## Licenses and attribution

The overall checkpoint is distributed subject to the **LFM Open License v1.0**
in [`LICENSE`](LICENSE), inherited from the LFM host. Review that license before
redistribution or commercial use.

In particular, the LFM license does not grant commercial-use rights to a legal
entity whose annual revenue exceeds USD 10 million. Consult the complete license;
this summary is not legal advice.

The GLM-derived expert weights originate from `zai-org/GLM-5.3-Flash`, whose MIT
license is included at [`licenses/GLM-MIT.txt`](licenses/GLM-MIT.txt).

`qwen/qwen3.8-27b` was used only as a sequence-level teacher for router-control
training. No Qwen model weights are included in this repository.

Detailed, path-sanitized source revisions, selection rules, hashes, folding
checks, and training metrics are available under [`provenance/`](provenance/).

## Reproducibility anchors

```text
Combined weight index SHA-256:
939b9f2bf0c48523d6a1a2ef93d987876a3e20613b33fe3715bf6b78bbc2a1bb

Routing controls SHA-256:
740f15e9bcf68efcb4d9c0f4b2bcfebff66ba199aead9cd2666156dffc60b1ad

Training run fingerprint:
68f9fa90e18e180f7037dea5e057aa296c95b59267aa09f38285363b5e517c2a
```
