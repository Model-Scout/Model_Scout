---
license: apache-2.0
language:
  - en
  - ko
  - zh
  - ja
  - es
datasets:
  - nvidia/Nemotron-CC-v2.1
  - nvidia/Nemotron-Pretraining-Code-v2
  - HuggingFaceFW/fineweb-2
pipeline_tag: text-generation
library_name: vllm
base_model: skt/A.X-K2
tags:
  - nvfp4
  - axk2-nvfp4
---

# A.X K2

<div align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)"
            srcset="https://huggingface.co/skt/A.X-K2/resolve/main/assets/A.X_K2_BI_Negative.png">
    <img src="assets/A.X_K2_BI_Primary.png" alt="A.X Logo" width="300">
  </picture>
</div>
<p align="center">
  <a href="https://huggingface.co/collections/skt/ax-k2">🤗 Models</a> |
  <a href="https://github.com/SKT-AI/A.X-K2">🖥️ Github</a> |
  <a href="https://github.com/SKT-AI/A.X-K2/blob/main/A_X_K2_Tech_Report.pdf">📄 Technical Report</a>
</p>

## Model Summary

**A.X K2** is a large-scale Mixture-of-Experts (MoE) language model trained from scratch as a high-performance, **agentic** foundation model, and the successor to A.X K1.
The model contains **688 billion total parameters**, with **33 billion active parameters**, delivering strong reasoning and instruction-following performance while maintaining practical inference efficiency.

Through a **Think-Fusion** training recipe, a single unified model supports both a **thinking** mode for complex problem solving and a **non-thinking** mode for concise, low-latency responses, allowing the user to trade quality for cost on a per-request basis.

A.X K2 is developed as part of the Korean government's **Sovereign AI foundation model** project, aiming to build a frontier-scale model with deep understanding of the Korean language and culture.

# A.X K2 NVFP4

A.X K2 NVFP4 is an NVFP4-quantized version of **A.X K2**, a 688B-parameter Mixture-of-Experts language model developed by SK Telecom.

This checkpoint applies **NVFP4 W4A4 quantization to the routed experts**, while keeping the remaining modules in FP8 or BF16. It retains performance comparable to the FP8 checkpoint while reducing the model memory footprint by approximately half.

The model can be served on a single node with **4 NVIDIA B200 GPUs** using the A.X K2–enabled SKT-AI vLLM fork.

## Quantization

| Module                                            | Precision  |
| ------------------------------------------------- | ---------- |
| Routed experts                                    | NVFP4 W4A4 |
| Attention, router, shared expert, and dense layer | FP8        |
| Embedding and LM head                             | BF16       |

## Usage

Install the A.X K2–enabled vLLM fork:

```bash
git clone -b axk2-v0.23.0 https://github.com/SKT-AI/vllm.git
cd vllm
pip install -e .
```

Enable the FlashInfer NVFP4 MoE kernels:

```bash
export VLLM_USE_FLASHINFER_MOE_FP4=1
export FLASHINFER_DISABLE_VERSION_CHECK=1
```

Serve the model:

```bash
vllm serve skt/A.X-K2-NVFP4 \
  --served-model-name A.X-K2-NVFP4 \
  --host 0.0.0.0 \
  --port 8000 \
  --tensor-parallel-size 4 \
  --enable-expert-parallel \
  --attention-backend FLASHINFER_MLA_SPARSE \
  --reasoning-parser deepseek_v3
```

The A.X K2 implementation is registered directly in the SKT-AI vLLM branch, so `--trust-remote-code` is not required.

To enable automatic tool calling, add:

```bash
--enable-auto-tool-choice \
--tool-call-parser hermes
```

## Thinking Mode

Thinking mode can be controlled per request through `chat_template_kwargs`.

```bash
curl http://localhost:8000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "A.X-K2-NVFP4",
    "messages": [
      {
        "role": "user",
        "content": "Explain how speculative decoding works."
      }
    ],
    "max_tokens": 1024,
    "chat_template_kwargs": {
      "enable_thinking": true
    }
  }'
```

Set `enable_thinking` to `false` for a direct non-thinking response.

## Long Context

The checkpoint includes the YaRN configuration required for context lengths of up to **256K tokens**. No separate RoPE override is required when using the provided `config.json`.

The serving context can be reduced with `--max-model-len` when longer inputs are not required.

#### Needle-in-a-Haystack (NIAH)

NIAH probes exact fact retrieval by inserting a target fact (the "needle") at varying depths within a long context and asking the model to recover it. Under zero-shot YaRN scaling (scaling factors of 1, 2, and 4 for 128K, 256K, and 512K, respectively), A.X K2 attains a perfect retrieval score at every context length and needle depth—and does so even after NVFP4 (experts-only W4A4) quantization. The heatmaps below show the 256K and 512K results.

<div align="center">
  <img src="assets/axk2_niah_256k_nvfp4.png" alt="A.X K2 NIAH fact retrieval at 256K context under NVFP4 (experts-only W4A4)" width="900">
  <img src="assets/axk2_niah_512k_nvfp4.png" alt="A.X K2 NIAH fact retrieval at 512K context under NVFP4 (experts-only W4A4)" width="900">
</div>

<p align="center"><em>NIAH fact retrieval across context length (x-axis) and needle depth (y-axis): 256K (YaRN factor 2, top) and 512K (YaRN factor 4, bottom), under NVFP4 (experts-only W4A4) quantization. A.X K2 scores a perfect 100 at every position.</em></p>



## License

A.X K2 is released under the Apache License 2.0.

## Citation

```bibtex
@techreport{axk2-2026,
  title       = {A.X K2 Technical Report},
  author      = {SK Telecom},
  year        = {2026},
  institution = {SK Telecom},
  url         = {https://github.com/SKT-AI/A.X-K2/blob/main/A_X_K2_Tech_Report.pdf}
}
```