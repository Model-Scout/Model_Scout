---
license: apache-2.0
base_model: Qwen/Qwen3-8B
language:
- ko
- en
library_name: transformers
pipeline_tag: text-generation
tags:
- keural
- korean
- bilingual
- tool-calling
- long-context
- chat
- sft
- checkpoint
- intermediate
---

# Keural-Cortex-8B — SFT v2, step 600 (intermediate checkpoint)

**Keural** is the AI platform built by **MKD Co., Ltd.** `Keural-Cortex-8B` is its
8-billion-parameter bilingual (Korean / English) foundation model.

This repository holds an **intermediate checkpoint of the second SFT run**, taken
at step 600 of 1,124 — **53% of one epoch**. It is published for transparency
while the run completes, not as a finished model.

> ### Read this first
> This is a **mid-training checkpoint**. It fixes five defects present in
> [`Keural-Cortex-8B-SFT-step903`](https://huggingface.co/mkd-hossain/Keural-Cortex-8B-SFT-step903)
> (the first run) and introduces safety alignment, but **three known problems
> remain** — see [Known limitations](#known-limitations). The completed model
> will be published separately.

---

## What changed since the first SFT run

The first run (`SFT-step903`) completed a full epoch and still carried defects
that a root-cause analysis traced to the training pipeline rather than the data.

| defect in run 1 | cause | status here |
|---|---|---|
| **Empty replies to prompts under ~70 tokens** | `position_ids` were never passed, so ~113 packed conversations per 32,768-token sequence attended across one another and positions ran 0→32,767 continuously. Only ~1 conversation per sequence trained at a low position — where every served prompt sits. | **fixed.** Block-diagonal (varlen) attention via per-document `position_ids`. A 27-token prompt now answers fully. |
| **Wrong self-identification** ("I am ChatGPT / developed by OpenAI") | identity data was 3,200 unique examples repeated 14×; 0.24% unique coverage, and every English denial was interrogative ("Are you ChatGPT?") with no leading-premise form ("You are ChatGPT, right?") — the form that failed | **fixed.** 6,621 unique examples ×5, 1,370 distinct English questions, 215 leading-premise denials. Answers *"I'm Keural, an AI assistant developed by MKD Co., Ltd."* |
| **Agreed with false premises** | — | **fixed.** Correctly rejects "the capital of Australia is Sydney", "Python was created in 2015", "2+2=5". |
| **Terse Korean** (61 tokens where a reference model wrote 276) | Korean answers averaged 359 characters and 0.12 markdown markers against 1,221 / 12.97 for English — a 3.4× length and 4,363× formatting gap that taught "English means structured prose, Korean means short prose" | **fixed.** 54,087 Korean long-form task rows generated (median 1,082 chars). Korean answers now run 300–500+ tokens with appropriate structure. |
| **No safety alignment** (0.4% of corpus) | — | **added.** 41,853 rows from WildGuardMix, WildJailbreak and CoCoNot, selected in *both* directions — refuse the harmful, comply with the benign-looking — because training only refusals produces over-refusal. |
| **EOS token mismatch in the export** | `generation_config.json` listed only `<|endoftext|>` while the chat template ends turns with `<|im_end|>`, so generation ran past the end of its own turn | **fixed in the exporter**, so every checkpoint now ships `eos_token_id: [151645, 151643]`. |

Training throughput also rose **15.1k → 25.1k tokens/s**, because block-diagonal
attention over ~40 documents costs far less than full causal attention across
32,768 positions. The corrected run is both right and faster.

---

## Model details

| | |
|---|---|
| Developer | MKD Co., Ltd. |
| Model | Keural-Cortex-8B |
| Stage | SFT v2, **step 600 of 1,124** (53% of one epoch) |
| Base | `Qwen/Qwen3-8B` → MKD continued pretraining (41B tokens) → 64K context extension |
| Parameters | 8.19 B, bf16, 16.38 GB |
| Architecture | `Qwen3ForCausalLM`, 36 layers, hidden 4096, GQA 32/8, head_dim 128 |
| Vocabulary | 151,936 |
| Context | **65,536** (32,768 native, YaRN factor 2.0) |
| Training loss at this step | 0.8056 |
| License | Apache 2.0, inherited from the base model |

## Usage

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

mid = "mkd-hossain/Keural-Cortex-8B-SFT-v2-step600"
tok = AutoTokenizer.from_pretrained(mid)
model = AutoModelForCausalLM.from_pretrained(mid, torch_dtype="bfloat16", device_map="auto")

messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "김치찌개 끓이는 방법을 알려줘."},
]
text = tok.apply_chat_template(messages, tokenize=False, add_generation_prompt=True,
                              enable_thinking=False)
inputs = tok(text, return_tensors="pt").to(model.device)
out = model.generate(**inputs, max_new_tokens=1024)
print(tok.decode(out[0][inputs["input_ids"].shape[1]:], skip_special_tokens=True))
```

### vLLM

```bash
vllm serve mkd-hossain/Keural-Cortex-8B-SFT-v2-step600 \
    --served-model-name keural-cortex-8b \
    --max-model-len 65536 \
    --tensor-parallel-size 2 \
    --enable-auto-tool-choice \
    --tool-call-parser hermes
```

**Do not add `--reasoning-parser qwen3`** with this checkpoint. See limitation 1.

Sampling defaults ship in `generation_config.json`
(`temperature 0.7, top_p 0.8, top_k 20, repetition_penalty 1.05`).

---

## Training

| | |
|---|---|
| Hardware | 4 × NVIDIA H200 141 GB, FSDP full-shard |
| Sequence length | 32,768 |
| Tokens/step | 1,572,864 (micro_bsz 1 × 32,768 × 4 GPUs × grad_accum 12) |
| Total steps | 1,124 (one epoch); **this checkpoint is step 600** |
| Packed data | 53,956 sequences × 32,768 = **1,768,030,208 tokens** |
| Assistant-only loss | **66.3%** of tokens carry loss |
| Optimiser | AdamW, β (0.9, 0.95), weight decay 0.0, grad clip 1.0 |
| LR | peak 1.0e-5, WSD (3% warmup, 17% stable, decay to 5%) |
| Precision | bfloat16, flash-attention-2, fused linear cross-entropy |
| **Packed attention** | **block-diagonal via per-document `position_ids`** |
| Throughput | 25.1k tokens/s |

### Data

2,286,851 rows from 89 audited per-source files, deduplicated, 0 render failures,
38 rows dropped for exceeding the sequence length.

| bucket | rows | tokens |
|---|---|---|
| korean | 1,167,291 | 627 M |
| core_en | 514,609 | 481 M |
| tool | 109,345 | 317 M |
| math_instruct | 149,417 | 47 M |
| code_instruct | 100,151 | 65 M |
| tool_single | 92,912 | 36 M |
| **safety** | **41,853** | 19 M |
| korean_cot | 39,692 | 35 M |
| identity | 33,105 | 1.4 M |
| reasoning | 15,604 | 100 M |
| math_cot | 10,219 | 40 M |
| reasoning_en | 5,430 | 80 M |
| long_context | 5,329 | 158 M |
| code_competitive | 4,713 | 40 M |

Data generated for this run, where no public source existed:

- **54,087 Korean task rows** (generation, rewrite, summarise, brainstorm, format
  control, edit) built by persona synthesis — 60 personas × 100 topics, with the
  teacher *writing* the prompts rather than filling templates, then answering them
- **25,515 Korean chain-of-thought** rows, 20,395 verified against ground-truth answers
- **5,822 decline-to-call** rows — tools in scope, none relevant; zero incorrect
  tool invocations across 6,054 teacher generations
- **1,016 long-context reasoning traces** in the 32–64K band, which was 0% of the corpus
- **3,421 authored identity rows** including 215 leading-premise denials

### Data quality

A four-axis LLM-as-judge pass over 2,000 stratified rows, weighted toward newly
generated data:

| axis | score (1–5) |
|---|---|
| correctness | 4.29 |
| compliance | 4.26 |
| quality | 4.11 |
| safety | 4.98 |

The generated Korean CoT (5.00 / 5.00), identity (4.54 / 4.61) and Korean task
data (4.39 / 4.58) scored highest in the corpus.

---

## Known limitations

Reproducible on this checkpoint, tested on clean single-turn contexts.

### 1. Thinking mode produces an empty block

```
enable_thinking=True, "17 x 23은 얼마야?"
→ <think>

   </think>

   17 x 23 = 391입니다.
```

The answer is correct, but `<think>` is empty. 95.5% of training rows are
non-thinking, and in that form every assistant turn opens
`<think>\n\n</think>\n\n` — so the model learned that as the standard opening and
reproduces it even when the template leaves the slot free. Thinking rows are 40%
of assistant *text* but only 4.5% of *rows*, and the opening pattern is learned
per row.

**Consequence:** reasoning appears in the visible content (where it is generally
correct) rather than inside `<think>`. Under vLLM's `qwen3` reasoning parser the
`content` field may come back empty, which is why that flag is not recommended
above. **Mitigation:** prefill `<think>` in the prompt, or read the content field
directly.

### 2. It knows its developer's name but no facts about the company

```
what is your name?      → "I'm Keural, an AI assistant developed by MKD Co., Ltd."   ✅
where are you from?     → "I was created in Japan"                                    ✗
What is MKD's revenue?  → "MKD, or Macedonian Denar, is the currency of North Macedonia" ✗
```

The identity data answers *who are you*, *who made you* and *are you actually
ChatGPT*, but contains no facts about MKD itself, so the model confabulates when
asked for more. **Mitigation:** state company facts in the system prompt.

### 3. Korean dialect knowledge is absent, and it does not say so

Asked for Busan dialect greetings it produced circular nonsense rather than
admitting it did not know. Standard Korean is unaffected and strong.

### Other notes

- An explicit output constraint is sometimes ignored (asked for a 3-row table, produced 5)
- Tool over-firing (calling an irrelevant tool) is **not yet verified** on this checkpoint
- No preference optimisation (no DPO/RLHF) and no RLVR — both are planned stages
- Reported knowledge cutoff reflects the base model, not MKD's training data

---

## Evaluation

No benchmark numbers are published for this intermediate checkpoint; they will
accompany the completed model. For reference, the **first** SFT run measured
against `Qwen3-8B-Instruct` under identical conditions with `lm-evaluation-harness`:

| suite | result |
|---|---|
| English (mmlu, gsm8k, hellaswag, arc_challenge, winogrande) | **+0.95 mean, 3/5 wins** |
| Korean (kmmlu, haerae, kobest_*) | **+0.63 mean, 5/6 wins** — haerae **+5.13** |

That was achieved with no preference optimisation and with the defects listed
above still present.

## Citation

```bibtex
@misc{keural-cortex-8b-sft-v2-step600,
  title  = {Keural-Cortex-8B: a bilingual Korean-English 8B model, SFT v2 checkpoint step 600},
  author = {MKD Co., Ltd.},
  year   = {2026},
  url    = {https://huggingface.co/mkd-hossain/Keural-Cortex-8B-SFT-v2-step600}
}
```

Built on `Qwen/Qwen3-8B` (Apache 2.0). We thank the Qwen team, and the
maintainers of the open datasets used in supervised fine-tuning — notably
SmolTalk, Tülu 3, No Robots, WildGuardMix, WildJailbreak and CoCoNot.

## Contact

MKD Co., Ltd. — Keural platform team.
