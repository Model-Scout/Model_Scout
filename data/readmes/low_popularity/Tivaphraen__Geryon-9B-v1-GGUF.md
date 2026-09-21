---
language:
  - en
  - fr
  - zh
  - ja
  - ko
  - id
  - es
  - it
  - pt
  - tr
  - fa
license: apache-2.0
pipeline_tag: text-generation
base_model: Tivaphraen/Geryon-9B-v1
base_model_relation: quantized
tags:
- qwen
- qwen3.5
- agent
- coding
- reasoning
- gguf
- quantized
- multilingual
---

# 🐉 Geryon-9B-v1 (GGUF)

![banner_geryon_gguf_pixel](https://cdn-uploads.huggingface.co/production/uploads/67a868f51bb804b976598654/sssozVxIAZrsjiMs3i9BP.png)

This repository contains the **GGUF quantizations** of the **Geryon-9B-v1** experimental merge.

**Original Safetensors repository and full merge details:**  
[https://huggingface.co/Tivaphraen/Geryon-9B-v1](https://huggingface.co/Tivaphraen/Geryon-9B-v1)

## About Geryon-9B-v1

Geryon-9B-v1 is a DARE-TIES merge of three highly specialized Qwen 3.5 fine-tunes:

- `empero-ai/Qwythos-9B-Claude-Mythos-5-1M`
- `empero-ai/Qwable-9B-Claude-Fable-5`
- `Tesslate/OmniCoder-9B`

The goal of this merge is to explore how effectively multiple agentic, reasoning, and coding fine-tunes can be layered over a dense 9B-parameter base model.

Initial GSM8K scoring (~85.1%) suggests strong reasoning retention, but comprehensive benchmarking is still needed.

> **Important note**  
> This GGUF release is configured strictly for **text generation**. Multimodal (vision) tensors and Multi-Token Prediction (MTP) layers were deliberately excluded from the conversion to prevent `llama.cpp` tensor-mapping errors.

## Evaluation Results

The GGUF files in this repository are quantized exports of the original **Geryon-9B-v1** merge.

At the time of writing, **no separate benchmark suite has been run for each individual quantization level**. The main reference results currently available are the following local measurements on the **Q8_0 GGUF** variant:

| Benchmark | Setting | Metric | Value | Notes |
| :--- | :--- | :--- | :---: | :--- |
| GSM8K | 5-shot, flexible | exact_match | **0.8514** | Measured locally on the `Q8_0` GGUF quantization |
| GSM8K | 5-shot, strict | exact_match | **0.8506** | Measured locally on the `Q8_0` GGUF quantization |

For context, one of the main parent models, `empero-ai/Qwythos-9B-Claude-Mythos-5-1M`, reports the following GSM8K results. The local results for **Geryon-9B-v1** are included below for direct comparison:

| Task | Metric | Base Qwen3.5-9B | Qwythos-9B | Geryon-9B-v1 (Q8_0 GGUF, local) | Δ vs Base | Δ vs Qwythos |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: |
| gsm8k | exact_match (flexible) | 0.6700 | **0.8600** | 0.8514 | +0.1814 | -0.0086 |
| gsm8k | exact_match (strict) | 0.5100 | 0.8100 | **0.8506** | +0.3406 | +0.0406 |

These results suggest that Geryon-9B-v1 remains very close to Qwythos on **flexible** GSM8K scoring, while slightly exceeding the published Qwythos number on the currently available **strict** local run. This comparison should still be interpreted cautiously because quantization level, inference backend, and metric convention (**strict** vs **flexible**) can all influence the final score.

> **Note:** Lower-bit variants such as `Q4_K_M` may show measurable degradation on complex reasoning and coding tasks compared to the `Q8_0` result reported above.

For full evaluation context and future benchmark updates, please refer to the original repository:  
[https://huggingface.co/Tivaphraen/Geryon-9B-v1](https://huggingface.co/Tivaphraen/Geryon-9B-v1)

## Intended Use

This repository is intended for:
- local inference with `llama.cpp` and compatible runtimes
- coding and reasoning workflows
- experimentation with quantized merged models
- users who want smaller, more deployable formats than Safetensors

## Out-of-Scope Use

This GGUF release is **not recommended** for:
- safety-critical applications
- high-risk autonomous agents
- legal, medical, or financial decisions without expert oversight
- environments where strong and reliable safety refusals are mandatory

## Available Files

| Filename | Format | Size | Description |
| :--- | :--- | :--- | :--- |
| `Geryon-9B-v1-Q8_0.gguf` | Q8_0 | ~9.5 GB | Minimal quality loss. Requires ~12 GB VRAM. |
| `Geryon-9B-v1-Q6_K.gguf` | Q6_K | ~7.5 GB | Excellent balance of quality and size. |
| `Geryon-9B-v1-Q5_K_M.gguf` | Q5_K_M | ~6.5 GB | Good for 8 GB VRAM cards with moderate context. |
| `Geryon-9B-v1-Q4_K_M.gguf` | Q4_K_M | ~5.6 GB | **Recommended.** Best performance/speed ratio for many 8 GB GPUs. |

## Prompt Format

Geryon-9B-v1 uses the standard **ChatML** template.

## Usage with llama.cpp

Because of its Qwythos heritage, the model may support extended contexts. If needed, YaRN RoPE scaling can be used for context windows larger than 32k.

**Example server launch command:**

```bash
./llama-server -m Geryon-9B-v1-Q4_K_M.gguf --ctx-size 32768 -ngl 99 --flash-attn on --temp 0.6 --top-p 0.95 --top-k 20 --repeat-penalty 1.1
```

_Adjust `--ctx-size` and `-ngl` based on your available VRAM._

## Recommended Settings

Suggested baseline sampling settings:

- **Temperature:** `0.6`
- **Top-P:** `0.95`
- **Top-K:** `20`
- **Repetition Penalty:** `1.1`

## Limitations, Risks, and Biases

As a merge of domain-specific models, Geryon-9B-v1 may show:
- unstable behavior across prompts
- inconsistent formatting
- variable refusal behavior
- hallucinations outside its strongest domains
- reduced reliability at lower quantization levels on demanding reasoning or coding tasks

One of the parent models is uncensored, meaning Geryon-9B-v1 may not reliably refuse instructions related to sensitive or unsafe topics. Downstream users are responsible for implementing appropriate safety guardrails.

For full details on limitations, evaluation status, and provenance caveats, please refer to the original Safetensors repository:  
[https://huggingface.co/Tivaphraen/Geryon-9B-v1](https://huggingface.co/Tivaphraen/Geryon-9B-v1)

## License and Provenance

These GGUF files are derived quantizations of **Geryon-9B-v1** and are released under the **Apache-2.0** license, consistent with the base model lineage as documented in the original repository.

Users should still review the provenance and synthetic-data caveats described in the Safetensors repository before commercial or downstream reuse.
