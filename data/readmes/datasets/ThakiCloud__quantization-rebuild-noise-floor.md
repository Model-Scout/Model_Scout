---
license: apache-2.0
language: [en, ko]
tags: [quantization, gptq, evaluation, reproducibility, measurement]
pretty_name: Quantization Rebuild Noise Floor
size_categories: [n<1K]
task_categories:
- text-generation
---

# Quantization Rebuild Noise Floor

**Running the same quantization recipe twice produces two checkpoints that differ by more than most
papers' reported deltas.** This dataset is the measurement.

We quantized `Qwen3.8-27B` to W4A16 with GPTQ, then ran **the exact same recipe a second time** —
same model, same settings, same calibration set, only a different quantization run. We evaluated both
builds in a single serving run so no engine or configuration difference could leak in, then measured
how far apart they landed.

| Task | Metric | Gap between two identical-recipe builds |
|---|---|---|
| GSM8K (en) | exact_match, strict | **3.56 pp** (1.83σ, n=1,319) |
| GSM8K (en) | exact_match, flexible | 2.27 pp (1.18σ) |
| GSM8K (ko) | exact_match, strict | 2.13 pp (1.10σ) |
| GSM8K (ko) | exact_match, flexible | 1.37 pp (0.73σ) |
| **RAG, absent-information** | **fabrication rate** | **27.08 pp (7.5σ, n=240)** |

## Paper

A short write-up of this measurement is included in the repository:
**[One-Versus-One Checkpoint Comparison Can Manufacture a Recipe Effect](paper/rebuild-noise-floor.pdf)**
(6 pages, LaTeX source at `paper/rebuild-noise-floor.tex`).

The paper prints every value it uses in its own tables, so each statistic in it can be
recomputed from the text alone without opening this repository. It is deliberately narrow: it
reports the rebuild floor on both tasks, the sign reversal, the near-miss described below, and
the sample-size caveat, and it makes no claim beyond them.

The paper is released under **CC BY 4.0**; the data files in this repository remain under the
repository license (Apache-2.0) recorded above.

## Why this matters

Quantization work routinely compares checkpoints built once each — recipe A versus recipe B, one build
apiece — and attributes the difference to the recipe. If the build-to-build spread is larger than the
observed gap, that attribution does not hold.

Our own work ran into this. We had concluded that one of our checkpoints hallucinated far more than a
third-party one on absent-information questions (9.17% vs 1.25%). Then we measured the floor: a second
build of *the same recipe* scored **36.25%**. The gap we were about to ship a decision on was smaller
than the noise.

**A practical rule that falls out of this: if the observed difference is under 2× the rebuild floor for
that metric, do not attribute it to the treatment.** Report it as unresolved and build more copies.

## The second finding: accuracy metrics hide it

The bad build was not bad everywhere. `ours-r2` had the **highest extraction accuracy of all four arms**
(0.5375) and an identical grounded-answer score. Only abstention behaviour — refusing to answer when the
document does not contain the value — collapsed. A quality gate built on accuracy alone would have
shipped it.

## Contents

- `data/measurements.jsonl` — per-arm, per-metric results with the serving configuration attached.
  Arms: `ours` (build #1), `ours-r2` (identical recipe, second run), `ours-mamba` (third build with a
  different ignore list), `bf16` (unquantized), `int4-redhat` (third-party frozen artifact).
- `data/rebuild_noise_floor.jsonl` — the derived floor per task and metric.

## Method

Both GSM8K arms ran in one serving session (vLLM 0.27.1, lm-eval 0.4.12, greedy decoding, full
1,319-item sets, `max_model_len=8192`, `max_num_seqs=64`). The RAG arms ran in a separate single session
(`max_model_len=131072`, `max_num_seqs=256`, n=240 synthetic Korean procurement documents at hard
difficulty). Serving configuration was identical across arms within each session; only the model path
changed. **Do not compare absolute values across the two sessions** — the configurations differ.

## Limits

- **One pair.** Two builds give one difference. That is a lower bound on the spread, not a standard
  deviation. Estimating the distribution needs more copies.
- **Floors are per metric and per task.** The 3.56 pp figure does not transfer to other benchmarks.
- **This is our pipeline.** Frozen third-party checkpoints are shipped artifacts; a customer receives
  that exact file, so build variance is not part of their decision. It is part of ours, because we
  rebuild.
- **`ours-mamba` is a third build with a different ignore list**, so its gap mixes treatment and build
  noise. It is included for completeness, not as a controlled comparison.
- One model family, one quantization method, one hardware generation.

## Citation

```
@misc{thakicloud2026rebuildfloor,
  title  = {Quantization Rebuild Noise Floor},
  author = {ThakiCloud},
  year   = {2026},
  url    = {https://huggingface.co/datasets/ThakiCloud/quantization-rebuild-noise-floor}
}
```

## Collection

Part of [Evals & Reproducibility](https://huggingface.co/collections/ThakiCloud/evals-and-reproducibility-6a9e6effa3c3b027077af99e).
