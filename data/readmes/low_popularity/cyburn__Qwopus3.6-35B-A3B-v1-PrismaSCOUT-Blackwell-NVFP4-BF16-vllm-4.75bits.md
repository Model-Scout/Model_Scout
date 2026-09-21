---
base_model: Jackrong/Qwopus3.6-35B-A3B-v1
base_model_relation: quantized
language:
- en
- zh
- ja
- ko
- fr
license: apache-2.0
tags:
- quantized
- compressed-tensors
- vllm
- mixed-precision
- nvfp4
- prismaquant
- moe
- qwen3_5_moe
- reasoning
- multimodal
- image-text-to-text
- blackwell
pipeline_tag: image-text-to-text
library_name: transformers
---

# Qwopus3.6-35B-A3B-v1 — PrismaSCOUT Mixed-Precision Quantization (4.75 bpp, NVFP4/BF16/MXFP8, vLLM)

This is a **4.75 bits-per-parameter mixed-precision quantization** of [Jackrong/Qwopus3.6-35B-A3B-v1](https://huggingface.co/Jackrong/Qwopus3.6-35B-A3B-v1), produced with [PrismaQuant](https://github.com/RobTand/prismaquant) using the **PrismaSCOUT** selection algorithm.

The output is a standard `compressed-tensors` checkpoint served natively by vLLM — no custom kernels or patched runtimes required.

---

## Source Model

[Qwopus3.6-35B-A3B-v1](https://huggingface.co/Jackrong/Qwopus3.6-35B-A3B-v1) is a reasoning-enhanced fine-tune of [Qwen3.6-35B-A3B](https://huggingface.co/Qwen/Qwen3.6-35B-A3B), a hybrid sparse MoE model with:

- **35B total parameters, 3B active per token**
- Gated DeltaNet linear attention interleaved with full attention (1:3 ratio)
- 256 routed experts, 8 active per token
- Native **262K context window**
- MTP (Multi-Token Prediction) speculative decoding head
- Vision encoder (Qwen3VL) for image and video inputs

---

## Quantization Details

### Method: PrismaQuant + PrismaSCOUT

[PrismaQuant](https://github.com/RobTand/prismaquant) is a mixed-precision format allocator that assigns each Linear layer to a format based on its calibration-measured sensitivity. The **PrismaSCOUT** selection algorithm extends the base knapsack allocator with a multi-level real end-to-end KL validation cascade — surrogates generate candidates, real KL selects the shipping assignment. The polish step uses production-faithful per-Linear weights (joint NVFP4 sibling-coherent input global scales, GPTQ reconstruction, scale sweep, calibrated activation clip).

### Format Assignment

Calibration: 32 samples × 1024 tokens, text-only.

| Scope | Format | Count |
|---|---|---|
| Text body Linears | NVFP4 | 181 |
| Text body Linears | BF16 | 97 |
| Text body Linears | MXFP8_E4M3 | 1 |
| Visual encoder Linears | BF16 | 110 (uniform) |
| lm_head | BF16 (passthrough) | — |

Full export recipe (512 entries): `BF16: 305, NVFP4: 205, MXFP8: 2`.

**Achieved bit rate: 4.751 bpp** (target: 4.75).

Detailed per-layer assignment is in `mixed_native_manifest.json` and `model.safetensors.index.json`.

### Pipeline Configuration

```
FORMATS=NVFP4,MXFP8_E4M3,BF16
TARGET_BITS=4.75
NSAMPLES=32  SEQLEN=1024
VISUAL_FORMAT=BF16
CALIBRATION_MODALITY=text-only
```

Allocator Pareto curve excerpt:

| Target bpp | Achieved | Pred. ΔLoss | NVFP4 | MXFP8 | BF16 |
|---|---|---|---|---|---|
| 4.500 | 4.501 | 1.027×10⁵ | 247 | 1 | 31 |
| 4.600 | 4.601 | 2.427×10⁴ | 224 | 2 | 53 |
| 4.700 | 4.701 | 9.684×10³ | 200 | 0 | 79 |
| **4.750** | **4.751** | **6.399×10³** | **181** | **1** | **97** |
| 4.850 | 4.851 | 1.814×10³ | 159 | 0 | 120 |
| 5.000 | 5.001 | 7.588×10² | 163 | 1 | 115 |

---

## Usage

### vLLM (recommended)

Requires an NVIDIA Blackwell GPU (RTX 50xx / B100 / B200) for native NVFP4 kernel support.

```bash
vllm serve <repo_id> \
  --quantization compressed-tensors \
  --trust-remote-code \
  --kv-cache-dtype fp8 \
  --attention-backend flashinfer \
  --enable-prefix-caching \
  --speculative-config '{"method":"mtp","num_speculative_tokens":3}'
```

### Python (transformers + vLLM)

```python
from vllm import LLM, SamplingParams

llm = LLM(
    model="<repo_id>",
    quantization="compressed-tensors",
    trust_remote_code=True,
    kv_cache_dtype="fp8",
)

sampling_params = SamplingParams(temperature=0.7, max_tokens=512)

messages = [{"role": "user", "content": "Explain the Mixture-of-Experts architecture."}]

outputs = llm.chat(messages, sampling_params=sampling_params)
print(outputs[0].outputs[0].text)
```

### Hardware Requirements

| Component | Minimum | Recommended |
|---|---|---|
| GPU | RTX 5090 / B100 (Blackwell, NVFP4) | RTX 5090 |
| VRAM | ~24 GB | 32 GB+ |
| vLLM version | 0.8+ | latest |

> **Note:** NVFP4 weights require Blackwell-class hardware for native throughput. On older GPUs the compressed-tensors runtime will dequantize to BF16 on the fly — functional but slower.

---

## Limitations & Notes

- Visual encoder is kept in BF16 (not quantized) for quality preservation.
- `lm_head` is excluded from quantization (passthrough BF16).
- Calibration was text-only; multimodal performance is uninstrumented but expected to be close to BF16 given the BF16 visual encoder.
- The source model ([Qwopus3.6-35B-A3B-v1](https://huggingface.co/Jackrong/Qwopus3.6-35B-A3B-v1)) is an experimental community release and has not undergone complete safety evaluation.

---

## Reproduce

```bash
git clone https://github.com/RobTand/prismaquant
cd prismaquant

export MODEL_PATH=/path/to/Jackrong--Qwopus3.6-35B-A3B-v1
export WORK_DIR=./dq-runs/Qwopus3.6-35B-A3B-v1-PrismaSCOUT-Blackwell-NVFP4-BF16-vllm-4.75bits
export FORMATS=NVFP4,MXFP8_E4M3,BF16
export TARGET_BITS=4.75

./prismaquant/run-pipeline.sh
```

---

## Citation

If you use this quantization, please also cite:

```bibtex
@software{prismaquant2026,
  title  = {PrismaQuant: Mixed-Precision LLM Quantization Selected on Real End-to-End KL},
  author = {Tand, Robert},
  year   = {2026},
  url    = {https://github.com/RobTand/prismaquant},
}

@misc{jackrong_qwopus36_35b_a3b_v1,
  title     = {Qwopus3.6-35B-A3B-v1},
  author    = {Jackrong},
  year      = {2026},
  publisher = {Hugging Face},
}
```
