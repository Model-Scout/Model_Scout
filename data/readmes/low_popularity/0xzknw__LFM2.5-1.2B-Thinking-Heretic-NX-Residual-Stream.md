---
base_model: LiquidAI/LFM2.5-1.2B-Thinking
library_name: transformers
pipeline_tag: text-generation
license: other
license_name: lfm-open-license-v1.0
license_link: LICENSE
language:
- en
- ar
- zh
- fr
- de
- ja
- ko
- es
tags:
- lfm2
- lfm2.5
- reasoning
- bf16
- gguf
- lm-studio
- abliterated
- uncensored
- model-editing
- heretic-nx
- residual-stream
- prime
---

# LFM2.5 1.2B Thinking — Heretic NX Residual-Stream

This is a BF16 behavioral edit of
[`LiquidAI/LFM2.5-1.2B-Thinking`](https://huggingface.co/LiquidAI/LFM2.5-1.2B-Thinking)
focused on aggressive false-refusal removal while preserving the base model's
general behavior as closely as possible.

The naming has three distinct levels:

- **Heretic NX** is the model-editing engine and research project.
- **Residual-Stream** is the algorithm profile used for this checkpoint.
- **PRIME** is the project's capability-preservation and evidence protocol.

PRIME is an internal validation protocol, not a third-party certification.

## Files

- `model.safetensors`: native Transformers checkpoint in BF16.
- `LFM2.5-1.2B-Thinking-Heretic-NX-Residual-Stream-BF16.gguf`: full BF16
  GGUF for LM Studio/llama.cpp. It is **not quantized**.
- `PROVENANCE.json`: portable source, code, evaluation and artifact hashes.
- `MODIFICATION_NOTICE.md`: derivative-model modification notice.

## Results

The frozen candidate was compared with fresh, hash-bound artifacts produced by
the official Heretic `master` and `v1.4.0` code. Heretic-wide is the stronger
previously disclosed comparator. All arms use the same prompts and deterministic
evaluation settings; no post-comparison tuning was performed.

| Evaluation | Base | Heretic master | Heretic v1.4 | Heretic-wide | Residual-Stream |
| --- | ---: | ---: | ---: | ---: | ---: |
| XSTest lexical refusals, 450 rows | 131 | 50 | 19 | 12 | **5** |
| XSTest safe-prompt refusals, 250 rows | 16 | 4 | 2 | 2 | **0** |
| StrongREJECT lexical refusals, 313 rows | 240 | 114 | 48 | **14** | **14** |
| Combined target refusals, 513 rows | 355 | 160 | 65 | 24 | **19** |
| Paired capability slice, 854 rows | 22.95% | 23.07% | 22.95% | 22.95% | **23.42%** |

With familywise alpha 5% corrected over three metrics and three Heretic arms,
Residual-Stream has positive paired target lower bounds against the official
master (`+0.2203`) and v1.4.0 (`+0.0526`) runs. It also passes the zero-margin
safe-behavior gate and the preregistered 3 percentage-point capability
non-inferiority gate against both. Under the published model-specific protocol,
it therefore outperforms those two pinned official Heretic runs.

Against Heretic-wide, Residual-Stream has fewer observed combined refusals
(19 versus 24), but the corrected target interval crosses zero; that comparison
remains descriptive. The capability test uses deterministic first-token A/B/C/D
scoring on ARC-Challenge, HellaSwag and MMLU. It is a capability slice, not a
comprehensive benchmark suite.

The release-time teacher-forced sequence-drift comparison is unchanged:
Residual-Stream scored full-sequence KL `0.0701` versus `0.1438` for the pinned
Heretic-wide comparator on development prompts, and `0.0643` versus `0.1343`
on the locked holdout.

Refusal-marker counts are lexical proxies. They do not measure semantic task
success, correctness or safety. These results support a corrected, matched
comparison on this exact LFM model, not a universal engine or model ranking.

## Transformers usage

Install a recent Transformers release with LFM2 support:

```bash
pip install "transformers>=5.0" accelerate torch
```

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "0xzknw/LFM2.5-1.2B-Thinking-Heretic-NX-Residual-Stream"

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    dtype=torch.bfloat16,
    device_map="auto",
).eval()

messages = [{"role": "user", "content": "Explain why the sky is blue."}]
inputs = tokenizer.apply_chat_template(
    messages,
    add_generation_prompt=True,
    return_tensors="pt",
).to(model.device)

with torch.inference_mode():
    output = model.generate(inputs, max_new_tokens=256)

print(tokenizer.decode(output[0][inputs.shape[-1]:], skip_special_tokens=True))
```

## LM Studio

Download the `...Residual-Stream-BF16.gguf` file and import it into LM Studio.
The published file was loaded with full GPU offload at a 4096-token context on
the development machine. An end-to-end arithmetic generation smoke test
returned the expected answer, found EOS, and ran at 75.77 tokens/s. Performance
depends on hardware and runtime version.

The GGUF was produced by llama.cpp `b10603` at commit
`c060ca974c773c7c3d17fd1b66dc9d312bc292c0` using `--outtype bf16`.

## Reproducibility

Engine source, release scripts, tests and compact evidence are pinned at
[`heretic-nx@2147c09`](https://github.com/0xZKnw/heretic-nx/tree/2147c09c5464df26b5855e19affa1b2b4b515dd3).
The exact base, candidate, comparator, dataset, report and GGUF hashes are in
`PROVENANCE.json` and in the repository's
[`release evidence`](https://github.com/0xZKnw/heretic-nx/blob/2147c09c5464df26b5855e19affa1b2b4b515dd3/evidence/lfm25-residual-stream/release.json).

The corrected closed comparison, exact upstream configurations, item-level
observations and multiplicity-adjusted intervals are pinned at
[`heretic-nx@4347278`](https://github.com/0xZKnw/heretic-nx/tree/43472788cec0b2b955116ed7db48f81b3951cb37), with a compact
[`hash-bound summary`](https://github.com/0xZKnw/heretic-nx/blob/43472788cec0b2b955116ed7db48f81b3951cb37/evidence/lfm25-closed-track/summary.json).

## Limitations and responsibility

This edit intentionally weakens refusal behavior. That can increase compliance
with unsafe, illegal, incorrect or otherwise harmful requests. It does not add
factuality, security boundaries or reliable judgment. Run untrusted generations
in an appropriate sandbox and apply independent application-level safeguards.

The BF16 checkpoint is the evaluated artifact. The BF16 GGUF has a runtime
smoke pass, but it has not independently repeated every PRIME capability slice.
Q8/Q6/Q4 variants are not included and would require their own evaluation.

Use is subject to the included LFM Open License v1.0.
