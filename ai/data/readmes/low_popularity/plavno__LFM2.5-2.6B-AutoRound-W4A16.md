---
base_model: LiquidAI/LFM2.5-2.6B
base_model_relation: quantized
license: other
license_name: lfm1.0
license_link: https://huggingface.co/LiquidAI/LFM2.5-2.6B/blob/main/LICENSE
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
pipeline_tag: text-generation
library_name: transformers
tags:
  - liquid
  - lfm2.5
  - edge
  - auto-round
  - autoround
  - gptq
  - int4
  - quantized
  - w4a16
---

# LFM2.5-2.6B — AutoRound W4A16 (4-bit weights / fp16 activations)

4-bit weight-only quantization of [`LiquidAI/LFM2.5-2.6B`](https://huggingface.co/LiquidAI/LFM2.5-2.6B),
produced with [Intel AutoRound](https://github.com/intel/auto-round) and packed for
GPTQ/Marlin kernels so it runs on vLLM without any extra flags.

Built and released by [Plavno](https://plavno.io).

This is the **smallest and fastest** variant: ~1.7 GB of weights and the highest decode
throughput. It also carries a real quality cost — please read
[Quality: read before using](#quality-read-before-using) before choosing it.

## Quantization details

| | |
|---|---|
| Method | AutoRound (signed-gradient rounding optimization) |
| Weight precision | 4-bit integer, symmetric |
| Activations | fp16 (not quantized) |
| Group size | 128 (required for the fast Marlin kernels in vLLM) |
| Packing format | `auto_round:auto_gptq` |
| Quantized modules | 166 of 167 — all `model.layers` linear projections |
| Kept in higher precision | `lm_head` |
| Calibration | conversational multilingual text, 256 samples × 512 tokens, balanced 16×16 across all 16 supported languages |
| Weights on disk | ~1.7 GB (vs ~5.4 GB bf16) |

## Calibration

This build and its 8-bit sibling
[`plavno/LFM2.5-2.6B-AutoRound-W8A16`](https://huggingface.co/plavno/LFM2.5-2.6B-AutoRound-W8A16)
were calibrated on the **same language-balanced set** — the only difference between the
two repos is the weight bit width.

The set is conversational multilingual text: 256 samples of 512 tokens, with an exactly
equal share of **16 samples per language** across all 16 languages the base model
supports:

Arabic · Chinese · English · French · German · Hindi · Indonesian · Italian ·
Japanese · Korean · Polish · Portuguese · Russian · Spanish · Thai · Vietnamese

Calibration was deliberately balanced rather than English-only, so that quantization
error is not concentrated on the non-English languages. The register is conversational
(utterance-level) rather than encyclopedic prose, which suits dialogue and speech-derived
workloads.

Note that balanced calibration reduces the cross-language imbalance described below —
it does not eliminate it, and it cannot recover the accuracy that 4-bit weight capacity
gives up in the first place.

## Quality: read before using

**4-bit weights cost real accuracy on this model, and the loss is not spread evenly
across languages.** The base model is small (2.6B), which makes it more sensitive to
aggressive weight quantization than larger models are.

Concretely, what to expect relative to the bf16 base model:

* Noticeable overall quality degradation — visible in language-modelling quality, not
  just in edge cases.
* **Uneven degradation across languages.** Some non-English languages lose
  substantially more than English does; balanced calibration reduces this imbalance
  but does not remove it.
* A meaningfully shifted output distribution. Greedy decoding picks a different token
  than the bf16 model on a significant fraction of positions, so any workload that
  reads token-level logprobs — classification, routing, scoring, endpoint/turn
  detection — is affected more than free-form generation is.

If accuracy matters, or the workload is multilingual, or you consume logprobs, use the
8-bit build instead: [`plavno/LFM2.5-2.6B-AutoRound-W8A16`](https://huggingface.co/plavno/LFM2.5-2.6B-AutoRound-W8A16).
It is near-lossless relative to bf16 and still meaningfully faster than bf16 at decode,
at ~2.9 GB instead of ~1.7 GB.

Use this 4-bit build when VRAM is the binding constraint, or when maximum decode
throughput matters more than fidelity.

## Running on vLLM

LFM2 is natively supported from vLLM 0.23.0 onward. The quantization is detected
automatically from `config.json`, so no `--quantization` flag is needed.

```bash
pip install "vllm>=0.23"

vllm serve plavno/LFM2.5-2.6B-AutoRound-W4A16 \
  --max-model-len 4096 \
  --gpu-memory-utilization 0.90
```

Add `--enable-prefix-caching` when many requests share a long common prefix
(system prompt, few-shot block, shared context) — only the new suffix is then
prefilled on each request:

```bash
vllm serve plavno/LFM2.5-2.6B-AutoRound-W4A16 \
  --enable-prefix-caching \
  --max-model-len 4096
```

Query the OpenAI-compatible endpoint:

```bash
curl http://localhost:8000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "plavno/LFM2.5-2.6B-AutoRound-W4A16",
    "messages": [{"role": "user", "content": "Say hi in one word."}],
    "max_tokens": 16
  }'
```

```python
from openai import OpenAI

client = OpenAI(base_url="http://localhost:8000/v1", api_key="EMPTY")
resp = client.chat.completions.create(
    model="plavno/LFM2.5-2.6B-AutoRound-W4A16",
    messages=[{"role": "user", "content": "List three primary colors."}],
    max_tokens=64,
)
print(resp.choices[0].message.content)
```

### Offline batch inference

```python
from vllm import LLM, SamplingParams

llm = LLM(model="plavno/LFM2.5-2.6B-AutoRound-W4A16", max_model_len=4096)
out = llm.generate(
    ["Explain what a REST API is in two sentences."],
    SamplingParams(temperature=0, max_tokens=128),
)
print(out[0].outputs[0].text)
```

## Notes

* `group_size=128` and symmetric quantization are what let vLLM select the fast Marlin
  kernel. Changing the group size to 32 would improve accuracy but give up Marlin.
* Short convolution layers of the LFM2 architecture and `lm_head` stay in higher
  precision; this is expected and correct for this architecture.
* The chat template opens a reasoning block (`<think>`) in the generation prompt. If
  you need a bare single-token answer (classification, routing), drive
  `/v1/completions` with your own prompt and close the block yourself
  (`<think></think>`) rather than relying on `/v1/chat/completions`.

## License

Inherits the license of the base model, [LFM Open License v1.0](https://huggingface.co/LiquidAI/LFM2.5-2.6B/blob/main/LICENSE).
Refer to the base model card for intended use and limitations.

---

Quantized and published by [Plavno](https://plavno.io).
