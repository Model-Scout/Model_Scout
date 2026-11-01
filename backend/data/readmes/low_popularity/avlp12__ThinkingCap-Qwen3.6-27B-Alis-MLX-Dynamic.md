---
language:
- en
- ko
- zh
license: apache-2.0
base_model: bottlecapai/ThinkingCap-Qwen3.6-27B
base_model_relation: quantized
library_name: mlx
pipeline_tag: image-text-to-text
tags:
- mlx
- qwen3_5
- quantized
- mixed-precision
- apple-silicon
- token-efficient
- efficient-thinking
- conversational
---

# ThinkingCap-Qwen3.6-27B-Alis-MLX-Dynamic

Apple Silicon (MLX) **mixed-precision** quantization of [bottlecapai/ThinkingCap-Qwen3.6-27B](https://huggingface.co/bottlecapai/ThinkingCap-Qwen3.6-27B) — the token-efficiency finetune of Qwen3.6-27B (~50% fewer thinking tokens at preserved accuracy). **4.601 bpw, 15.47 GB, GPQA-Diamond 83.3% — 0.5pt from bf16.**

| build | weights | GPQA-D* | avg think tokens | decode† | peak mem |
|---|---|---|---|---|---|
| **`main` (this)** — multimodal | **16.13 GB** | **83.3%**¹ | **2,838** | 35.6 tok/s | 16.7 GB |
| [`text`](https://huggingface.co/avlp12/ThinkingCap-Qwen3.6-27B-Alis-MLX-Dynamic/tree/text) — text-only | 15.47 GB | 83.3% | 2,838 | 36.5 tok/s | 15.8 GB |
| [BottleCapAI Q4_K_M GGUF (official)](https://huggingface.co/bottlecapai/ThinkingCap-Qwen3.6-27B-GGUF) | 16.81 GB | 82.3% | 3,654 | — | — |
| BottleCapAI bf16 (original) | 55.56 GB | 83.8% | 3,019 | — | — |

\* n=198, temperature 1.0, seed-fixed shuffled choices, 32K token cap — identical harness for all three rows (harness validated by reproducing the ThinkingCap card's published 83.8 exactly).
† single-stream on an M3 Ultra, short prompt.

![Showdown: accuracy, size and thinking tokens vs the official Q4_K_M GGUF and bf16](https://huggingface.co/avlp12/ThinkingCap-Qwen3.6-27B-Alis-MLX-Dynamic/resolve/main/assets/fig_showdown.png)

## Why this build

Smaller **and** more accurate than BottleCapAI's official 4-bit GGUF, with 22% fewer thinking
tokens per answer — on Apple Silicon, fewer generated tokens is the speedup that
matters. Fits 24 GB Macs with room for context (15.8 GB measured peak at short
context; int8 KV keeps long-context overhead small — only 16 of 64 layers carry KV
in this 3:1 DeltaNet hybrid).

## The finding behind it: short thinkers survive quantization

Across our GPQA campaign, the **same 4.6bpw recipe** loses 12.8pt on vanilla
Qwen3.6-27B (85.5 → 72.7) but only 0.5pt on ThinkingCap (83.8 → 83.3). Long
reasoning chains accumulate quantization drift token by token; ThinkingCap's
~3K-token chains stay on track where vanilla's ~11K-token chains derail.
**Token-efficiency finetune first, quantize second** — the two compound.

![GPQA vs bits-per-weight: vanilla quants degrade steeply; the ThinkingCap quant sits on the bf16 line](https://huggingface.co/avlp12/ThinkingCap-Qwen3.6-27B-Alis-MLX-Dynamic/resolve/main/assets/fig_gpqa_curve.png)

## Multimodal (default)

`main` carries the full multimodal stack: the 4.6bpw text weights (¹ GPQA measured on the
identical text weights) + the vision tower at 8-bit. 16.13 GB total — still smaller than
the 16.81 GB *text-only* GGUF. Verified with OCR + visual-reasoning tests (EN/KO).
Text-only users: `main` loads fine under plain mlx-lm (vision weights are skipped), or
use the `text` branch to save 0.66 GB.

```bash
pip install mlx-vlm
python -m mlx_vlm generate \
  --model avlp12/ThinkingCap-Qwen3.6-27B-Alis-MLX-Dynamic \
  --image photo.jpg --prompt "이미지의 텍스트를 읽어줘." --max-tokens 300
```

## Usage

```python
from mlx_lm import load, generate

model, tokenizer = load("avlp12/ThinkingCap-Qwen3.6-27B-Alis-MLX-Dynamic")
prompt = tokenizer.apply_chat_template(
    [{"role": "user", "content": "뮤텍스와 세마포어의 차이를 설명해줘."}],
    add_generation_prompt=True,
)
print(generate(model, tokenizer, prompt=prompt, max_tokens=512))
```

```bash
mlx_lm.generate --model avlp12/ThinkingCap-Qwen3.6-27B-Alis-MLX-Dynamic --prompt "..." -m 512
mlx_lm.server --model avlp12/ThinkingCap-Qwen3.6-27B-Alis-MLX-Dynamic --port 8080
```

Long context: `--kv-bits 8 --kv-group-size 64` (measured quality-free on this family: KL vs bf16-KV ≤ 0.003).

## Recipe (verified from `config.json`)

Per-tensor bits by marginal utility from a full weight-space sensitivity scan,
**validated end-to-end** (the scan alone misranks formats — see the nvfp4 note on the
[vanilla 27B repo](https://huggingface.co/avlp12/Qwen3.6-27B-Alis-MLX-Dynamic)):

| component | precision |
|---|---|
| bulk (90.1% of params) | affine 4-bit g64 |
| sensitivity-ranked top 9.8% | affine 5-bit g64 |
| routers / small gates | 6-bit pins |
| embed / lm_head | ≥4-bit |

No DWQ retune: at ≥4bpw the validation-gated DWQ rejects every round (already
teacher-close); conversion-time weights ship as-is.

## Notes & provenance

- `main` carries the full multimodal stack (mlx-vlm); the `text` branch is the mlx-lm text-only artifact.
- Eval artifacts: same 198-question GPQA protocol for every row of the table above.
- Built on an M3 Ultra 512 GB · mlx-lm 0.31.3 · mlx 0.31.2 · 2026-07.
- Siblings: [Qwen3.6-27B-Alis-MLX-Dynamic](https://huggingface.co/avlp12/Qwen3.6-27B-Alis-MLX-Dynamic) (vanilla golden + 5.5bpw reasoning tier), [Qwen3.6-35B-A3B-Alis-MLX-Dynamic](https://huggingface.co/avlp12/Qwen3.6-35B-A3B-Alis-MLX-Dynamic) (MoE, 102 tok/s).

## Credits

- **[bottlecapai](https://huggingface.co/bottlecapai)** — ThinkingCap-Qwen3.6-27B, the token-efficiency finetune this quantizes (and the Q4_K_M GGUF benchmarked against).
- **[Qwen team](https://huggingface.co/Qwen)** — the underlying Qwen3.6-27B.
- **[Apple MLX team](https://github.com/ml-explore/mlx)** — mlx / mlx-lm.
- Quantization recipe & evals: [Alis (avlp12)](https://huggingface.co/avlp12) with the [alis-dwq](https://github.com/avlp12/alis-dwq) pipeline; built with assistance from Claude (Anthropic).
