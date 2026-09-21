---
base_model: upstage/Solar-Open2-250B
base_model_relation: quantized
library_name: vllm
license: other
license_name: upstage-solar-license
license_link: LICENSE
pipeline_tag: text-generation
language:
  - en
  - ko
  - ja
tags:
  - quantization
  - nvfp4
  - pruning
  - vllm
  - moe
  - nota
---

# Solar Open2 250B — Globally Pruned and Quantized to NVFP4 by Nota

[Nota AI](https://www.nota.ai/) presents a 4-bit quantized **and expert-pruned** release
of [Upstage](https://www.upstage.ai/)'s
[Solar Open2 250B](https://huggingface.co/upstage/Solar-Open2-250B), produced with
Nota AI's proprietary quantization technology specialized for Mixture-of-Experts (MoE)
large language models.

On top of NVFP4 quantization, this variant applies **additional expert pruning** so that
the model fits on fewer GPUs. Rather than removing the same number of experts uniformly
from every block, Nota AI's proprietary **global importance-estimation** technique
measures expert importance across the whole network and keeps only the most important
experts on a per-layer basis (**global pruning**). As a result, the number of routed
experts varies from layer to layer, preserving accuracy far better than uniform pruning
while shrinking the memory footprint enough to serve on **1×B200 GPUs**.

**Method clarification.** This model does **not use REAP-style uniform expert pruning**, 
in which the same number or proportion of experts is removed from every layer.
Instead, we use **our proprietary global-scale expert importance score** to compare 
experts across the entire network and determine a different number of retained experts for each layer.
Consequently, the pruned architecture has **layer-wise variable expert counts**, which are explicitly
recorded in the model configuration and require the **patched vLLM model definition** provided in this repository.

## Highlights

- **NVFP4 (4-bit float, W4A4)** — `group_size=16`, packed in the `llm-compressor`
  (compressed-tensors) format for direct serving in
  [vLLM](https://github.com/vllm-project/vllm). Both weights and activations are
  quantized to 4-bit floating point.
  - > **Requires NVIDIA Blackwell.** NVFP4 relies on the FP4 tensor cores introduced in
    > the Blackwell architecture (e.g. B200 / GB200), so inference must run on a
    > Blackwell-class GPU. Earlier architectures (Hopper, Ada, Ampere) do not support
    > NVFP4 execution.
- **Global expert pruning.** Nota AI's proprietary global importance-estimation method
  prunes experts non-uniformly across layers — keeping only the experts that matter most
  in each layer — so the quantized model runs on fewer GPUs with minimal accuracy loss.
- **Nota AI's proprietary MoE quantization framework.** This release is built upon a
  suite of techniques developed by Nota AI to preserve model quality under aggressive
  low-bit quantization of MoE architectures:
  - A MoE-specialized calibration-dataset construction method, which achieved
    **1st place across all tracks** at the NVIDIA Nemotron Hackathon.
  - [**DREAM-MoE**](https://openreview.net/pdf?id=Wyhqwjl51A) and
    [**SRA-MoE**](https://openreview.net/pdf?id=H0NoX02erJ), two quantization algorithms
    proposed by Nota AI (published at the *ICML 2026 Workshop on AdaptFM*), which
    preserve MoE routing decisions and align expert-routing behavior throughout the
    quantization process.

## License

Solar Open 2 is distributed under the [**Upstage Solar License**](https://huggingface.co/upstage/Solar-Open2-250B/blob/main/LICENSE).

**Key requirements for Derivative AI Models** (create / train / fine-tune / distill / improve using Solar Open 2):

- **Naming:** prefix your model name with "Solar" (e.g., `Solar-MyModel-v1`).

- **Attribution:** prominently display "Built with Solar" in related public-facing materials.

- **Notice:** include a copy of the Upstage Solar License with your derivative model.

## Performance

### Weight footprint & GPU requirements

![Weight footprint and estimated H100 GPUs required, comparing BF16, Nota INT4, Nota NVFP4, and their Global-Pruned variants](assets/memory.png)

### Accuracy

![Average accuracy on three high-difficulty reasoning benchmarks: Nota INT4, Nota INT4 Global-Pruned, and Nota INT4 Uniform-Pruned](assets/performance.png)

### Latency

Measured with [vLLM](https://github.com/vllm-project/vllm) `v0.1.dev16959+g00907fc9b` on **4×NVIDIA B300 SXM6** (TP=4).
Long-context serving workload: **32,768 input tokens / 2,048 output tokens** per request.
All latency figures are **p50 (median)**.

**Concurrency = 1 (single user — latency floor)**

| Model | Output tok/s | TTFT (ms) | TPOT (ms) | tok/s/user | E2E latency (s) |
|---|---|---|---|---|---|
| Solar-Open-2 (BF16) | 119.8 | 975 | 7.87 | 127.0 | 17.1 |
| Solar-Open-2-Nota-NVFP4 | 144.5 | **734** | 6.56 | 152.5 | 14.2 |
| Solar-Open-2-Nota-NVFP4-Global-Pruned | **146.9** | 741 | **6.45** | **155.1** | **13.9** |

Speedup vs BF16 — NVFP4 **1.21×**, NVFP4-Global-Pruned **1.23×** (output throughput).

**Concurrency = 32 (32 simultaneous users)**

| Model | Output tok/s<br>*(all 32 users)* | Total tok/s<br>*(all 32 users)* | Req/s | tok/s/user<br>*(per user)* | TTFT (ms) | TPOT (ms) | E2E latency (s) |
|---|---|---|---|---|---|---|---|
| Solar-Open-2 (BF16) | 1,010.8 | 17,183.6 | 0.49 | 35.2 | **4,856** | 28.44 | 62.4 |
| Solar-Open-2-Nota-NVFP4 | 1,468.2 | 24,958.6 | 0.72 | 53.7 | 4,893 | 18.62 | 42.4 |
| Solar-Open-2-Nota-NVFP4-Global-Pruned | **1,503.5** | **25,560.2** | **0.73** | **56.2** | 5,337 | **17.79** | **41.6** |

Speedup vs BF16 — NVFP4 **1.45×**, NVFP4-Global-Pruned **1.49×** (output throughput).

> **Reading the numbers.** *Output tok/s* and *Total tok/s* are **aggregate across all concurrent users** (server capacity).
> *tok/s/user*, *TTFT*, *TPOT*, and *E2E latency* are what a **single user** experiences (`tok/s/user = 1000 / TPOT`).

## Quick Start

This model relies on **non-uniform (per-layer) expert counts**, which upstream vLLM does
not yet support. Before serving, replace vLLM's Solar Open2 model definition with the
patched version provided in this repository:

```bash
# Enable global-pruning (per-layer variable experts) support in vLLM
cp patch/solar_open2.py \
   path/to/vllm/model_executor/models/solar_open2.py
```

Then serve directly with vLLM on **1×B200**:

```bash
uv venv --python 3.12 --seed solar_open2_venv
source .venv/bin/activate

VLLM_PRECOMPILED_WHEEL_LOCATION="https://github.com/vllm-project/vllm/releases/download/v0.22.0/vllm-0.22.0%2Bcu129-cp38-abi3-manylinux_2_28_x86_64.whl" \
VLLM_USE_PRECOMPILED=1 \
uv pip install --reinstall-package vllm --torch-backend=cu129 \
  "git+https://github.com/UpstageAI/vllm.git@v0.22.0-solar-open2"
```

```bash
vllm serve nota-ai/Solar-Open2-250B-Nota-NVFP4-GlobalPruned \
  --served-model-name solar-open2-250b \
  --tensor-parallel-size 1 \
  --default-chat-template-kwargs '{"think_render_option":"preserved"}' \
  --max-model-len 131072 \
  --reasoning-parser solar_open2 \
  --tool-call-parser solar_open2 \
  --enable-auto-tool-choice \
  --logits-processors vllm.v1.sample.logits_processor.solar_open2:SolarOpen2TemplateLogitsProcessor
```

- The example above uses a 131K-token context length, but a longer context length can be configured on 1 x B200 GPUs by increasing `--max-model-len.`

- See the original model card for the prompt format, parser configuration, and further details.

Send a chat completion request:

```bash
curl http://localhost:8000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "solar-open2-250b",
    "messages": [
      {"role": "user", "content": "What is Upstage?"}
    ],
    "max_tokens": 131584,
    "temperature": 1.0,
    "top_p": 1.0,
    "reasoning_effort": "high"
  }'
```

## Citation
```bibtex
@inproceedings{park2026dreammoe,
  title     = {{DREAM-MoE}: Downstream Routing Error-Aware Margin-Preserving Quantization for Mixture-of-Experts Large Language Models},
  author    = {Park, Hancheol and Lee, Geonho and Kim, Tae-Ho},
  booktitle = {ICML 2026 Workshop on Resource-Adaptive Foundation Model Inference (AdaptFM)},
  year      = {2026},
  url       = {https://openreview.net/forum?id=Wyhqwjl51A},
}

@inproceedings{lee2026sramoe,
  title     = {{SRA-MoE}: Output-Aware Selective Router Alignment for MoE Quantization},
  author    = {Lee, Geonho and Park, Hancheol and Lee, Seunghyun and Choi, Jungwook and Kim, Tae-Ho},
  booktitle = {ICML 2026 Workshop on Resource-Adaptive Foundation Model Inference (AdaptFM)},
  year      = {2026},
  url       = {https://openreview.net/forum?id=H0NoX02erJ},
}
```
