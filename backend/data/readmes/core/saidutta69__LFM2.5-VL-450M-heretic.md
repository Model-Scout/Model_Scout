---
license: other
license_name: lfm1.0
license_link: https://huggingface.co/LiquidAI/LFM2.5-VL-450M/blob/main/LICENSE
library_name: transformers
pipeline_tag: image-text-to-text
language:
- en
- ar
- zh
- fr
- de
- ja
- ko
- es
- pt
tags:
- liquid
- lfm2
- lfm2-vl
- lfm2.5
- lfm2.5-vl
- edge
- on-device
- vision-language
- vlm
- multimodal
- image-text-to-text
- grounding
- ocr
- heretic
- uncensored
- decensored
- abliterated
- reproducible
- gguf
- roleplay
- local-llm
base_model: LiquidAI/LFM2.5-VL-450M
---

# LFM2.5-VL-450M-heretic

<div align="center">
  <img src="https://photu.kashyalabanavli.site/racer-is-op.png" alt="RACER IS OP" width="100%">
</div>

<br>

A decensored variant of [LiquidAI/LFM2.5-VL-450M](https://huggingface.co/LiquidAI/LFM2.5-VL-450M),
produced with [Heretic](https://github.com/p-e-w/heretic) v1.4.0 (directional ablation / "abliteration").
Liquid's hybrid conv+attention text backbone keeps its native tool-call format and multilingual coverage,
and the vision tower is untouched - refusal behaviour is suppressed via targeted weight edits to the
attention output and MLP down-projections of the language model rather than fine-tuning.

> [!IMPORTANT]
> **The GGUF here is fully multimodal - text *and* vision.** The vision tower and projector ship
> separately as `LFM2.5-VL-450M-heretic-mmproj-F16.gguf` (0.19 GB), and the two files together are the model.
> For image input you **must** load both - see [Quickstart](#quickstart). Text-only use needs only the
> main GGUF. Nothing is lost in the conversion: the projector GGUF holds
> 94,234,880 tensor elements (the SigLIP2 tower plus the merger), and it
> carries the tiling metadata llama.cpp needs to match the original image preprocessing.

**Who this is for:** developers who want a genuinely tiny multimodal model that answers instead of
declining. At 450M total parameters (0.35B text tower, 0.09B
SigLIP2 vision tower) this is the smallest model in the collection that still sees images, and it
speaks nine languages. Refusals drop from **93/100 to 5/100**. Best for on-device image Q&A, captioning,
bounding-box grounding, OCR on small screenshots, and local vision agents on a phone, a Pi, or a
browser tab. If you need text-only at this size, [SmolLM2-360M-Instruct-heretic](https://huggingface.co/saidutta69/SmolLM2-360M-Instruct-heretic)
is the sibling to reach for.

## Runs anywhere

At 450M there is no VRAM ladder - pick a quant by how much RAM and bandwidth your device has:

| Device | Recommended quant | Text weights | Text + vision |
| :--- | :--- | :--- | :--- |
| Phone / browser (4 GB RAM) | Q4_K_M | 0.23 GB | 0.42 GB |
| Raspberry Pi 5 (4 GB) | Q4_K_M | 0.23 GB | 0.42 GB |
| Laptop (8 GB, Apple Silicon) | Q8_0 | 0.38 GB | 0.57 GB |
| Server / multi-tenant | Q6_K | 0.29 GB | 0.48 GB |

The right-hand column is what you actually need on disk for image input: the text GGUF plus the
0.19 GB projector, which is fixed-size because vision weights are not quantized.
Because the backbone is mostly cheap convolution blocks, this model is far more
decode-bandwidth-sensitive than its parameter count suggests - fast RAM matters more than a fast GPU.

## Abliteration parameters

Trial of a 200-trial Heretic run (seed `836943652`), `direction_index` selected per layer.

| Parameter | Value |
| :-------- | :---: |
| **direction_index** | 10.51 |
| **attn.o_proj.max_weight** | 1.00 |
| **attn.o_proj.max_weight_position** | 12.14 |
| **attn.o_proj.min_weight** | 0.86 |
| **attn.o_proj.min_weight_distance** | 8.89 |
| **mlp.down_proj.max_weight** | 0.98 |
| **mlp.down_proj.max_weight_position** | 10.58 |
| **mlp.down_proj.min_weight** | 0.75 |
| **mlp.down_proj.min_weight_distance** | 1.36 |

## Performance

| Metric | This model | Original model ([LiquidAI/LFM2.5-VL-450M](https://huggingface.co/LiquidAI/LFM2.5-VL-450M)) |
| :----- | :--------: | :---------------------------: |
| **KL divergence** | 0.0187 | 0 *(by definition)* |
| **Refusals** | 5/100 | 93/100 |

Read those two numbers together, they are only meaningful as a pair. KL 0.0187 is one of the
tightest edits in this collection, and it lands refusals at 5/100 - so the edit did real work
without meaningfully moving the model's behaviour. That combination matters more than the raw KL.

The base started at 93/100 refusals, which is heavy alignment for a model this small; 88 of the 93
are cleared. The base model's own published scores - which the abliteration does not change, since
it only removes refusal directions - are MMStar 43.00, RealWorldQA 58.43, MMBench 60.91, MMVet 41.10,
InfoVQA 43.02, OCRBench 684, and on the language side GPQA 25.66, MMLU-Pro 19.32, IFEval 61.16,
Multi-IF 34.63, BFCLv4 21.08. Those are the base model's numbers, reproduced from the upstream card;
no separate benchmark sweep was run on this abliterated checkpoint.

## Why abliteration instead of fine-tuning

Fine-tuning a "helpful" persona on top of RLHF'd refusals fights the base model's training and tends
to degrade coherence. Abliteration instead finds and edits the specific weight directions responsible
for refusal, leaving the rest of the network (and its capabilities) untouched. See the
[Heretic repo](https://github.com/p-e-w/heretic) and the
[original abliteration writeup](https://huggingface.co/blog/mlabonne/abliteration) for the mechanism.

> Made with ❤️ by **RACER IS OP** - follow for more uncensored models

## Files

### Safetensors

| File | Size |
|---|---|
| `model.safetensors` | 0.90 GB |

BF16, 0.45B total (0.35B text tower + 0.09B
vision tower + 0.01B projector). The `reproduce/` directory carries the full Heretic
recipe - `config.toml`, `requirements.txt`, the Optuna study journal, and SHA-256 sums - so this exact
model can be regenerated bit-for-bit with `heretic --reproduce reproduce/reproduce.json`.

### GGUF quantizations
Full quantization set (14 quants + F16) produced with [llama.cpp](https://github.com/ggml-org/llama.cpp),
plus the vision projector.

| File | Format | Size |
|---|---|---|
| `LFM2.5-VL-450M-heretic-F16.gguf` | GGUF F16 | 0.71 GB |
| `LFM2.5-VL-450M-heretic-Q2_K.gguf` | GGUF Q2_K | 0.16 GB |
| `LFM2.5-VL-450M-heretic-IQ3_S.gguf` | GGUF IQ3_S | 0.18 GB |
| `LFM2.5-VL-450M-heretic-Q3_K_S.gguf` | GGUF Q3_K_S | 0.18 GB |
| `LFM2.5-VL-450M-heretic-Q3_K_M.gguf` | GGUF Q3_K_M | 0.19 GB |
| `LFM2.5-VL-450M-heretic-Q3_K_L.gguf` | GGUF Q3_K_L | 0.20 GB |
| `LFM2.5-VL-450M-heretic-IQ4_XS.gguf` | GGUF IQ4_XS | 0.21 GB |
| `LFM2.5-VL-450M-heretic-Q4_K_S.gguf` | GGUF Q4_K_S | 0.22 GB |
| `LFM2.5-VL-450M-heretic-Q4_0.gguf` | GGUF Q4_0 | 0.22 GB |
| `LFM2.5-VL-450M-heretic-Q4_1.gguf` | GGUF Q4_1 | 0.24 GB |
| `LFM2.5-VL-450M-heretic-Q4_K_M.gguf` | GGUF Q4_K_M | 0.23 GB |
| `LFM2.5-VL-450M-heretic-Q5_K_S.gguf` | GGUF Q5_K_S | 0.26 GB |
| `LFM2.5-VL-450M-heretic-Q5_K_M.gguf` | GGUF Q5_K_M | 0.26 GB |
| `LFM2.5-VL-450M-heretic-Q6_K.gguf` | GGUF Q6_K | 0.29 GB |
| `LFM2.5-VL-450M-heretic-Q8_0.gguf` | GGUF Q8_0 | 0.38 GB |

| File | Format | Size |
|---|---|---|
| `LFM2.5-VL-450M-heretic-mmproj-F16.gguf` | vision projector (F16) | 0.19 GB |

Total GGUF payload: 4.13 GB across 16 files.

The text tower is GGUF architecture `lfm2` (148 tensors, 16 blocks - 12 convolution blocks and 4
full-attention blocks). The projector is GGUF architecture `clip` with projector type `lfm2`
(201 tensors, 12 vision blocks). Both load natively in llama.cpp, LM Studio, Jan and Ollama.

## Quickstart

### Text only

```bash
# pulls the default quant for you
llama-cli -hf saidutta69/LFM2.5-VL-450M-heretic:Q4_K_M -ngl 99
```

### Text and images

Use a multimodal entry point. `llama-cli` is the text-only binary and will **not** fetch the
projector; `llama-mtmd-cli` will, because llama.cpp looks for a sibling GGUF whose name contains
`mmproj`:

```bash
llama-mtmd-cli \
  -hf saidutta69/LFM2.5-VL-450M-heretic:Q4_K_M \
  --image path/to/photo.png \
  -p "Describe this image in one sentence." \
  -ngl 99
```

```bash
# or from a local checkout, passing the projector explicitly
llama-mtmd-cli \
  -m LFM2.5-VL-450M-heretic-Q4_K_M.gguf \
  --mmproj LFM2.5-VL-450M-heretic-mmproj-F16.gguf \
  --image photo.png \
  -p "Describe this image in one sentence."
```

```python
# transformers (vision-language)
from transformers import AutoProcessor, AutoModelForImageTextToText
from transformers.image_utils import load_image

model_name = "saidutta69/LFM2.5-VL-450M-heretic"
model = AutoModelForImageTextToText.from_pretrained(model_name, dtype="auto", device_map="auto")
processor = AutoProcessor.from_pretrained(model_name)

image = load_image("https://example.com/photo.jpg")
conversation = [
    {"role": "user", "content": [
        {"type": "image", "image": image},
        {"type": "text", "text": "What is in this image?"},
    ]},
]
inputs = processor.apply_chat_template(
    conversation, add_generation_prompt=True, return_tensors="pt",
    return_dict=True, tokenize=True,
).to(model.device)
outputs = model.generate(**inputs, max_new_tokens=64)
print(processor.batch_decode(outputs, skip_special_tokens=True)[0])
```

Requires `transformers>=5.20.0` - `config.json` uses `dtype:` rather than `torch_dtype:` and the
tokenizer is a `TokenizersBackend`, so older transformers will not load it. Use `dtype="auto"`.

### Visual grounding

LFM2.5-VL supports bounding-box prediction. Ask for it in words and it answers in JSON:

```python
prompt = ('Detect all instances of: status. Response must be a JSON array '
          '[{"label": ..., "bbox": [x1, y1, x2, y2]}, ...]. '
          'Coordinates are normalized to [0,1].')
```

### Sampling

The base model documents `temperature=0.1`, `min_p=0.15`, `repetition_penalty=1.05` for text.
Those are the values to start from - this is a small model and the defaults in most runners
(`temperature=0.7`, `top_p=0.95`) make it noticeably less coherent.

### Image preprocessing knobs

From `processor_config.json`: `min_image_tokens` 64, `max_image_tokens` 256, `do_image_splitting`
true, `min_tiles` 2, `max_tiles` 10, `tile_size` 512, `max_pixels_tolerance` 2.0. Images up to
512x512 are handled without upscaling and non-standard aspect ratios are preserved without
distortion. Larger images are split into non-overlapping 512x512 tiles with a thumbnail for global
context. Lower `max_image_tokens` and `max_tiles` to trade image quality for speed; these are the
knobs the model was tuned to expose.

## Model details

| | |
|---|---|
| **Architecture** | `Lfm2VlForConditionalGeneration` |
| **Text backbone** | LFM2.5-350M hybrid - convolution blocks + full attention (every 4th layer) |
| **Vision backbone** | SigLIP2 shape-optimized encoder, 12 layers, hidden 768, patch 16 |
| **Parameters** | 0.45B total - 0.35B text, 0.09B vision, 0.01B projector |
| **Text layers** | 16 - 12 convolution, 4 full attention (every 4th) |
| **Attention** | 16 attention heads, 8 KV heads, head dim 64 |
| **Hidden / intermediate** | 1024 / 6656 (auto-adjusted to 4608 in GGUF) |
| **Position embedding** | RoPE theta = 1,000,000, plus learned positional encoding |
| **Context length** | 128,000 (the upstream card advertises 32,768 as the usable window) |
| **Vocab** | 65,536 (embeddings tied) |
| **Vision tower** | 12 layers, hidden 768, patch 16, image size 256 for the encoder |
| **GGUF** | arch `lfm2`, 148 tensors, 16 blocks; projector arch `clip`, type `lfm2`, 201 tensors |
| **Precision** | bfloat16 |
| **Modalities** | Text and image in; text out |
| **Languages** | English, Arabic, Chinese, French, German, Japanese, Korean, Portuguese, Spanish |
| **Base model** | [LiquidAI/LFM2.5-VL-450M](https://huggingface.co/LiquidAI/LFM2.5-VL-450M) |

The `450M` in the name counts the whole model, not just the language tower: 0.35B
of text plus 0.09B of SigLIP2 vision. The text backbone is the same
LFM2.5-350M that Liquid ships as a standalone edge model.

## About LFM2.5-VL

LFM2.5-VL is Liquid AI's refreshed version of the first vision-language model, LFM2-VL-450M, built on
an updated LFM2.5-350M backbone. It handles native-resolution images without upscaling, splits large
images into non-overlapping tiles with a thumbnail for global context, exposes the image-token budget
as a runtime knob, and supports function calling on text-only input. Beyond llama.cpp and Ollama it
is integrated with vLLM and SGLang, and it can be fine-tuned with SFT via Unslame and TRL.

## Responsible use

Refusal suppression is deliberate and works as intended: this model will comply with requests the
base model would refuse, including some it shouldn't. There is no safety filtering layered on top.
You are responsible for how you deploy it - don't put this behind an unmoderated public-facing endpoint
serving third parties. It inherits LFM2.5-VL's factual limitations and biases; abliteration removes
refusal directions, it doesn't add capability or judgment.

## License

`lfm1.0` - the [LFM Open License](https://huggingface.co/LiquidAI/LFM2.5-VL-450M/blob/main/LICENSE),
inherited from the base model. **This is not Apache-2.0.** The LFM Open License carries its own terms;
read it before deploying commercially.

## Related

- [LiquidAI/LFM2.5-VL-450M](https://huggingface.co/LiquidAI/LFM2.5-VL-450M) - the base model
- [LiquidAI/LFM2.5-VL-450M-GGUF](https://huggingface.co/LiquidAI/LFM2.5-VL-450M-GGUF) - Liquid's own GGUF, for comparison
- [saidutta69/LFM2.5-350M-heretic](https://huggingface.co/saidutta69/LFM2.5-350M-heretic) - the text-only backbone, also decensored
- [saidutta69/SmolLM2-360M-Instruct-heretic](https://huggingface.co/saidutta69/SmolLM2-360M-Instruct-heretic) - the smallest text-only model in the collection

## Abliteration hardware

Recorded in `reproduce/reproduce.json`:

- **GPU:** NVIDIA GeForce RTX 3090 (23.56 GB VRAM)
- **CPU:** AMD Ryzen 5 3600 6-Core Processor
- **OS:** `Linux-6.8.0-147-generic-x86_64-with-glibc2.35`
- **CUDA / driver:** CUDA 12.8, driver 595.91.07
- **Software:** PyTorch 2.7.1+cu128, Heretic 1.4.0

Heretic notes that KL-divergence and refusal numbers can vary slightly with hardware and library versions.
