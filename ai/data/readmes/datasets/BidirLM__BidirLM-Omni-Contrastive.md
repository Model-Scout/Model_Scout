---
license: apache-2.0
task_categories:
- feature-extraction
language:
- en
tags:
- omnimodal
- contrastive-learning
- bidirlm
- retrieval
- contrastive
- multimodal
arxiv: 2604.02045
viewer: false
size_categories:
- 1M<n<10M
pretty_name: BidirLM Omni-Contrastive
---

# BidirLM-Omni-Contrastive

This repository serves as the centralized documentation and integration hub for the omnimodal contrastive datasets used to train [**BidirLM-Omni**](https://huggingface.co/BidirLM/BidirLM-Omni-2.5B-Embedding) and introduced in the paper [*BidirLM: From Text to Omnimodal Bidirectional Encoders by Adapting and Composing Causal LLMs*](https://arxiv.org/pdf/2604.02045).

Rather than forcing a massive, monolithic download, this hub provides direct links to the modality-specific repositories and the exact Python code required to load, shuffle, and sample the data for training.

## 📊 Dataset Inventory & Direct Links

The complete training mixture consists of **1,800,000 samples** balanced across multiple modalities. You can visit the source repositories directly using the links below.

| Modality | Source Repository | Target Samples |
| :--- | :--- | :--- |
| **Text ↔ Text** | [BidirLM/BidirLM-Contrastive](https://huggingface.co/datasets/BidirLM/BidirLM-Contrastive) | 1,200,000 |
| **Audio ↔ Text** | [BidirLM/laion_audio_contrastive](https://huggingface.co/datasets/BidirLM/laion_audio_contrastive) | 200,000 |
| **Audio ↔ Text** | [BidirLM/librispeech_contrastive](https://huggingface.co/datasets/BidirLM/librispeech_contrastive) | 100,000 |
| **Image ↔ Text**| [BidirLM/colpali_train_retrieval](https://huggingface.co/datasets/BidirLM/colpali_train_retrieval) | 100,000 |
| **Image ↔ Text** | [BidirLM/natcap](https://huggingface.co/datasets/BidirLM/natcap) | 100,000 |
| **Image ↔ Text** | [BidirLM/mscoco_contrastive](https://huggingface.co/datasets/BidirLM/mscoco_contrastive) | 100,000 |

---

## 🛠️ Loading, Shuffling, and Sampling

To construct the exact 1.8M sample mixture used in BidirLM, use the following code snippets in your training preparation scripts.

### 1. Multimodal Datasets (Image, Audio, Retrieval)
For the standard multimodal datasets, you can use the `datasets` library to load the repository, shuffle it globally, and select your exact sample count.

```python
from datasets import load_dataset

# Set a consistent seed for reproducibility
SEED = 42

# 1. LAION Audio (200k samples)
laion = load_dataset("BidirLM/laion_audio_contrastive", split="train")
laion = laion.shuffle(seed=SEED).select(range(200000))

# 2. LibriSpeech (100k samples)
librispeech = load_dataset("BidirLM/librispeech_contrastive", split="train")
librispeech = librispeech.shuffle(seed=SEED).select(range(100000))

# 3. ColPali Document Retrieval (100k samples)
colpali = load_dataset("BidirLM/colpali_train_retrieval", split="train")
colpali = colpali.shuffle(seed=SEED).select(range(100000))

# 4. NatCap (100k samples)
natcap = load_dataset("BidirLM/natcap", split="train")
natcap = natcap.shuffle(seed=SEED).select(range(100000))

# 5. MSCOCO (100k samples)
mscoco = load_dataset("BidirLM/mscoco_contrastive", split="train")
mscoco = mscoco.shuffle(seed=SEED).select(range(100000))
```

### 2. Text Dataset (1.2M Samples)
Because the text data is stored relationally (Queries referencing a separate Document Corpus), use the following script to download, globally shuffle, sample exactly 1,200,000 queries, and join them with their text.

```python
import json
import pandas as pd
from huggingface_hub import snapshot_download, HfFileSystem
from datasets import Dataset

fs = HfFileSystem()
base_repo = "datasets/BidirLM/BidirLM-Contrastive"
subsets = [d["name"].split("/")[-1] for d in fs.ls(base_repo, detail=True) if d["type"] == "directory"]

# Pass 1: Collect all queries and globally shuffle
all_queries = []
for s in subsets:
    if fs.exists(f"{base_repo}/{s}/queries.parquet"):
        local_path = snapshot_download(repo_id="BidirLM/BidirLM-Contrastive", allow_patterns=[f"{s}/queries.parquet", f"{s}/dataset_metadata.json"])
        q_df = pd.read_parquet(f"{local_path}/{s}/queries.parquet")
        q_df["subset"] = s
        with open(f"{local_path}/{s}/dataset_metadata.json", "r") as f:
            q_df["instruction"] = json.load(f).get("query_instruction", "")
        all_queries.append(q_df)

# Shuffle and select exactly 1.2M
master_q_df = pd.concat(all_queries, ignore_index=True)
master_q_df = master_q_df.sample(frac=1, random_state=42).reset_index(drop=True).head(1200000)

# Pass 2: Resolve the text corpus for the selected samples
resolved_rows = []
for s, group_df in master_q_df.groupby("subset"):
    local_path = snapshot_download(repo_id="BidirLM/BidirLM-Contrastive", allow_patterns=f"{s}/corpus.parquet")
    corpus = dict(zip(pd.read_parquet(f"{local_path}/{s}/corpus.parquet")["id"], pd.read_parquet(f"{local_path}/{s}/corpus.parquet")["text"]))
    
    for _, row in group_df.iterrows():
        resolved_rows.append({
            "question": row["question"],
            "instruction": row["instruction"],
            "positive_docs": [corpus[p["id"]] for p in row["pos_doc"] if p["id"] in corpus],
            "negative_docs": [corpus[n["id"]] for n in row["neg_doc"] if n["id"] in corpus],
        })

# Final ready-to-train text dataset
text_dataset = Dataset.from_pandas(pd.DataFrame(resolved_rows)).shuffle(seed=42)
```

---

## 📜 Citation

If you use this dataset mixture in your research, please cite our work:

```bibtex
@misc{boizard2026bidirlmtextomnimodalbidirectional,
      title={BidirLM: From Text to Omnimodal Bidirectional Encoders by Adapting and Composing Causal LLMs}, 
      author={Nicolas Boizard and Théo Deschamps-Berger and Hippolyte Gisserot-Boukhlef and Céline Hudelot and Pierre Colombo},
      year={2026},
      eprint={2604.02045},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2604.02045}, 
}
```