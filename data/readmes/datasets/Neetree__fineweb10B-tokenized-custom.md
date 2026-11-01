---
pretty_name: "LittleTzu FineWeb-Edu Tokenized (Custom 65k Balanced)"
language:
- en
- zh
- ja
- ko
- it
- es
- de
license: other
task_categories:
- text-generation
tags:
- pretraining
- tokenized
- fineweb-edu
- numpy
- custom-tokenizer
- bpe
size_categories:
- 10B<n<100B
---

# LittleTzu FineWeb-Edu Tokenized (Custom 65k Balanced)

Tokenized shards of **FineWeb-Edu** (`HuggingFaceFW/fineweb-edu`, config: `sample-10BT`) for language model pretraining. 

This dataset stores a derived, tokenized representation of the original FineWeb-Edu corpus. It has been tokenized using **LittleTzu's custom 65K balanced tokenizer**, optimized for multi-domain training (English, multilingual text, math, and code) while maintaining a compact vocabulary footprint that fits within a `uint16` data type.

## Dataset Structure

The dataset consists of flat 1D NumPy binary shards (`.npy` files) serialized in `uint16` format:
- `edufineweb_val_000000.npy` (Validation set: first shard, containing exactly 100M tokens)
- `edufineweb_train_000001.npy`
- `edufineweb_train_000002.npy`
- ...
- `edufineweb_train_000099.npy`

Each shard contains exactly **100,000,000** (100M) tokens. Shards are created by tokenizing raw documents from the source, prefixing/delimiting each document with the `<|eos|>` token, and packing them into contiguous 100M token arrays.

## Custom Tokenizer: `tokenizer_65k_balanced`

To overcome the vocabulary size overhead of tokenizers like OpenAI's `cl100k_base` (100k vocab) or Llama 3 (128k vocab) when training smaller models (~124M to 500M parameters), we trained a custom **Byte-Level BPE tokenizer** with a vocabulary size of **65,536**.

### Tokenizer Configuration
- **Model Type**: Byte-Level BPE (Byte Pair Encoding)
- **Vocabulary Size**: 65,536 (fits natively in `uint16` arrays, saving 50% memory/storage overhead during loading compared to standard `uint32` or `int32`/`int64` loaders!)
- **Pre-tokenization**: 
  - `ByteLevel(add_prefix_space=False)`
  - `Digits(individual_digits=True)` — Splits digits individually (e.g. `123` becomes `1`, `2`, `3`) to prevent the vocabulary from being bloated with random numbers and to ensure stable mathematical tokenization.
- **Special & Control Tokens**:
  - Standard: `<|pad|>`, `<|bos|>`, `<|eos|>`, `<|unk|>`, `<|sep|>`
  - Chat Format: `<|im_start|>`, `<|im_end|>`
  - Reserved: 50 reserved placeholders (`<|reserved_0|>` to `<|reserved_49|>`) for future-proofing and custom special tokens.

### Training Mixture (Balanced Corpus)
To ensure the tokenizer remains highly efficient across various domains despite its compact vocabulary, it was trained on a balanced 5,000,000 document subset spanning the following domains:
1. **English (General & Educational)**: `HuggingFaceFW/fineweb-edu` (25%)
2. **Multilingual Chinese**: `epfml/FineWeb2-HQ` (`cmn_Hani` config) (20%)
3. **Multilingual Italian**: `HuggingFaceFW/fineweb-2` (`ita_Latn` config) (15%)
4. **Math / Scientific**: `open-web-math/open-web-math` (15%)
5. **Multilingual Japanese**: `epfml/FineWeb2-HQ` (`jpn_Jpan` config) (10%)
6. **Code (Programming)**: `bigcode/the-stack-v2-train-smol` (10%)
7. **Multilingual Korean**: `HuggingFaceFW/fineweb-2` (`kor_Hang` config) (5%)

### Tokenization Compression Efficiency (Chars/Token)
The balanced training corpus ensures the custom tokenizer compresses multilingual text and code far more efficiently than general-purpose English tokenizers, even with 35% fewer vocabulary dimensions:

| Language / Domain | Custom 65k (chars/token) | OpenAI cl100k_base (chars/token) | Relative Efficiency |
|---|---|---|---|
| **English** | 5.13 | 5.13 | **Parity** (1.00x) |
| **Italian** | 5.19 | 3.59 | **+44.5%** (1.44x) |
| **Korean** | 1.71 | 1.09 | **+56.8%** (1.57x) |
| **Japanese** | 1.38 | 0.85 | **+62.3%** (1.62x) |
| **Chinese** | 1.20 | 0.94 | **+27.6%** (1.28x) |
| **Python Code** | 2.35 | 2.94 | -20.0% (0.80x) |

*By optimizing for multi-domain text, each sequence packed into the model context carries denser semantic information, speeding up pre-training convergence on multilingual benchmarks.*

## Data Preparation & Preprocessing

This dataset was tokenized and sharded via a parallelized processing script (`fineweb.py`) which:
1. Streams documents from the original `HuggingFaceFW/fineweb-edu` (`sample-10BT`) dataset.
2. Tokenizes document text using the `tokenizer_65k_balanced.json` model.
3. Prepends the `<|eos|>` token to every document.
4. Packs token streams into contiguous `1D` NumPy array buffers of size `100,000,000`.
5. Casts and saves each shard as `np.uint16` to a local directory or uploads to Hugging Face.

## How to Load and Stream

You can download and stream these tokenized shards using the Hugging Face Hub snapshot API or load them directly into your dataset loaders.

### 1. Download Shards
```python
from huggingface_hub import snapshot_download

snapshot_download(
    repo_id="Neetree/fineweb10B-tokenized-custom",
    repo_type="dataset",
    local_dir="data/edu_fineweb10B",
    allow_patterns="*.npy",
)
```

### 2. PyTorch DataLoader Example
Here is how you can implement an efficient, lightweight streaming dataloader using `np.load`:

```python
import os
import numpy as np
import torch

class ShardDataLoader:
    def __init__(self, data_dir, batch_size, seq_len, split="train"):
        self.B = batch_size
        self.T = seq_len
        self.shards = sorted([os.path.join(data_dir, f) for f in os.listdir(data_dir) if split in f])
        assert len(self.shards) > 0, f"No shards found for split: {split}"
        
        self.current_shard_idx = 0
        self._load_shard()
        
    def _load_shard(self):
        shard_path = self.shards[self.current_shard_idx]
        # Memory-map the file to prevent loading the entire 100M array into RAM at once
        self.tokens = np.load(shard_path, mmap_mode="r")
        self.current_pos = 0
        
    def next_batch(self):
        B, T = self.B, self.T
        # We need B * T + 1 tokens to construct input (X) and target (Y)
        needed = B * T + 1
        
        if self.current_pos + needed > len(self.tokens):
            # Advance to the next shard
            self.current_shard_idx = (self.current_shard_idx + 1) % len(self.shards)
            self._load_shard()
            
        buf = self.tokens[self.current_pos : self.current_pos + needed]
        self.current_pos += B * T
        
        # Convert uint16 array to torch.long for embedding layer lookup
        tensor = torch.from_numpy(buf.astype(np.int64))
        x = tensor[:-1].view(B, T)
        y = tensor[1:].view(B, T)
        
        return x, y
```

## Intended Use

- Large-scale causal language model pretraining.
- Benchmarking dataloading pipelines.
- Lightweight and budget-friendly model training baseline (compatible with LittleTzu training configs).

## Citation & Original Dataset

Original dataset is FineWeb-Edu by Hugging Face:
```bibtex
@misc{lozhkov2024fineweb-edu,
    author       = { Lozhkov, Anton and Ben Allal, Loubna and von Werra, Leandro and Wolf, Thomas },  
    title        = { FineWeb-Edu: the Finest Collection of Educational Content }, 
    year         = 2024,  
    url          = { https://huggingface.co/datasets/HuggingFaceFW/fineweb-edu },  
    doi          = { 10.57967/hf/2497 },
    publisher    = { Hugging Face }
}
```
If you use this sharded/tokenized representation, please cite the original creators of the FineWeb-Edu dataset.