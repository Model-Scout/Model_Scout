---
library_name: mlx
base_model: LiquidAI/d1-3B
license: other
license_name: lfm1.0
license_link: LICENSE
pipeline_tag: image-text-to-text
language:
  - ar
  - zh
  - en
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
  - mlx
  - mlx-vlm
  - lfm2
  - lfm2-vl
  - lfm2.5
  - decision
  - system-one
  - edge
  - classification
  - calibration
---

# d1-3B MLX (8-bit)

## What

An MLX-native 8-bit conversion of [LiquidAI/d1-3B](https://huggingface.co/LiquidAI/d1-3B), pinned at revision `da1fe36a861f24690f27f622dca1d8688503d113`. Upstream d1-3B is a 3B-parameter **decision model** (System One) finetuned from LiquidAI/LFM2.5-VL-3B: named questions over a state (text, JSON, or images) → calibrated typed answers in ONE forward pass. Answers are read off the logits at the answer slot — nothing is decoded, so tokens generated per decision is zero and a schema violation is impossible. Question types: `noul` (yes/no → P(yes)), `choice` (named options → pick + probabilities), `score` (ordered levels → expected level + probabilities + legend).

Model file: `model.safetensors` (3,718,720,809 bytes), 3.72 GB, 9.52 bits-per-weight average, SHA-256 `c003549c43780cdcdef9fe3af8647ddde573e7eeea816315f7718179f109cce8`.

Quantization is RTN affine (`mlx_vlm convert -q --q-bits 8 --q-group-size 64`). The **language model weights are quantized; the vision tower, multi-modal projector, and all layer norms stay BF16** (mlx-vlm's default multimodal skip), verified from the shard dtypes.

## Why

The upstream checkpoint is distributed in transformers format for PyTorch. This conversion maps it to the MLX layout and quantizes the language model to 8-bit so Apple Silicon users can run System One decisions in 3.72 GB (the BF16 weights are 6.25 GB).

## Why it matters

A decision model answers in a single forward pass with calibrated probabilities, so what matters is that quantization does not move the answers. The BF16 conversion itself is verified: all 707 source tensors map to the MLX layout (key remap plus 22 conv-weight transposes), shapes all match, and every BF16 tensor is bit-exact (max |diff| = 0). Functionally, the same three questions (noul + score + choice) over the same state through the upstream transformers runner (MPS, BF16) and the BF16 MLX conversion differ by at most **0.0044** in per-option probability, with identical argmax decisions everywhere. This 8-bit variant agrees with BF16 on smoke decisions (refund noul 0.9841, BF16 0.9841; team choice billing 0.9825, BF16 0.9825).

Per the upstream card: Decision Index 0.2.1 score 48.57, best decision model under 10B; scores 74.1 on 11 public image benchmarks; multimodal images+text; 16 languages; context 32,768 tokens; vision encoder SigLIP2 NaFlex. Those are upstream claims, not ours.

## Results

Local, single-machine measurement on an Apple M3 Max with 36 GB unified memory, Python 3.12, mlx 0.32.3, mlx-vlm 0.7.6, transformers 5.19.0, macOS. Greedy, warm runs. "Decision" is a single noul question over a short text state, median of n=10. Decode/prefill numbers are from a 246-token image prompt. These are local results, not a vendor benchmark.

| Metric | Value |
|---|---:|
| Decision latency (median, n=10) | 52.0 ms (51.3–53.6) |
| Decode tok/s (246-token image prompt) | 79.0 |
| Prefill tok/s | 746 |
| TTFT | 0.349 s |
| Active memory | 3.72 GB |

Decision latency is a single forward pass (no tokens generated); quantization does not speed it up much at this size (prefill-dominated). Decode tok/s scales strongly with quantization: 79.0 tok/s here versus 50.4 at BF16 and 134.0 at 4-bit.

## How to use

Install mlx 0.32.3+ and mlx-vlm 0.7.6+ on Apple Silicon. Each repo ships `system_one.py`, a faithful MLX port of the upstream transformers System One runner (prompt rendering and logit readout are identical; the forward pass goes through mlx-vlm). It supports noul / choice / score, string or JSON states, and images (capped at 1024×1024 pixels like upstream).

CLI:

```bash
python system_one.py --model DJLougen/d1-3B-MLX-8bit --state '<text or JSON>' --questions '<JSON>' [--image path]
```

Python:

```python
from system_one import SystemOne
SystemOne("DJLougen/d1-3B-MLX-8bit").system_one(state, questions, images)
```

Plain generation with mlx-vlm:

```bash
python -m mlx_vlm.generate \
  --model DJLougen/d1-3B-MLX-8bit \
  --image image.jpg --prompt "Describe this image." --max-tokens 128
```

Note: one forward pass is made **per question** (upstream packs several questions of one state into a shared trunk with no padding — same answers, more compute). A `calibration` hook exists but no calibration data ships with these repos.

## Known issues

- Quantization is RTN (no AWQ/GPTQ calibration); the vision tower stays BF16.
- The helper re-reads the state once per question; upstream's packed-tree batching is not ported.
- Decision latency was measured on short text states only; no long-context decision measurements.
- Generation numbers are from one machine (M3 Max 36 GB), short prompts, greedy; not a vendor benchmark.
- d1-3B is a decision model, not a chat model; the backbone can generate but that is not its purpose.
- The upstream `.py` files (modeling_d1.py, runner.py, prompt.py, api.py, hybrid.py, lfm2_vl.py) are copied into each repo for provenance; they are transformers code and inert for mlx-vlm.

## License

The weights and associated upstream-derived model artifacts are distributed under Liquid AI's [LFM Open License v1.0](LICENSE), as required by the upstream d1-3B repository. The verbatim LICENSE file (10,574 bytes) is included in this repo.
