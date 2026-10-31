---
license: cc-by-4.0
language:
- en
- ja
- zu
- yo
- zh
- ko
- th
- sw
tags:
- medical
size_categories:
- 1K<n<10K
---

# MultiMed-X

**MultiMed-X** is a multilingual benchmark for **medical reasoning evaluation** across **natural language inference (NLI)** and **open-ended question answering (QA)**.  
The dataset is designed to assess **reasoning quality, factual accuracy, and localization** of large language models in **non-English medical settings**, with particular emphasis on **low-resource languages**.

This dataset accompanies the paper: [**MED-COREASONER: Reducing Language Disparities in Medical Reasoning via Language-Informed Co-Reasoning**](https://arxiv.org/pdf/2601.08267).


---

## Dataset Overview

MultiMed-X-350 is constructed by translating and expert-validating two established English medical benchmarks:

- **BioNLI** → Multilingual **medical natural language inference (NLI)**, original data from [BioNLI: Generating a Biomedical NLI Dataset Using Lexico-semantic Constraints for Adversarial Examples](https://arxiv.org/abs/2210.14814).
- **LiveQA** → Multilingual **open-ended medical question answering (QA)**, original data from [LiveQA: A Question Answering Dataset over Sports Live](https://aclanthology.org/2020.ccl-1.98.pdf).

Each instance is translated into multiple target languages and **independently reviewed and revised by bilingual medical experts** to ensure clinical correctness and linguistic naturalness.

### Languages

The dataset covers **7 non-English languages**:

- Chinese (**ZH**)
- Japanese (**JA**)
- Korean (**KO**)
- Swahili (**SW**)
- Thai (**TH**)
- Yoruba (**YO**)
- Zulu (**ZU**)

---


## Data Format

All data are released as a **single unified table** (e.g., JSONL / Parquet compatible with Hugging Face `datasets`).

### Common Fields

| Field   | Type   | Description |
|--------|--------|-------------|
| `id`   | string | Unique instance ID |
| `lang` | string | Language code (e.g., `zu`, `sw`) |
| `task` | string | Task type: `nli` or `qa` |
| `source` | string | Data source (`BioNLI` or `LiveQA`) |
| `text` | string | Original content in the target language |
| `label` | string / null | Gold label (NLI only) |

---

### ID Convention

- **NLI (BioNLI)**  
  `bionli-<lang>-XYZ`

- **QA (LiveQA)**  
  `qa-<lang>-XYZ`

Only **3-digit numeric suffixes** are used.

---

### Example Entries

#### NLI Example

```json
{
  "id": "bionli-zu-042",
  "lang": "zu",
  "task": "nli",
  "source": "BioNLI",
  "text": "Premise: ... Hypothesis: ...",
  "label": "entailment"
}
```

#### QA Example

```json
{
  "id": "qa-sw-117",
  "lang": "sw",
  "task": "qa",
  "source": "LiveQA",
  "text": "Swali: ... Jibu: ...",
  "label": null
}
```

---

## Data Statistics

- **350 instances per language**
  - 150 NLI (BioNLI)
  - 200 QA (LiveQA)
- **~2,450 total instances**
- Annotated and validated by **~12 physicians or senior medical students**

---

## Intended Use

MultiMed-X-350 is intended for:

- Multilingual medical reasoning evaluation
- Cross-lingual robustness analysis
- Low-resource language benchmarking
- Evaluation of reasoning strategies (e.g., CoT, structured reasoning, agentic systems)

⚠️ **Not intended for clinical deployment or direct medical decision-making.**

---

## Ethical Considerations

- All data are derived from **publicly available datasets**
- Translations are **expert-reviewed**
- No private patient data are included
- Annotators were formally recruited and compensated or credited as co-authors

---

## Citation

```bibtex
@article{gao2026medcoreasoner,
  title={MED-COREASONER: Reducing Language Disparities in Medical Reasoning via Language-Informed Co-Reasoning},
  author={Gao, Fan and Tong, Sherry T. and Sohn, Jiwoong and Huang, Jiahao and Jiang, Junfeng and Xia, Ding and Ittichaiwong, Piyalitt and Veerakanjana, Kanyakorn and Kim, Hyunjae and Chen, Qingyu and Taylor, Edison Marrese and Kobayashi, Kazuma and Aizawa, Akiko and Li, Irene},
  journal={arXiv preprint arXiv:2601.08267},
  year={2026}
}
```

---

## License

This dataset is released for **research and evaluation purposes only**, under the same licensing terms as the original source datasets (BioNLI, LiveQA).