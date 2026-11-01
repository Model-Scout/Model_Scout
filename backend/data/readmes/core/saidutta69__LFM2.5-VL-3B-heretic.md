---
license: other
license_name: lfm1.0
license_link: https://huggingface.co/LiquidAI/LFM2.5-VL-3B/blob/main/LICENSE
library_name: transformers
pipeline_tag: image-text-to-text
language:
- en
- ar
- zh
- fr
- de
- it
- ja
- ko
- pt
- es
- vi
- th
- id
- hi
- ru
- pl
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
- layout
- tool-use
- heretic
- uncensored
- decensored
- abliterated
- reproducible
- gguf
- local-llm
base_model: LiquidAI/LFM2.5-VL-3B
---

# LFM2.5-VL-3B-heretic

<div align="center">
  <img src="https://photu.kashyalabanavli.site/racer-is-op.png" alt="RACER IS OP" width="100%">
</div>

<br>

A decensored variant of [LiquidAI/LFM2.5-VL-3B](https://huggingface.co/LiquidAI/LFM2.5-VL-3B), produced with
[Heretic](https://github.com/p-e-w/heretic) v1.4.0 (directional ablation / "abliteration").
Liquid's hybrid conv+attention text backbone and the SigLIP2 NaFlex vision tower are kept intact -
refusal behaviour is suppressed with targeted weight edits to the attention output and MLP
down-projections of the language model, not by fine-tuning. Visual grounding, full-page OCR with
layout annotation, multi-image input and tool calling all still work.

> [!IMPORTANT]
> **The GGUF here is fully multimodal - text *and* vision.** The vision tower and projector ship
> separately as `LFM2.5-VL-3B-heretic-mmproj-F16.gguf` (0.85 GB); the two files together are the model. For image
> input you **must** load both - see [Quickstart](#quickstart). Text-only use needs only the main GGUF.
> Nothing is dropped from the text path: the text GGUF carries the full language tower
> (266 tensors, 30 blocks), and the projector GGUF carries the complete
> 426,285,296-element SigLIP2 tower plus merger, measured from its own header,
> including the tiling metadata (`min_tiles` 2, `max_tiles` 10, `tile_size` 512,
> `max_pixels_tolerance` 2.0) llama.cpp needs to reproduce the original image preprocessing.

**Who this is for:** people who want a small vision-language model that answers instead of
declining. At 3.12B total (2.70B text + 0.41B SigLIP2 vision +
0.01B projector) it is the larger of the two LFM2.5-VL heretics here, and it is
built for document and screen work: full-page OCR with layout regions, bounding-box
grounding from a natural-language query, screenshots and UI understanding, chart reading, and multi-
image input. Refusals drop from **100/100 to 6/100**. 16 languages. If you want the same capability
at a fraction of the size, [LFM2.5-VL-450M-heretic](https://huggingface.co/saidutta69/LFM2.5-VL-450M-heretic)
is the sibling; if you need text only, [LFM2.5-1.2B-Instruct-heretic](https://huggingface.co/saidutta69/LFM2.5-1.2B-Instruct-heretic)
or [Qwen3-4B-Thinking-heretic](https://huggingface.co/saidutta69/Qwen3-4B-Thinking-heretic) fit better.

Not the right pick for long-context or reasoning-heavy work. Liquid explicitly recommends this family
for single-turn, high-throughput, low-latency tasks and warns against visual web design or highly
technical blueprint Q&A. Context is 32,768 tokens.

## GPU matrix

The vision tower is **not** quantized, so image input costs the text quant plus the fixed
0.85 GB projector at every tier:

| Hardware | Recommended quant | Text weights | Text + vision |
| :--- | :--- | :--- | :--- |
| 6 GB GPU / 8 GB unified | Q4_K_M | 1.67 GB | 2.53 GB |
| 8 GB GPU | Q5_K_M | 1.94 GB | 2.79 GB |
| 12 GB GPU | Q6_K | 2.22 GB | 3.08 GB |
| 16 GB+ GPU / CPU-only | Q8_0 | 2.87 GB | 3.73 GB |

Add roughly 1-2 GB of KV/activation overhead on top. Liquid reports about 3.3 GB resident for the
unquantized model, so the Q4_K_M pair comfortably fits a 6 GB card.

## Abliteration parameters

Trial **67 of 200** (seed `3853387823`), `direction_index` selected per layer.

| Parameter | Value |
| :-------- | :---: |
| **direction_index** | per layer |
| **attn.o_proj.max_weight** | 1.078 |
| **attn.o_proj.max_weight_position** | 17.475 |
| **attn.o_proj.min_weight** | 0.698 |
| **attn.o_proj.min_weight_distance** | 8.406 |
| **mlp.down_proj.max_weight** | 1.332 |
| **mlp.down_proj.max_weight_position** | 21.896 |
| **mlp.down_proj.min_weight** | 0.750 |
| **mlp.down_proj.min_weight_distance** | 14.053 |

## Performance

| Metric | This model | Original model ([LiquidAI/LFM2.5-VL-3B](https://huggingface.co/LiquidAI/LFM2.5-VL-3B)) |
| :----- | :--------: | :---------------------------: |
| **KL divergence** | 0.0645 | 0 *(by definition)* |
| **Refusals** | 6/100 | 100/100 |

Read the pair, not the KL alone. 0.0645 is a mid-pack edit: looser than granite-4.2-3b (0.0095) and
Qwen3-4B-Thinking (0.0011), tighter than granite-4.1-3b (0.0852) and the gemma-4-E2B run (0.1841).
The base refused **all 100** evaluation prompts - heavier alignment than the Qwen2.5-VL-3B base
(99/100) - and 94 of them now clear. That is real work at a weight distance that did not have to be
extreme, which is the combination worth trusting.

The base model's own published scores (the abliteration only removes refusal directions, so these
describe the underlying capability, not a fresh sweep of this checkpoint):

| Benchmark | LFM2.5-VL-3B (base) |
| :--- | :---: |
| ScreenSpot-v2 | 80.7 |
| RefCOCO (Macro Prec@1) | 87.9 |
| BLINK | 61.5 |
| MuirBench | 58.3 |
| ToolSandBox | 59.5 |
| BFCLv4 | 32.5 |
| MME | 73.1 |
| MMStar | 63.3 |
| RealWorldQA | 73.1 |
| CountBenchQA | 87.3 |
| MMMB | 83.0 |
| MM-IF Eval | 60.6 |
| MathVista | 68.5 |
| MMMU Pro | 30.5 |
| ChartQA | 81.3 |
| OCRBenchv2 (English subset) | 47.5 |
| POPE | 88.7 |

## Why abliteration instead of fine-tuning

Fine-tuning a "helpful" persona on top of RLHF'd refusals fights the base model's training and tends
to degrade coherence. Abliteration instead finds and edits the specific weight directions responsible
for refusal, leaving the rest of the network - including the vision tower, OCR behaviour and tool-call
format - untouched. See the [Heretic repo](https://github.com/p-e-w/heretic) and the
[original abliteration writeup](https://huggingface.co/blog/mlabonne/abliteration) for the mechanism.

> Made with ❤️ by **RACER IS OP** - follow for more uncensored models

## Files

### Safetensors

| File | Size |
|---|---|
| `model-00001-of-00002.safetensors` | 5.00 GB |
| `model-00002-of-00002.safetensors` | 1.25 GB |

BF16, 3.12B total - 2.70B text tower + 0.41B
SigLIP2 vision tower + 0.01B multimodal projector (6.25 GB on disk). The
`reproduce/` directory carries the full Heretic recipe - `config.toml`, `requirements.txt`, the Optuna
journal, SHA-256 sums - so this exact model can be regenerated with
`heretic --reproduce reproduce/reproduce.json`.

### GGUF quantizations

Full ladder (14 quants + F16) from [llama.cpp](https://github.com/ggml-org/llama.cpp), plus the
vision projector:

| File | Format | Size |
|---|---|---|
| `LFM2.5-VL-3B-heretic-F16.gguf` | GGUF F16 | 5.40 GB |
| `LFM2.5-VL-3B-heretic-Q2_K.gguf` | GGUF Q2_K | 1.09 GB |
| `LFM2.5-VL-3B-heretic-IQ3_S.gguf` | GGUF IQ3_S | 1.27 GB |
| `LFM2.5-VL-3B-heretic-Q3_K_S.gguf` | GGUF Q3_K_S | 1.27 GB |
| `LFM2.5-VL-3B-heretic-Q3_K_M.gguf` | GGUF Q3_K_M | 1.37 GB |
| `LFM2.5-VL-3B-heretic-Q3_K_L.gguf` | GGUF Q3_K_L | 1.45 GB |
| `LFM2.5-VL-3B-heretic-IQ4_XS.gguf` | GGUF IQ4_XS | 1.53 GB |
| `LFM2.5-VL-3B-heretic-Q4_K_S.gguf` | GGUF Q4_K_S | 1.60 GB |
| `LFM2.5-VL-3B-heretic-Q4_0.gguf` | GGUF Q4_0 | 1.59 GB |
| `LFM2.5-VL-3B-heretic-Q4_1.gguf` | GGUF Q4_1 | 1.75 GB |
| `LFM2.5-VL-3B-heretic-Q4_K_M.gguf` | GGUF Q4_K_M | 1.67 GB |
| `LFM2.5-VL-3B-heretic-Q5_K_S.gguf` | GGUF Q5_K_S | 1.90 GB |
| `LFM2.5-VL-3B-heretic-Q5_K_M.gguf` | GGUF Q5_K_M | 1.94 GB |
| `LFM2.5-VL-3B-heretic-Q6_K.gguf` | GGUF Q6_K | 2.22 GB |
| `LFM2.5-VL-3B-heretic-Q8_0.gguf` | GGUF Q8_0 | 2.87 GB |

| File | Format | Size |
|---|---|---|
| `LFM2.5-VL-3B-heretic-mmproj-F16.gguf` | vision projector (F16) | 0.85 GB |

Total GGUF payload: 29.79 GB across 16 files (28.94 GB of text
weights + 0.85 GB projector).

The text tower is GGUF architecture `lfm2` (266 tensors, 30 blocks -
22 convolution and 8 full-attention, at indices 2, 5, 9, 13, 17, 21, 24 and 27), context 32,768.
The projector is GGUF architecture `clip` with projector type `lfm2` (441 tensors, the
27-block SigLIP2-so400m tower at hidden 1,152, patch 16, projection dim 2,048). Both load natively in
llama.cpp, LM Studio, Jan and Ollama.

## Quickstart

### Text only

```bash
# pulls the default quant for you
llama-completion -hf saidutta69/LFM2.5-VL-3B-heretic:Q4_K_M -ngl 99
```

### Text and images

`llama-mtmd-cli` auto-discovers the sibling whose name contains `mmproj`:

```bash
llama-mtmd-cli \
  -hf saidutta69/LFM2.5-VL-3B-heretic:Q4_K_M \
  --image path/to/page.png \
  -p "Transcribe this page." \
  -ngl 99
```

```bash
# or pass the projector explicitly from a local checkout
llama-mtmd-cli \
  -m LFM2.5-VL-3B-heretic-Q4_K_M.gguf \
  --mmproj LFM2.5-VL-3B-heretic-mmproj-F16.gguf \
  --image page.png \
  -p "Transcribe this page."
```

```python
# transformers (vision-language), needs transformers>=5.0.0
from transformers import AutoProcessor, AutoModelForImageTextToText

model_name = "saidutta69/LFM2.5-VL-3B-heretic"
model = AutoModelForImageTextToText.from_pretrained(model_name, dtype="auto", device_map="auto")
processor = AutoProcessor.from_pretrained(model_name)

conversation = [
    {"role": "user", "content": [
        {"type": "image", "url": "https://example.com/photo.jpg"},
        {"type": "text", "text": "Describe this image in one sentence."},
    ]},
]
inputs = processor.apply_chat_template(
    conversation, add_generation_prompt=True, return_tensors="pt",
    return_dict=True, tokenize=True,
).to(model.device)
outputs = model.generate(**inputs, do_sample=True, temperature=0.2, top_k=50,
                         repetition_penalty=1.0, max_new_tokens=256)
print(processor.batch_decode(outputs[:, inputs["input_ids"].shape[1]:],
                             skip_special_tokens=True)[0])
```

`config.json` uses `dtype:` rather than `torch_dtype:`, so use `dtype="auto"` and a recent
transformers. The `reproduce/requirements.txt` pins 5.20.2 for exact regeneration.

### Visual grounding

Ask in words; it answers with normalized boxes:

```python
prompt = ('Detect all instances of: the red button. Response must be a JSON array '
          '[{"label": ..., "bbox": [x1, y1, x2, y2]}, ...]. '
          'Coordinates are normalized to [0,1].')
```

### OCR with layout

The model can return reading-order layout regions (`image_index=<n> <label> [xmin, ymin, xmax, ymax]`
followed by the region content, with OTSL for tables and LaTeX for equations). Ask for the format
explicitly - it is documented but still experimental upstream.

### Sampling

Text defaults from the base card: `temperature=0.2`, `top_k=50`, `repetition_penalty=1.0`. Vision
preprocessing is read from `processor_config.json`; do not override it in llama.cpp, the projector
GGUF already carries the tiling parameters.

## Model details

| | |
|---|---|
| **Architecture** | `Lfm2VlForConditionalGeneration` |
| **Text backbone** | LFM2.5-2.6B hybrid - 22 convolution blocks + 8 full-attention blocks |
| **Vision backbone** | SigLIP2-so400m NaFlex, 27 layers, hidden 1,152, patch 16, projection 2,048 |
| **Parameters** | 3.12B total - 2.70B text, 0.41B vision, 0.01B projector |
| **Text layers** | 30 - 22 convolution, 8 full attention (indices 2, 5, 9, 13, 17, 21, 24, 27) |
| **Attention** | 32 heads, 8 KV heads, head dim 64 |
| **Hidden / intermediate** | 2,048 / 10,752 |
| **Position embedding** | RoPE theta = 1,000,000 |
| **Context length** | 32,768 |
| **Vocab** | 128,000 (embeddings tied) |
| **Image handling** | native resolution; 512x512 tiles (`min_tiles` 2, `max_tiles` 10) plus a whole-image thumbnail |
| **GGUF** | arch `lfm2`, 266 tensors, 30 blocks; projector arch `clip`, type `lfm2`, 441 tensors |
| **Precision** | bfloat16 |
| **Modalities** | Text and image in; text out |
| **Languages** | English, Arabic, Chinese, French, German, Italian, Japanese, Korean, Portuguese, Spanish, Vietnamese, Thai, Indonesian, Hindi, Russian, Polish |
| **Base model** | [LiquidAI/LFM2.5-VL-3B](https://huggingface.co/LiquidAI/LFM2.5-VL-3B) |

## About LFM2.5-VL

LFM2.5-VL is Liquid AI's refresh of LFM2-VL, built on the LFM2.5-2.6B language model. It keeps
SigLIP2 NaFlex native-resolution processing (large images split into 512x512 tiles with a thumbnail),
adds full-page OCR with layout annotation, improves grounding, and still exposes Pythonic tool calls.
Liquid quotes 228 tok/s on an Apple M5 Max, 116 tok/s on an AMD Ryzen AI Max+ 395, about 3.3 GB
resident, and 20 tok/s on a Galaxy S26 Ultra. It is tuned for single-turn, high-throughput,
low-latency work rather than long-context reasoning.

## Responsible use

Refusal suppression is deliberate and works as intended: this model will comply with requests the
base model would refuse, including some it shouldn't. There is no safety filtering layered on top.
You are responsible for how you deploy it - don't put this behind an unmoderated public-facing
endpoint serving third parties. It inherits the base model's factual limitations and biases;
abliteration removes refusal directions, it does not add capability or judgment.

## License

`lfm1.0` - the [LFM Open License](https://huggingface.co/LiquidAI/LFM2.5-VL-3B/blob/main/LICENSE), inherited from
the base model. **This is not Apache-2.0.** The heretic repository itself ships no `LICENSE` file, so
the link above points at the base repository's license blob. Read it before deploying commercially.

## Related

- [LiquidAI/LFM2.5-VL-3B](https://huggingface.co/LiquidAI/LFM2.5-VL-3B) - the base model
- [LiquidAI/LFM2.5-VL-3B-GGUF](https://huggingface.co/LiquidAI/LFM2.5-VL-3B-GGUF) - Liquid's own GGUF, for comparison
- [saidutta69/LFM2.5-VL-450M-heretic](https://huggingface.co/saidutta69/LFM2.5-VL-450M-heretic) - the tiny multimodal sibling
- [saidutta69/LFM2.5-1.2B-Instruct-heretic](https://huggingface.co/saidutta69/LFM2.5-1.2B-Instruct-heretic) - text-only LFM2.5

## Abliteration hardware

Recorded in `reproduce/reproduce.json`:

- **GPU:** NVIDIA RTX PRO 6000 Blackwell Server Edition (94.97 GB VRAM)
- **OS:** `Linux-4.19.0-gvisor-x86_64-with-glibc2.41`
- **CUDA / driver:** CUDA 13.0, driver 595.71.05
- **Software:** PyTorch 2.14.1+cu130, Heretic 1.4.0

Heretic notes that KL-divergence and refusal numbers can vary slightly with hardware and library versions.
