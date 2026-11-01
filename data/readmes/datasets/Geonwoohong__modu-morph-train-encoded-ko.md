---
pretty_name: modu-morph-encoded-ko
language:
- ko
license: other
size_categories:
- 1M<n<10M
---

## Dataset Description

This dataset is a **morphologically encoded Korean corpus** constructed for **morph-related research**.  
It integrates **eight cleaned Korean sources** — *written, spoken, nonpublication, newspaper, messenger, aspect_emotion, emotion,* and *dialogue* —  
and encodes each sample into structured morpheme sequences for **semantic** and **stylistic** streams.

Each sentence was analyzed using **Kiwi (Korean Intelligent Word Identifier)**,  
split into **semantic**, **stylistic**, and **combined** morpheme representations,  
and encoded into numerical tensors stored in `.npz` shards for direct model loading.

---

## Dataset Structure

### Files

| File Type | Example | Description |
|------------|----------|-------------|
| Vocabulary | `form_vocab.json`, `tag_vocab.json`, `text_vocab.json` | Morpheme, POS, and text token vocabularies (shared across shards, size = 64,000) |
| NPZ Shards | `train_tensor.shard0001.npz` – `train_tensor.shard0023.npz` | Packed arrays containing morpheme IDs and offsets for semantic/stylistic/text |

### Data Fields (inside each `.npz`)

| Field | Type | Description |
|--------|------|-------------|
| `sem_form_values`, `sem_form_offsets` | `np.ndarray[int32, int64]` | Semantic morpheme token IDs + offsets |
| `sem_tag_values`, `sem_tag_offsets` | `np.ndarray[int32, int64]` | Semantic POS tag IDs + offsets |
| `sty_form_values`, `sty_form_offsets` | `np.ndarray[int32, int64]` | Stylistic morpheme token IDs + offsets |
| `sty_tag_values`, `sty_tag_offsets` | `np.ndarray[int32, int64]` | Stylistic POS tag IDs + offsets |
| `txt_form_values`, `txt_form_offsets` | `np.ndarray[int32, int64]` | Combined morpheme token stream (for text reconstruction) |
| `source_ids`, `source_strings` | `np.ndarray[int32], np.ndarray[str]` | Source corpus metadata (domain index and name) |
| `line_no` | `np.ndarray[int64]` | Original line index within its source |
| `uid64` | `np.ndarray[uint64]` | 64-bit hash for document identity (from `blake2b`) |

---

## Example Record

Each row corresponds to a single document entry.

```python
{
  "uid64": 473217028191553817,
  "source": "AIHub Web Reviews",
  "semantic": [
    {"form": "제품", "tag": "NNG"},
    {"form": "이", "tag": "JKS"},
    {"form": "좋", "tag": "VA"},
    {"form": "아요", "tag": "EF"}
  ],
  "stylistic": [
    {"form": "이", "tag": "JKS"},
    {"form": "어요", "tag": "EF"}
  ]
}
```

---

## Data Splits

- **Split:** `train`  
- **Size:** ~5.8 M documents (≈ 23 NPZ shards, each 0.8–1.4 GB compressed)  
- **Composition:** Merged from eight major public Korean sources.  
  Each entry contains both **semantic** and **stylistic** morpheme streams.

---

## Preprocessing

Morphological analysis and segmentation were performed via:

```python
from kiwipiepy import Kiwi
kiwi = Kiwi(model_type="cong", num_workers=8, typos="basic_with_continual_and_lengthening")
tokens = kiwi.tokenize(text, normalize_coda=True)
```

Then split into semantic/stylistic streams:

```python
SEMANTIC_TAGS = {"NNG","NNP","VV","VA","XR","MM","MAG","SN","SL"}
STYLE_TAGS    = {"JKS","JKO","JKB","EP","EF","EC","ETN","ETM","IC","XSN","XSV"}
```

Finally, the encoded dataset was generated via `encode_morph.py`:
```bash
python encode_morph.py \
  --jsonl_name train_morph.jsonl.gz \
  --min_freq_form 1 \
  --max_form_vocab 64000 \
  --shard_size 400000 \
  --tensor_out train_tensor.npz
```

---

## Usage

```python
import numpy as np, glob

# Load a shard
f = sorted(glob.glob("train_tensor.shard*.npz"))[0]
z = np.load(f, allow_pickle=False)

print(z["sem_form_values"].shape, z["sem_tag_values"].shape)
print(len(z["source_strings"]), "unique sources")
```

For Hugging Face integration:
```python
from datasets import load_dataset

ds = load_dataset("Geonwoohong/modu-morph-encoded-ko", split="train", streaming=True)
for sample in ds.take(2):
    print(sample)
```

---

## Notes

> ⚠️ The dataset viewer may be unavailable due to large shard sizes.  
> To inspect locally, use:
> ```python
> import numpy as np
> z = np.load("train_tensor.shard0001.npz")
> print(z.files)
> ```

- Vocabulary capped at **64,000** morpheme tokens.  
- Morpheme-based structure optimized for **dual-stream encoders** (semantic + stylistic).  
- Designed for **representation learning**, **anomaly detection**, and **style disentanglement** tasks.  
- Encoded with **Kiwi(CoNg)** for robust Korean morphological decomposition.  
- Each shard self-contained (no external metadata required).

---

## Citation

---

