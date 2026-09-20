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
  - vllm
  - moe
  - nota
---

# Solar Open2 250B — Nota NVFP4

[Nota AI](https://www.nota.ai/) presents a 4-bit quantized release of
[Upstage](https://www.upstage.ai/)'s
[Solar Open2 250B](https://huggingface.co/upstage/Solar-Open2-250B), produced with
Nota AI's proprietary quantization technology specialized for Mixture-of-Experts (MoE)
large language models.

## Highlights

- **NVFP4 (4-bit float, W4A4)** — `group_size=16`, packed in the `llm-compressor`
  (compressed-tensors) format for direct serving in
  [vLLM](https://github.com/vllm-project/vllm). Both weights and activations are
  quantized to 4-bit floating point.
  - > **Requires NVIDIA Blackwell.** NVFP4 relies on the FP4 tensor cores introduced in
    > the Blackwell architecture (e.g. B200 / GB200), so inference must run on a
    > Blackwell-class GPU. Earlier architectures (Hopper, Ada, Ampere) do not support
    > NVFP4 execution.
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

### Weight footprint

| Precision          | Weight footprint |
| ------------------ | :--------------: |
| BF16               |     500.6 GB     |
| Nota NVFP4         |     153.3 GB     |

### Benchmarks

| Benchmark               |       BF16       | Nota NVFP4 |
| ----------------------- | :--------------: | :---------------: |
| Tau2-Bench              |      75.20       |       75.08       |
| HLE                     |      27.88       |       27.66       |
| GPQA Diamond            |      86.26       |       85.45       |
| IFBench                 |      80.00       |       81.02       |
| LiveCodeBench (v5–v6)   |      87.03       |       88.55       |
| MMLU-Pro                |      86.19       |       86.15       |
| AIME 2026 (EN)          |      95.67       |       96.67       |
| IFEval (EN)             |      94.09       |       92.61       |
| HMMT                    |      92.05       |       90.15       |
| KMMLU-Pro               |      78.38       |       77.93       |
| HAE-RAE Bench v1.1      |      73.84       |       72.84       |
| AIME (KO)               |      97.67       |       97.00       |
| KBL                     |      75.51       |       75.40       |
| KBank-MMLU              |      80.80       |       80.68       |
| KorMedMCQA              |      92.99       |       93.05       |
| **Avg.**                |    **81.57**     |     **81.35**     |

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

This model is packed in the NVFP4 (compressed-tensors) format and can be served directly
with vLLM on a **Blackwell-class GPU**:

```bash
uv venv --python 3.12 --seed solar_open2_venv
source .venv/bin/activate

VLLM_PRECOMPILED_WHEEL_LOCATION="https://github.com/vllm-project/vllm/releases/download/v0.22.0/vllm-0.22.0%2Bcu129-cp38-abi3-manylinux_2_28_x86_64.whl" \
VLLM_USE_PRECOMPILED=1 \
uv pip install --reinstall-package vllm --torch-backend=cu129 \
  "git+https://github.com/UpstageAI/vllm.git@v0.22.0-solar-open2"
```

```bash
vllm serve nota-ai/Solar-Open2-250B-Nota-NVFP4 \
  --served-model-name solar-open2-250b \
  --tensor-parallel-size 4 \
  --default-chat-template-kwargs '{"think_render_option":"preserved"}' \
  --reasoning-parser solar_open2 \
  --tool-call-parser solar_open2 \
  --enable-auto-tool-choice \
  --logits-processors vllm.v1.sample.logits_processor.solar_open2:SolarOpen2TemplateLogitsProcessor
```

- Set `--tensor-parallel-size` according to the number of GPUs available in your serving environment.

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

