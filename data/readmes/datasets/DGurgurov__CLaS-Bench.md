---
language:
- bo
- mt
- it
- es
- de
- ja
- ar
- zh
- nl
- fr
- pt
- ru
- ko
- hi
- tr
- pl
- sv
- da
- no
- en
- sk
- el
- sw
- kk
- ka
- uk
- fa
- th
- id
- vi
- cs
- ro
license: cc-by-4.0
task_categories:
- text-generation
- translation
pretty_name: CLaS-Bench
tags:
- multilingual
- language-steering
- mechanistic-interpretability
- language-model-evaluation
- parallel-corpus
---

# CLaS-Bench - Cross-Lingual Alignment and Steering Benchmark

**CLaS-Bench** is a lightweight parallel-question benchmark for evaluating
*language-forcing* / *language-steering* behaviour in large language models
(LLMs) across **32 typologically diverse languages**.

Beyond language steering and alignment evaluation, the dataset can also be
used for a variety of multilingual research tasks, including cross-lingual
transfer, language identification, representation analysis, multilingual
robustness evaluation, and studies of typological generalization.

---

## Overview

| Property | Value |
|---|---|
| Languages | 32 |
| Questions per language | 70 |
| Total instances | 2,240 |
| Source questions | Vicuna benchmark (curated subset) |
| Translation | Google Translate API + native-speaker proofreading |
| Question domains | Reasoning · Knowledge · Personal opinion · Creative · Professional writing |

---

## Languages

Tibetan, Maltese, Italian, Spanish, German, Japanese, Arabic, Chinese,
Dutch, French, Portuguese, Russian, Korean, Hindi, Turkish, Polish, Swedish,
Danish, Norwegian, English, Slovak, Greek, Swahili, Kazakh, Georgian,
Ukrainian, Persian, Thai, Indonesian, Vietnamese, Czech, Romanian.

---

## Dataset Structure

```
CLaS-Bench/
├── en   # 70 English questions
├── de   # 70 German questions
├── ...
└── all  # all 2,240 questions with language metadata
```

Each row contains:

| Field | Type | Description |
|---|---|---|
| `id` | string | Unique identifier, e.g. `en_001` |
| `language_code` | string | ISO 639-1 code |
| `language` | string | Full English language name |
| `question_id` | int | Question index 1–70 |
| `question` | string | The question text |

---

## Evaluation Metrics

CLaS-Bench measures steering effectiveness along two axes:

- **Language Forcing Success (LFS)** – fraction of outputs detected (via
  FastText LID) to be in the target language.
- **Output Relevance (OR)** – semantic fidelity scored 0/1/2 by an
  LLM-as-a-judge (Qwen-3-8B), normalised to [0, 1].
- **Language Steering Score (LSS)** – harmonic mean of LFS and OR.

---

## Usage

```python
from datasets import load_dataset

# All languages combined
ds = load_dataset("DGurgurov/CLaS-Bench", split="all")

# Single language split
de = load_dataset("DGurgurov/CLaS-Bench", split="de")
```

---

## Acknowledgements

We are deeply grateful to the many volunteer native and fluent speakers who contributed their time and expertise to proofread and verify the translations in CLaS-Bench. Their careful revisions helped ensure that the dataset is as natural, fluent, and high-quality as possible across all 32 languages. This benchmark would not have been possible without their invaluable contributions.

---

## Citation

```bibtex
@inproceedings{gurgurov-etal-2026-clas,
    title = "{CL}a{S}-Bench: A Cross-Lingual Alignment and Steering Benchmark",
    author = "Gurgurov, Daniil  and
      Al Ghussin, Yusser  and
      Baeumel, Tanja  and
      Chou, Cheng-Ting  and
      Schramowski, Patrick  and
      Mosbach, Marius  and
      van Genabith, Josef  and
      Ostermann, Simon",
    editor = "Liakata, Maria  and
      Moreira, Viviane P.  and
      Zhang, Jiajun  and
      Jurgens, David",
    booktitle = "Findings of the {A}ssociation for {C}omputational {L}inguistics: {ACL} 2026",
    month = jul,
    year = "2026",
    address = "San Diego, California, United States",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2026.findings-acl.1086/",
    doi = "10.18653/v1/2026.findings-acl.1086",
    pages = "21591--21628",
    ISBN = "979-8-89176-395-1",
    abstract = "Understanding and controlling the behavior of large language models (LLMs) is an increasingly important topic in multilingual NLP. Beyond prompting or fine-tuning, $\textit{language steering}$, i.e.,{~}manipulating internal representations during inference, has emerged as a more efficient and interpretable technique for adapting models to a target language. Yet, no dedicated benchmarks or evaluation protocols exist to quantify the effectiveness of steering techniques. We introduce $CLaS-Bench$, a lightweight parallel-question benchmark for evaluating language-forcing behavior in LLMs across 32 languages, enabling systematic evaluation of multilingual steering methods. We evaluate a broad array of steering techniques, including residual-stream DiffMean interventions, probe-derived directions, language-specific neurons, PCA/LDA vectors, Sparse Autoencoders, and prompting baselines. Steering performance is measured along two axes: language control and semantic relevance, combined into a single harmonic-mean steering score. We find that across languages simple residual-based DiffMean method consistently outperforms all other methods. Moreover, a layer-wise analysis reveals that language-specific structure emerges predominantly in later layers and steering directions cluster based on language family. $CLaS-Bench$ is the first standardized benchmark for multilingual steering, enabling both rigorous scientific analysis of language representations and practical evaluation of steering as a low-cost adaptation alternative."
}
```

