---
language:
- en
- vi
- es
- zh
- ja
- ko
- fr
- de
- pt
- ru
- ar
- hi
- id
- th
- it
- tr
license: apache-2.0
library_name: peft
base_model: google/gemma-4-e4b-it
tags:
- gemma4
- unsloth
- lora
- qlora
- fine-tuning
- hackathon
- gemma-4-good-hackathon
- kaggle
- translation
- speech-recognition
- accessibility
- on-device
datasets:
- mlabonne/FineTome-100k
pipeline_tag: text-generation
---

![Bánh mì chuyển ngữ — live translation subtitles, powered by Gemma 4](cover.png)

# Bánh mì chuyển ngữ — Gemma 4 E4B Fine-Tuned with Unsloth QLoRA

**Competition:** [The Gemma 4 Good Hackathon](https://www.kaggle.com/competitions/gemma-4-good-hackathon) on Kaggle  
**Tracks:** Digital Equity & Inclusivity (primary) · Unsloth ($10K) · Future of Education  
**Framework:** [Unsloth](https://unsloth.ai) — 2× faster fine-tuning  
**Base model:** [`google/gemma-4-e4b-it`](https://huggingface.co/google/gemma-4-e4b-it) (4B params, instruction-tuned)

This adapter powers **Bánh mì chuyển ngữ** ("Trans-Bread"), a macOS application that captures any audio playing on a user's device and renders it as **live translated subtitles** in a floating, click-through overlay — fully on-device, in 16 languages. Built for the **300M+ people worldwide who live in a country where they don't speak the dominant language.**

## Highlights

- **99.6% training loss reduction** — from 2.916 (baseline) to **0.0115** (final)
- **5 epochs** of QLoRA fine-tuning on 10,000 high-quality samples
- **Only 2.29% of parameters trained** (146.8M / 6.4B) via rank-stabilized LoRA
- **~12 hours total training** on a single NVIDIA L4 GPU (24 GB)
- **Deployed on-device** via Apple MLX 4-bit on Apple Silicon — no cloud, no API keys

## Use Case

The fine-tuned model is paired with the `mlx-vlm` runtime in a native macOS Swift app. ScreenCaptureKit captures system audio, a hysteresis VAD segments utterances, and a single-pass Gemma prompt produces the translated subtitle. End-to-end latency is sub-2 seconds, fully offline.

## How to Use

### With Unsloth (recommended)

```python
from unsloth import FastModel

model, tokenizer = FastModel.from_pretrained(
    "bradduy/banhmi-gemma4-e4b",
    max_seq_length=2048,
    load_in_4bit=True,
)
FastModel.for_inference(model)

messages = [
    {"role": "user", "content": "Translate to Vietnamese: The doctor will see you now."}
]

inputs = tokenizer.apply_chat_template(
    messages, tokenize=True, add_generation_prompt=True, return_tensors="pt"
).to("cuda")

outputs = model.generate(
    input_ids=inputs,
    max_new_tokens=128,
    temperature=0.3,
    do_sample=True,
)
print(tokenizer.decode(outputs[0][inputs.shape[1]:], skip_special_tokens=True))
```

### With Transformers + PEFT

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
from peft import PeftModel

base_model = AutoModelForCausalLM.from_pretrained(
    "google/gemma-4-e4b-it",
    device_map="auto",
    load_in_4bit=True,
)
model = PeftModel.from_pretrained(base_model, "bradduy/banhmi-gemma4-e4b")
tokenizer = AutoTokenizer.from_pretrained("bradduy/banhmi-gemma4-e4b")
```

### With Ollama / llama.cpp (GGUF)

Two pre-quantized GGUF files ship in this repo for local CPU inference:

| File | Quantization | Size | Quality | Best for |
|---|---|---|---|---|
| [`banhmi-gemma4.Q4_K_M.gguf`](banhmi-gemma4.Q4_K_M.gguf) | Q4_K_M — 4-bit K-quant, Medium | **3.4 GB** | ~3–4% perplexity vs full precision | **Recommended default** — what Ollama expects |
| [`banhmi-gemma4.Q3_K_S.gguf`](banhmi-gemma4.Q3_K_S.gguf) | Q3_K_S — 3-bit K-quant, Small | **3.1 GB** | ~6–8% perplexity vs full precision | Edge / low-RAM devices, mobile |

```bash
# Download the recommended Q4_K_M build
hf download bradduy/banhmi-gemma4-e4b banhmi-gemma4.Q4_K_M.gguf --local-dir .

# Build + run with Ollama
ollama create banhmi-gemma4 -f Modelfile
ollama run banhmi-gemma4
```

The accompanying [`Modelfile`](https://github.com/bradduy/Any2AnyModels/blob/main/submission/Modelfile) uses the Gemma 4 chat template and ships a translation-specific system prompt out of the box. To switch to the smaller Q3_K_S variant, change the `FROM` line in the Modelfile.

## Supported Languages (16)

English · Vietnamese · Spanish · Chinese (Simplified) · Japanese · Korean · French · German · Portuguese · Russian · Arabic · Hindi · Indonesian · Thai · Italian · Turkish

## Training Details

### Configuration

| Parameter | Value |
|-----------|-------|
| Base model | `google/gemma-4-e4b-it` (4B params) |
| Quantization | 4-bit QLoRA via bitsandbytes |
| LoRA rank | 64 |
| LoRA alpha | 64 |
| RSLoRA | Enabled (rank-stabilized scaling) |
| Learning rate | 7e-5 |
| LR scheduler | Cosine |
| Epochs | 5 |
| Dataset size | 10,000 samples |
| Effective batch size | 8 (1 × 8 grad accumulation) |
| Weight decay | 0.01 |
| Warmup steps | 50 |
| Total steps | 6,250 |
| Max seq length | 2048 |
| Optimizer | AdamW 8-bit |
| Mixed precision | bf16 |
| Seed | 3407 |
| Response masking | `train_on_responses_only` enabled |

### Dataset

- **Source:** [`mlabonne/FineTome-100k`](https://huggingface.co/datasets/mlabonne/FineTome-100k)
- **Samples used:** 10,000
- **Format:** Multi-turn chat conversations in Gemma 4 native format (`role: "model"`, not `"assistant"`)
- **Masking:** Only model responses contribute to loss
- **No proprietary, personal, or copyrighted data is used in training.**

### Hardware

- **GPU:** NVIDIA L4 (24 GB VRAM)
- **RAM:** 32 GB
- **Training time:** ~12 h (with checkpoint resume)
- **Peak GPU memory:** ~14.8 GB during training

## Experiment Journey

We ran 8 systematic experiments to find the optimal configuration:

| Exp | LoRA r | Epochs | Samples | LR | Train Loss | Key Finding |
|-----|--------|--------|---------|-----|-----------|-------------|
| 01 | 16 | 0.13 | 3k | 2e-4 | 2.916 | Baseline |
| 02 | 32 | 0.24 | 5k | 2e-4 | 1.725 | Higher rank helps |
| 03 | 64+RSLoRA | 0.20 | 10k | 2e-4 | 1.460 | RSLoRA + more data |
| 04 | 64+RSLoRA | 0.40 | 20k | 1e-4 | ~1.05 | Lower LR improves convergence |
| 05 | 128+RSLoRA | 0.40 | 20k | 5e-5 | 1.134 | r=128 slower than r=64 |
| 06 | 64+RSLoRA | 3 | 10k | 1e-4 | ~0.30 | **Multi-epoch is transformative** |
| 07 | 128+RSLoRA | 3 | 10k | 1e-4 | ~0.59 | r=64 > r=128 for multi-epoch |
| **08** | **64+RSLoRA** | **5** | **10k** | **7e-5** | **0.0115** | **5 epochs = 99.6% reduction** |

### The multi-epoch discovery

```
Epoch 1: loss ~0.90  (learning patterns)
Epoch 2: loss ~0.60  (reinforcing)
Epoch 3: loss ~0.30  (deep memorization)
Epoch 4: loss ~0.10  (fine polishing)
Epoch 5: loss ~0.01  (near-perfect fitting)
```

### Other key insights
1. **r=64 with RSLoRA is the sweet spot** — r=128 converges slower with no multi-epoch benefit.
2. **Lower LR (7e-5) stabilizes long training** — higher LR (2e-4) destabilizes after epoch 2.
3. **`train_on_responses_only` is essential** — masks user/system tokens so the model only learns from responses.
4. **Checkpoint every 250 steps** — long CUDA runs crash from memory fragmentation; checkpoint-resume solves it.
5. **10k high-quality samples > 20k samples** for multi-epoch — quality over quantity.

## Reproduce Training

The full Unsloth training pipeline ships with this model repository:

| Path | Purpose |
|---|---|
| [`configs/train_config.yaml`](configs/train_config.yaml) | Pinned hyperparameters — the exact exp08 winning config |
| [`scripts/train.py`](scripts/train.py) | Unsloth `FastModel` + TRL `SFTTrainer` pipeline (defaults reproduce exp08 with no flags) |
| [`scripts/prepare_data.py`](scripts/prepare_data.py) | Dataset preparation (Gemma 4 chat template, ShareGPT standardization) |
| [`scripts/training_logger.py`](scripts/training_logger.py) | Loss curve + training summary logger |
| [`scripts/evaluate.py`](scripts/evaluate.py) | Evaluation harness |
| [`scripts/export_model.py`](scripts/export_model.py) | Export to merged 16-bit / GGUF / HF Hub |
| [`notebooks/train_kaggle.ipynb`](notebooks/train_kaggle.ipynb) | Kaggle-free-tier reproducibility notebook (T4 / P100) |
| [`notebooks/demo.ipynb`](notebooks/demo.ipynb) | Inference demo for this adapter |

Quick reproduction (defaults = exp08 winning config — no flags needed):

```bash
pip install unsloth
python scripts/train.py
```

Or run from the pinned YAML for an exact match:

```bash
python scripts/train.py --lora-rank 64 --use-rslora \
  --learning-rate 7e-5 --num-epochs 5 --max-samples 10000 \
  --grad-accum 8 --weight-decay 0.01 --warmup-steps 50 \
  --save-steps 250 --save-total-limit 3
```

## On-Device Deployment

For the macOS app we use a smaller MLX-quantized variant of the family: [`unsloth/gemma-4-E2B-it-UD-MLX-4bit`](https://huggingface.co/unsloth/gemma-4-E2B-it-UD-MLX-4bit), which fits comfortably on Apple Silicon and produces sub-2-second per-utterance latency. The fine-tuned adapter in this repository targets the larger E4B variant for cloud/Ollama inference.

### macOS App Source (`apps/macos/`)

The full Swift source for the *Bánh mì chuyển ngữ* menu-bar app is included in this repository under [`apps/macos/`](apps/macos):

| Path | Purpose |
|---|---|
| [`apps/macos/Package.swift`](apps/macos/Package.swift) | Swift Package Manager manifest (macOS 13+, Swift 5.9) |
| [`apps/macos/build.sh`](apps/macos/build.sh) | One-shot build → `.app` bundle, code-signs, installs to `~/Applications/` |
| [`apps/macos/Sources/BanhMi/`](apps/macos/Sources/BanhMi) | 13 Swift files: app entry, audio capture, hysteresis VAD, recognizer, overlay, settings |
| [`apps/macos/scripts/gemma_sidecar.py`](apps/macos/scripts/gemma_sidecar.py) | Python MLX inference sidecar that hosts the Gemma 4 model |
| [`apps/macos/Resources/Info.plist`](apps/macos/Resources/Info.plist) | Bundle metadata + TCC permission strings |

**Quick build:**

```bash
cd apps/macos
./build.sh
open "$HOME/Applications/Bánh mì chuyển ngữ.app"
```

Requires Apple Silicon, macOS 13+, Swift 5.9+, and `mlx-vlm` available to a Python 3 interpreter (point `BANHMI_PYTHON` at it).

## Limitations

- **4B parameter model** — larger variants (26B, 31B) would deliver higher translation quality but require more VRAM.
- **Training loss ≠ task accuracy** — task-level metrics (BLEU, end-to-end latency) are still being measured and will be added.
- **Optimized for short utterance translation** — not a general-purpose long-form translation model.
- **Audio capture is macOS-only** — Windows/Linux ports of the app are future work.

## License & Data Provenance

- **Adapter weights:** released under Google's [Gemma Terms of Use](https://ai.google.dev/gemma/terms) (inherited from base model).
- **Training data:** `mlabonne/FineTome-100k` under its original license.
- **No proprietary or personal data used in training.**

## Acknowledgments

- **Google DeepMind** for the [Gemma 4](https://blog.google/technology/developers/gemma-4/) model family
- **[Unsloth](https://unsloth.ai)** for making QLoRA fine-tuning 2× faster and memory-efficient
- **Apple MLX** team for on-device 4-bit inference
- **[Kaggle](https://www.kaggle.com)** for hosting the Gemma 4 Good Hackathon
- **[mlabonne](https://huggingface.co/mlabonne)** for the FineTome-100k dataset

## License

Apache 2.0 (same as Gemma 4)
