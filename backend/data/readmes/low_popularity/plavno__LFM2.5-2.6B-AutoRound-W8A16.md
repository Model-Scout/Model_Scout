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
  - int8
  - quantized
  - w8a16
---

# LFM2.5-2.6B — AutoRound W8A16 (8-bit weights / fp16 activations)

8-bit weight-only quantization of [`LiquidAI/LFM2.5-2.6B`](https://huggingface.co/LiquidAI/LFM2.5-2.6B),
produced with [Intel AutoRound](https://github.com/intel/auto-round) and packed for
GPTQ/Marlin kernels so it runs on vLLM without any extra flags.

Built and released by [Plavno](https://plavno.io).

This is the **accuracy-preserving** variant. A smaller 4-bit sibling is available at
[`plavno/LFM2.5-2.6B-AutoRound-W4A16`](https://huggingface.co/plavno/LFM2.5-2.6B-AutoRound-W4A16),
but it carries a real quality cost — see [Choosing between the two](#choosing-between-the-two).

## Quantization details

| | |
|---|---|
| Method | AutoRound (signed-gradient rounding optimization) |
| Weight precision | 8-bit integer, symmetric |
| Activations | fp16 (not quantized) |
| Group size | 128 |
| Packing format | `auto_round:auto_gptq` |
| Quantized modules | 166 of 167 — all `model.layers` linear projections |
| Kept in higher precision | `lm_head` |
| Calibration | conversational multilingual text, 256 samples × 512 tokens, balanced 16×16 across all 16 supported languages |
| Weights on disk | ~2.9 GB (vs ~5.4 GB bf16) |

## Calibration

This build and its 4-bit sibling
[`plavno/LFM2.5-2.6B-AutoRound-W4A16`](https://huggingface.co/plavno/LFM2.5-2.6B-AutoRound-W4A16)
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

## Running on vLLM

LFM2 is natively supported from vLLM 0.23.0 onward. The quantization is detected
automatically from `config.json`, so no `--quantization` flag is needed.

```bash
pip install "vllm>=0.23"

vllm serve plavno/LFM2.5-2.6B-AutoRound-W8A16 \
  --max-model-len 4096 \
  --gpu-memory-utilization 0.90
```

Add `--enable-prefix-caching` when many requests share a long common prefix
(system prompt, few-shot block, shared context) — only the new suffix is then
prefilled on each request:

```bash
vllm serve plavno/LFM2.5-2.6B-AutoRound-W8A16 \
  --enable-prefix-caching \
  --max-model-len 4096
```

Query the OpenAI-compatible endpoint:

```bash
curl http://localhost:8000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "plavno/LFM2.5-2.6B-AutoRound-W8A16",
    "messages": [{"role": "user", "content": "Say hi in one word."}],
    "max_tokens": 16
  }'
```

```python
from openai import OpenAI

client = OpenAI(base_url="http://localhost:8000/v1", api_key="EMPTY")
resp = client.chat.completions.create(
    model="plavno/LFM2.5-2.6B-AutoRound-W8A16",
    messages=[{"role": "user", "content": "List three primary colors."}],
    max_tokens=64,
)
print(resp.choices[0].message.content)
```

### Offline batch inference

```python
from vllm import LLM, SamplingParams

llm = LLM(model="plavno/LFM2.5-2.6B-AutoRound-W8A16", max_model_len=4096)
out = llm.generate(
    ["Explain what a REST API is in two sentences."],
    SamplingParams(temperature=0, max_tokens=128),
)
print(out[0].outputs[0].text)
```

## Choosing between the two

| | W8A16 (this repo) | W4A16 |
|---|---|---|
| Weights on disk | ~2.9 GB | ~1.7 GB |
| Quality vs bf16 | near-lossless | noticeable degradation, uneven across languages |
| Best for | accuracy-sensitive work, multilingual input, reading token logprobs | tight VRAM budgets, maximum decode throughput |

Pick this 8-bit build when output quality matters, when the workload is multilingual,
or when you read token-level logprobs (classification, routing, scoring) — the 4-bit
build shifts the output distribution enough to affect those.

Pick the 4-bit build when VRAM is the binding constraint or when decode throughput
matters more than fidelity.

## Notes

* Short convolution layers of the LFM2 architecture and `lm_head` stay in higher
  precision; this is expected and correct for this architecture.
* The chat template opens a reasoning block (`<think>`) in the generation prompt. If
  you need a bare single-token answer (classification, routing), drive
  `/v1/completions` with your own prompt and close the block yourself
  (`<think></think>`) rather than relying on `/v1/chat/completions`.
* 8-bit weight-only quantization reduces the bytes moved per decode step, which helps
  memory-bandwidth-bound generation. It does not speed up compute-bound prefill,
  where the dequantization step is additional work.

## License

Inherits the license of the base model, [LFM Open License v1.0](https://huggingface.co/LiquidAI/LFM2.5-2.6B/blob/main/LICENSE).
Refer to the base model card for intended use and limitations.

---

Quantized and published by [Plavno](https://plavno.io).
