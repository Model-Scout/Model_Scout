---
license: apache-2.0
base_model: Qwen/Qwen3.8-27B
language: [ko, en]
tags: [knowledge-distillation, cross-tokenizer, korean, research-checkpoint]
pipeline_tag: text-generation
---

# ktransfer-27b-ce-s400

Research checkpoint from **"Anchor or Transfer?"** — an exploratory study of cross-tokenizer knowledge distillation
for Korean adaptation (student Qwen3.8-27B, teacher Gemma-4-31B-it). Paper link: TBA.

**This run:** CE-only fine-tune, step 400. Full fine-tuning of `Qwen/Qwen3.8-27B` with cross-entropy (CE) only.
No teacher signal was used in this run (it is a matched CE-only control).

Released for reproducibility of the paper's tables, including negative results. It is **not** an improved general-purpose model.

## Training
| item | value |
|---|---|
| base | Qwen/Qwen3.8-27B (text stack trained; non-text modules frozen) |
| steps | 400 (run `e1f_27b`) |
| effective batch | 33 sequences × max length 1024 |
| optimizer / lr | adamw8bit / 5e-06, warmup 0.05, weight decay 0.1 |
| hardware | 3× A100-80GB, FSDP, bf16 |
| KD weight | 0.0 (static); KD disabled on the English replay domain |
| seed | 42 |

`training_config.json` holds the full run config (private paths removed).

## Data
A ~14M-character Korean/English mix: a private character-dialogue corpus (~30% of characters), Korean Wikipedia,
Namuwiki, Korean web and news text, and an English FineWeb-Edu replay (15%). **The training data is not released.**

## Evaluation (as reported in the paper draft)
| HRM8K acc | KMMLU acc | ko PPL | en PPL |
|---|---|---|---|
| 0.750 | 0.550 | 27.45 | 9.85 |

200-item subsets of HRM8K and KMMLU with greedy decoding; accuracy is from an automatic grader and is **provisional**
(items flagged for manual review are being re-adjudicated; numbers may change slightly). PPL on held-out Korean / English text.

## Limitations
Single seed, one model pair, short budgets. KD runs showed more repetition under sampling than CE-only.
Not safety-tuned beyond the base model; outputs may reflect the style of the private dialogue corpus.

## License
Apache-2.0, as a modification of Qwen3.8-27B (Apache-2.0). The teacher Gemma-4-31B-it is also Apache-2.0.
See `LICENSE` and `NOTICE`.
