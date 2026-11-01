---
license: cc0-1.0
---

# Text to Mermaid

## Description

A curated dataset designed for fine-tuning small language models on diagram generation tasks. Each example follows a strict response format: when prompted for a diagram, the model outputs **only** the Mermaid syntax—no explanations, no markdown fences, no extra text.

Derived from [Celiadraw/text-to-mermaid-2](https://huggingface.co/datasets/Celiadraw/text-to-mermaid-2), this version has been verified, pruned, cleaned, and reworded for reliability and consistency.

## Dataset Statistics

| Metric | Value |
|--------|-------|
| Source rows | 5,410 |
| Final rows | 3,837 |
| Final validation pass | 100% valid (Mermaid v11, core) |

## Validation Pipeline

**Source:** [Celiadraw/text-to-mermaid-2](https://huggingface.co/datasets/Celiadraw/text-to-mermaid-2)

### Phase 1 — Initial Validation
Validated all diagrams against **Mermaid v11 (core only)**.

| Result | Count |
|--------|-------|
| Valid | 4,493 |
| Invalid | 917 |

### Phase 2 — Diagram Type Filtering
Dropped **386 rows** containing unsupported or non-core diagram types.

### Phase 3 — Text-Level Fixes
Applied automated and manual text-level corrections.

### Phase 4 — Re-Validation After Cleaning
Re-ran validation on the cleaned subset.

| Result | Count |
|--------|-------|
| Now valid | 3,837 |
| Still invalid | 656 *(dropped)* |

### Phase 5 — Prompt Rewording
Reworded all prompts to **strictly specify the target chart or diagram type**, ensuring unambiguous task framing.

**Final output:** **3,837 rows**

## Intended Use

- Fine-tuning small LLMs for structured diagram generation
- Training models to emit raw Mermaid syntax without conversational wrapper text
- Benchmarking diagram-to-code capabilities in compact model architectures