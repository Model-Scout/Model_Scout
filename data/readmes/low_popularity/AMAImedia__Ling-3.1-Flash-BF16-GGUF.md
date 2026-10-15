---
license: mit
base_model:
- inclusionAI/Ling-3.1-flash
- AtomicChat/Ling-3.1-flash-GGUF
pipeline_tag: text-generation
library_name: transformers
tags:
- gguf
- moe
- long-context
language:
- en
- ru
- kk
- zh
- ja
- vi
- af
- am
- ar
- as
- ast
- az
- be
- bg
- bn
- bs
- ca
- ceb
- ckb
- cs
- cy
- da
- de
- el
- es
- et
- eu
- fa
- ff
- fi
- fil
- fr
- ga
- gl
- gn
- gu
- ha
- he
- hi
- hr
- hu
- hy
- id
- ig
- is
- it
- jv
- ka
- kam
- kea
- km
- kmr
- kn
- ko
- ky
- lb
- lg
- ln
- lo
- lt
- luo
- lv
- mi
- mk
- ml
- mn
- mr
- ms
- mt
- mvy
- my
- ne
- nl
- 'no'
- nso
- ny
- oc
- om
- or
- pa
- pl
- ps
- pt
- qxp
- ro
- rw
- sd
- sk
- skr
- sl
- sn
- so
- sr
- sv
- sw
- ta
- te
- tg
- th
- ti
- tk
- tr
- ug
- uk
- umb
- ur
- uz
- wo
- xh
- yo
- yue
- zu
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
 
- **Original repository:** [inclusionAI/Ling-3.1-flash](https://huggingface.co/inclusionAI/Ling-3.1-flash)
- **GGUF:** [AtomicChat/Ling-3.1-flash-GGUF](https://huggingface.co/AtomicChat/Ling-3.1-flash-GGUF)

---
<p align="center">
    <img src="https://mdn.alipayobjects.com/huamei_qa8qxu/afts/img/A*4QxcQrBlTiAAAAAAQXAAAAgAemJ7AQ/original" width="100"/>
</p>
<p align="center">🤗 <a href="https://huggingface.co/inclusionAI/Ling-3.1-flash">Hugging Face</a>&nbsp;&nbsp; | &nbsp;&nbsp;🤖 <a href="https://modelscope.cn/organization/inclusionAI">ModelScope </a>&nbsp;&nbsp; | &nbsp;&nbsp;🐙 <a href="https://openrouter.ai/inclusionai/ling-3.1-flash">OpenRouter </a>&nbsp;&nbsp;</p>

<p align="center"><img src="https://huggingface.co/AMAImedia/Ling-3.1-Flash-BF16-GGUF/resolve/main/test.jpeg" alt="test.jpeg"/></p>

We're introducing **Ling-3.1-flash**, an upgraded native hybrid reasoning model designed for complex, real-world tasks. With **560B** total parameters, **25B** active parameters per token, and a **1M-token context window**, Ling-3.1-flash builds upon Ling-3.0-flash with improvements in architecture, performance on real-world capabilities.

With stronger real-world capabilities, Ling-3.1-flash shows improvements across a range of real-world tasks, including general-purpose agents, search, office productivity, and software engineering. It demonstrates strong performance on benchmarks such as **GDPVal-AA V2.1, HealthBench Professional, FrontierSWE, and Terminal-Bench 4.0**, covering office tasks, healthcare, software engineering, and terminal-based tool use. The model also shows improvements in specialized domains such as finance and materials science.

<img src="https://huggingface.co/AMAImedia/Ling-3.1-Flash-BF16-GGUF/blob/main/test.jpeg" width="4606" alt="" title="" crop="0,0,1,1" id="u912c619f" class="ne-image">

## Model Overview
The model summary information and architecture diagram are as follows:

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



<img src="https://intranetproxy.alipay.com/skylark/lark/0/2026/png/23157180/1791966963600-8408d222-3dc1-43c6-87af-f4f905a681db.png" width="599" alt="" title="" crop="0,0,1,1" id="uf3580cdc" class="ne-image">

## Evaluation
We have conducted a comprehensive evaluation of Ling-3.1-flash across multiple authoritative benchmarks. **Ling-3.1-flash** performs strongly on representative coding/agentic benchmarks including **Terminal-Bench 4.0, SWE-bench Pro, FrontierSWE, GDPVal-AA V2.1, Automationbench, MCP-Atlas**,  **SkillsBench, etc**. In practice, Ling-3.1-flash delivers a strong user experience across frameworks including **Claude Code**,** Kilo Code**,** Qwen Code**,** Hermes Agent**,** **and** OpenClaw**, etc. Beyond agentic tasks, Ling-3.1-flash performs strongly on real-world tasks across **STEM, healthcare, and finance**. 

We also introduce **LingCode**, a harness built on the open-source coding agent Pi, and enhanced to support complex, long-horizon coding tasks that run for hours, involve hundreds of rounds of tool calls, and require repeated context compaction. LingCode delivers significant performance gains on some coding agent tasks, and we are considering open-sourcing it in the future.

<img src="https://intranetproxy.alipay.com/skylark/lark/0/2026/png/202156655/1791988674787-5f49370c-0853-4940-96ea-9f1e4ff20d57.png" width="2481.7499260380887" alt="" title="" crop="0,0,1,1" id="u5ec842ae" class="ne-image">

## Quickstart
#### SGLang (Recommended)

The day-0 SGLang image includes Ling-3.1-flash support, MTP (NEXTN) speculative decoding, and the Hopper decode optimizations:

```bash
docker pull lmsysorg/sglang:dev-ling-3.1-flash
```

##### Run Inference

**Server** (8x H200, TP8 + EP8):

```bash
docker run --gpus all --network host --ipc=host --rm \
  lmsysorg/sglang:dev-ling-3.1-flash \
  python3 -m sglang.launch_server \
    --model-path inclusionAI/Ling-3.1-flash \
    --tp 8 --ep 8 \
    --speculative-algorithm NEXTN \
    --host 0.0.0.0 --port 30000
```

On 4x GB300, use `--tp 4 --ep 4` instead. Hopper decode optimizations (optional, ~10% faster batch-1 decode) can be enabled with `SGLANG_ENABLE_FP8_BLOCK_GEMV=1` and `SGLANG_ENABLE_FUSED_KDA_OUTPUT_QUANT=1`.

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

#### vLLM
##### Environment Preparation
```bash
pip install uv

uv venv ~/my_ling_env

source ~/my_ling_env/bin/activate

git clone -b vllm https://github.com/vllm-project/vllm.git

cd vllm

VLLM_USE_PRECOMPILED=1 uv pip install --editable . --torch-backend=auto
```

#### Run inference
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
It is recommended to use the sampling params (temperature=1.0, top_p=0.95, top_k=20) and turn on enable_thinkingfor better performance.

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

## Training content summary

The public training-content summary identifying **Ling-3.1-flash** is available below. Please refer to the document for its covered model versions, training-content scope, summary version, and update date.

- [Training-content summary (PDF)](https://huggingface.co/inclusionAI/AI-Transparency/resolve/main/Ling-3.1_TDS-Summary.pdf)
- [Training-content documentation index](https://huggingface.co/inclusionAI/AI-Transparency)

This summary concerns training-content disclosure; it does not replace the model’s technical documentation, usage terms, or license.



# How to Run Ling 3.1 flash Locally
<p style="margin-top: 0; margin-bottom: 0;">
  <em>GGUF builds of inclusionAI's Ling 3.1 flash with our own importance matrix. The <a href="https://huggingface.co/datasets/AtomicChat/calib-corpora">calibration corpora</a> behind our builds are public.</em>
</p>
<div style="display: flex; gap: 8px; align-items: center; margin-top: 10px; margin-bottom: 10px;">
  <a href="https://atomic.chat/?utm_source=huggingface&utm_medium=referral&utm_campaign=hf_ling_3_1_flash&utm_content=btn_atomic"><img src="https://huggingface.co/AtomicChat/Qwen3.8-27B-GGUF/resolve/main/btn_atomic.png" width="162" alt="Atomic Chat"></a>
  <a href="https://discord.gg/8wGSsvmg4V"><img src="https://huggingface.co/AtomicChat/Qwen3.8-27B-GGUF/resolve/main/btn_discord.png" width="119" alt="Discord"></a>
  <a href="https://github.com/AtomicBot-ai/Atomic-Chat"><img src="https://huggingface.co/AtomicChat/Qwen3.8-27B-GGUF/resolve/main/btn_github.png" width="115" alt="GitHub"></a>
</div>
<ul style="margin: 0 0 12px 0;">
  <li>Runs in llama.cpp build b11571 or newer.</li>
  <li>Day-one upload: more files and the measurements (KL divergence and top-1 against the BF16 model) land on this card today.</li>
</ul>
<hr style="margin: 0 0 16px 0;">

## Pick a file

| File | Size on disk | KL divergence | top-1 | Status |
|---|---:|---:|---:|---|
| `AD-Q8_0` | 600.8 GB | 0.00503 | 97.88% | available |
| `AD-Q6_K` | 478.0 GB | 0.00557 | 97.72% | available |
| `AD-Q5_K_M` | 400.2 GB | measuring | measuring | available |
| `AD-Q4_K_M` | 354.4 GB | 0.01114 | 96.86% | available |
| `AD-IQ4_XS` | 337.8 GB | measuring | measuring | uploading today |
| `AD-IQ4_XXS` | 311.4 GB | measuring | measuring | available |
| `AD-IQ3_M` | 277.1 GB | measuring | measuring | available |
| `AD-IQ3_XXS` | 256.4 GB | 0.03436 | 94.48% | available |
| `AD-IQ2_M` | 218.1 GB | measuring | measuring | available |
| `AD-IQ2_XS` | 198.2 GB | measuring | measuring | uploading today |
| `AD-IQ2_XXS` | 174.1 GB | measuring | measuring | uploading today |
| `AD-IQ1_M` | 160.9 GB | measuring | measuring | available, experimental |
| `AD-IQ1_S` | 141.8 GB | measuring | measuring | available, experimental |

`KL divergence` is how far the quantized model's predictions drift from the
BF16 model's. Lower is better, and zero means identical. `top-1` is how often it
picks the same next token the BF16 model would have picked. Both are measured
on held-out text; how is at the bottom. Rows that say "measuring" fill in today.

`AD-` marks an **Atomic Dynamic** layout: the routed experts (97% of the weights)
take the low-bit type, while attention, the shared expert, the router and the
dense layers stay at q8_0 or higher. The file name is the type of the experts'
gate and up projections; their down projections, and all experts of the last
five blocks, get a step more.

## How much memory it needs

The file has to fit, plus a little for the context. Context is cheap on this
model: 63 of its 72 layers use linear attention with a fixed-size state, and
only 9 keep a compressed attention cache. That is about 0.5 GB per conversation
plus about 10 KB per token.

| Total memory (VRAM or unified) | File |
|---|---|
| 192 GB | `AD-IQ1_M` |
| 256 GB | `AD-IQ2_M` |
| 384 GB | `AD-Q4_K_M` |
| 512 GB | `AD-Q5_K_M` |
| 640 GB | `AD-Q8_0` |

On a Mac, raise the GPU memory limit first, for example
`sudo sysctl iogpu.wired_limit_mb=240000` on a 256 GB machine.

## Running it

```bash
llama-server -hf AtomicChat/Ling-3.1-flash-GGUF:AD-Q4_K_M -ngl 99 -c 32768 --jinja
```

Each file sits in a folder of its name, split into shards of up to 45 GB; point
llama.cpp at the first shard and it loads the rest:

```bash
hf download AtomicChat/Ling-3.1-flash-GGUF --include "AD-Q4_K_M/*" --local-dir .
llama-server -m AD-Q4_K_M/Ling-3.1-flash-AD-Q4_K_M-00001-of-00009.gguf -ngl 99 -c 32768 --jinja
```

The chat template is inside every file. Thinking is on by default; put
`detailed thinking off` in the system prompt to turn it off.

## How we measured

Reference: BF16 weights converted from inclusionAI's FP8 release and run
unquantized (perplexity 2.3590 on the held-out set). Converting FP8 to BF16
rounds each weight once, far below what Q8_0 adds.

Held-out text: `eval_neutral` from our
[calibration dataset](https://huggingface.co/datasets/AtomicChat/calib-corpora),
never used for calibration, 144 chunks of 4096 tokens. Metric: per-token KL
divergence of each file's predictions against the reference, plus top-1
agreement. Hardware: 8x A100-SXM4-80GB, llama.cpp 097cf33d9 for every file.

The importance matrix is the one we computed on 5.5M tokens of the
`ling3-moe` corpus (thinking on and off, tool calls, 30 languages, code, long
documents up to 32k tokens), rendered through this model's own chat template.

## Model details

Mixture of experts: 512 routed experts in each of 68 layers (the first 4 layers
are dense), 8 routed plus 1 shared expert per token, about 24B parameters active
of 564B. Hybrid attention: 63 Kimi Delta Attention (linear) layers and 9
multi-head latent attention layers. Hidden size 4096, vocabulary 157,184,
context 262,144. The multi-token-prediction head of the release is not
included.

Built from inclusionAI's FP8 release (revision `b426279f`), converted to BF16
and quantized with llama.cpp b11571 (097cf33d9); needs llama.cpp with
`bailingmoe3` support.

## License and credits

MIT, as the original. Base model **Ling 3.1 flash** by
[inclusionAI](https://huggingface.co/inclusionAI). Quantization and evaluation
by **AtomicChat**.

