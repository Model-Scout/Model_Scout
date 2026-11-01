---
license: other
license_name: lfm-open-license-v1.0
license_link: https://huggingface.co/HCHs/RivetCoder-9B-A4B-GGUF/blob/main/LICENSE
library_name: gguf
pipeline_tag: text-generation
base_model: HCHs/RivetCoder-9B-A4B
base_model_relation: quantized
language:
  - en
  - ko
tags:
  - gguf
  - llama.cpp
  - custom-architecture
  - mixture-of-experts
  - coding
  - code-generation
  - q8_0
  - q4_k_m
  - cuda
---

# RivetCoder-9B-A4B-GGUF

Q8_0 and Q4_K_M GGUF quantizations of
[HCHs/RivetCoder-9B-A4B](https://huggingface.co/HCHs/RivetCoder-9B-A4B).
Both files were quantized directly from the canonical BF16 checkpoint, not
from the FP8 distribution.

## Compatibility: custom llama.cpp required

These GGUFs use `general.architecture = rivetcoder`, a computation graph that
is not present in stock llama.cpp. Use the Windows CUDA runtime supplied in
`bundle/`, or rebuild the supplied source overlay against the recorded
llama.cpp base commit.

At release time, ordinary llama.cpp, LM Studio, and Ollama builds cannot load
these files. Renaming the architecture to `lfm2` is not a workaround because
that would omit the routed expert sidecar.

## Files

| File | Bytes | SHA-256 | Purpose |
|---|---:|---|---|
| `RivetCoder-9B-A4B-Q8_0.gguf` | 9,296,262,848 | `6e71dd349df93f734b89fd70f2d0590037ddd3bdc11a4e9533991a0eab47b85e` | Higher fidelity |
| `RivetCoder-9B-A4B-Q4_K_M.gguf` | 5,318,260,416 | `980adc81f64b52bc71228abd0e2bed02a1b6a00bdda9afbfd6d5e0c124ac5600` | Lower VRAM |
| `bundle/rivetcoder-llama-windows-cuda-sm120.zip` | recorded in `provenance/checksums.sha256` | recorded in `provenance/checksums.sha256` | RTX 50-series CLI/server |
| `bundle/rivetcoder-llama-source-overlay.zip` | recorded in `provenance/checksums.sha256` | recorded in `provenance/checksums.sha256` | converter and runtime source overlay |

## What was verified

The release criterion is runtime operation, not model-quality evaluation.

- BF16, Q8_0, and Q4_K_M all loaded with the custom CUDA llama.cpp build and
  generated real tokens with exit code `0`.
- Q8_0 and Q4_K_M each passed the 506-tensor schema check.
- All 150 routing-control values matched the BF16 Hugging Face checkpoint.
- Router matrices, correction biases, token-gate weights and biases, and
  effective residual scales stayed F32 after quantization.
- `llama-server` loaded Q8_0 with full GPU offload and returned
  `GET /health -> {"status":"ok"}`.
- Q4_K_M also generated tokens with full GPU offload.

This is not a coding benchmark and makes no HumanEval, MBPP, SWE-bench, or
general quality claim.

Test system: Windows x86-64, NVIDIA GeForce RTX 5070 Ti 16GB, driver 616.56,
CUDA Toolkit 13.1, custom llama.cpp base commit
`ca3d5a3e10d53f7ea672cb9b6178faca3e2807bc`.

Short one-turn runtime checks at a 512-token context measured approximately:

| Quant | Prompt | Generation |
|---|---:|---:|
| Q8_0 | 134.9 tok/s | 130.1 tok/s |
| Q4_K_M | 127.9 tok/s | 170.1 tok/s |

These are smoke-run timings, not controlled performance benchmarks.

## Windows CUDA quick start

Extract `bundle/rivetcoder-llama-windows-cuda-sm120.zip`, then run:

```powershell
.\llama-server.exe `
  --model .\RivetCoder-9B-A4B-Q4_K_M.gguf `
  --alias RivetCoder-9B-A4B `
  --host 127.0.0.1 `
  --port 8080 `
  --n-gpu-layers all `
  --ctx-size 4096 `
  --parallel 1 `
  --batch-size 512 `
  --ubatch-size 256 `
  --flash-attn on `
  --reasoning-budget 512
```

For direct answers without a thinking trace, replace
`--reasoning-budget 512` with `--reasoning-budget 0`. The embedded chat
template opens a thinking section by default, so an unlimited reasoning budget
can consume the entire output allowance before `message.content` is produced.

OpenAI-compatible request:

```powershell
$body = @{
  model = 'RivetCoder-9B-A4B'
  messages = @(
    @{ role = 'user'; content = 'Write a Python hello-world program.' }
  )
  temperature = 0
  max_tokens = 512
} | ConvertTo-Json -Depth 8

Invoke-RestMethod `
  -Method Post `
  -Uri http://127.0.0.1:8080/v1/chat/completions `
  -ContentType application/json `
  -Body $body
```

The GGUF metadata declares a 131,072-token context. Release smoke tests used
512 and 4,096 tokens; 128K memory use and long-context quality were not tested.

## Architecture retained in GGUF

Every one of the 30 LFM host layers keeps its native dense FFN and adds a
sparse routed sidecar:

```text
x       = ffn_norm(hidden)
dense   = LFM_dense_FFN(x)
experts = clamped SwiGLU experts selected by sigmoid Top-4 routing
gate    = sigmoid(token_gate(x))
output  = hidden + dense + effective_scale * gate * experts
```

There are 16 candidate experts per layer and four active experts per token.
The Hugging Face checkpoint stores a raw residual scale; conversion folds it
once as `0.1 * tanh(raw_scale)`. GGUF stores that signed effective F32 value,
and the C++ graph multiplies it directly without applying `tanh` again.

The graph also retains the post-sigmoid selection correction, normalized
uncorrected routing weights, expert gate/up clamps, all 22 ShortConv layers,
and all eight full-attention layers.

## Runtime bundle

The Windows bundle is a static llama.cpp/ggml build with CUDA enabled,
`GGML_NATIVE=OFF`, an AVX2 CPU fallback, and `sm_120a` GPU code. It contains
`llama-cli.exe`, `llama-server.exe`, the required redistributable CUDA cuBLAS
and MSVC runtime DLLs, build metadata, and license notices. An NVIDIA driver
supporting the RTX 50 series is still required.

The source-overlay ZIP records every modified and new file relative to the
exact upstream base commit so the converter/runtime can be rebuilt for other
platforms. Stock upstream source plus only the GGUF files is insufficient.

## License and attribution

The model remains subject to the LFM Open License v1.0 in [`LICENSE`](LICENSE),
including its commercial-use conditions. Read the full license; this summary
is not legal advice.

GLM-derived expert weights originate from `zai-org/GLM-5.3-Flash`; its MIT
license is included at [`licenses/GLM-MIT.txt`](licenses/GLM-MIT.txt). The
custom llama.cpp runtime/source remains under llama.cpp's MIT license, with
third-party redistributable notices included in the runtime archive.

No Qwen weights are included. Qwen was used only as a sequence-level teacher
during routing-control training.
