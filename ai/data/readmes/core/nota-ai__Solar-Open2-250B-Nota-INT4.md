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
  - vllm
  - moe
  - nota
---

# Solar Open2 250B — Nota INT4

[Nota AI](https://www.nota.ai/) presents a 4-bit quantized release of
[Upstage](https://www.upstage.ai/)'s
[Solar Open2 250B](https://huggingface.co/upstage/Solar-Open2-250B), produced with
Nota AI's proprietary quantization technology specialized for Mixture-of-Experts (MoE)
large language models.

## Highlights

- **W4A16 (weight-only INT4)** — `group_size=128`, packed in the `auto_round`
  (GPTQ-compatible) format. Formatted with AutoRound for direct, out-of-the-box
  serving in [vLLM](https://github.com/vllm-project/vllm).
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

| Precision         | Weight footprint |
| ----------------- | :--------------: |
| BF16              |     500.6 GB     |
| Nota INT4.        |     142.9 GB     |

### Benchmarks

| Benchmark               |       BF16       | Nota INT4 |
| ----------------------- | :--------------: | :---------------: |
| Tau2-Bench              |      75.20       |       74.04       |
| HLE                     |      27.88       |       27.15       |
| GPQA Diamond            |      86.26       |       85.86       |
| IFBench                 |      80.00       |       80.54       |
| LiveCodeBench (v5–v6)   |      87.03       |       85.50       |
| MMLU-Pro                |      86.19       |       86.29       |
| AIME 2026 (EN)          |      95.67       |       96.00       |
| IFEval (EN)             |      94.09       |       93.35       |
| HMMT                    |      92.05       |       90.91       |
| KMMLU-Pro               |      78.38       |       78.79       |
| HAE-RAE Bench v1.1      |      73.84       |       72.53       |
| AIME (KO)               |      97.67       |       97.67       |
| KBL                     |      75.51       |       75.20       |
| KBank-MMLU              |      80.80       |       80.88       |
| KorMedMCQA              |      92.99       |       92.85       |
| **Avg.**                |    **81.57**     |     **81.17**     |

## Quick Start

This model is packed in the AutoRound (GPTQ-compatible) INT4 format and can be served
directly with vLLM:

```bash
uv venv --python 3.12 --seed solar_open2_venv
source .venv/bin/activate

VLLM_PRECOMPILED_WHEEL_LOCATION="https://github.com/vllm-project/vllm/releases/download/v0.22.0/vllm-0.22.0%2Bcu129-cp38-abi3-manylinux_2_28_x86_64.whl" \
VLLM_USE_PRECOMPILED=1 \
uv pip install --reinstall-package vllm --torch-backend=cu129 \
  "git+https://github.com/UpstageAI/vllm.git@v0.22.0-solar-open2"
```

```bash
vllm serve nota-ai/Solar-Open2-250B-Nota-INT4 \
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

