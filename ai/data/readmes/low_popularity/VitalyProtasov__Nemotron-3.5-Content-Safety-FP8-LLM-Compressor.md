---
license: other
license_name: openmdw-license-agreement 
license_link: >-
  https://raw.githubusercontent.com/OpenMDW/OpenMDW/refs/heads/main/1.1/LICENSE.OpenMDW-1.1
language:

- en
- ar
- de
- es
- fr
- hi
- ja
- th
- nl
- it
- ko
- zh
base_model: nvidia/Nemotron-3.5-Content-Safety
base_model_relation: quantized
library_name: transformers
pipeline_tag: image-text-to-text
tags:
- fp8
- compressed-tensors
- llm-compressor
- vllm
- b300
---

# Nemotron 3.5 Content Safety — LLM Compressor FP8

This is an independently produced FP8 quantization of [nvidia/Nemotron-3.5-Content-Safety](https://huggingface.co/nvidia/Nemotron-3.5-Content-Safety). NVIDIA developed the source model but did not produce or endorse this quantized checkpoint. The original model card is retained below, following the additional quantization and benchmark information for this derivative.

## Quantized checkpoint overview

| Property | Value |
|---|---|
| Source checkpoint | `nvidia/Nemotron-3.5-Content-Safety` |
| Compression tool | LLM Compressor `0.9.0.4` |
| Serialization | compressed-tensors `0.13.0` |
| Weight / activation scheme | `FP8_DYNAMIC` W8A8 |
| Weights | Static, symmetric, per-channel FP8 |
| Activations | Dynamic, symmetric, per-token FP8 |
| KV cache | Static, symmetric, per-tensor FP8 scales |
| Modules left unquantized | `lm_head` and the complete vision tower |
| Checkpoint size | 6.4 GiB on disk |
| Source-model context length | Up to 128K tokens |

The language-model linear layers were compressed with:

```python
QuantizationModifier(
    targets="Linear",
    scheme="FP8_DYNAMIC",
    ignore=["lm_head", r"re:model\.vision_tower.*"],
    kv_cache_scheme=QuantizationArgs(
        num_bits=8,
        type="float",
        strategy="tensor",
        dynamic=False,
        symmetric=True,
    ),
)
```

`FP8_DYNAMIC` uses static per-channel weight scales and dynamic per-token activation scales, so the W8A8 path itself does not require an activation-calibration corpus. The 512 CNN/DailyMail samples at sequence length 512 were used only to determine the static per-tensor FP8 KV-cache scales.

The export retained `lm_head` and the SigLIP vision tower in their original precision. Unused vision KV-scale tensors were removed for vLLM compatibility; language-model weight tensors and text K/V scale values were not modified by that compatibility step. The export ran on one NVIDIA H100 80 GB. The checkpoint is not hardware-bound; the serving benchmark below ran on one NVIDIA B300.

## B300 benchmark

The following is a custom, text-only deployment benchmark, not an NVIDIA benchmark and not a replacement for the source model's published evaluations. It is included to show the measured quality/performance trade-off against the unquantized source checkpoint under one matched serving setup.

### Quality

Quality was scored on the strict common intersection of 10,269 binary conversation/category pairs from 3,614 internally annotated conversations across all five B300 deployments in the full experiment. Only the BF16 and LLM Compressor FP8 rows relevant to this checkpoint are shown here. Every model evaluated all seven moderation categories in one request. Rows without a valid parse from any of the five deployments were excluded from every score. The reference annotations were generated automatically with GPT-5.6 and are not multi-reviewer human ground truth.

| B300 deployment | Precision | Recall | Micro-F1 | Accuracy | Balanced accuracy |
|---|---:|---:|---:|---:|---:|
| Source BF16 | 0.614 | 0.148 | 0.239 | 0.840 | 0.565 |
| This LLM Compressor FP8 checkpoint | **0.628** | **0.151** | **0.244** | **0.841** | **0.566** |

The observed `+0.005` Micro-F1 difference is small and should not be interpreted as evidence that quantization improves model quality. This evaluation also contains no positive sexually explicit examples and only 13 positive hate-speech examples, so those category estimates are absent or unstable.

### Streaming performance

Both deployments used one physical NVIDIA B300 SXM6 PC (275,040 MiB reported), tensor parallelism 1, vLLM `0.20.2`, PyTorch `2.11.0+cu130`, CUDA 13.0, a 131,072-token limit, maximum 64 sequences, 90% GPU-memory utilization, prefix caching, and text-only serving. Generation used temperature 0, top-p 1, thinking disabled, and at most 256 output tokens. The FP8 deployment used `--kv-cache-dtype fp8`; BF16 used the automatic BF16 KV cache.

The timing cohort contained 500 length-stratified prompts disjoint from the quality cohort: 100 prompts at each concurrency level. Each deployment started in a fresh vLLM process. Prefix caching remained enabled within a deployment run, matching the intended serving configuration.

| Deployment | Concurrency | Success | Requests/s | Prompt tokens/s | TTFT P50 | TTFT P95 | Decode P50 | Decode P95 | Decode P50 ms/token |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Source BF16 | 1 | 100/100 | 12.11 | 72,638 | 38.7 ms | 159.3 ms | 27.3 ms | 67.9 ms | 3.03 |
| This FP8 checkpoint | 1 | 100/100 | 13.26 | 79,502 | 37.6 ms | 136.5 ms | 23.5 ms | 54.0 ms | 2.72 |
| Source BF16 | 2 | 100/100 | 15.67 | 99,623 | 59.3 ms | 206.3 ms | 27.4 ms | 125.0 ms | 3.11 |
| This FP8 checkpoint | 2 | 100/100 | 17.63 | 112,070 | 54.4 ms | 215.2 ms | 20.1 ms | 116.6 ms | 2.62 |
| Source BF16 | 4 | 99/100 | 19.60 | 127,313 | 109.6 ms | 335.8 ms | 27.4 ms | 209.0 ms | 3.46 |
| This FP8 checkpoint | 4 | 99/100 | 22.40 | 145,512 | 97.7 ms | 275.2 ms | 20.0 ms | 162.9 ms | 2.76 |
| Source BF16 | 8 | 98/100 | 22.44 | 147,303 | 187.6 ms | 632.3 ms | 73.8 ms | 357.2 ms | 10.39 |
| This FP8 checkpoint | 8 | 100/100 | 26.85 | 175,016 | 171.1 ms | 466.8 ms | 55.2 ms | 253.4 ms | 7.56 |
| Source BF16 | 16 | 100/100 | 23.25 | 160,177 | 370.2 ms | 977.5 ms | 181.2 ms | 758.0 ms | 26.11 |
| This FP8 checkpoint | 16 | 100/100 | **28.56** | **196,797** | **285.6 ms** | **781.0 ms** | **162.3 ms** | **440.0 ms** | **25.88** |

Peak measured throughput increased from 23.25 to 28.56 requests/s (`+22.8%`) while Micro-F1 remained within `+0.005` of the BF16 result on the strict common set.

TTFT is measured client-side from request start to the first non-empty SSE content delta. It includes HTTP overhead, scheduler queueing, prefill, and first-token decoding. Decode time is measured from the first content delta to stream completion. `Decode P50 ms/token` is the median per-request value of `decode_ms / max(completion_tokens - 1, 1)`; the first token is excluded because it is already included in TTFT. These are end-to-end deployment metrics, not isolated GPU-kernel measurements.

The BF16 and FP8 deployments differ in both W8A8 compression and KV-cache precision. The benchmark therefore measures the complete deployment and cannot attribute the observed change specifically to FP8 weights, activations, or KV-cache quantization.

## Serving with vLLM

The B300 benchmark used the following text-only configuration:

```bash
vllm serve VitalyProtasov/Nemotron-3.5-Content-Safety-FP8-LLM-Compressor \
  --served-model-name nemotron-content-safety-fp8 \
  --quantization compressed-tensors \
  --dtype bfloat16 \
  --kv-cache-dtype fp8 \
  --tensor-parallel-size 1 \
  --max-model-len 131072 \
  --max-num-seqs 64 \
  --gpu-memory-utilization 0.90 \
  --enable-prefix-caching \
  --language-model-only
```

Remove `--language-model-only` when the vision encoder is required. Multimodal behavior was not evaluated in the custom benchmark above.

## Compatibility notes

- Validated for text-only serving with vLLM `0.20.2` on NVIDIA B300.
- vLLM loaded the checkpoint through the `compressed-tensors` quantization backend and used an FP8 KV cache.
- At startup, vLLM may warn that separately calibrated attention `q_scale` and `prob_scale` values are unavailable and use fallback values. This is a serving-stack limitation and may affect results.
- The tokenizer may emit a Mistral-regex compatibility warning in some Transformers/vLLM versions. Validate tokenization when changing the serving stack.
- The benchmark data is internal and cannot be used to reproduce the reported scores from this repository alone.

## Source model and license

This checkpoint is a quantized derivative of [NVIDIA Nemotron-3.5-Content-Safety](https://huggingface.co/nvidia/Nemotron-3.5-Content-Safety). Refer to the source model card for architecture, training data, supported languages, intended use, safety evaluation, and model-specific limitations.

Use is governed by the [OpenMDW License Agreement 1.1](https://raw.githubusercontent.com/OpenMDW/OpenMDW/refs/heads/main/1.1/LICENSE.OpenMDW-1.1), the [Gemma Terms of Use](https://ai.google.dev/gemma/terms), and the [Gemma Prohibited Use Policy](https://ai.google.dev/gemma/prohibited_use_policy). NVIDIA produced the source model but did not produce or endorse this quantized checkpoint.
