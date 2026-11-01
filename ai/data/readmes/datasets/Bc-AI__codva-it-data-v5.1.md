---
license: mit
task_categories:
- text-generation
language:
- en
- zh
- ko
tags:
- code
- instruction-tuning
- sft
- chatml
size_categories:
- 1M<n<10M
---

# CodVa IT/SFT Dataset v5.1

**Multilingual instruction tuning dataset for CodVa model**

## Overview

- 🌍 **Languages:** English, Chinese (Simplified), Korean
- 📏 **Context Length:** 4096 tokens
- 💬 **Format:** Pure ChatML (no domain tokens)
- 🎯 **Task Coverage:** Coding, Math, Reasoning, General QA
- 🔥 **Anchor Samples:** ~3,000-5,000 multi-turn conversation examples

## Dataset Stats

Check `metadata.json` for exact counts. Approximate:
- **Training Examples:** ~2.2M
- **Validation Examples:** ~44K
- **Total Tokens:** ~9B tokens (2.2M × 4096)

## Files

| File | Size | Description |
|------|------|-------------|
| `train_input_ids.npy` | ~21.7 GB | Training input token IDs (int32, shape: [N, 4096]) |
| `train_labels.npy` | ~21.7 GB | Training labels with -100 for non-assistant tokens (int32) |
| `train_attention_mask.npy` | ~5.4 GB | Training attention masks (uint8) |
| `val_input_ids.npy` | ~450 MB | Validation input token IDs |
| `val_labels.npy` | ~450 MB | Validation labels |
| `val_attention_mask.npy` | ~110 MB | Validation attention masks |
| `metadata.json` | Small | Dataset statistics and configuration |
| `token_map.json` | Small | Special token ID mappings |
| `codva_tokenizer.json` | Small | GPT-2 tokenizer with ChatML special tokens |

## Usage

### Option 1: Direct numpy load (recommended for training)

```python
import numpy as np

# Memory-mapped loading (efficient for large files)
train_ids = np.load("train_input_ids.npy", mmap_mode='r')
train_labels = np.load("train_labels.npy", mmap_mode='r')
train_attn = np.load("train_attention_mask.npy", mmap_mode='r')

print(f"Training examples: {len(train_ids):,}")
print(f"Shape: {train_ids.shape}")  # (N, 4096)
print(f"Total tokens: {len(train_ids) * 4096 / 1e9:.2f}B")
```

### Option 2: HuggingFace datasets (auto-downloads)

```python
from datasets import load_dataset

# This will download and cache the files
dataset = load_dataset("Bc-AI/codva-it-data-v5.1")

print(dataset)
```

## ChatML Format

All examples follow strict ChatML format with special tokens:

```
<|im_start|>system
You are CodVa, a helpful, honest, and highly capable AI assistant specialized in coding, mathematics, reasoning, and general knowledge.
<|im_end|>
<|im_start|>user
Write a Python function to calculate fibonacci numbers.
<|im_end|>
<|im_start|>assistant
Here's an efficient implementation:

def fibonacci(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
<|im_end|>
```

## Training Details

- **Loss Mask:** Only assistant turns contribute to loss (labels = -100 for system/user turns)
- **Attention Mask:** Binary mask for padding (1 = real token, 0 = padding)
- **Padding:** Right-padded to 4096 tokens with `<|endoftext|>` (token ID from `token_map.json`)

## Special Tokens

See `token_map.json` for exact IDs. Key tokens:
- `<|im_start|>` — Start of turn
- `<|im_end|>` — End of turn  
- `<|endoftext|>` — EOS / padding token

## Dataset Composition

### English Sources
- Code instruction datasets (Magicoder, Glaive, CodeFeedback)
- Math datasets (MetaMath, MathInstruct, Orca-Math)
- Reasoning datasets (OpenHermes, WizardLM, UltraChat)
- General QA (Alpaca, Dolly, No-Robots)

### Chinese Sources
- `shibing624/alpaca-zh` — Chinese instruction tuning
- `codefuse-ai/CodeExercise-Python-27k` — Chinese coding problems

### Korean Sources
- `nlpai-lab/kullm-v2` — Korean instruction tuning

### Anchor Samples
- 3,000-5,000 hand-crafted multi-turn conversations
- Identity reinforcement (who is CodVa, what can it do)
- Safety refusals (harmful requests)
- Coding debugging flows
- Math tutoring chains
- Casual conversation patterns

## Training Recommendations

```python
# SFT hyperparameters (tested)
learning_rate = 2e-5
min_lr = 2e-6
warmup_tokens = 2_000_000
epochs = 2-3  # DO NOT OVERTRAIN
batch_size = 4-8  # auto-search recommended
grad_accumulation = 4
weight_decay = 0.01
```

**⚠️ Warning:** Do not train for >3 epochs or you may overfit to ChatML format and lose pretrain knowledge.

## License

MIT License — Free for research and commercial use

## Citation

```bibtex
@misc{codva-it-v5.1-2024,
  title={CodVa Instruction Tuning Dataset v5.1: Multilingual ChatML Format},
  author={SmilyAI Labs},
  year={2024},
  howpublished={\url{https://huggingface.co/datasets/Bc-AI/codva-it-data-v5.1}},
}
```

## Questions?

Open an issue or discussion on the HuggingFace repo page.

---

**Built with 🔥 by SmilyAI Labs**
