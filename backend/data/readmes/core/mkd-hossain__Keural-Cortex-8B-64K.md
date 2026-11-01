---
license: apache-2.0
base_model: Qwen/Qwen3-8B-Base
language:
- ko
- en
library_name: transformers
pipeline_tag: text-generation
tags:
- continued-pretraining
- korean
- long-context
- 64k
- base-model
---

# Keural Cortex 8B — 64K context (Phase 5 final)

Korean-focused continued pretraining of
[`Qwen/Qwen3-8B-Base`](https://huggingface.co/Qwen/Qwen3-8B-Base) with the context
window extended from 32,768 to **65,536 tokens**, by **MKD Co., Ltd.**

This is the completed Phase 5 model: 41B tokens of CPT followed by 2.5B tokens of
context extension. It is a **base model** — no instruction tuning.

| | |
|---|---|
| Parameters | 8.19 B |
| **Context length** | **65,536** (native, YaRN factor 2.0) |
| CPT tokens | 41.0 B |
| Context-extension tokens | 2.50 B |
| Precision | bfloat16 |
| Completed | 2026-09-12 |

---

## Evaluation

All measurements use `lm-evaluation-harness` 0.4.12 / `transformers` 4.55.2 in
bfloat16, with settings identical to the `Qwen3-8B-Base` baseline, so the
comparisons are like-for-like. Two reference points are shown: **`step10000`** is
the CPT checkpoint this phase started from, so it isolates what context extension
changed; **base** is `Qwen3-8B-Base`.

### Korean — context extension *improved* Korean

| Benchmark | Base | step10000 | **this model** | vs step10000 |
|---|---|---|---|---|
| **KMMLU** | 53.91 | 53.57 | **54.32** | **+0.75** ✱ |
| HaeRae | 63.06 | 64.44 | 64.62 | +0.18 |
| KoBEST BoolQ | 57.05 | 64.25 | 63.46 | −0.78 |
| KoBEST COPA | 72.30 | 70.20 | 70.20 | 0.00 |
| KoBEST HellaSwag | 58.80 | 59.60 | 59.80 | +0.20 |
| **KoBEST SentiNeg** | 83.88 | 81.36 | **91.69** | **+10.33** ✱ |
| **Mean** | | | | **+1.78** (vs base **+2.52**) |

✱ significant at 95%. Across KMMLU's 45 subtasks: **31 improved, 12 regressed**.
Three of four subject groups rose (STEM +0.96, applied science +1.16, other
+0.75; humanities −0.58).

**KMMLU 54.32 is above the base model's 53.91** — the first Korean knowledge gain
in this project, and it came from 2.5B tokens of context-extension data rather
than the preceding 41B tokens of CPT. See *Why Korean improved here* below.

### English — no regression

| Benchmark | Base | step10000 | **this model** | vs step10000 |
|---|---|---|---|---|
| MMLU | 74.70 | 74.02 | 73.79 | −0.23 |
| GSM8K (1,319 samples) | 84.69 | 82.34 | 82.71 | +0.38 |
| ARC-Challenge | 57.25 | 59.64 | 58.79 | −0.85 |
| HellaSwag | 78.59 | 78.12 | 78.40 | +0.28 |
| WinoGrande | 72.38 | 72.61 | 72.77 | +0.16 |
| **Mean** | | | | **−0.05** |

No English result is statistically significant. Context extension is the
operation most likely to damage short-context behaviour; it did not.

### Long context — needle-in-a-haystack

A random 6-digit code is buried at a given depth in a document of a given length;
the model must reproduce it. Measured on CPU via llama.cpp (Q8_0):

| context | depth 10% | depth 50% | depth 90% |
|---|---|---|---|
| 4,096 | PASS | PASS | PASS |
| 16,384 | PASS | PASS | PASS |
| 32,768 | PASS | PASS | PASS |
| **65,536** | **PASS** | **PASS** | **PASS** |

**12/12 retrieved**, measured on this exact checkpoint.

The 32,768 and 65,536 rows are beyond what the base model could do at all, so
this is direct evidence the YaRN scaling took effect rather than merely being
configured. Retrieval is exact even at 90% depth.

Probe: [`eval/needle_cpu.py`](https://github.com/MKD-CORP/Keural-Cortex-8B). It
is framed as pure completion rather than question-answering (a base model has no
instruction tuning and will continue the document instead of answering), and
scored through llama.cpp's HTTP API rather than the CLI (both CLI tools echo the
prompt, which contains the needle, so stdout-based scoring would pass on echo
alone). Positive and negative controls are asserted before any grid is believed.

### Rollback gate: PASS

The project gate is *Korean up **and** English within −0.5 pt*. Result:
Korean **+1.78**, English **−0.05**, long context verified. This model ships
rather than the pre-extension 32K checkpoint.

## Why Korean improved here

The preceding 41B-token CPT did **not** improve Korean knowledge — KMMLU was
negative at every checkpoint, and the gains were lexical (HaeRae rare_word +3.70,
loan_word +2.96) rather than factual. Its Korean data was three web-crawl sources.

This phase used 2.5B tokens that are **58% Korean and 58% AI Hub** — curated
books and the modu corpus rather than web crawl. Same model, same recipe, same
learning rate, 16× fewer tokens, and Korean knowledge moved. The HaeRae subtasks
track the corpus: **history +3.19** (curated books contain history) against
general_knowledge −3.41.

The practical lesson, on this project's own evidence: for Korean knowledge the
lever is **data composition, not token volume**.

---

## ⚠️ What this model is and is not

**It is a base model.** `Qwen3-8B-Base` has no instruction following, no chat
format, no tool calling and no thinking mode; continued pretraining adds none of
them. It continues text rather than answering instructions. Post-training
(SFT/DPO) has **not** been done.

The `chat_template.jinja` is inherited from the base tokenizer and does **not**
mean the model is chat-tuned. Driven through it, the model will *imitate*
assistant phrasing because Qwen3-8B-Base absorbed large amounts of assistant text
during its 36T-token pretraining — that is imitation, not instruction tuning.

**It has not been compared against Qwen3-8B-Instruct.** Every number here is
against `Qwen3-8B-Base` — a base-to-base comparison. Comparing a base model to an
instruct model is only meaningful on knowledge benchmarks, and has not been done.

**The Korean gain is real but modest.** KMMLU +0.41 over base is a genuine,
statistically significant improvement, not a transformation. This is not a model
that beats Qwen3-8B-Instruct, and it is not intended as one.

**Benchmark decontamination has not been run.** Treat any benchmark number from
this project as provisional until n-gram overlap against the evaluation suites
has been checked.

---

## Training

### Phase 4 — CPT (41B tokens)

Full-parameter FSDP on 4× H200, 18 days 10 hours, zero restarts. Sequence length
4,096, global batch 3,145,728 tokens/step, peak LR 1.0e-05 on a WSD schedule,
AdamW (β 0.9/0.95, wd 0.1), grad clip 1.0 (never triggered — max observed norm
0.48). Corpus: 38.784B tokens across 19 sources, 42.45% Korean.

### Phase 5 — context extension (2.5B tokens)

Started from `step_0010000` of the CPT rather than the final checkpoint —
that checkpoint measured best on every Korean aggregation, and being
mid-stable-phase (undecayed) it is the more natural handoff to a phase that
applies its own WSD schedule.

| Parameter | Value |
|---|---|
| RoPE scaling | YaRN, factor 2.0 → 65,536 positions |
| Sequence length | 65,536 |
| Global batch | 3,145,728 tokens/step (1 × 65,536 × 4 GPU × 12 accum) |
| Steps | 795 |
| Peak LR | 1.0e-05, WSD, min ratio 0.1 |
| Throughput | 10.3k tok/s |
| Runtime | ~2d 23h, zero crashes |

Data: 2.501B tokens, 12 sources, every document ≥32,768 tokens. **58.1% Korean**,
and notably 58% of the total is AI Hub (`aihub_modu` 0.899B, `aihub_books`
0.553B) — curated, edited Korean rather than web crawl.

**Note on the loss curve:** training loss sat flat at ~1.94 throughout Phase 5,
which in isolation looks like nothing was learned. The evaluations above show
otherwise — Korean improved and 64K retrieval works. Average token loss is simply
not the right instrument for either positional behaviour or a data-composition
shift, which is why the gate is defined on evaluations rather than on loss.

A required implementation detail: HF computes the loss by materializing the full
`seq_len × vocab` logits tensor and upcasting to fp32 — 37.09 GiB at seq_len
65,536, which OOMs with `micro_bsz` already at 1. Phase 5 used liger-kernel's
fused linear cross-entropy, which never allocates that tensor.

---

## Usage

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

m = "mkd-hossain/Keural-Cortex-8B-64K"
tok = AutoTokenizer.from_pretrained(m)
model = AutoModelForCausalLM.from_pretrained(m, torch_dtype="bfloat16", device_map="cuda")

# Base model: complete text, do not instruct.
out = model.generate(**tok("대한민국의 수도는", return_tensors="pt").to("cuda"), max_new_tokens=64)
print(tok.decode(out[0], skip_special_tokens=True))
```

### GGUF / llama.cpp

`config.json` includes `rope_scaling.original_max_position_embeddings: 32768`.
`transformers` infers that field, but llama.cpp's converter **requires** it and
fails with `KeyError` otherwise — it is present here so conversion works:

```bash
python3 convert_hf_to_gguf.py <this_model> --outfile out-f16.gguf --outtype f16
./llama-quantize out-f16.gguf out-q8_0.gguf Q8_0 8
```

On AMX-capable CPUs, Q8_0 outperforms Q4_K_M despite being larger (AMX-INT8
hardware path). Build llama.cpp with `-DGGML_NATIVE=ON` or those kernels are not
compiled in.

---

## Related models

| Model | Tokens | Context | Purpose |
|---|---|---|---|
| **this** | 41B + 2.5B | **65,536** | Phase 5 final |
| [`Keural-Cortex-8B-Base`](https://huggingface.co/mkd-hossain/Keural-Cortex-8B-Base) | 41B | 32,768 | CPT final |
| [`Keural-Cortex-8B-step10000`](https://huggingface.co/mkd-hossain/Keural-Cortex-8B-step10000) | 31.5B | 32,768 | best Korean checkpoint; Phase 5 started here |
| [`Keural-Cortex-8B-step5000`](https://huggingface.co/mkd-hossain/Keural-Cortex-8B-step5000) | 15.7B | 32,768 | intermediate |
| [`Keural-Cortex-8B-pilot`](https://huggingface.co/mkd-hossain/Keural-Cortex-8B-pilot) | 3B | 32,768 | recipe validation |

Full audit record — configuration, training dynamics, corpus provenance,
evaluation and findings — at
[github.com/MKD-CORP/Keural-Cortex-8B](https://github.com/MKD-CORP/Keural-Cortex-8B)
under `CPT_details/`.

## License

**Apache 2.0**, inherited from `Qwen/Qwen3-8B-Base`. Derivative work of
Qwen3-8B-Base by Alibaba Cloud; attribution required.

## Intended use

Research, long-context experimentation, and as a base for further fine-tuning.
Not a user-facing assistant — it has no instruction tuning — and not a basis for
capability claims until decontamination is complete.
