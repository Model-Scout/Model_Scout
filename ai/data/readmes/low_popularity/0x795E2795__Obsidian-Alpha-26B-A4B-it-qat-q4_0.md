---
tags:
- gemma4
- gguf
- q4_0
- moe
- text-generation
- llama-cpp
pipeline_tag: text-generation
base_model:
- google/gemma-4-26B-A4B
base_model_relation: finetune
license: apache-2.0
language:
- ko
- en
- zh
- ja
- fr
- de
- es
- it
- ru
- ar
- hi
- pt
- vi
- th
- id
- nl
- da
- pl
- tr
---

# Obsidian Alpha 26B-A4B — GGUF Q4_0

**Obsidian Alpha** is an experimental 26B-class sparse Mixture-of-Experts language model with approximately **3.8B active parameters per token**.

This repository provides the model in **GGUF Q4_0** format for lightweight local inference, hardware-efficient deployment, and compatibility testing with GGUF-based runtimes.

This release is intended for early testing, independent evaluation, runtime compatibility testing, quantization research, and community feedback.

> **Alpha release:** model behavior, compatibility, formatting, configuration, and weights may change in future revisions.

## Model Overview

| Property                 | Value                     |
| ------------------------ | ------------------------- |
| Model                    | Obsidian Alpha 26B-A4B    |
| Architecture             | Sparse Mixture-of-Experts |
| Total parameters         | 26B-class                 |
| Active parameters        | ~3.8B                     |
| Layers                   | 30                        |
| Experts                  | 128                       |
| Routed experts           | Top-8                     |
| Context length           | 262,144 tokens            |
| Sliding attention window | 1,024 tokens              |
| Format                   | GGUF                      |
| Quantization             | Q4_0                      |
| Release status           | Alpha / Experimental      |

Parameter counts reported by individual libraries or hosting platforms may differ depending on whether embeddings, auxiliary parameters, routing components, and other tensors are included.

## GGUF Quantization

This repository uses the **Q4_0** GGUF quantization format.

Q4_0 provides a compact model representation with broad support across GGUF-compatible inference engines.

This checkpoint is primarily provided for:

* local inference
* lower-memory deployment
* llama.cpp-compatible environments
* CPU/GPU hybrid inference
* runtime compatibility testing
* quantization evaluation
* behavioral comparison against W4A16 and other quantized releases

Because quantization changes numerical precision, outputs may differ from higher-precision or alternative Obsidian Alpha checkpoints even when identical prompts and generation settings are used.

Small numerical differences can also lead to different generation trajectories over longer outputs.

## Context

Obsidian Alpha is configured for a maximum context length of:

**262,144 tokens**

The architecture also uses a local sliding attention window of:

**1,024 tokens**

Actual usable context length depends heavily on:

* available system memory
* available VRAM
* KV-cache precision
* inference backend
* attention implementation
* runtime configuration
* GPU offloading strategy

Very-long-context behavior remains experimental.

Using the full configured context length may require substantially more memory than loading the model weights alone.

## Recommended Generation Settings

A reasonable starting point is:

```text
temperature: 1.225
top_p: 0.95
top_k: 64
```

These values are not strict requirements.

Different workloads may benefit from different sampling configurations.

For benchmark evaluation, use the generation settings required by the benchmark rather than these defaults.

## llama.cpp Usage

Example:

```bash
./llama-cli \
  -m obsidian-alpha-26B_q4_0-it.gguf \
  -cnv \
  -c 8192 \
  --temp 1.225 \
  --top-p 0.95 \
  --top-k 64
```

For GPU offloading:

```bash
./llama-cli \
  -m obsidian-alpha-26B_q4_0-it.gguf \
  -cnv \
  -c 8192 \
  -ngl 999 \
  --temp 1.225 \
  --top-p 0.95 \
  --top-k 64
```

Adjust context length and GPU offloading according to your hardware.

Support may depend on the version of `llama.cpp` or other GGUF-compatible runtimes being used.

## Server Example

Obsidian Alpha can also be served through a compatible `llama.cpp` server build.

```bash
./llama-server \
  -m obsidian-alpha-26B_q4_0-it.gguf \
  -c 8192 \
  -ngl 999 \
  --host 0.0.0.0 \
  --port 8080
```

Runtime flags may differ between versions.

For API serving, context size, batch configuration, parallelism, and GPU offloading should be adjusted according to available hardware.

## Hardware Notes

Memory usage depends on more than the GGUF file size.

Additional memory is required for:

* KV cache
* runtime buffers
* compute buffers
* context processing
* attention operations
* GPU offloading
* backend-specific allocations

Long context lengths can significantly increase memory consumption even when the model weights themselves fit comfortably in memory.

CPU-only inference is possible in compatible runtimes, although performance will depend strongly on CPU capabilities and system memory bandwidth.

GPU acceleration can significantly improve prompt processing and generation performance when supported by the runtime.

## Benchmarks

**Benchmark evaluation is currently in progress.**

Results will be published after the evaluation suite has been completed and the measurements have been verified.

The evaluation is intended to cover areas including:

* general knowledge
* reasoning
* mathematics
* coding
* instruction following
* quantization quality retention
* long-context behavior
* behavioral consistency

Preliminary or incomplete benchmark numbers are intentionally not included in this README.

## Comparing Quantized Releases

Different quantization formats should not be assumed to behave identically.

Obsidian Alpha may also be distributed in other formats, including native **W4A16 QAT** checkpoints.

When comparing this Q4_0 release against other Obsidian Alpha checkpoints, useful measurements include:

* task accuracy
* answer flips
* token-level agreement
* token-distribution divergence
* perplexity
* output consistency
* prompt processing speed
* generation speed
* memory usage
* long-context stability

A single benchmark accuracy score may not fully describe quantization quality.

In particular, models with similar aggregate accuracy may still differ substantially in individual answers or generation trajectories.

## Alpha Testing

This release is primarily intended to collect real-world observations across different hardware and inference environments.

Useful feedback includes:

* inference backend
* backend version
* CPU
* GPU / accelerator
* RAM
* VRAM
* context length
* KV-cache configuration
* GPU offload settings
* generation settings
* memory usage
* prompt processing speed
* generation speed
* output quality
* reproducible compatibility issues
* comparisons against other quantization formats

When reporting performance, using **tok/s** for generation speed is preferred.

Providing enough runtime and hardware information to reproduce a result is strongly encouraged.

## Known Limitations

Obsidian Alpha is an experimental checkpoint.

Current limitations may include:

* backend-specific compatibility issues
* behavior changes caused by Q4_0 quantization
* output differences relative to W4A16 or other Obsidian Alpha releases
* sensitivity to sampling configuration
* inconsistent behavior at extremely long context lengths
* runtime-specific numerical differences
* reduced numerical fidelity compared with higher-precision checkpoints
* differences between inference implementations

Outputs should not be assumed to be bit-for-bit or behaviorally identical across different inference engines.

## Intended Use

Obsidian Alpha GGUF is intended for:

* research
* experimentation
* local inference
* model evaluation
* reasoning and mathematics evaluation
* coding evaluation
* quantization research
* software development
* testing GGUF inference engines
* testing CPU/GPU offloading configurations
* low-memory inference experiments

As an Alpha release, it should be evaluated carefully before use in reliability-sensitive applications.

## License

This model follows the **Gemma 4 license and usage terms**.

Users are responsible for reviewing and complying with the applicable Gemma license terms and usage restrictions when downloading, modifying, redistributing, or using this model.

## Disclaimer

Obsidian Alpha is provided as an experimental model release.

Generated outputs may be inaccurate, inconsistent, biased, or otherwise unsuitable for a particular use case.

Users should independently verify important outputs and evaluate the model for their intended application.

Performance, compatibility, and behavior may vary depending on hardware, inference software, quantization implementation, and generation configuration.

## Feedback

Bug reports, compatibility results, benchmark measurements, quantization comparisons, and other technical feedback are welcome.

When reporting results, please include enough runtime, hardware, context, and generation configuration information to reproduce the test where possible.