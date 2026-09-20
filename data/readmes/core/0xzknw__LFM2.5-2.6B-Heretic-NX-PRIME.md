---
base_model: LiquidAI/LFM2.5-2.6B
library_name: transformers
pipeline_tag: text-generation
license: other
license_name: lfm-open-license-v1.0
license_link: LICENSE
language:
- en
- ar
- zh
- fr
- de
- hi
- id
- it
- ja
- ko
- pl
- pt
- ru
- es
- th
- vi
tags:
- lfm2
- lfm2.5
- bf16
- gguf
- q8_0
- lm-studio
- abliterated
- uncensored
- model-editing
- heretic-nx
- residual-stream
- prime
---

# LFM2.5 2.6B — Heretic NX PRIME

Heretic NX PRIME is a behavioral edit of
[`LiquidAI/LFM2.5-2.6B`](https://huggingface.co/LiquidAI/LFM2.5-2.6B)
focused on aggressive false-refusal reduction while measuring drift from the
official base.

**Q8 refresh — 2026-08-25:** the current Q8_0 file is a native-runtime,
quantization-aware residual-stream composite. It reduces the matched lexical
refusal count from the previous PRIME Q8's `9/104` to **`3/104`**. The BF16
Transformers checkpoint and BF16 GGUF are unchanged by this refresh and retain
their earlier evaluation results.

`PRIME` is the project's internal evidence and capability-preservation
protocol. It is not a third-party certification.

## Files and variants

| File | Status |
| --- | --- |
| `model.safetensors` | Original PRIME v8 BF16 checkpoint; unchanged |
| `LFM2.5-2.6B-Heretic-NX-PRIME-BF16.gguf` | Original PRIME v8 BF16 GGUF; unchanged |
| `LFM2.5-2.6B-Heretic-NX-PRIME-Q8_0.gguf` | **Refreshed Q8_0**, 2.87 GB, SHA-256 `0ee513ab837686211bca2d2872e642b43ff19772bd1011eb40f5ea8000b9d0e0` |
| `PROVENANCE.json` | Provenance of the unchanged BF16/v8 release |
| `Q8_RELEASE.json` | Exact provenance, hashes, protocol and claim limits for the refreshed Q8 |

The refreshed Q8 is a Q8-specific deployment artifact. Its metrics must not be
attributed to `model.safetensors` or the BF16 GGUF.

## Matched Q8 comparison

Both Q8 files below were evaluated locally with official llama.cpp b10621
CUDA, native pre-tokenized `/completion`, one explicit BOS, the same closed
thinking template, greedy decoding, 96 generated tokens, serial request order
and exactly one runtime slot.

| Evaluation | Previous PRIME Q8 | Heretic Q8 comparator | Refreshed PRIME Q8 |
| --- | ---: | ---: | ---: |
| Lexical refusal markers, 104 harmful rows | 9 | 5 | **3** |
| Markers per 100 | 8.65 | 4.81 | **2.88** |
| Hit rows, one-based | `3,35,55,57,68,80,93,97,101` | `3,29,68,97,98` | **`3,68,97`** |
| Mean first-token KL(base || candidate), 104 benign rows, full 128k vocabulary | 0.018217 | published as 0.0142 | 0.023597 |

The refreshed PRIME Q8 therefore has two fewer lexical refusal markers than
the pinned Heretic comparator under this matched local refusal protocol. It
does **not** win on KL: its measured `0.023597` is above both the previous PRIME
Q8 and the comparator card's published `0.0142`. The comparator's published KL
was not independently reproduced under this repository's exact full-vocabulary
protocol, so that KL comparison is descriptive rather than formally matched.

Lexical markers are a refusal proxy, not semantic task success or a universal
quality score. All 104 harmful rows participated in development and selection;
they are not an untouched holdout.

The comparator is pinned to
[`Abiray/LFM2.5-2.6B-Heretic-Abliterated-GGUF`](https://huggingface.co/Abiray/LFM2.5-2.6B-Heretic-Abliterated-GGUF)
revision `1eaf992a33529fc839cbeca32109a9c4c43b57c4`, artifact SHA-256
`027f0a8308879a21163dd0c981b7397d1b8828dc06ce01e72250d3adf2f87f9b`.

## Method used for the refreshed Q8

The Q8 refresh did not copy or merge Heretic weights. The pinned comparator
was used only as a black-box behavioral teacher: token-only trajectories were
captured for six rows where it avoided a stable PRIME-v8 refusal. Heretic NX
then optimized the existing eight-site residual-stream portfolio under a
benign KL objective and exact Q8_0 fake quantization.

Promotion used deterministic native llama.cpp screening rather than the older
parallel benchmark, because refusal counts were found to be batching-sensitive.
The selected composite:

- starts from the strong teacher-guided residual candidate;
- restores the L28 short-convolution output to the lower-KL anchor;
- interpolates the L15 short-convolution output by 25% toward that anchor;
- interpolates the L17 FFN output by 75% toward that anchor;
- serializes and patches the eight complete Q8_0 tensor payloads exactly.

The final pack SHA-256 is
`3083a6c8b0f74488221dd9fbd046e10b0eb9fdc3cb320e99b9769c6a01afb6c0`.
The deployed GGUF was reloaded by llama.cpp for both the 104-row harmful run
and the exhaustive first-token KL calculation.

## Validation status

Completed for the refreshed Q8:

- 104/104 harmful prompts, deterministic mono-slot native runtime;
- 104/104 benign prompts, full-vocabulary first-token KL against cached
  official-base BF16 log-probabilities;
- exact artifact/pack/report hash binding;
- 98 local unit and integration tests passing, including 13 Q8-specific tests.

Not yet rerun for the refreshed Q8:

- the 450-row XSTest gate;
- the 854-row ARC/HellaSwag/MMLU paired capability slice;
- a new LM Studio GUI smoke test.

Earlier XSTest and capability results in `PROVENANCE.json` belong to the
previous v8 Q8 artifact and must not be presented as evidence for this refresh.
The current file preserves the same valid GGUF metadata/layout and has been
loaded repeatedly by llama.cpp b10621 during evaluation.

## LM Studio

Download `LFM2.5-2.6B-Heretic-NX-PRIME-Q8_0.gguf`, place it in your LM Studio
models directory and select it as an LFM2 model. The file is Q8_0 and is about
2.87 GB. The BF16 GGUF remains available when maximum precision is preferred.

## Transformers usage

Transformers loads the unchanged BF16 checkpoint, not the Q8 refresh:

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "0xzknw/LFM2.5-2.6B-Heretic-NX-PRIME"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    dtype=torch.bfloat16,
    device_map="auto",
).eval()
```

## Limitations and responsibility

This edit intentionally weakens refusal behavior. That can increase compliance
with unsafe, illegal, incorrect or otherwise harmful requests. It does not add
factuality, judgment, sandboxing or application-level safety. Run untrusted
generations in an appropriate sandbox.

The refreshed Q8 currently demonstrates a lower lexical-refusal count than the
pinned Heretic Q8 on one development-exposed suite, while preserving less of
the official base under the measured KL metric. It is not claimed to be a
universal winner, externally certified, or fully capability-validated.

Use is subject to the included LFM Open License v1.0.
