---
license: apache-2.0
language:
  - de
  - en
  - es
  - fr
  - it
  - ja
  - ko
  - zh
tags:
  - mixar
  - pixel-language-model
  - tokenizer-free
  - multilingual
  - text-generation
pipeline_tag: text-generation
library_name: transformers
---

# MIXAR 477M (32x32 patches), stage 2

The stage-2 model of **MIXAR**, a multilingual language model that reads and writes text as rendered pixels instead of tokens. It refines the stage-1 backbone [`llama-pixar-477m-p32`](https://huggingface.co/TYTTYTTYT/llama-pixar-477m-p32) (477M, 32x32 patches) with a short reinforcement-learning stage based on GRPO, which makes the model a much stronger free-running generator.

[Code](https://github.com/april-tools/mixar) · [Paper](https://arxiv.org/abs/2604.11575)

## Results

| Benchmark | Score |
| --- | --- |
| bAbI task 1, English, free generation | 34.6 |
| LAMBADA, free generation (avg of 5 languages) | 15.3 (en 13.4 / de 16.4 / es 17.6 / fr 14.0 / it 15.0) |
| bAbI task 1, CJK, free generation | zh 1.4 / ja 11.0 / ko 1.0 |
| SIB-200, 22 languages | seen 78.5 / unseen 28.7 / unseen low-resource 25.6 |
| XNLI, 10 languages | seen 74.1 / unseen 62.8 |
| GLUE | 73.8 |

Free-generation scores are accuracies judged by a Qwen3.6-35B-A3B OCR judge
with a pixel-exact shortcut (bAbI task 1 few-shot, 2 shots; LAMBADA
zero-shot last-word prediction). SIB-200 (macro-F1) and XNLI (accuracy,
translate-train) are finetuned per language; SIB-200 has 8 languages seen in
pretraining and 14 unseen ones, including a low-resource subset. GLUE is the average over its
tasks. Full tables and protocols are in the paper.

## Stage-2 training

The generator samples groups of 8 continuations of 3 blocks from word onsets in
mC4 text. Each continuation is rewarded with a blend of a discriminator's
realism score and its match with the reference continuation:

r = 0.5 · σ(D) + 0.5 · (0.7 · tile match + 0.3 · pixel match)

The loss combines the clipped PPO objective (weight 10), a KL penalty to the
stage-1 model (weight 0.05) and the stage-1 reconstruction loss (weight 0.1). The
generator and the discriminator are trained in alternating phases, gated by
the discriminator's smoothed accuracy.

| | |
| --- | --- |
| Initialization | the champion of one earlier GRPO generation |
| Batch / micro-batch | 128 / 8 |
| Learning rate | 1e-5, constant |
| Steps per generation | 2,000 |
| Group size | 8 |
| Word gap (px) | 12 |

The released weights are a 0.6/0.4 average of two checkpoints of one run. See the paper's stage-2 appendix for the
full recipe.

## Usage

```bash
pip install "transformers==4.57.3" "pixar-render==0.5.1" torch
```

```python
import torch
from transformers import AutoModelForCausalLM
from huggingface_hub import snapshot_download
from pixar_render import PixarProcessor

path = snapshot_download("TYTTYTTYT/llama-pixar-477m-p32-stage2")
device = "cuda" if torch.cuda.is_available() else "cpu"

model = AutoModelForCausalLM.from_pretrained(
    path, trust_remote_code=True).to(device).eval()
processor = PixarProcessor.load(f"{path}/render_config")
BLOCK_W = processor._block_width          # pixel width of one block

def to_model_space(pixel_values_uint8):
    """uint8 [0,255] render -> 1-channel binary in [-1, 1] (white=+1, ink=-1)."""
    grey = pixel_values_uint8.float().mean(dim=1, keepdim=True)
    return (grey >= 128).float().mul_(2).sub_(1)

@torch.no_grad()
def generate(prompts, max_new_blocks=200, eos_threshold=0.1):
    enc = processor.render(prompts, padding_side="left", add_eos=False, truncate=True)
    enc = processor.align_text_to_right_edge(enc, 2)   # keep the prompt at the writing edge
    cur = to_model_space(enc.pixel_values.to(device))  # [B,1,H,W]
    attn = enc.attention_mask.to(device)
    B = cur.shape[0]
    seq, kv, stopped = [cur], None, [False] * B
    for _ in range(max_new_blocks):
        out = model(inputs_embeds=cur if kv is None else cur[..., -BLOCK_W:],
                    attention_mask=attn, past_key_values=kv, use_cache=True)
        kv = out.past_key_values
        nxt = (out.logits[..., -BLOCK_W:] > 0).float().mul_(2).sub_(1)
        for b in range(B):                              # blank block ≈ EOS
            if nxt[b].mean() > 1 - eos_threshold: stopped[b] = True
            if stopped[b]: nxt[b] = 1.0
        seq.append(nxt)
        cur = torch.cat([cur, nxt], dim=-1)
        attn = torch.cat([attn, attn.new_ones(B, 1)], dim=-1)
        if all(stopped): break
    return torch.cat(seq, dim=-1)

pixels = generate(["The capital of France is"])
# pixels: [-1,1] model space; ink is -1. Render back to images:
from pixar_render import PixarEncoding
uint8 = ((pixels > 0).to(torch.uint8) * 255).repeat(1, 3, 1, 1).cpu()
images = processor.convert_to_pil(PixarEncoding(
    pixel_values=uint8,
    attention_mask=torch.ones(uint8.shape[0], uint8.shape[-1] // BLOCK_W, dtype=torch.long),
    sep_patches=[[] for _ in range(uint8.shape[0])]), square=True)
images[0].save("output.png")
```

For sequence classification (fine-tuning), load
`LlamaPixarForSequenceClassification` from this repo's `modeling_llama_pixar.py`
the same way (`trust_remote_code=True` exposes it via the module).

## Model details

| | |
| --- | --- |
| Parameters | 477M (24 layers, hidden 896, 14 heads, MLP 6656) |
| Input and output | 1-channel binary pixels, 32x32 patches, 2 patches per block |
| Context | up to 32,768 blocks (trained on 180-block windows) |
| Pretraining objective | per-pixel binary cross-entropy on the next block |
| Pretraining data | mC4 in de, en, es, fr, it, ja, ko, zh, documents sampled uniformly from the pooled corpus (es .243, de .207, fr .171, ja .127, en .126, it .088, zh .024, ko .015) |
| Pretraining schedule | 1M steps, global batch 384, AdamW (0.9, 0.95), weight decay 0.1, LR 3e-4 cosine to 3e-5, 2k warmup |
| Pretraining compute | about 62 hours on 4 H200 GPUs |
| Packing | documents packed into 180-block sequences with EOS separators and per-document attention masks |

`render_config/` holds the exact fonts and rendering settings used in
pretraining. Use it as-is: a different font or rendering setup is a
distribution shift for the model.

## All released models

| Model | Stage 1 | Stage 2 (GRPO) |
| --- | --- | --- |
| 113M, 8x8 patches | [llama-pixar-116m-p8](https://huggingface.co/TYTTYTTYT/llama-pixar-116m-p8) | [llama-pixar-116m-p8-stage2](https://huggingface.co/TYTTYTTYT/llama-pixar-116m-p8-stage2) |
| 116M, 32x32 patches | [llama-pixar-116m-p32](https://huggingface.co/TYTTYTTYT/llama-pixar-116m-p32) | [llama-pixar-116m-p32-stage2](https://huggingface.co/TYTTYTTYT/llama-pixar-116m-p32-stage2) |
| 477M, 32x32 patches | [llama-pixar-477m-p32](https://huggingface.co/TYTTYTTYT/llama-pixar-477m-p32) | [llama-pixar-477m-p32-stage2](https://huggingface.co/TYTTYTTYT/llama-pixar-477m-p32-stage2) |

Also released: the adversarial stage-2 ablation
[llama-pixar-116m-p8-stage2-gan](https://huggingface.co/TYTTYTTYT/llama-pixar-116m-p8-stage2-gan) and the
tokenizer-based baseline [mgpt2-124m-mc4](https://huggingface.co/TYTTYTTYT/mgpt2-124m-mc4), pretrained on
the same corpus.

## License

The weights and the code in this repository are released under the Apache
License 2.0. The fonts in `render_config/fonts/` are bundled unmodified and are
licensed under the SIL Open Font License 1.1 (`render_config/fonts/OFL.txt`).

## Citation

```bibtex
@article{hu2026mixar,
  title   = {{MIXAR}: Scaling Autoregressive Pixel-based Language Models to Multiple Languages and Scripts},
  author  = {Hu, Chen and Tai, Yintao and Vergari, Antonio and Keller, Frank and Suglia, Alessandro},
  journal = {arXiv preprint arXiv:2604.11575},
  year    = {2026}
}
```
