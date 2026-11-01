---
license: apache-2.0
language:
- en
- id
- ms
- zh
- ja
- ko
- ta
- hi
- ur
library_name: pytorch
pipeline_tag: text-generation
base_model: AneekC/quipu-moe-1B-A149M
tags:
- from-scratch
- mixture-of-experts
- small-language-model
- multilingual
- code
- distillation
datasets:
- HuggingFaceFW/fineweb-edu
- HuggingFaceFW/fineweb-2
- codeparrot/github-code-clean
- CohereForAI/aya_dataset
- OpenAssistant/oasst2
- nvidia/OpenCodeInstruct
- codeparrot/apps
---

# quipu-moe-1B-A149M-chat-distill

A mixture-of-experts language model trained from scratch: **998,007,552 parameters
in total, 148,660,992 active per token** (998.0M total / 148.7M active). Own tokenizer, own data
pipeline, no fine-tuned base. Code and ten languages: English, Indonesian, Malay,
Simplified and Traditional Chinese, Japanese, Korean, Tamil, Hindi (Devanagari and
romanised) and romanised Urdu.

This is the **distilled chat model**: [quipu-moe-1B-A149M](https://huggingface.co/AneekC/quipu-moe-1B-A149M)
after the same short supervised fine-tune as [quipu-moe-1B-A149M-chat](https://huggingface.co/AneekC/quipu-moe-1B-A149M-chat),
with one change: 3,100 coding answers from an open-weight teacher
(Qwen/Qwen2.5-Coder-1.5B-Instruct, Apache-2.0) added to the human-written conversations.
Every teacher answer kept was **run against its unit tests in a sandbox**; answers that
failed, did not finish, or had no code were dropped (3,277 of 5,000 passed).

| greedy pass@1 | HumanEval (164) | MBPP sanitized test (257) |
|---|---:|---:|
| quipu-moe-1B-A149M-chat | 0.0% (0) | 1.9% (5) |
| **quipu-moe-1B-A149M-chat-distill** | **0.6% (1)** | **7.4% (19)** |

Both measured with the same harness, prompts and greedy decoding (see Evaluation).
That is still low in absolute terms: reference models of similar total size score far
higher (table below). At this size it is often wrong. It is published as an honest record
of what a small sparse model learns when pretrained under a $20 compute cap.

Project page: <https://quipulm.dev> · Code: <https://github.com/Aneek1/quipu>

## Architecture

| | |
|---|---|
| Type | Decoder-only transformer, sparse mixture of experts |
| Parameters | 998,007,552 total / 148,660,992 active per token (998.0M / 148.7M; embeddings tied, counted once) |
| Layers / width | 16 layers, d_model 768 |
| Attention | grouped-query, 12 query / 4 key-value heads, head dim 64, RoPE base 10000 |
| Feed-forward | 1 shared expert(s) (hidden 768) + 64 routed experts (hidden 384), top-4 |
| Routing | softmax router, Top-k on score + bias, weights renormalised over the chosen experts; Quantile Balancing (auxiliary-loss-free bias) |
| Expert activation | SwiGLU. The A/B rule kept SiTU-GLU (pair 3, below), but the full run was overridden to SwiGLU: a 0.047 loss gain did not pay for its lower tokens/s |
| Depth mixing | plain pre-norm residual (Block Attention Residuals not used) (per the A/B winners, results/moe/run_config.toml) |
| Optimizer | Muon (Newton-Schulz orthogonalised per attention head) for weight matrices, AdamW for the rest (per the A/B winners, results/moe/run_config.toml) |
| Training precision | bf16 (router and balancing math in fp32; per the A/B winners, results/moe/run_config.toml) |
| Context | 2,048 tokens |
| Tokenizer | byte-level BPE, 49,152 tokens, trained for this model (code-aware whitespace, ten languages) |

## Data

| source | dataset | revision | licence |
|---|---|---|---|
| code | codeparrot/github-code-clean | `c48d40f9e70f` | the permissive subset of codeparrot/github-code-clean (each file keeps its own licence) |
| english | HuggingFaceFW/fineweb-edu | `87f09149ef47` | HuggingFaceFW/fineweb-edu, ODC-By 1.0 |
| fineweb2 | HuggingFaceFW/fineweb-2 | `af9c13333eb9` | HuggingFaceFW/fineweb-2, ODC-By 1.0 |

Mix achieved (share of training tokens): code 60.0%, eng_Latn 28.0%, other_languages 12.0%.

Training tokens in the shard set: 8,300,000,000 (the train split; validation and evaluation splits are separate).

Code licences kept: mit, apache-2.0, bsd-2-clause, bsd-3-clause, isc, cc0-1.0, unlicense.

Language identification: every text document was checked with the fastText specialist from [AneekC/lid-specialists-9plus1](https://huggingface.co/AneekC/lid-specialists-9plus1) (MIT, revision `117966eb565a`), the owner's own model; a document whose top label is not its source language was dropped, and FineWeb-2's cmn_Hani was split into Simplified and Traditional Chinese by its labels.

| language | kept | dropped | kept while unsure |
|---|---:|---:|---:|
| English | 2,118,540 | 920 | 0 |
| Urdu (romanised) | 13,692 | 55,629 | 0 |
| Hindi (romanised) | 80,968 | 5,188 | 0 |
| Tamil | 98,348 | 536 | 0 |
| Malay | 130,638 | 5,783 | 0 |
| Hindi (Devanagari) | 107,087 | 63,675 | 0 |
| Korean | 107,219 | 1,086 | 0 |
| Indonesian | 103,664 | 2,846 | 0 |
| Japanese | 102,510 | 222 | 0 |
| Chinese (script not split) | 230,766 | 166 | 0 |

### Benchmark decontamination

Documents dropped because they contain a HumanEval or MBPP problem (rule, from the shard manifest: a document is dropped when it contains a problem's text (HumanEval: prompt, canonical_solution; MBPP: code, task text) as a whitespace-collapsed substring of at least 60 characters, or, for one of the problem's n-gram texts (its solution; HumanEval also its prompt and each docstring in it), at least 50% and at least 2 of that text's distinct 13-grams (tokens: \w+ runs and single punctuation characters; a text with fewer than 2 13-grams takes no part)):

| split | humaneval | mbpp |
|---|---:|---:|
| train_code | 79 | 44 |
| train_text | 0 | 1 |
| code_val | 0 | 0 |
| val | 0 | 0 |
| val_lang | 0 | 0 |

### Chat fine-tuning data

Human-written conversations plus execution-verified teacher answers; from the SFT data manifest:

| source | dataset | revision | licence | examples | tokens |
|---|---|---|---|---:|---:|
| aya | CohereForAI/aya_dataset | `f9ea04583f02` | Apache-2.0 | 39,487 | 7,100,208 |
| oasst2 | OpenAssistant/oasst2 | `179dd21fc551` | Apache-2.0 | 6,084 | 2,677,174 |
| stepbuild | data/stepbuild | - | per repository (permissive; the row's licence field) | 397 | 652,045 |
| distill | teacher answers (below) | - | problems: OpenCodeInstruct CC-BY-4.0, APPS MIT; answers: Apache-2.0 teacher | 3,100 | 1,039,887 |

**The distill source.** 5,000 function-style problems (4,000 from nvidia/OpenCodeInstruct,
rows with `average_test_score == 1.0`; 1,000 from codeparrot/apps), decontaminated
against HumanEval and MBPP. The teacher, `Qwen/Qwen2.5-Coder-1.5B-Instruct` at revision
`2e1fd397ee46`, answered each once (greedy). An answer was kept only if it finished on
its own, had a code block defining the expected function, and passed every assert in a
sandbox: 3,277 kept (65.5%; OpenCodeInstruct 74.2%, APPS 31.0%). Reference solutions
were never shown to the teacher or written to the training data. 3,100 kept answers are
in the train split after decontamination; the held-out `distill` split is below.

## Training

Pretraining (the base model, unchanged):

| | |
|---|---|
| Tokens trained | 4,261,937,152 (8,129 steps) |
| Throughput | 44,331 tokens/s (throughput gate) |
| Hardware | 1 x RTX 5090 32 GB (rented, Vast.ai) |
| Cost | $18.75 from the spend ledger: GPU session (hourly); excludes Vast bandwidth charges. The GPU box's hours (setup, A/B runs, the full run, the chat fine-tune, evaluation) plus the CPU shard-build box |
| Schedule | peak LR 0.0006, warmup 500 steps, cosine to 6e-05; batch 524,288 tokens |

Chat fine-tune (this model):

| | |
|---|---|
| Initialised from | quipu-moe-1B-A149M, final pretraining step 8,129 |
| Steps / tokens | 308 steps, 40,370,176 tokens (the SFT epoch cap: about 3 passes over 13.5M tokens of data) |
| Schedule | peak LR 6e-05 (Muon 0.002), warmup 20 steps, cosine to 0; batch 131,072 tokens |
| Expert activation | SwiGLU, pinned to match the base model's weights |
| Hardware | 1 x RTX 5090 (rented, Vast.ai) |
| Cost | in a separate session capped at $3.00 (teacher answers, sandbox checks, this fine-tune); not in the $18.75 above |

### A/B tests (run before the full run, results kept either way)

**Runs** (from results/ab/summary.md, verbatim)

| # | run | config diff | tokens | status | final loss (decision) | english val | bpb | tokens/s | spikes | skipped | startup s | overhead s | compile | decision |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | p1-adamw | (config) | 200,000,000 | completed | 4.0599 | 4.9218 | 1.6016 | 93,145 | 0 | 0 | 56 | 12 | off | pair 1: not kept |
| 2 | p1-muon | optimizer=muon | 200,000,000 | completed | 3.3207 | 4.4059 | 1.4337 | 91,394 | 0 | 0 | 59 | 14 | off | pair 1: kept; pair 2: kept; pair 3: not kept |
| 3 | p1-muon-seed1338 | optimizer=muon, seed=1338 | 200,000,000 | completed | 3.3487 | 4.4167 | 1.4372 | 91,494 | 0 | 0 | 59 | 15 | off | seed re-run of p1-muon |
| 4 | p2-attnres | optimizer=muon, attnres_blocks=4 | 200,000,000 | completed | 3.0322 | 4.2076 | 1.3692 | 77,266 | 0 | 0 | 70 | 19 | off | pair 2: not kept |
| 5 | p3-situ_glu | optimizer=muon, activation=situ_glu | 200,000,000 | completed | 3.2733 | 4.3792 | 1.4250 | 83,595 | 0 | 0 | 65 | 21 | off | pair 3: kept |

**Decisions** (from results/ab/summary.md, verbatim)

| pair | simpler | other | kept | noise | reason |
|---|---|---|---|---|---|
| 1 optimizer | p1-adamw | p1-muon | optimizer=muon (p1-muon) | 0.0280 | lower loss by 0.7392, beyond noise 0.0280 |
| 2 attnres | p1-muon | p2-attnres | attnres_blocks=0 (p1-muon) | 0.0280 | AttnRes throughput cost 15.5% is over the 10% limit [shared noise: pair 1's seed re-run] |
| 3 activation | p1-muon | p3-situ_glu | activation=situ_glu (p3-situ_glu) | 0.0280 | lower loss by 0.0474, beyond noise 0.0280 [shared noise: pair 1's seed re-run] |

Rules (on the decision loss above): the other option needs lower final loss by more than the seed noise; AttnRes <= 10% tokens/s cost; SiTU-GLU no more spikes (step loss > 1.5 x EMA, beta 0.98); FP8 >= 1.2x tokens/s, loss within noise, no more spikes. A missing arm keeps the simpler option (AdamW, no AttnRes, SwiGLU, bf16).

### FP8

FP8 training was not tried in the paid run: the owner decided (2026-09-29) not to spend A/B time on the FP8 pair, so the run is bf16. The FP8 option exists in the training code (quipu/fp8.py) and was only checked on the laptop.

## Evaluation

### Bits per byte per language (base model, during pretraining)

Bits per byte (lower is better; comparable across tokenizers) on held-out text per language and held-out code. Definition: summed next-token loss in bits over the UTF-8 bytes of the target tokens. Every <|endoftext|> document separator is a target too: its loss counts but it is 0 bytes of text, so these numbers are slightly higher (more pessimistic) than a separator-free measure.

| checkpoint | step | English | Indonesian | Malay | Chinese (Simplified) | Chinese (Traditional) | Japanese | Korean | Tamil | Hindi (Devanagari) | Hindi (romanised) | Urdu (romanised) | Code |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| step_000163 | 163 | 1.919 | 2.503 | 2.532 | 3.797 | 3.740 | 2.669 | 2.774 | 1.025 | 1.294 | 2.844 | 3.156 | 1.993 |
| step_000407 | 407 | 1.421 | 1.755 | 1.792 | 2.860 | 2.806 | 1.924 | 1.968 | 0.739 | 0.894 | 2.092 | 2.459 | 0.925 |
| step_000813 | 813 | 1.232 | 1.611 | 1.617 | 2.487 | 2.393 | 1.689 | 1.684 | 0.652 | 0.780 | 1.812 | 2.220 | 0.712 |
| step_001626 | 1,626 | 1.131 | 1.409 | 1.421 | 2.387 | 2.264 | 1.546 | 1.542 | 0.602 | 0.702 | 1.650 | 2.030 | 0.609 |
| step_003252 | 3,252 | 1.054 | 1.296 | 1.303 | 2.026 | 2.002 | 1.402 | 1.380 | 0.554 | 0.644 | 1.470 | 1.807 | 0.534 |
| step_005690 | 5,690 | 0.990 | 1.208 | 1.208 | 1.843 | 1.813 | 1.295 | 1.252 | 0.513 | 0.595 | 1.316 | 1.656 | 0.477 |
| step_008129 | 8,129 | 0.959 | 1.157 | 1.162 | 1.768 | 1.728 | 1.234 | 1.199 | 0.491 | 0.568 | 1.255 | 1.582 | 0.448 |

### Code: HumanEval and MBPP

| model | params | metric / setting | HumanEval pass@1 | HumanEval pass@10 | MBPP pass@1 | MBPP pass@10 | source |
|---|---|---|---:|---:|---:|---:|---|
| **quipu-moe-1B-A149M-chat-distill** | 998.0M total / 148.7M active | greedy pass@1 (T=0, one completion); HumanEval 164; MBPP sanitized test (257); chat template | 0.6 | - | 7.4 | - | measured here |
| quipu-moe-1B-A149M-chat (before distillation) | 998.0M total / 148.7M active | greedy pass@1 (T=0, one completion); HumanEval 164; MBPP sanitized test (257); chat template; same harness | 0.0 | - | 1.9 | - | measured here |
| CodeGen-350M-mono | 350M | sampled, top-p 0.95, best of T in {0.2, 0.6, 0.8} per k (Table 1 caption); HumanEval 164; 0-shot; no MBPP in that table | 12.8 | 23.1 | - | - | published, not re-run: Nijkamp et al., CodeGen (ICLR 2023), arXiv:2203.13474, Table 1 |
| SantaCoder-1.1B | 1.1B | sampled n=200, T=0.2 for pass@1 and T=0.8 for pass@10 (paper, sec. on evaluation); HumanEval and MBPP as MultiPL-E's Python versions, MBPP derived from the sanitized subset (paper), not necessarily our 257-problem test split | 18.0 | 29.0 | 35.0 | 58.0 | published, not re-run: bigcode/santacoder model card (self-reported; Allal et al., arXiv:2301.03988) |
| SmolLM-135M | 135M | no number in the text (HumanEval shown as a chart only) | - | - | - | - | published, not re-run: huggingface.co/blog/smollm; cheap to re-run on the laptop |
| SmolLM-360M | 360M | no number in the text (HumanEval shown as a chart only) | - | - | - | - | published, not re-run: huggingface.co/blog/smollm; cheap to re-run on the laptop |
| Qwen2.5-Coder-1.5B (base) | 1.5B | unverified setting: the report does not state the decoding for this table (the word 'greedy' does not appear) nor which MBPP problems or how many shots this column uses (a separate MBPP 3-shot column exists); HumanEval (164) and MBPP are reported beside EvalPlus's HumanEval+ / MBPP+ | 43.9 | - | 69.2 | - | published, not re-run: Hui et al., Qwen2.5-Coder Technical Report, arXiv:2409.12186, Table 5 |

Published numbers are copied from their sources with the setting each source states; they were produced with other prompts, decoding and harnesses, so compare them with care (a row's setting says what differs).

**Protocol** (both quipu rows; results/code_eval_local/quipu-moe-1B-A149M-chat-distill.json and quipu-moe-1B-A149M-chat.json, run on the same laptop)

- Mode: chat.
- HumanEval prompt: chat template <|user|>...<|end|><|assistant|>; the user turn asks to complete the function and shows the published prompt in a ```python fence; the reply's first code block (or the whole reply) is the code.
- HumanEval stop sequences: none.
- MBPP prompt: chat template; the user turn is the task text, 'Your code should pass this test:' and the first assert; the reply's first code block is the code.
- MBPP stop sequences: none.
- Stop tokens: <|end|>, <|endoftext|>; at most 384 new tokens.
- Greedy: temperature 0 (argmax), one completion per problem -> greedy pass@1.
- Sampled: not run (greedy only).
- Execution: 10.0 s timeout per program; subprocess `python -I` in a temporary directory with a reliability guard (no deleting / renaming files, no writing outside the temp dir, no subprocesses, sockets cannot connect, resource limits on POSIX); best effort, not a security boundary: run it only where executing untrusted model output is acceptable.


### Held-out chat loss

Held-out chat loss per source (the SFT's validation conversations, micro-batch 1), this
model vs the chat model without distillation:

| source | this model | quipu-moe-1B-A149M-chat | assistant tokens |
|---|---:|---:|---:|
| aya | 2.2347 | 2.2564 | 106,935 |
| oasst2 | 2.1162 | 2.1185 | 38,773 |
| stepbuild | 0.2739 | 0.2658 | 2,525 |
| distill | 0.3466 | - | 21,394 |

Expert usage and fixed-prompt chat samples were not re-measured for this model;
the base and chat model cards have them for the models they describe. int4 was
measured for this model (16 Oct 2026); see below.

Standalone-loader parity (max |logit difference| against the training code, fp32, real
validation tokens): 2.6e-05, with logits up to about 22 and the top token agreeing at
every position. The export check's tolerance was 5e-05 for this model (1e-05 for the others).

## int4

Weight-only int4 (int4-groupwise-asym-v1, groups of 128 along the last dimension, fp16 scale + minimum per group) for the attention, shared and routed expert matrices; embedding bf16; router, norms and biases fp32. Dequantized to fp32 on load (the file is smaller; memory once loaded is not).

| file | size |
|---|---:|
| `model.safetensors` | 3,992.1 MB |
| `model-int4.safetensors` | 588.5 MB |
| `model (bf16, for comparison, not shipped)` | 1,996.0 MB |

| split | tokens | fp32 bpb | bf16 bpb | int4 bpb | int4 vs bf16 |
|---|---:|---:|---:|---:|---:|
| English | 32,768 | 1.0086 | 1.0088 | 1.0361 | +0.0274 (+2.71%) |
| Indonesian | 32,768 | 1.1190 | 1.1190 | 1.1517 | +0.0327 (+2.92%) |
| Malay | 32,768 | 1.1821 | 1.1820 | 1.2163 | +0.0342 (+2.89%) |
| Chinese (Simplified) | 32,768 | 1.9927 | 1.9925 | 2.0604 | +0.0679 (+3.41%) |
| Chinese (Traditional) | 32,768 | 1.7960 | 1.7957 | 1.8573 | +0.0615 (+3.43%) |
| Japanese | 32,768 | 1.4171 | 1.4169 | 1.4683 | +0.0514 (+3.62%) |
| Korean | 32,768 | 1.3353 | 1.3353 | 1.3891 | +0.0538 (+4.03%) |
| Tamil | 32,768 | 0.5495 | 0.5494 | 0.5773 | +0.0279 (+5.08%) |
| Hindi (Devanagari) | 32,768 | 0.5740 | 0.5741 | 0.5955 | +0.0214 (+3.73%) |
| Hindi (romanised) | 32,768 | 1.2481 | 1.2482 | 1.2758 | +0.0276 (+2.21%) |
| Urdu (romanised) | 32,768 | 1.6713 | 1.6711 | 1.7103 | +0.0392 (+2.34%) |
| Code | 32,768 | 0.5196 | 0.5198 | 0.5384 | +0.0187 (+3.59%) |

The first tokens of each evaluation split (count per row). bf16 = the weights rounded to bf16, arithmetic in fp32 (spec 12's baseline); fp32 = the trained weights as saved.

Standalone-loader parity (max |logit difference| against the training code): final (fp32) 2.6e-05; int4 (dequantized) 2.0e-05.

## Usage

```bash
pip install torch safetensors tokenizers huggingface_hub
```

```python
from huggingface_hub import hf_hub_download
import importlib.util, sys

path = hf_hub_download("AneekC/quipu-moe-1B-A149M-chat-distill", "modeling_quipu_moe.py")
spec = importlib.util.spec_from_file_location("modeling_quipu_moe", path)
mq = importlib.util.module_from_spec(spec)
sys.modules["modeling_quipu_moe"] = mq
spec.loader.exec_module(mq)

model = mq.load("AneekC/quipu-moe-1B-A149M-chat-distill")                                    # fp32
# model = mq.load("AneekC/quipu-moe-1B-A149M-chat-distill", weights="model-int4.safetensors")  # int4 file
tok = mq.load_tokenizer("AneekC/quipu-moe-1B-A149M-chat-distill")
print(mq.chat(model, tok, [{"role": "user", "content": "Write a Python function that reverses a string."}]))
```

This is not a `transformers` model; there is no `AutoModel` class for it. The loader
runs the experts one after another without a KV cache: correct, not fast.

## Limitations

- Small: 148,660,992 parameters are active per token. It states false things
  with confidence; do not use its output as information.
- The nine languages other than English together are 12.0% of the training tokens (English 28.0%, code 60.0%; shard manifest, mix achieved). Expect weaker output in them than in English, and some mixing of languages.
- Code: greedy decoding solves 0.6% of HumanEval and 7.4% of MBPP problems (see above). Treat generated code as untested.
- The distillation data is Python, function-style and fairly short; gains outside that kind of task were not measured.
- Trained on web text and public code, which carry their biases; no safety tuning.
- How well it follows instructions was not measured beyond the held-out chat loss per source and the chat-mode HumanEval / MBPP numbers above.

## Credits and licence

Weights and code: Apache-2.0. Language identification of the training text used
[AneekC/lid-specialists-9plus1](https://huggingface.co/AneekC/lid-specialists-9plus1) (MIT). Training data: FineWeb-Edu
and FineWeb-2 (ODC-By 1.0, © Hugging Face) and the permissively licensed subset of
codeparrot/github-code-clean (files keep their licences). Chat fine-tuning data: [CohereForAI/aya_dataset](https://huggingface.co/datasets/CohereForAI/aya_dataset) (Apache-2.0), [OpenAssistant/oasst2](https://huggingface.co/datasets/OpenAssistant/oasst2) (Apache-2.0), the stepbuild train split (FILE-block replies mined from permissively licensed public repositories, each keeping its repository's licence; built for this project, its test split and benchmark apps held out), and execution-verified answers from [Qwen/Qwen2.5-Coder-1.5B-Instruct](https://huggingface.co/Qwen/Qwen2.5-Coder-1.5B-Instruct) (Apache-2.0) to problems from [nvidia/OpenCodeInstruct](https://huggingface.co/datasets/nvidia/OpenCodeInstruct) (CC-BY-4.0) and [codeparrot/apps](https://huggingface.co/datasets/codeparrot/apps) (MIT). HumanEval
(MIT) and MBPP (CC-BY-4.0) were used for evaluation only and filtered (substring /
13-gram matching) from the training data.
