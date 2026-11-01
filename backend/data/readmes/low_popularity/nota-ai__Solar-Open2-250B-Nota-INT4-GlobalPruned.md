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
  - int4
  - pruning
  - vllm
  - moe
  - nota
---

# Solar Open2 250B — Globally Pruned and Quantized to INT4 by Nota

[Nota AI](https://www.nota.ai/) presents a 4-bit quantized and **expert-pruned** release
of [Upstage](https://www.upstage.ai/)'s
[Solar Open2 250B](https://huggingface.co/upstage/Solar-Open2-250B), produced with
Nota AI's proprietary quantization technology specialized for Mixture-of-Experts (MoE)
large language models.

On top of INT4 quantization, this variant applies **additional expert pruning** so that
the model fits on fewer GPUs. Rather than removing the same number of experts uniformly
from every block, Nota AI's proprietary **global importance-estimation** technique
measures expert importance across the whole network and keeps only the most important
experts on a per-layer basis (**global pruning**). As a result, the number of routed
experts varies from layer to layer, preserving accuracy far better than uniform pruning
while shrinking the memory footprint enough to serve on **2×H100 GPUs**.

**Method clarification.** This model does **not use REAP-style uniform expert pruning**, 
in which the same number or proportion of experts is removed from every layer.
Instead, we use **our proprietary global-scale expert importance score** to compare 
experts across the entire network and determine a different number of retained experts for each layer.
Consequently, the pruned architecture has **layer-wise variable expert counts**, which are explicitly
recorded in the model configuration and require the **patched vLLM model definition** provided in this repository.

## Highlights

- **W4A16 (weight-only INT4)** — `group_size=128`, packed in the `auto_round`
  (GPTQ-compatible) format. Formatted with AutoRound for direct, out-of-the-box
  serving in [vLLM](https://github.com/vllm-project/vllm).
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

Global pruning drops the INT4 model to a **117.8 GB** weight footprint. Because the hidden
size is even, tensor parallelism does not support an **odd** number of GPUs, so the
tensor-parallel size must be even (2, 4). The unpruned INT4 model exceeds the
capacity of 2 GPUs and therefore has to jump to **4×H100**, whereas this globally pruned
model fits within **2×H100** — halving the GPU requirement. (The KV-cache figures shown
below are estimates.)

![Weight footprint and estimated H100 GPUs required, comparing BF16, Nota INT4, Nota NVFP4, and their Global-Pruned variants](assets/memory.png)

### Accuracy

Average score over three high-difficulty reasoning benchmarks. Nota AI's global pruning
retains **83.39**, close to the unpruned INT4 model (**83.99**) and far ahead of uniform
pruning at the same ratio (**78.79**).

![Average accuracy on three high-difficulty reasoning benchmarks: Nota INT4, Nota INT4 Global-Pruned, and Nota INT4 Uniform-Pruned](assets/performance.png)

## Quick Start

This model relies on **non-uniform (per-layer) expert counts**, which upstream vLLM does
not yet support. Before serving, replace vLLM's Solar Open2 model definition with the
patched version provided in this repository:

```bash
# Enable global-pruning (per-layer variable experts) support in vLLM
cp patch/solar_open2.py \
   path/to/vllm/model_executor/models/solar_open2.py
```

Then serve directly with vLLM on **2×H100**:

```bash
uv venv --python 3.12 --seed solar_open2_venv
source .venv/bin/activate

VLLM_PRECOMPILED_WHEEL_LOCATION="https://github.com/vllm-project/vllm/releases/download/v0.22.0/vllm-0.22.0%2Bcu129-cp38-abi3-manylinux_2_28_x86_64.whl" \
VLLM_USE_PRECOMPILED=1 \
uv pip install --reinstall-package vllm --torch-backend=cu129 \
  "git+https://github.com/UpstageAI/vllm.git@v0.22.0-solar-open2"
```

```bash
vllm serve nota-ai/Solar-Open2-250B-Nota-INT4-GlobalPruned \
  --served-model-name solar-open2-250b \
  --tensor-parallel-size 1 \
  --default-chat-template-kwargs '{"think_render_option":"preserved"}' \
  --max-model-len 131072
  --reasoning-parser solar_open2 \
  --tool-call-parser solar_open2 \
  --enable-auto-tool-choice \
  --logits-processors vllm.v1.sample.logits_processor.solar_open2:SolarOpen2TemplateLogitsProcessor
```

- The example above uses a 131K-token context length, but a longer context length can be configured on 2× H100 GPUs by increasing `--max-model-len`.

- See the original model card for prompt format and further details:
[upstage/Solar-Open2-250B](https://huggingface.co/upstage/Solar-Open2-250B).

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
