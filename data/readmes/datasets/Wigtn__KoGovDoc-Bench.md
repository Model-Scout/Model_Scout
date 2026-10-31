---
license: apache-2.0
language:
  - ko
  - en
tags:
  - document-parsing
  - ocr
  - korean
  - government-documents
  - benchmark
  - vlm
  - synthetic-data
  - distillation
size_categories:
  - n<1K
---

# KoGovDoc-Bench

**KoGovDoc-Bench** is an evaluation benchmark specifically designed for high-fidelity Korean government document parsing. It was used to evaluate [WigtnOCR-2B](https://huggingface.co/Wigtn/Qwen3-VL-2B-WigtnOCR), a model trained via pseudo-label distillation.

## 🚀 Data Pipeline & Engineering

This dataset is not just a collection of raw outputs. It is the result of a rigorous **Synthetic Data Distillation & Quality Assurance (QA)** pipeline.

### 1. Pseudo-GT Generation (Teacher-Student Distillation)
* **Teacher Model:** `Qwen3-VL-30B-Instruct`
* **Source Pool:** 4,501 pages (KoGovDoc: 3,637 / arXiv: 864)
* **Key Finding:** During initial trials with **Reasoning (Thinking) models**, we observed output instability (e.g., `<think>` tag leakage, token truncation). We found that **Instruction-tuned models** are significantly more stable for long-form document transcription tasks.

### 2. GT Quality Assurance (LLM-as-a-Judge)
* **Judge Model:** `Qwen3.5-122B`
* **Method:** 5-point scale evaluation based on text-only quality.
* **Heuristics:** We focused on identifying "trainable quality" rather than pixel-perfect matching. The Judge model successfully filtered out repetitive loops, truncated text, and residual reasoning traces.
* **Pass Rate:** KoGovDoc (75.1%) / arXiv (73.8%).
* **Filter:** Only samples with **Score ≥ 3** were included in the final dataset.

### 3. Data Cleaning & Balancing
* **Bias Mitigation:** Identified a skew where a single document (kogov_008) accounted for 53% of the pool. We applied `max_doc_ratio=0.25` to ensure diverse document representation.
* **De-noising:** Manually reviewed and cleaned **277 samples** contaminated with reasoning residues (English thought processes) from earlier model versions.
* **Final Split:** **Train: 2,667 samples / Val (Benchmark): 294 samples.**

---

## 📊 Dataset Structure

| Attribute | Value |
|-----------|-------|
| Total Benchmark Pages | 294 |
| Document Types | 38 (9 Korean Gov + 29 ArXiv Papers) |
| Format | Page images (PNG) + Pseudo-GT (Markdown) |
| Validation Logic | Qwen3.5-122B Cross-validation |

```json
// val.jsonl Example
{
  "messages": [
    {"role": "system", "content": "Convert the image to markdown..."},
    {"role": "user", "content": "<image>"},
    {"role": "assistant", "content": "# High Quality Markdown Output..."}
  ],
  "images": ["images/documents/kogov_001/page_0001.png"]
}
```

---

## 📈 Evaluation Results

### NED (Text Quality) - Lower is Better
| Model | NED ↓ |
|-------|:-----:|
| **WigtnOCR-2B** | **0.285** |
| Qwen3-VL-30B | 0.334 |
| Qwen3-VL-2B | 0.390 |

### Retrieval Performance (Semantic Chunking → BGE-M3 → FAISS)
| Model | Hit@1 ↑ | MRR@10 ↑ |
|-------|:-------:|:--------:|
| **WigtnOCR-2B** | **0.739** | **0.788** |
| Qwen3-VL-30B | 0.716 | 0.771 |
| Marker / MinerU | 0.711 / 0.608 | 0.771 / 0.682 |

---

## Citation

```bibtex
@software{wigtnocr2026,
  title   = {WigtnOCR: Pseudo-Label Distillation for Structure-Preserving Document Parsing},
  author  = {Kim, Hyeongseob},
  year    = {2026},
  url     = {https://github.com/Hyeongseob91/research-vlm-based-document-parsing}
}
```
