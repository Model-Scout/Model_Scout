---
library_name: transformers
pipeline_tag: text-generation
base_model: LiquidAI/LFM2.5-2.6B
license: other
license_name: lfm1.0
license_link: LICENSE
language:
  - ar
  - zh
  - en
  - fr
  - de
  - hi
  - id
  - it
  - ja
  - ko
  - pl
  - pt
  - ru
  - es
  - th
  - vi
tags:
  - liquid
  - lfm2.5
  - transformers
  - safetensors
  - gguf
  - llama.cpp
  - bfloat16
  - text-generation
  - reasoning
  - long-context
  - abliterated
  - uncensored
  - refusal-reduction
---

# LFM2.5-2.6B - UNCENSORED ABLITERATED PHILADELPHIA CLASS

**This is LiquidAI's LFM2.5-2.6B with its refusal behavior aggressively reduced.** It keeps the compact 2.7B hybrid architecture, but answers requests the stock post-trained model refused. In our tests, refusals fell from 132/842 to 8/842 and from 19/126 to 1/126 on a held-out set, while the average change across five public capability benchmarks was only -0.50 percentage points.

**PHILADELPHIA CLASS** includes the full BF16 checkpoint as one `model.safetensors` file plus a tested BF16 GGUF for llama.cpp. Both retain LFM2.5's tokenizer, reasoning chat template, and 128K configured context.

## Modification notice

This repository redistributes modified model weight files derived from `LiquidAI/LFM2.5-2.6B` at revision `dca1825886789bd40b94368f53b1d9ada4c94598`. The local untouched checkpoint was verified against all 11 files in that Hub revision before release preparation.

The candidate was produced with two sequential output-space biprojection stages. Exact comparison with the untouched source found 58 intentionally modified output-projection tensors out of 266 total; 208 tensors remained exactly equal, with no missing, unexpected, shape-mismatched, or dtype-mismatched tensors. The Transformers release is packaged as one `model.safetensors` file.

## Release at a glance

| Property | Value |
|---|---|
| Base model | `LiquidAI/LFM2.5-2.6B` post-trained model |
| Upstream revision | `dca1825886789bd40b94368f53b1d9ada4c94598` |
| Architecture | `Lfm2ForCausalLM` |
| Parameters | 2,697,198,592 |
| Precision | BF16 |
| Transformers weights | One BF16 `model.safetensors` file (5.39 GB) |
| GGUF | Tested BF16 build (5.40 GB) |
| Layers | 30: 22 convolution blocks and 8 grouped-query attention blocks |
| Configured context | 128,000 tokens |
| Vocabulary | 128,000 tokens |
| Status | RC1; strong refusal-reduction candidate, not safety-certified |
| Lossy quantization | No lossy quantized build is included |

## Internal behavioral diagnostics

> These are automated OBLITERATUS development diagnostics, not standardized leaderboards or independent safety audits. "Direct," "warning," "refusal," and "usable" are deterministic response-form labels; they do not establish factuality, legality, harmlessness, or human approval.

### Matched 842-item opening screen

Both checkpoints used the same prompt indices, chat template, system prompt, seed, greedy decoding, and 96 generated tokens.

| Cohort | Untouched source direct / warning / refusal | PHILADELPHIA CLASS direct / warning / refusal |
|---|---:|---:|
| Harmful 842 | 149 / 561 / **132** | **773** / 61 / **8** |
| Paired harmless 842 | 795 / 45 / 2 | **812** / 30 / **0** |

Of the source model's 132 harmful refusals, 131 cleared. Seven source non-refusals became refusals, so this is a large net reduction rather than monotonic improvement on every item.

### Exact-prompt-hash holdout

The 126 holdout prompt hashes were excluded from direction fitting. This blocks exact prompt identity reuse but is not a semantic or paraphrase-family holdout.

| Cohort | Untouched source direct / warning / refusal | PHILADELPHIA CLASS direct / warning / refusal |
|---|---:|---:|
| Harmful holdout 126 | 15 / 92 / **19** | **114** / 11 / **1** |
| Paired harmless holdout 126 | 118 / 8 / 0 | **123** / 3 / 0 |

### Coherence and long-form diagnostics

LFM2.5 begins inside a reasoning block. These evaluators scored the final answer after a completed `</think>` block using identical source/candidate settings.

| Diagnostic | Untouched source | PHILADELPHIA CLASS |
|---|---:|---:|
| LFM-aware coherence24 | 17/24 | **20/24** |
| Code syntax | 4/6 | **6/6** |
| Code semantic tests | 2/6 | **5/6** |
| JSON validity | 4/4 | 4/4 |
| Long-form refusals | 18/24 | **0/24** |
| Long-form strictly usable | 6/24 | **18/24** |

The long-form result is a major responsiveness improvement, but not a perfect structural result. The candidate had five repetition flags, three degenerate openings, and two empty or incomplete final answers; those flags overlap across six failed rows. This limitation is disclosed rather than hidden behind the zero-refusal count.

Sanitized aggregate details are in [`evals/evaluation_summary.json`](evals/evaluation_summary.json).

## Matched public capability evaluation

> This is a matched candidate-versus-untouched-source comparison, not a cross-model leaderboard. Both checkpoints completed the same full `lm-evaluation-harness` 0.4.12 suite.

| Task | Primary metric | Shots | n | Untouched source | PHILADELPHIA CLASS | Delta |
|---|---|---:|---:|---:|---:|---:|
| MMLU | `acc` | 0 | 14,042 | 23.81% | **24.05%** | +0.24 pp |
| HellaSwag | `acc_norm` | 0 | 10,042 | 56.71% | **57.00%** | +0.29 pp |
| TruthfulQA MC2 | `acc` | 0 | 817 | **56.20%** | 53.79% | -2.41 pp |
| GSM8K | `exact_match` (`strict-match`) | 5 | 1,319 | **69.83%** | 69.45% | -0.38 pp |
| WinoGrande | `acc` | 0 | 1,267 | **60.46%** | 60.22% | -0.24 pp |

The unweighted mean of the five primary metric deltas is **-0.50 percentage points**. MMLU and HellaSwag improved slightly; GSM8K and WinoGrande changed by less than 0.4 points. TruthfulQA MC2 is the only notable point decline. Its smaller 817-item set and aggregate uncertainty prevent a claim that the decline is a proven material regression, but it is explicitly reported.

Both checkpoints used BF16, the Transformers `hf` backend, batch size 8, no evaluation limit, no chat template or system instruction, task-default few-shot counts, and identical seeds. The suite covered 27,487 documents, 104,752 likelihood requests, and 1,319 generation requests per checkpoint. The results support "no material overall capability loss observed on this matched suite"; they do not prove equivalence or an overall rank.

Exact values, standard errors, source-result hashes, task versions, and protocol fields are in [`evals/matched_public_capability_lm_eval_0_4_12.json`](evals/matched_public_capability_lm_eval_0_4_12.json).

## Transformers quickstart

LFM2.5 requires a recent Transformers release with native `lfm2` support.

```bash
pip install -U "transformers>=5.12.1" accelerate safetensors torch
```

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = (
    "KridgeDookie/"
    "LFM2.5-2.6B-UNCENSORED-ABLITERATED-PHILADELPHIA-CLASS"
)

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    dtype=torch.bfloat16,
    device_map="auto",
).eval()

messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Explain why the sky appears blue."},
]

inputs = tokenizer.apply_chat_template(
    messages,
    add_generation_prompt=True,
    return_tensors="pt",
    tokenize=True,
    return_dict=True,
).to(model.device)
input_length = inputs["input_ids"].shape[-1]

with torch.inference_mode():
    output = model.generate(
        **inputs,
        max_new_tokens=512,
        do_sample=True,
        temperature=0.1,
        top_k=50,
        repetition_penalty=1.1,
    )

print(tokenizer.decode(
    output[0, input_length:],
    skip_special_tokens=True,
))
```

The upstream chat template starts assistant generation inside a `<think>` block. Applications that display only the final answer should parse the completed reasoning block rather than assuming the first generated tokens are user-facing prose.

The 128,000-token configured context does not imply that the full window will fit on a particular device. Weight memory, runtime overhead, attention state, and KV cache all require additional capacity.

## llama.cpp / GGUF

A tested BF16 GGUF is included for recent llama.cpp builds with LFM2 support:

```bash
hf download KridgeDookie/LFM2.5-2.6B-UNCENSORED-ABLITERATED-PHILADELPHIA-CLASS \
  LFM2.5-2.6B-UNCENSORED-ABLITERATED-PHILADELPHIA-CLASS-BF16.gguf \
  --local-dir .

llama-cli \
  -m LFM2.5-2.6B-UNCENSORED-ABLITERATED-PHILADELPHIA-CLASS-BF16.gguf \
  -ngl 99 \
  -c 4096 \
  -cnv
```

The release GGUF was converted and smoke-tested with [llama.cpp commit `6ea215d`](https://github.com/ggml-org/llama.cpp/commit/6ea215d171fd31df943bf1ac8227129f2b963160) on an NVIDIA A40. It loaded with full GPU offload and correctly completed a deterministic arithmetic prompt using its embedded chat template. This is a runtime smoke test, not a repeat of the full Transformers benchmark suite.

## Intended use

- Controlled research on refusal behavior and model editing
- Local general-assistant, extraction, tool-use, and creative experimentation
- Red-team and interpretability work with independent safeguards
- Application-specific systems that validate outputs and enforce their own policy layer

This model is not recommended as an unsupervised safety filter, medical or legal authority, autonomous cyber operator, or public-facing assistant without additional controls.

## Limitations and risks

- The modification deliberately weakens refusal behavior, including for harmful prompts.
- Outputs can be unsafe, illegal, biased, private, misleading, or factually wrong.
- "Uncensored" does not guarantee an answer for every prompt, language, backend, context length, or decoding configuration.
- The behavioral diagnostics are automated heuristics, not manual answer-quality adjudication.
- The holdout is exact-prompt-hash disjoint, not semantic-family disjoint.
- Long-form generation still showed repetition and incomplete-answer failures on 6/24 diagnostic rows.
- The broad suite is one deterministic matched run and does not establish formal equivalence.
- Quantization or alternate inference runtimes can change behavior; BF16 results do not automatically transfer.

## Weight integrity

```text
model.safetensors                                                                    5d1c91a44e6832e7e1517ebe5e529eab3114c7dc0ac19b66885afde9a1c422e3
LFM2.5-2.6B-UNCENSORED-ABLITERATED-PHILADELPHIA-CLASS-BF16.gguf                    ce3a4cc32c75e3940ae22336bccff7d549017d5d06bb1bc87313459a0e17d4bc
```

The evaluated checkpoint completed the refusal/coherence diagnostics and full matched public capability suite. Before release, the single-file Transformers artifact was independently verified as exactly tensor-equal to the evaluated shards, then passed a strict BF16 load and generation test on an NVIDIA A40. The BF16 GGUF separately passed a pinned llama.cpp CUDA load and generation smoke test.

## License and attribution

This is a community derivative of [`LiquidAI/LFM2.5-2.6B`](https://huggingface.co/LiquidAI/LFM2.5-2.6B). Liquid AI is not affiliated with this release and does not endorse it.

The model is redistributed under the **LFM Open License v1.0** included as [`LICENSE`](LICENSE). The license contains redistribution, attribution, and commercial-use conditions, including a commercial-use limitation for legal entities at or above its USD 10 million annual-revenue threshold. Read the complete license before using or redistributing the model; this summary is not legal advice.

- Upstream model: [LiquidAI/LFM2.5-2.6B](https://huggingface.co/LiquidAI/LFM2.5-2.6B)
- Upstream base model: [LiquidAI/LFM2.5-2.6B-Base](https://huggingface.co/LiquidAI/LFM2.5-2.6B-Base)
- Liquid AI model documentation: [LFM2.5-2.6B model card](https://huggingface.co/LiquidAI/LFM2.5-2.6B)

## Citation

```bibtex
@misc{philadelphia_class_lfm25_26b_2026,
  title  = {LFM2.5-2.6B -- UNCENSORED ABLITERATED PHILADELPHIA CLASS},
  author = {KridgeDookie},
  year   = {2026},
  url    = {https://huggingface.co/KridgeDookie/LFM2.5-2.6B-UNCENSORED-ABLITERATED-PHILADELPHIA-CLASS}
}
```
