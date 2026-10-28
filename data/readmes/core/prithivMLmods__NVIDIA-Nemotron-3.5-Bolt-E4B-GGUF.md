---
language:
- no
- en
- ar
- bg
- cs
- da
- de
- el
- es
- et
- fi
- fr
- hi
- hr
- hu
- id
- it
- ja
- ko
- lt
- lv
- nl
- pl
- pt
- ro
- ru
- sk
- sl
- sv
- th
- tr
- uk
- vi
- zh
license: other
license_name: openmdw-1.1
license_link: https://openmdw.ai/license/1-1/
base_model:
- nvidia/NVIDIA-Nemotron-3.5-Bolt-E4B-BF16
library_name: transformers
tags:
- text-generation-inference
- llama-cpp
- nvidia
- any-to-any
- nemotron-3.5
- image-text-to-text
- llama-cli
datasets:
- nvidia/nemotron-post-training-v3
- nvidia/nemotron-pre-training-datasets
pipeline_tag: text-generation
---

# **NVIDIA-Nemotron-3.5-Bolt-E4B-GGUF**

> **NVIDIA-Nemotron-3.5-Bolt-E4B-BF16** is NVIDIA's full-precision small language model, post-trained from Google's Gemma-4-E4B-it (8B total, 4B effective parameters), aimed at fast local voice and device assistants, interactive personas and embedded or edge interfaces. It keeps Gemma's conversational strengths and improves multi-turn tool use, instruction following and input grounding, with low memory use and low time to first token. Post-training was multi-environment reinforcement learning (GRPO, asynchronous, with NeMo RL and NeMo Gym) over instruction following, multi-step tool use, multi-turn conversation and structured-output environments. The model is text-in, text-out, with up to 64K tokens of input and output. It has chat-template switches for thinking (`enable_thinking`) and for a `conversational_mode` that gives concise, less formatted replies suited to spoken use, plus a documented client for capping the thinking budget at runtime. Against Gemma-4-E4B-it, Qwen3.5-4B and Nemotron-3-Nano-4B, measured by NVIDIA under NeMo Gym, it leads the BF16 group on most rows, including MultiChallenge (53.10), RoleBench (67.05), IHEval (84.79), IFBench (63.79) and RelyToolBench (63.16). Qwen3.5-4B is ahead on Tau2-Bench (75.06 vs 55.10), RULER at 64K, LongBench v2, BFCL-v3 and ToolSandbox, and Gemma leads EQ-Bench v3. The card also reports Q4_K_M results for the companion 4 GB build, which stay close to the BF16 scores. It is served with vLLM (v0.31.0) using the Gemma-4 tool and reasoning parsers, and a companion DFlash drafter is offered for speculative decoding. The card says this BF16 release is intended mainly for customization, post-training, quantization and research rather than direct production inference, and points to the Q4_K_M build for deployment. It is released under the OpenMDW-1.1 license, and the card notes the model was post-trained on Gemma 4.

## Model Files

| File Name | Quant Type | File Size | File Link | Description |
|-----------|------------|-----------|-----------|-------------|
| NVIDIA-Nemotron-3.5-Bolt-E4B.BF16.gguf | BF16 | 15.1 GB | [Link](https://huggingface.co/prithivMLmods/NVIDIA-Nemotron-3.5-Bolt-E4B-GGUF/blob/main/NVIDIA-Nemotron-3.5-Bolt-E4B.BF16.gguf) | Full BF16 weights. Highest quality, largest file size. |
| NVIDIA-Nemotron-3.5-Bolt-E4B.Q2_K.gguf | Q2_K | 4.4 GB | [Link](https://huggingface.co/prithivMLmods/NVIDIA-Nemotron-3.5-Bolt-E4B-GGUF/blob/main/NVIDIA-Nemotron-3.5-Bolt-E4B.Q2_K.gguf) | Lowest quality, smallest size, good for extreme low RAM availability. |
| NVIDIA-Nemotron-3.5-Bolt-E4B.Q3_K_L.gguf | Q3_K_L | 5.02 GB | [Link](https://huggingface.co/prithivMLmods/NVIDIA-Nemotron-3.5-Bolt-E4B-GGUF/blob/main/NVIDIA-Nemotron-3.5-Bolt-E4B.Q3_K_L.gguf) | Lower quality but usable, good for low RAM availability. |
| NVIDIA-Nemotron-3.5-Bolt-E4B.Q3_K_M.gguf | Q3_K_M | 4.85 GB | [Link](https://huggingface.co/prithivMLmods/NVIDIA-Nemotron-3.5-Bolt-E4B-GGUF/blob/main/NVIDIA-Nemotron-3.5-Bolt-E4B.Q3_K_M.gguf) | Low quality. |
| NVIDIA-Nemotron-3.5-Bolt-E4B.Q3_K_S.gguf | Q3_K_S | 4.65 GB | [Link](https://huggingface.co/prithivMLmods/NVIDIA-Nemotron-3.5-Bolt-E4B-GGUF/blob/main/NVIDIA-Nemotron-3.5-Bolt-E4B.Q3_K_S.gguf) | Lowest of the Q3 variants, very low RAM usage. |
| NVIDIA-Nemotron-3.5-Bolt-E4B.Q4_0.gguf | Q4_0 | 5.19 GB | [Link](https://huggingface.co/prithivMLmods/NVIDIA-Nemotron-3.5-Bolt-E4B-GGUF/blob/main/NVIDIA-Nemotron-3.5-Bolt-E4B.Q4_0.gguf) | Standard 4-bit quantization, older format but widely supported. |
| NVIDIA-Nemotron-3.5-Bolt-E4B.Q4_K_M.gguf | Q4_K_M | 5.34 GB | [Link](https://huggingface.co/prithivMLmods/NVIDIA-Nemotron-3.5-Bolt-E4B-GGUF/blob/main/NVIDIA-Nemotron-3.5-Bolt-E4B.Q4_K_M.gguf) | Good quality, default size for most use cases, *recommended*. |
| NVIDIA-Nemotron-3.5-Bolt-E4B.Q4_K_S.gguf | Q4_K_S | 5.2 GB | [Link](https://huggingface.co/prithivMLmods/NVIDIA-Nemotron-3.5-Bolt-E4B-GGUF/blob/main/NVIDIA-Nemotron-3.5-Bolt-E4B.Q4_K_S.gguf) | Slightly lower quality with more space savings, *recommended*. |
| NVIDIA-Nemotron-3.5-Bolt-E4B.Q5_0.gguf | Q5_0 | 5.69 GB | [Link](https://huggingface.co/prithivMLmods/NVIDIA-Nemotron-3.5-Bolt-E4B-GGUF/blob/main/NVIDIA-Nemotron-3.5-Bolt-E4B.Q5_0.gguf) | Standard 5-bit quantization, older format but widely supported. |
| NVIDIA-Nemotron-3.5-Bolt-E4B.Q5_K_M.gguf | Q5_K_M | 5.76 GB | [Link](https://huggingface.co/prithivMLmods/NVIDIA-Nemotron-3.5-Bolt-E4B-GGUF/blob/main/NVIDIA-Nemotron-3.5-Bolt-E4B.Q5_K_M.gguf) | High quality, *recommended*. |
| NVIDIA-Nemotron-3.5-Bolt-E4B.Q5_K_S.gguf | Q5_K_S | 5.69 GB | [Link](https://huggingface.co/prithivMLmods/NVIDIA-Nemotron-3.5-Bolt-E4B-GGUF/blob/main/NVIDIA-Nemotron-3.5-Bolt-E4B.Q5_K_S.gguf) | High quality, *recommended*. |
| NVIDIA-Nemotron-3.5-Bolt-E4B.Q6_K.gguf | Q6_K | 6.22 GB | [Link](https://huggingface.co/prithivMLmods/NVIDIA-Nemotron-3.5-Bolt-E4B-GGUF/blob/main/NVIDIA-Nemotron-3.5-Bolt-E4B.Q6_K.gguf) | Very high quality, near perfect, *recommended*. |
| NVIDIA-Nemotron-3.5-Bolt-E4B.Q8_0.gguf | Q8_0 | 8.01 GB | [Link](https://huggingface.co/prithivMLmods/NVIDIA-Nemotron-3.5-Bolt-E4B-GGUF/blob/main/NVIDIA-Nemotron-3.5-Bolt-E4B.Q8_0.gguf) | Extremely high quality, generally unneeded but max available quant. |
| NVIDIA-Nemotron-3.5-Bolt-E4B.mmproj-bf16.gguf | mmproj-bf16 | 992 MB | [Link](https://huggingface.co/prithivMLmods/NVIDIA-Nemotron-3.5-Bolt-E4B-GGUF/blob/main/NVIDIA-Nemotron-3.5-Bolt-E4B.mmproj-bf16.gguf) | Multimodal projection file in BF16 format. Used for vision/language models. |

## Q4_K_M Test Run

Tested `NVIDIA-Nemotron-3.5-Bolt-E4B.Q4_K_M.gguf` on an NVIDIA RTX PRO 6000 Blackwell Server Edition GPU with `96 GB` of VRAM, using `llama-cli` with full GPU offloading.

### Performance Metrics

| Metric | Value |
| --- | --- |
| Average Prompt Processing Speed | 434.22 tokens/s |
| Average Generation Speed | 189.54 tokens/s |
| Total Wall Time | 44.1 seconds |
| Context Length | 8,192 tokens |
| KV Cache (K) | `q8_0` |
| GPU | NVIDIA RTX PRO 6000 Blackwell Server Edition |
| GPU VRAM Capacity | 96 GB |
| Peak GPU VRAM Usage | 3.76 GiB |
| Peak GPU Utilization | 85% |
| GPU Layers Offloaded | 99 (`-ngl 99`) |
| Random Seed | 42 |
| Speculative Decoding | Disabled |
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
  -m /path/to/models/NVIDIA-Nemotron-3.5-Bolt-E4B.Q4_K_M.gguf \
  -ngl 99 \
  -c 8192 \
  --cache-type-k q8_0 \
  --seed 42 \
  -n 8192 \
  -st \
  -p "Your prompt here"
```

*Performance results reflect this specific hardware and inference configuration. Actual throughput may vary depending on the prompt, model, software build, and runtime settings.*

## llama.cpp

LLM inference in C/C++ — https://github.com/ggml-org/llama.cpp

---

## Snapshots (5)

![download](https://cdn-uploads.huggingface.co/production/uploads/65bb837dbfb878f46c77de4c/aPx4Hf_v0uiKy8GoGTDAK.png)
![download (1)](https://cdn-uploads.huggingface.co/production/uploads/65bb837dbfb878f46c77de4c/yJ90VUSTl2-V9IwHX2z8N.png)
![download (2)](https://cdn-uploads.huggingface.co/production/uploads/65bb837dbfb878f46c77de4c/DtjWWKorwjAfmlGFO9esV.png)
![download (3)](https://cdn-uploads.huggingface.co/production/uploads/65bb837dbfb878f46c77de4c/V1YmgS8LNk-HekGhNhTvs.png)
![download (4)](https://cdn-uploads.huggingface.co/production/uploads/65bb837dbfb878f46c77de4c/1kY0EF3zOh-v3tRLeIecc.png)

---

Quantized using llama.cpp by [prithivMLmods](https://huggingface.co/prithivMLmods)