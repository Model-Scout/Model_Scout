---
license: apache-2.0
language:
- ko
- en
base_model:
- Qwen/Qwen3-Embedding-0.6B
pipeline_tag: feature-extraction
library_name: sentence-transformers
tags:
- embedding
- retrieval
- cybersecurity
- mitre-attack
- korean
- qwen3
---

# PurpleHound-Embed-v1

Developed by [78ResearchLab](https://huggingface.co/78ResearchLab).

A 1024-d text embedding model for **cybersecurity attack-technique retrieval** (Korean / English), fine-tuned from [Qwen/Qwen3-Embedding-0.6B](https://huggingface.co/Qwen/Qwen3-Embedding-0.6B). It powers the attack action search of the PurpleHound BAS (Breach and Attack Simulation) chatbot and is a drop-in replacement for the base model (same pooling, prompt format and context length).

| | |
|---|---|
| Parameters | 0.6B (595M) |
| Embedding dimension | 1024 |
| Max sequence length | 32,768 tokens |
| Pooling | last token, L2-normalised |
| Languages | Korean, English (multilingual base) |
| License | Apache-2.0 |

## Results

Leads every open model we compared on attack-technique retrieval, both public and in production; on general retrieval it stays within ~0.02 nDCG@10 of the base model.

| Benchmark (metric) | PurpleHound-Embed-v1 | Qwen3-Embedding-0.6B (base) | Best other open model |
|---|---|---|---|
| ATT&CK technique retrieval, public (nDCG@10) | **0.586** | 0.538 | 0.516 (ATTACK-BERT) |
| Attack action search, production (R@5) | **0.876** | 0.810 | 0.850 (arctic-embed-l-v2.0) |
| MTEB Korean retrieval, 8 tasks (avg nDCG@10) | 0.712 | 0.732 | 0.773 (BGE-m3-ko) |
| MTEB English retrieval, 5 tasks (avg nDCG@10) | 0.482 | 0.494 | 0.465 (multilingual-e5-large-instruct) |

### Security: text → MITRE ATT&CK technique (public)

3,170 English threat-report sentences from [Security-TTP-Mapping](https://huggingface.co/datasets/tumeteor/Security-TTP-Mapping) (test) retrieving over all 596 ATT&CK v12.1 Enterprise techniques.

| Model | nDCG@10 | R@1 | R@5 | R@10 | MRR@10 |
|---|---|---|---|---|---|
| **PurpleHound-Embed-v1** | **0.586** | **0.433** | **0.700** | **0.787** | **0.543** |
| Qwen3-Embedding-0.6B | 0.538 | 0.369 | 0.659 | 0.751 | 0.491 |
| bge-m3 | 0.463 | 0.310 | 0.567 | 0.673 | 0.418 |
| KURE-v1 | 0.450 | 0.293 | 0.548 | 0.658 | 0.403 |
| multilingual-e5-large | 0.431 | 0.277 | 0.524 | 0.643 | 0.382 |
| arctic-embed-l-v2.0 | 0.477 | 0.325 | 0.579 | 0.677 | 0.433 |
| multilingual-e5-large-instruct | 0.388 | 0.244 | 0.483 | 0.585 | 0.343 |
| BGE-m3-ko | 0.464 | 0.313 | 0.564 | 0.667 | 0.420 |
| ATTACK-BERT † (110M, en) | 0.516 | 0.365 | 0.624 | 0.717 | 0.473 |

† Reference public cybersecurity embedding model ([basel/ATTACK-BERT](https://huggingface.co/basel/ATTACK-BERT), MPNet, English-only).

### Security: attack action search (production, internal data)

4,928 held-out Korean/English queries against the production index of 1,260 attack actions.

| Model | R@1 | R@5 | R@10 | MRR |
|---|---|---|---|---|
| **PurpleHound-Embed-v1** | **0.721** | **0.876** | **0.901** | **0.770** |
| Qwen3-Embedding-0.6B | 0.657 | 0.810 | 0.846 | 0.706 |
| bge-m3 | 0.662 | 0.826 | 0.855 | 0.715 |
| KURE-v1 | 0.652 | 0.827 | 0.856 | 0.708 |
| multilingual-e5-large | 0.675 | 0.830 | 0.859 | 0.725 |
| arctic-embed-l-v2.0 | 0.700 | 0.850 | 0.874 | 0.748 |
| multilingual-e5-large-instruct | 0.618 | 0.796 | 0.832 | 0.676 |
| BGE-m3-ko | 0.657 | 0.828 | 0.859 | 0.711 |
| ATTACK-BERT † (110M, en) | 0.197 | 0.299 | 0.347 | 0.232 |

### General retrieval: MTEB (nDCG@10)

| Model | Korean retrieval (8 tasks) | English retrieval (5 tasks) |
|---|---|---|
| **PurpleHound-Embed-v1** | 0.712 | 0.482 |
| Qwen3-Embedding-0.6B | 0.732 | **0.494** |
| bge-m3 | 0.755 | 0.415 |
| KURE-v1 | 0.773 | 0.418 |
| multilingual-e5-large | 0.755 | 0.440 |
| arctic-embed-l-v2.0 | 0.769 | 0.462 |
| multilingual-e5-large-instruct | 0.742 | 0.465 |
| BGE-m3-ko | **0.773** | 0.417 |

<details><summary>Per-task scores</summary>

| Task | **PurpleHound-Embed-v1** | Qwen3-Embedding-0.6B | bge-m3 | KURE-v1 | multilingual-e5-large | arctic-embed-l-v2.0 | multilingual-e5-large-instruct | BGE-m3-ko |
|---|---|---|---|---|---|---|---|---|
| AutoRAG (ko) | 0.781 | 0.828 | 0.832 | **0.874** | 0.814 | 0.840 | 0.779 | 0.874 |
| Ko-StrategyQA | 0.732 | 0.758 | 0.793 | 0.801 | 0.802 | 0.805 | **0.806** | 0.796 |
| LawIRKo | 0.733 | 0.753 | 0.716 | 0.743 | 0.729 | **0.758** | 0.721 | 0.731 |
| SQuADKor v1 | 0.848 | 0.849 | 0.904 | 0.936 | 0.905 | 0.912 | 0.894 | **0.941** |
| PublicHealthQA (ko) | 0.805 | 0.809 | 0.804 | 0.818 | **0.824** | 0.817 | 0.799 | 0.821 |
| Belebele (ko-ko) | 0.893 | 0.912 | 0.931 | 0.950 | 0.944 | 0.928 | 0.929 | **0.951** |
| XPQA (ko-ko) | 0.337 | 0.334 | 0.360 | 0.381 | 0.358 | **0.430** | 0.349 | 0.382 |
| MIRACL-HN v2 (ko) | 0.566 | 0.610 | **0.698** | 0.683 | 0.664 | 0.664 | 0.658 | 0.689 |
| SciFact | 0.717 | 0.699 | 0.642 | 0.645 | 0.703 | 0.711 | **0.719** | 0.651 |
| NFCorpus | **0.366** | 0.363 | 0.315 | 0.312 | 0.340 | 0.352 | 0.356 | 0.311 |
| ArguAna | 0.674 | **0.693** | 0.541 | 0.575 | 0.544 | 0.592 | 0.584 | 0.557 |
| SCIDOCS | 0.231 | **0.243** | 0.164 | 0.152 | 0.175 | 0.203 | 0.187 | 0.161 |
| FiQA-2018 | 0.423 | 0.472 | 0.413 | 0.407 | 0.438 | 0.454 | **0.478** | 0.403 |
| **Avg (Korean, 8)** | 0.712 | 0.732 | 0.755 | 0.773 | 0.755 | 0.769 | 0.742 | **0.773** |
| **Avg (English, 5)** | 0.482 | **0.494** | 0.415 | 0.418 | 0.440 | 0.462 | 0.465 | 0.417 |

</details>

<details><summary>Evaluation details</summary>

- **ATT&CK**: corpus = every technique and sub-technique in the ATT&CK v12.1 Enterprise STIX bundle as `<id> <name>: <description>`; a query is relevant to each technique it is labelled with. Instruction for instruction-following models: *"Given a description of attacker behavior, retrieve the matching MITRE ATT&CK technique"*; other models use their documented query prefix.
- **Action search**: 2,520 indexed rows (1,260 distinct actions, Korean descriptions), documents as `{name} | {description}`, cosine top-10 with similarity threshold 0.3, no metadata filters — the production `action_search` path. Queries use the instruction the production system sends; with the built-in `query` prompt instead the model scores R@1 0.694 / R@5 0.862 / R@10 0.889 / MRR 0.747, still first.
- **MTEB**: `mteb==2.20.11`, bf16, `max_seq_length=1024`, MTEB default task instructions, Korean subsets only for multilingual tasks. Comparators are same-size (0.56–0.6B) open models; KURE-v1 and BGE-m3-ko are Korean-specialised fine-tunes.

</details>

## Training

- Base: Qwen/Qwen3-Embedding-0.6B
- Data: 7,380 (query, action description) pairs — 1,250 attack actions × ~6 LLM-generated queries (≈90% Korean, rest English). Evaluation uses different queries for the same actions. The action corpus is proprietary and not released.
- InfoNCE with in-batch negatives (τ = 0.05), 3 epochs, batch 32, AdamW lr 2e-5, max length 512
- Queries carry a task instruction in the base model's `Instruct: {task}\nQuery:` format; documents have no prefix

## Usage

```python
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("78ResearchLab/PurpleHound-Embed-v1")

queries = ["credential dumping from LSASS memory",
           "scheduled task used for persistence after initial access"]
docs = ["T1003.001 LSASS Memory: adversaries may attempt to access credential material stored in the process memory of LSASS ...",
        "T1053.005 Scheduled Task: adversaries may abuse the Windows Task Scheduler to perform task scheduling for persistence ..."]

q = model.encode(queries, prompt_name="query")   # built-in attack-technique instruction
d = model.encode(docs)
print(model.similarity(q, d))
```

Queries take an instruction prefix (`Instruct: {task}\nQuery: {text}`), documents do not. Any task instruction works; the built-in `query` prompt is a good default.

<details><summary>Plain transformers</summary>

```python
import torch, torch.nn.functional as F
from transformers import AutoModel, AutoTokenizer

tok = AutoTokenizer.from_pretrained("78ResearchLab/PurpleHound-Embed-v1", padding_side="left")
model = AutoModel.from_pretrained("78ResearchLab/PurpleHound-Embed-v1")

def embed(texts, instruction=None):
    if instruction:
        texts = [f"Instruct: {instruction}\nQuery: {t}" for t in texts]
    batch = tok(texts, padding=True, truncation=True, max_length=2048, return_tensors="pt")
    emb = model(**batch).last_hidden_state[:, -1]   # last token (left padding)
    return F.normalize(emb, dim=-1)
```

</details>

## Limitations

- Tuned for short attack-behaviour queries; long-document retrieval is inherited from the base model, not improved.
- The action-search benchmark uses internal data and cannot be reproduced outside 78ResearchLab; the MTEB and ATT&CK numbers can.
- Retrieves descriptions of attack techniques for security testing and training; it is not a detection or safety model.

## Citation

```bibtex
@misc{purplehound-embed-v1,
  title        = {PurpleHound-Embed-v1: A Cybersecurity Attack-Technique Retrieval Embedding Model},
  author       = {78ResearchLab},
  year         = {2026},
  publisher    = {Hugging Face},
  howpublished = {\url{https://huggingface.co/78ResearchLab/PurpleHound-Embed-v1}}
}
```

Please also cite the base model:

```bibtex
@article{qwen3embedding,
  title   = {Qwen3 Embedding: Advancing Text Embedding and Reranking Through Foundation Models},
  author  = {Zhang, Yanzhao and Li, Mingxin and Long, Dingkun and Zhang, Xin and Lin, Huan and Yang, Baosong and Xie, Pengjun and Yang, An and Liu, Dayiheng and Lin, Junyang and Huang, Fei and Zhou, Jingren},
  journal = {arXiv preprint arXiv:2506.05176},
  year    = {2025}
}
```
