---
license: other
license_name: lfm-open-license-v1.0
license_link: LICENSE
library_name: transformers
pipeline_tag: text-generation
base_model: HCHs/RivetCoder-9B-A4B
base_model_relation: quantized
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
  - fp8
  - torchao
  - top-k-routing
  - trust-remote-code
---

# RivetCoder-9B-A4B-FP8

RivetCoder-9B-A4B-FP8 is the TorchAO FP8 deployment build of
[`HCHs/RivetCoder-9B-A4B`](https://huggingface.co/HCHs/RivetCoder-9B-A4B).
It keeps the same experimental coding-oriented architecture: a frozen
`LiquidAI/LFM2.5-2.6B` host plus 16 layer-qualified GLM-derived FFN candidates
at each of 30 layers, with Top-4 routing per token.

This repository contains custom Transformers code and must be loaded with
`trust_remote_code=True`.

## FP8 format

The checkpoint was quantized with TorchAO
`Float8DynamicActivationFloat8WeightConfig` using E4M3 FP8 weights and dynamic
FP8 activations for compatible `nn.Linear` modules.

| Item | Value |
|---|---:|
| Source revision | `9a90b1917d9b5438e4d2fe1a4f6aea884db59a60` |
| Approx. total parameters | 8.74B |
| Approx. active parameters | 4.21B |
| FP8 tensor-subclass parameters | 1,636 |
| FP8-quantized parameter elements | 8,475,574,272 |
| Stored tensor bytes | 9,000,638,976 |
| Safetensors shards | 5 |
| Tested resident CUDA allocation | about 8.4 GiB |

Embeddings, convolution parameters, token gates, correction biases, residual
scales, and other small or precision-sensitive tensors remain BF16 or FP32.
Router projection matrices are FP8, while the custom router still computes its
logits in FP32. “FP8” therefore describes compatible Linear matrices, not every
scalar in the checkpoint.

## Installation

The exact local stack used to create and validate this build was PyTorch
`2.12.0+cu130`, Transformers `5.16.1`, Accelerate `1.13.0`, Safetensors `0.8.0`,
and TorchAO `0.15.0` on an NVIDIA GeForce RTX 5070 Ti (SM 12.0).

```bash
pip install "torch>=2.12,<2.13" "transformers>=5.16.1,<5.17" "accelerate>=1.13" \
  "safetensors>=0.8" "torchao==0.15.0"
```

## Usage

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "HCHs/RivetCoder-9B-A4B-FP8"

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    trust_remote_code=True,
    device_map=0,
    dtype=torch.bfloat16,
).eval()

messages = [{
    "role": "user",
    "content": "Implement merge_intervals in Python and include concise tests.",
}]
inputs = tokenizer.apply_chat_template(
    messages,
    add_generation_prompt=True,
    return_tensors="pt",
    return_dict=True,
).to("cuda")

# Use no_grad with the tested TorchAO/PyTorch stack.
with torch.no_grad():
    output = model.generate(
        **inputs,
        max_new_tokens=1024,
        temperature=0.2,
        do_sample=True,
    )

print(tokenizer.decode(
    output[0, inputs["input_ids"].shape[-1]:],
    skip_special_tokens=True,
))
```

The bundled chat template opens a reasoning segment before the final answer.
Allocate enough output tokens for both reasoning and code.

## Validation

The saved FP8 tensors were independently reloaded entirely on one RTX 5070 Ti.
The clean reload took about 338 seconds, found no CPU or `meta` parameters, and
restored all 1,636 FP8 parameters. A separate six-token forward pass produced
finite logits with shape `(1, 6, 128000)`.

On the tested Windows stack, `torch.inference_mode()` is incompatible with the
TorchAO FP8 tensor subclass and raises a version-counter error. Use
`torch.no_grad()` as shown above.

TorchAO 0.15.0 also reports that its optional C++ extensions are skipped with
the tested PyTorch 2.12 build. The native CUDA FP8 path used by this checkpoint
still passed quantization, serialization, clean reload, and forward validation.

## Fast grouped-FP8 serving

The repository includes an inference-only Triton runtime that replaces the
Python 16-expert loop with two grouped FP8 GEMMs per fused layer: one combined
gate/up projection and one down projection. It also bypasses TorchAO's
tensor-subclass dispatch for 196 remaining compatible FP8 Linear modules and
calls their existing qdata/scales through `_scaled_mm` directly. It preserves
Top-4 routing and the reference FP8 logits while releasing the unpacked expert
tensors after runtime packing.

For direct Transformers use, enable it after loading:

```python
runtime_report = model.enable_fast_fp8_serving()
print(runtime_report)
```

For an OpenAI-compatible, queue-to-completion microbatch server:

```powershell
pip install -r requirements-serve.txt
python serve.py `
  --model HCHs/RivetCoder-9B-A4B-FP8 `
  --no-local-files-only `
  --host 0.0.0.0 `
  --port 8000 `
  --max-batch-size 16 `
  --batch-wait-ms 3
```

On Windows, the first Triton JIT requires Visual Studio 2022 C++ Build Tools.
The runtime automatically imports the installed Developer environment and
records the resolved `cl.exe` path in its startup report. The first request for
a new shape includes autotuning; later calls use the Triton cache.

RTX 5070 Ti validation with a one-token full forward produced:

| Runtime | Latency | Relative throughput |
|---|---:|---:|
| Original TorchAO path | 4.894 s | 1.00x |
| Grouped/direct-FP8 fast path | 0.304 s | 16.08x |

The logits were bit-exact (`MAE=0`, `max error=0`, identical top-1), repeated
execution was deterministic, and resident VRAM was about 8.43 GiB. With the
fast path enabled, fixed microbatch throughput scaled as follows:

| Batch | Forward latency | Sequences/s |
|---:|---:|---:|
| 1 | 0.337 s | 2.96 |
| 4 | 0.316 s | 12.65 |
| 8 | 0.340 s | 23.50 |
| 16 | 0.309 s | 51.71 |

These are local full-forward measurements, not standardized generation
benchmarks. Batch 16 increased throughput about 17.5x over batch 1 without a
latency increase in this short test, which is why the bundled server defaults
to batch 16.

## Limitations

- This is an experimental fusion with only 60 routing-control optimizer steps.
- HumanEval, MBPP, SWE-bench, and broad regression results have not been reported.
- The fixed GLM-to-LFM bridge is deterministic and was not learned.
- This TorchAO checkpoint is not a GGUF file and is not directly compatible
  with llama.cpp, LM Studio, or Ollama.
- Hardware and software combinations other than the tested stack may need
  additional compatibility work.
- The bundled server does not stream tokens and batches only requests with the
  same generation parameters.

See `provenance/quantization.json` and `provenance/fast-serving.json` for the
local quantization, placement, parity, and throughput reports. Architecture,
source-model, expert-selection, and router-training provenance are retained
from the BF16 repository.

## License and attribution

The LFM host remains subject to the included LFM Open License v1.0. GLM-derived
expert tensors retain the included MIT license and attribution. The grouped FP8
Triton kernels are adapted from Hugging Face's Apache-2.0
`kernels-community/finegrained-fp8`. Review `LICENSE`, `NOTICE.md`, and
`licenses/` before redistribution or deployment.
