---
license: mit
base_model:
- inclusionAI/Ling-3.1-flash-1019
- AtomicChat/Ling-3.1-flash-1019-GGUF
pipeline_tag: text-generation
library_name: transformers
tags:
- gguf
- moe
- long-context
language:
- zh
- en
- ru
- vi
- ja
- hi
- es
- fr
- de
- pt
- it
- ar
- ko
- th
- id
- ms
- bn
- tr
- pl
- uk
- nl
- cs
- sv
- ro
- el
- he
- fa
- ur
- kk
- uz
---

<!-- apex-banner -->
<div style="background-color: #f59e0b; color: white; padding: 20px; border-radius: 10px; text-align: center; margin: 20px 0;">
<h2 style="color: white; margin: 0 0 10px 0;">⚡ Each donation funds the next large quant.</h2>
<p style="font-size: 16px; margin: 0 0 15px 0;">I host free GGUF or MoE quants as independent research.<br>
Local hardware: <b>Mechrevo Kuangshi GM7AG0M</b> — RTX 3060 Laptop 6GB GDDR6, 64GB DDR5, i7-12700H (14C/20T, 4.7GHz), Windows 11, Samsung 990 Pro.<br>
Good for imatrix and 0.6–35B-class work in RAM. <b>9B+ and searches need rented H200/Blackwell</b>, typically $100 per quant.</p>
<p style="font-size: 20px; margin: 0;">
<a href="https://boosty.to/amaimediacom" style="color: white; text-decoration: underline;">🎉 Boosty🦄</a>  | 
<a href="https://donatex.gg/widgets/donation-goal/89bc59e8-b69c-467a-9aa0-5e1c3f8842d6" style="color: white; text-decoration: underline;">☕ Buy Me a Coffee🦄</a>  | 
<a href="https://www.donationalerts.com/r/djbionicl" style="color: white; text-decoration: underline;">⭐ DonationAlerts🦄</a>
</p>
<p style="font-size: 14px; margin: 10px 0 0 0; opacity: 0.9;">💚 Thanks to Hugging Face for extra storage.🦄</p>
</div>

---

## NOESIS / AMAImedia

Released as part of the NOESIS Professional Multilingual Dubbing Automation Platform 
(framework: DHCF-FNO — Deterministic Hybrid Control Framework for Frozen Neural Operators)

- **Founder:** Ilia Bolotnikov
- **Organization:** AMAImedia.com
- **X (Twitter):** [@AMAImediacom](https://x.com/AMAImediacom)
- **LinkedIn:** [Ilia Bolotnikov](https://www.linkedin.com/in/ilia-bolotnikov)
- **Telegram:** [@djbionicl](https://t.me/djbionicl)
- **Release date:** 2026-10-14

## AMAImedia
 
- **Original repository:** [inclusionAI/Ling-3.1-flash-1019](https://huggingface.co/inclusionAI/Ling-3.1-flash-1019)
- **GGUF:** [AtomicChat/Ling-3.1-flash-1019-GGUF](https://huggingface.co/AtomicChat/Ling-3.1-flash-1019-GGUF)

---
<p align="center">
    <img src="https://mdn.alipayobjects.com/huamei_qa8qxu/afts/img/A*4QxcQrBlTiAAAAAAQXAAAAgAemJ7AQ/original" width="100"/>
</p>
<p align="center">🤗 <a href="https://huggingface.co/inclusionAI">Hugging Face</a>&nbsp;&nbsp; | &nbsp;&nbsp;🤖 <a href="https://modelscope.cn/organization/inclusionAI">ModelScope</a>&nbsp;&nbsp; | &nbsp;&nbsp;🐙 <a href="https://openrouter.ai/inclusionai/ling-3.1-flash">OpenRouter</a>&nbsp;&nbsp;</p>

## Introduction
We introduce **Ling-3.1-flash-1019**, an upgraded version of [Ling-3.1-flash](https://huggingface.co/inclusionAI/Ling-3.1-flash), with **560B** total parameters, **25B** active parameters per token, and a **1M-token context window**. With further post-training optimizations, **Ling-3.1-flash-1019** demonstrates significant improvements in reasoning and real-world agentic capabilities. Its **AA-Briefcase** score rises from approximately 1400 to **1524 Elo**, while performance on **AutomationBench-AA** increases from 62% to **68%**. The model also makes gains on scientific benchmarks, including **CritPt** (18% → **26%**) and **SciCode** (54% → **57%**). Overall, it scores **44** on the **Artificial Analysis Intelligence Index v4.3.2**, up from 41 for its predecessor. These gains highlight the model's improved capabilities in complex reasoning, multi-step task execution, and agentic workflows across diverse real-world scenarios.

![AA-44](https://cdn-uploads.huggingface.co/production/uploads/65d6aba7dee9f442f8ea7ded/aZ4wSjB4OCgUFnyYINngi.png)

## Model Overview
The table and diagram below summarize the model’s specifications and architecture.

| Architecture | Hybrid-linear MoE |
| --- | --- |
| Parameter Scale | Total 560B, Activated 25B |
| Transformer Layers | 63 KDA + 9 Gated MLA (7:1) |
| Number of Dense Layers | 4 |
| Number of Routed Experts | 512 |
| Number of Shared Experts | 1 |
| Number of Activated Experts | 8 |
| Attention Heads | 64 |
| Hidden Size | 4096 |
| Expert Intermediate Size | 1280 |
| Dense Intermediate Size | 10240 |
| Vocabulary Size | 157184 |

![image](https://cdn-uploads.huggingface.co/production/uploads/678143d4ddb1f1ce16daca8e/qwmfVu_K08auI7R_ijbIX.png)

## Quickstart
### SGLang (Recommended)

The day-0 SGLang image includes Ling-3.1-flash support, MTP (NEXTN) speculative decoding, and Hopper decode optimizations:

```bash
docker pull lmsysorg/sglang:dev-ling-3.1-flash
```

#### Run Inference

**Server** (8 × H200, TP8 + EP8):

```bash
docker run --gpus all --network host --ipc=host --rm \
  lmsysorg/sglang:dev-ling-3.1-flash \
  python3 -m sglang.launch_server \
    --model-path inclusionAI/Ling-3.1-flash \
    --tp 8 --ep 8 \
    --speculative-algorithm NEXTN \
    --host 0.0.0.0 --port 30000
```

On 4 × GB300, use `--tp 4 --ep 4` instead. Hopper decode optimizations (optional, ~10% faster batch-1 decode) can be enabled with `SGLANG_ENABLE_FP8_BLOCK_GEMV=1` and `SGLANG_ENABLE_FUSED_KDA_OUTPUT_QUANT=1`.

**Client**

```bash
curl -s http://localhost:30000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"model": "Ling-3.1-flash",
       "messages": [{"role": "user", "content": "What is the capital of France?"}],
       "chat_template_kwargs": {"enable_thinking": true},
       "stream": true,
       "temperature": 1.0,
       "top_k": 20,
       "top_p": 0.95}'
```

Verified recipes for H200, GB300, H800, H100, and B200, plus HiCache (Mooncake L3), reasoning on/off, tool calling, and measured accuracy/speed numbers, are in the [SGLang Ling-3.1-flash cookbook](https://docs.sglang.io/cookbook/autoregressive/InclusionAI/Ling-3.1-flash).

### vLLM
#### Environment Preparation
```bash
pip install uv

uv venv ~/my_ling_env

source ~/my_ling_env/bin/activate

git clone -b vllm https://github.com/vllm-project/vllm.git

cd vllm

VLLM_USE_PRECOMPILED=1 uv pip install --editable . --torch-backend=auto
```

#### Run Inference
**Server**

```bash
vllm serve "$MODEL_PATH" \
    --port "$PORT" \
    --trust-remote-code \
    --served-model-name auto \
    --tensor-parallel-size 8 \
    --gpu-memory-utilization 0.85 \
    --enable-prefix-caching \
    --enable-expert-parallel \
    --mamba-cache-mode align \
    --enable-auto-tool-choice \
    --tool-call-parser ling3 \
    --reasoning-parser ling3 \
    --speculative-config '{"method":"mtp","num_speculative_tokens":3}'
```

**Client**  
It is recommended to use the sampling parameters (`temperature=1.0`, `top_p=0.95`, `top_k=20`) and set `enable_thinking` to `true` for better performance.

```bash
curl -s http://${MASTER_IP}:${PORT}/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"model": "auto", 
       "messages": [{"role": "user", "content": "What is the capital of France?"}],
       "chat_template_kwargs": {"enable_thinking": true},
       "stream": true,
       "temperature": 1.0, 
       "top_k": 20,
       "top_p": 0.95}'
```

<!-- TDS-LINKS:START -->
## Training Content Summary

The public training-content summary identifying **Ling-3.1-flash** is available below. Please refer to the document for its covered model versions, training-content scope, summary version, and update date.

- [Training-content summary (PDF)](https://huggingface.co/inclusionAI/AI-Transparency/resolve/main/Ling-3.1_TDS-Summary.pdf)
- [Training-content documentation index](https://huggingface.co/inclusionAI/AI-Transparency)

This summary concerns training-content disclosure; 
it does not replace the model’s technical documentation, usage terms, or license.


---
base_model: inclusionAI/Ling-3.1-flash-1019
base_model_relation: quantized
quantized_by: AtomicChat
pipeline_tag: text-generation
library_name: gguf
license: mit
tags:
- gguf
- llama.cpp
- ling
- inclusionai
- moe
- imatrix
- quantized
- conversational
- mtp
- atomic-chat
---

# How to Run Ling 3.1 flash 1019 Locally
<p style="margin-top: 0; margin-bottom: 0;">
  <em>GGUF builds of inclusionAI's Ling 3.1 flash 1019, with the multi-token prediction head inside. The <a href="https://huggingface.co/datasets/AtomicChat/calib-corpora">calibration corpora</a> behind our builds are public.</em>
</p>
<div style="display: flex; gap: 8px; align-items: center; margin-top: 10px; margin-bottom: 10px;">
  <a href="https://atomic.chat/?utm_source=huggingface&utm_medium=referral&utm_campaign=hf_ling_3_1_flash_1019&utm_content=btn_atomic"><img src="https://huggingface.co/AtomicChat/Qwen3.8-27B-GGUF/resolve/main/btn_atomic.png" width="162" alt="Atomic Chat"></a>
  <a href="https://discord.gg/8wGSsvmg4V"><img src="https://huggingface.co/AtomicChat/Qwen3.8-27B-GGUF/resolve/main/btn_discord.png" width="119" alt="Discord"></a>
  <a href="https://github.com/AtomicBot-ai/Atomic-Chat"><img src="https://huggingface.co/AtomicChat/Qwen3.8-27B-GGUF/resolve/main/btn_github.png" width="115" alt="GitHub"></a>
  <a href="https://x.com/atomic_chat_hq"><img src="https://huggingface.co/AtomicChat/Qwen3.8-27B-GGUF/resolve/main/btn_x.png" width="108" alt="X"></a>
</div>
<ul style="margin: 0 0 12px 0;">
  <li>Built by the team behind <a href="https://atomic.chat/?utm_source=huggingface&utm_medium=referral&utm_campaign=hf_ling_3_1_flash_1019&utm_content=bullet_app">Atomic Chat</a>, the app that runs open-weight models locally and offline.</li>
  <li>Runs in llama.cpp build b11571 or newer.</li>
  <li>The multi-token prediction head is inside the file: add <code>--spec-type draft-mtp</code> to use it. In our check 57 to 69% of its drafted tokens were accepted.</li>
</ul>
<hr style="margin: 0 0 16px 0;">

## Pick a file

| File | Size on disk | Total memory (VRAM or unified) |
|---|---:|---|
| `AD-IQ2_M` | 226.8 GB | 256 GB |

`AD-` marks an **Atomic Dynamic** layout: the routed experts (97% of the weights)
take the low-bit type, while attention, the shared expert, the router, the dense
layers and the multi-token prediction block stay at q8_0 or higher. The file
name is the type of the experts' gate and up projections; their down
projections, and all experts of the last five blocks, get a step more.

This file has not been measured against the BF16 model. The same layout on the
previous checkpoint, with its KL divergence and top-1 agreement, and larger
files are in
[AtomicChat/Ling-3.1-flash-GGUF](https://huggingface.co/AtomicChat/Ling-3.1-flash-GGUF).

## How much memory it needs

The file has to fit, plus a little for the context. Context is cheap on this
model: 63 of its 72 layers use linear attention with a fixed-size state, and
only 9 keep a compressed attention cache. That is about 0.5 GB per conversation
plus about 10 KB per token.

On a Mac, raise the GPU memory limit first, for example
`sudo sysctl iogpu.wired_limit_mb=240000` on a 256 GB machine.

## Running it

```bash
llama-server -hf AtomicChat/Ling-3.1-flash-1019-GGUF:AD-IQ2_M -ngl 99 -c 32768 --jinja
```

The file is split into six shards of up to 45 GB. To download them yourself,
take all six and point llama.cpp at the first:

```bash
hf download AtomicChat/Ling-3.1-flash-1019-GGUF --include "*AD-IQ2_M*" --local-dir .
llama-server -m Ling-3.1-flash-1019-AD-IQ2_M-00001-of-00006.gguf -ngl 99 -c 32768 --jinja
```

With the multi-token prediction head:

```bash
llama-server -hf AtomicChat/Ling-3.1-flash-1019-GGUF:AD-IQ2_M -ngl 99 -c 32768 --jinja --spec-type draft-mtp
```

The chat template is inside the file. Thinking is on by default. The template
switches it with `enable_thinking`, so a system prompt alone does not turn it
off; start the server with

```bash
llama-server -hf AtomicChat/Ling-3.1-flash-1019-GGUF:AD-IQ2_M -ngl 99 -c 32768 --jinja --chat-template-kwargs '{"enable_thinking": false}'
```

or send `"chat_template_kwargs": {"enable_thinking": false}` with a request.

## How we built it

From inclusionAI's FP8 release (revision `dddfee4b`), converted to BF16 and
quantized with llama.cpp b11571 (097cf33d9). Converting FP8 to BF16 rounds each
weight once, far below what Q8_0 adds. The file is 3.17 bits per weight on
average; we checked that it loads in llama-server and completes text and code.

The importance matrix is the one we computed for Ling 3.1 flash on 5.5M tokens
of the `ling3-moe` corpus (thinking on and off, tool calls, 30 languages, code,
long documents up to 32k tokens), rendered through the model's chat template.
Ling 3.1 flash 1019 has the same architecture, configuration and chat template;
we did not recompute the matrix for this checkpoint. The matrix and the layouts
are in
[AtomicChat/Ling-3.1-flash-1019-GGUF-metrics](https://huggingface.co/datasets/AtomicChat/Ling-3.1-flash-1019-GGUF-metrics).

## Model details

Mixture of experts: 512 routed experts in each of 68 layers (the first 4 layers
are dense), 8 routed plus 1 shared expert per token, about 24B parameters active
of 564B, plus an 8B multi-token prediction block. Hybrid attention: 63 Kimi
Delta Attention (linear) layers and 9 multi-head latent attention layers. Hidden
size 4096, vocabulary 157,184, context 262,144. Needs llama.cpp with
`bailingmoe3` support.

## License and credits

MIT, as the original. 
Base model **Ling 3.1 flash 1019** by [inclusionAI](https://huggingface.co/inclusionAI). 
Quantization by **AtomicChat**.
 