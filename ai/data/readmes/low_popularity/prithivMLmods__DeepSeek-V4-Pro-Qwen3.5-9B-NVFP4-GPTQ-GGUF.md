---
language:
- en
- zh
- ko
- ja
- es
- ru
tags:
- mtp
- text-generation-inference
- llama-cpp
- transformers
- unsloth
- qwen3_5
- reasoning
- distillation
- deepseek
- sft
- rl
- gspo
- math
- stem
- tool-use
- function-calling
- speculative-decoding
- nvidia-blackwell
- rtx-pro-6000
- SM120
- GB202
- B200
- B300
- FP4
- blackwell
- Qwen3.5
- GPTQ
library_name: transformers
base_model:
- Jackrong/DeepSeek-V4-Pro-Qwen3.5-9B
license: apache-2.0
pipeline_tag: image-text-to-text
datasets:
- HuggingFaceH4/ultrachat_200k
---

# **DeepSeek-V4-Pro-Qwen3.5-9B-NVFP4-GPTQ-GGUF**

> **DeepSeek-V4-Pro-Qwen3.5-9B-NVFP4-GPTQ** is a 4-bit NVFP4 build of Jackrong's DeepSeek-V4-Pro-Qwen3.5-9B, quantized with GPTQ (Accurate Post-Training Quantization for Generative Pre-trained Transformers). GPTQ calibration plays a critical role in stabilizing and optimizing the NVFP4 compression, keeping accuracy close to the full-precision weights while cutting memory use and speeding up inference on NVFP4-capable hardware. The source is a 9B reasoning fine-tune of Qwen3.5-9B, distilled from DeepSeek-V4-Pro in Max Effect mode on about 250K math and STEM samples. It was trained with SFT and then a light GSPO RL stage, with no coding data. The source card reports 94.50% on GSM8K (four-run mean on its own NVFP4 checkpoint under vLLM) and a 90.53% average on a 1,500-question MMLU-Pro Math, Physics and Chemistry sample, 0.93 points above Qwen3.5-9B, with about 36% fewer reasoning tokens per correct answer. Those MMLU-Pro runs used MTP-Q8_0 GGUF, and none of the figures were measured on this GPTQ build. The benchmarks are the original author's own, on random samples rather than full subsets. The card also claims a terse single-letter answer 97.2% of the time when asked. The source card calls it an experimental community model whose outputs need verification. The weights are Apache 2.0.

> [!NOTE]
> MTP — Speculative Decoding: Yes | Accelerated FP4 Tensor Core Performance

> [!NOTE]
Multi-Token Prediction (MTP) GGUF is a specialized GGUF model file format extension that integrates speculative decoding directly into the model weights to significantly accelerate local inference.  Unlike traditional speculative decoding which requires a separate, smaller "draft" model, MTP GGUF files include additional output heads within the main model architecture that predict multiple future tokens in a single forward pass.

## Model Files

| File Name | Quant Type | File Size | File Link | Description |
|-----------|------------|-----------|-----------|-------------|
| DeepSeek-V4-Pro-Qwen3.5-9B-NVFP4-GPTQ.gguf | NVFP4 / GPTQ | 8.46 GB | [Link](https://huggingface.co/prithivMLmods/DeepSeek-V4-Pro-Qwen3.5-9B-NVFP4-GPTQ-GGUF/blob/main/DeepSeek-V4-Pro-Qwen3.5-9B-NVFP4-GPTQ.gguf) | NVFP4/GPTQ quantized weights. Highly optimized for **NVIDIA Blackwell** hardware accelerators **(e.g., RTX Pro 6000, RTX 50-series, B200, B300)**, offering native hardware-accelerated FP4 Tensor Core speeds and a strong balance of size and performance. |
| DeepSeek-V4-Pro-Qwen3.5-9B.mmproj.gguf | mmproj | 922 MB | [Link](https://huggingface.co/prithivMLmods/DeepSeek-V4-Pro-Qwen3.5-9B-NVFP4-GPTQ-GGUF/blob/main/DeepSeek-V4-Pro-Qwen3.5-9B.mmproj.gguf) | Multimodal projection file. Used for vision/language capabilities. |

## NVFP4 Test Run

Tested `DeepSeek-V4-Pro-Qwen3.5-9B-NVFP4-GPTQ.gguf` on an NVIDIA RTX PRO 6000 Blackwell Server Edition GPU with `96 GB` of VRAM, using `llama-cli` with full GPU offloading and MTP speculative decoding.

### Performance Metrics

| Metric | Value |
| --- | --- |
| Average Prompt Processing Speed | 272.78 tokens/s |
| Average Generation Speed | 222.57 tokens/s |
| Total Wall Time | 31.2 seconds |
| Context Length | 8,192 tokens |
| KV Cache (K) | `q8_0` |
| GPU | NVIDIA RTX PRO 6000 Blackwell Server Edition |
| GPU VRAM Capacity | 96 GB |
| Peak GPU VRAM Usage | 28.44 GiB |
| Peak GPU Utilization | 90% |
| GPU Layers Offloaded | 99 (`-ngl 99`) |
| Random Seed | 42 |
| Speculative Decoding | MTP (`draft_n_max=2`) |
| Test Runs | 5 |

### Test Shots

| Shot | Test |
| --- | --- |
| Shot 1 | C: Insert Node at End of Singly Linked List |
| Shot 2 | Jogger and Train Passing Time |
| Shot 3 | Two Pipes Filling a Tank |
| Shot 4 | Students in Examination Rooms |
| Shot 5 | Father and Son Ages |

### Run Inference

```bash
./build/bin/llama-cli \
  -m /path/to/models/DeepSeek-V4-Pro-Qwen3.5-9B-NVFP4-GPTQ.gguf \
  --spec-type draft-mtp \
  --spec-draft-n-max 2 \
  -ngl 99 \
  -c 8192 \
  --cache-type-k q8_0 \
  --seed 42 \
  -n 8192 \
  -st \
  -p "Your prompt here"
```

*Performance results reflect this specific hardware and inference configuration. Actual throughput may vary depending on the prompt, model, software build, and runtime settings.*

## Snapshots (5)

![download (1)](https://cdn-uploads.huggingface.co/production/uploads/65bb837dbfb878f46c77de4c/kYe5JPc6JdqTxBKBzIGrA.png)
![download (2)](https://cdn-uploads.huggingface.co/production/uploads/65bb837dbfb878f46c77de4c/5bz2v9mIuZo8XK9S3gOiP.png)
![download (3)](https://cdn-uploads.huggingface.co/production/uploads/65bb837dbfb878f46c77de4c/R6o_cbT76uzL6XP-pz2nC.png)
![download (4)](https://cdn-uploads.huggingface.co/production/uploads/65bb837dbfb878f46c77de4c/_uH1jzjdIeXXEYlRoLWGf.png)
![download (5)](https://cdn-uploads.huggingface.co/production/uploads/65bb837dbfb878f46c77de4c/Zpmp6UI8pHeI0S2rhDmEs.png)
![download](https://cdn-uploads.huggingface.co/production/uploads/65bb837dbfb878f46c77de4c/On_vic5KTQPIZ6o7pxNRs.png)

## llama.cpp

LLM inference in C/C++ — https://github.com/ggml-org/llama.cpp

Quantized using llama.cpp by [prithivMLmods](https://huggingface.co/prithivMLmods).