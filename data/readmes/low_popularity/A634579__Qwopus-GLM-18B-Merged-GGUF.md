---
license: apache-2.0
base_model:
  - Jackrong/Qwopus3.5-9B-v3.5
  - Jackrong/Qwen3.5-9B-GLM5.1-Distill-v1
tags:
  - merge
  - frankenmerge
  - qwen3.5
  - reasoning
  - text-generation
  - conversational
  - unsloth
  - agent
  - tool-use
  - chain-of-thought
  - gguf
  - qlora
  - multilingual
  - code-generation
model_type: qwen3_5
pipeline_tag: text-generation
language:
  - en
  - zh
  - ko
  - ja
  - fr
  - de
  - es
---

# Qwopus-GLM-18B-Merged 🧪

A **64-layer frankenmerge** of two of [Jackrong's](https://huggingface.co/Jackrong) incredible Qwen3.5-9B finetunes, stacking all 32 layers from each to create an ~18B parameter model, then **healed with a 1000-step LoRA fine-tune** to smooth the layer boundary.

**This was a fun experiment!** A lot of people have been asking for something between Jackrong's 27B and 9B models — something that runs well on 12–16 GB GPUs. This frankenmerge is an attempt at filling that gap, and the results are surprisingly good.



> [!NOTE]
> Thanks to the creator of this model, [@KyleHessling1](https://x.com/KyleHessling1) 🙌 This is still an experimental model, so it may have quirks or issues. If you run into anything weird, or if you make something cool with it, reach out on X.

## Heal Fine-Tune — It Works 🛠️

The raw frankenmerge had a known issue: **garbled code output**. Because two separately-trained models were stacked at layer 32, structured output (code blocks, HTML, bracket matching) would occasionally come out malformed or hallucinated.

We ran a **1000-step QLoRA heal fine-tune** using Jackrong's own training data to let gradients flow across the layer boundary — and the results are significant:

- **HTML generation is now clean and production-quality.** We tested a complex single-page weather dashboard (navbar, dark mode toggle, 5-day forecast grid, responsive sidebar, CSS variables, JavaScript) — the model produced 14,500+ chars of valid HTML/CSS/JS with **perfectly balanced CSS braces, perfectly balanced JS parentheses, no garbled text, and a complete `</html>` closure.**
- **Programming benchmark improved:** 11/15 (raw) -> 12/15 (healed), recovering the `longest_substring` sliding-window algorithm test (8/8 cases passing)
- **Overall score improved:** 39/44 -> **40/44 (90.9%)**, still comfortably beating Qwen 3.6 MoE (38/44) at less than half the VRAM
- **Loss dropped 39%** during training (1.02 -> 0.62), confirming the layer boundary was a real source of error that training could address

The healed GGUF (`Qwopus-GLM-18B-Healed-Q4_K_M.gguf`) is the only version in this repo. If you're interested in the raw unhealed merge for research purposes, reach out.



## Benchmark Results 📊

We ran a 44-test capability suite covering basic generation, reasoning, tool calling, agentic workflows, structured output, context handling, multilingual, programming, and performance.

The healed merge **outperforms the brand new Qwen 3.6-35B-A3B MoE** (Q4_K_M, 22 GB) despite being significantly smaller (Q4_K_M, 9.2 GB):

| Category | Qwopus 9B (source) | **Qwopus-GLM-18B (healed)** | Qwen 3.6-35B MoE |
|---|---|---|---|
| Basic | 6/6 | **6/6** | 5/6 |
| Reasoning | 4/4 | **4/4** | 4/4 |
| Tool Calling | 6/6 | **6/6** | 6/6 |
| Agentic | 4/4 | **4/4** | 4/4 |
| Structured Output | 2/2 | **2/2** | 2/2 |
| Context | 2/3 | **2/3** | 2/3 |
| Multilingual | 2/2 | **2/2** | 2/2 |
| Programming | 13/15 | **12/15** | 12/15 |
| Performance | 2/2 | **2/2** | 1/2 |
| **TOTAL** | **41/44 (93.2%)** | **40/44 (90.9%)** | **38/44 (86.4%)** |
| Throughput | 126.0 tok/s | 66.0 tok/s | 174.2 tok/s |
| GGUF Size | 5.3 GB | **9.2 GB** | 22 GB |

### Key Takeaways

- **40/44 tests passed (90.9% healed)** — beats Qwen 3.6 MoE's 38/44 (86.4%) at less than half the VRAM
- **Heal training recovered programming capability**: 11/15 raw -> 12/15 healed (matching Qwen 3.6 MoE)
- **Perfect tool calling (6/6)** — single calls, optional params, tool selection, complex params, response handling
- **Perfect agentic reasoning (4/4)** — plan generation, multi-step tool workflows, error recovery, self-correction
- **Highest Chinese output density** of any model tested: 129-138 CJK characters
- **~66 tok/s** with low throughput variance — stable inference
- **Fits in 12 GB VRAM** at Q4_K_M — runs on consumer GPUs like RTX 3060/4070

> [!WARNING]
> This model has not undergone a complete or comprehensive evaluation. These benchmark results are provided for reference only.

### Heal Fine-Tune Details

The raw frankenmerge had code formatting issues (garbled code blocks, missing brackets). We ran a 1000-step QLoRA heal fine-tune using Jackrong's training data to smooth the layer-32 boundary:

- **Method:** QLoRA (4-bit NF4), LoRA rank 64, targeting all attention + MLP projections
- **Data:** Blend of `Jackrong/Qwen3.5-reasoning-700x` (70%), `Jackrong/Competitive-Programming-python-blend` (15%), `Jackrong/MultiReason-ChatAlpaca` (15%)
- **Training:** 1000 steps, batch 8, lr 2e-5 cosine, ~14 hours on RTX 5090
- **Loss:** 1.02 -> 0.62 (39% reduction)
- **Result:** Recovered 1 programming test, HTML/CSS output is now clean and production-quality

### Where It Falls Short

Three programming tests still fail on the healed version: one function naming issue, one missing JS paren, and one that doesn't produce a code block for pytest generation. These are residual formatting artifacts from the merge.

## Frontend Code Generation — Stress Test Results 🎨

We put the healed model through a rigorous frontend stress test: 6 increasingly complex HTML/CSS/JS generation tasks, each requiring thousands of tokens of structurally valid code output. The results speak for themselves:

| Test | What We Asked For | Checks Passed | Output Size |
|---|---|---|---|
| Weather Dashboard | Responsive dashboard, CSS vars, dark mode toggle, 5-day forecast grid | **9/9** | 14.5K chars |
| E-Commerce Product Page | Image gallery, color swatches, quantity selector, tabbed content, sticky mobile bar | **12/12** | 16.7K chars |
| Animated SaaS Landing | Moving gradient, typing animation, IntersectionObserver scroll reveals, auto-rotating testimonial carousel, 3 pricing tiers | **13/13** | 24.1K chars |
| Analytics Dashboard | SVG bar chart with tooltips, SVG donut chart, sortable data table, collapsible sidebar, dark theme | **13/13** | 22.3K chars |
| Multi-Step Registration | 3-step form wizard, real-time validation, password strength meter, state dropdown, animated transitions, success modal | **12/12** | 23.3K chars |
| Snake Game | Canvas game loop, arrow key controls, collision detection, localStorage high score, increasing difficulty | **11/12** | 11.2K chars |

**62/63 total checks passed (98.4%)**

Every single output had:
- **Perfectly balanced CSS braces** (zero imbalance across all 6 files)
- **Perfectly balanced JS parentheses** (zero imbalance across all 6 files)
- **Zero garbled or hallucinated text**
- **Working JavaScript** — dark mode toggles, IntersectionObserver animations, SVG chart rendering, form validation, canvas game loops

The only miss: the Snake game had a minor closing tag typo (`html>` instead of `</html>`) at the very end.

This is remarkable for a frankenmerge of two 9B models with only 1000 steps of QLoRA healing. The model is producing **production-quality frontend code** — not just syntactically valid HTML, but sophisticated interactive applications with modern CSS (Grid, Flexbox, custom properties, keyframe animations) and non-trivial JavaScript (IntersectionObserver, requestAnimationFrame game loops, real-time form validation, SVG chart generation).

All 6 sample HTML files are included in the `samples/` directory of this repo — download them and open in a browser to see for yourself.

## Architecture 🧱

| Property | Value |
|---|---|
| **Total Layers** | 64 (32 + 32) |
| **Total Parameters** | ~18B |
| **Hidden Size** | 4096 |
| **Attention Heads** | 16 (4 KV heads, GQA) |
| **Intermediate Size** | 12288 |
| **Context Length** | 262,144 tokens |
| **Attention Type** | Hybrid (linear + full, every 4th layer) |
| **GGUF Q4_K_M Size** | 9.2 GB |

### Layer Composition

```
Layers  0–31:  Jackrong/Qwopus3.5-9B-v3.5         (Opus reasoning distill)
Layers 32–63:  Jackrong/Qwen3.5-9B-GLM5.1-Distill-v1  (GLM-5.1 reasoning distill)

Embeddings, LM head, MTP, vision encoder: from Qwopus3.5-9B-v3.5
```

## Source Models 🧬

All credit for the source models goes to **[Jackrong](https://huggingface.co/Jackrong)**, who created both of these excellent finetunes. I just stacked the layers — the quality comes from his work.

### Jackrong/Qwopus3.5-9B-v3.5

A reasoning-enhanced finetune of Qwen3.5-9B trained with ~2x more SFT data than v3, focused on structured reasoning, tool-augmented workflows, and multi-step agentic tasks.

Key insight from the v3.5 design: *"Scaling high-quality SFT data may further enhance the generalization ability of large language models."* Reasoning SFT helps models better utilize existing knowledge and activate latent knowledge through structured reasoning, rather than simply memorizing long Chain-of-Thought outputs.

**Performance highlights (27B line reference):**
- MMLU-Pro: 90.36% accuracy (+1.07% over v3)
- Agentic coding tests: 43/44 passed (97.7%)

**Resources:**
- [Model Card](https://huggingface.co/Jackrong/Qwopus3.5-9B-v3.5)
- [Fine-Tuning Guide (PDF)](https://github.com/R6410418/Jackrong-llm-finetuning-guide/blob/main/guidePDF/Qwopus3-5-9b-Colab_complete_guide_to_llm_finetuning.pdf)
- [GitHub](https://github.com/R6410418/Jackrong-llm-finetuning-guide)

### Jackrong/Qwen3.5-9B-GLM5.1-Distill-v1

A distilled variant of Qwen3.5-9B trained on high-quality reasoning data from a GLM-5.1 teacher model (~700x scale of Qwen3.5-reasoning-700x). Focused on structured reasoning ability, instruction-following consistency, and problem decomposition.

The model learns a structured reasoning scaffold: understand the task, break down the problem, reason step by step, then construct the final answer.

**Training data:**
- Primary: `Jackrong/GLM-5.1-Reasoning-1M-Cleaned` (cleaned from Kassadin88/GLM-5.1-1000000x)
- Auxiliary: `Jackrong/Qwen3.5-reasoning-700x`

**Resources:**
- [Model Card](https://huggingface.co/Jackrong/Qwen3.5-9B-GLM5.1-Distill-v1)
- [Fine-Tuning Guide (PDF)](https://github.com/R6410418/Jackrong-llm-finetuning-guide/blob/main/guidePDF/Qwopus3-5-27b-Colab_complete_guide_to_llm_finetuning.pdf)

## Why This Works 🤔

By stacking two differently-distilled reasoning models, this merge combines:

1. **Qwopus v3.5's strengths** in agentic tool use, code generation, and token-efficient reasoning (Opus-style training)
2. **GLM-5.1 Distill's strengths** in structured problem decomposition, instruction adherence, and chain-of-thought organization (GLM-style reasoning scaffold)

The hypothesis: deeper networks with diverse reasoning training produce more robust, capable models — and the benchmark results suggest it works, at least for the capabilities we tested.

## Merge Details

- **Method:** Passthrough frankenmerge (layer stacking)
- **Tool:** Custom script (mergekit did not support Qwen3.5's hybrid linear/full attention architecture)
- **Embeddings / LM Head / Visual / MTP:** From Qwopus3.5-9B-v3.5
- **Precision:** BF16 -> Q4_K_M GGUF
- **No additional training** was performed

## Usage 🚀

### With llama.cpp (recommended)

```bash
llama-server \
    -m Qwopus-GLM-18B-Merged-Q4_K_M.gguf \
    --chat-template-file your-qwen35-template.jinja \
    --ctx-size 65536 \
    --flash-attn on \
    --n-gpu-layers 99
```

### With Transformers

The full BF16 safetensors are not included in this GGUF repo. If you need them for further fine-tuning or experimentation, reach out on X.

## Limitations ⚠️

- **Experimental frankenmerge** — no additional training was done. Layer boundaries between the two source models may cause occasional coherence or formatting issues.
- **Code formatting** — the model sometimes garbles fenced code blocks (returns code without proper markdown fencing). The reasoning is usually correct even when the formatting isn't.
- **Not exhaustively tested** — this was a fun weekend project. There may be edge cases we haven't found yet.
- **Hallucination risk** — as with all autoregressive LLMs, outputs may contain factual errors.

## Supported Research

Both source models reference: **Ren et al., 2026 — *Rethinking Generalization in Reasoning SFT*** ([arXiv:2604.06628](https://arxiv.org/abs/2604.06628))

Key findings: reasoning SFT generalizes when sufficiently trained; high-quality long-CoT data enables cross-domain transfer; stronger models learn reasoning structure, not just longer outputs.

## Acknowledgements 🙏

- **[Jackrong](https://huggingface.co/Jackrong)** — the real MVP. Both source models, training pipelines, datasets, and documentation are his work. This merge exists because his finetunes are so good that even stacking them naively produces something surprisingly capable.
- **[Qwen](https://huggingface.co/Qwen)** for the excellent Qwen3.5-9B base model
- **[Unsloth AI](https://unsloth.ai)** for efficient fine-tuning infrastructure
- **GLM-5.1 team** for the teacher model used in distillation
- **[Kassadin88](https://huggingface.co/Kassadin88)** for the original GLM-5.1-1000000x dataset
- The broader open-source community

## Questions? 💬

This was just for fun — reach out on X if you have questions, find issues, or build something cool with it!

**[@KyleHessling1](https://x.com/KyleHessling1)**

> [!WARNING]
> ⚠️ This is an experimental test model created as part of a fun community exploration project. It is a frankenmerge built without additional post-training or comprehensive safety evaluation. As a result, the model may exhibit unstable behavior, formatting errors, inconsistent reasoning, or other unexpected artifacts. It is intended for research and experimentation only.

## Citations

```bibtex
@misc{jackrong_qwopus35_9b_v35,
  title  = {Qwopus3.5-9B-v3.5},
  author = {Jackrong},
  year   = {2026},
  publisher = {Hugging Face}
}

@misc{jackrong_qwen35_9b_glm51_distill_v1,
  title  = {Qwen3.5-9B-GLM5.1-Distill-v1},
  author = {Jackrong},
  year   = {2026},
  publisher = {Hugging Face}
}
```
