---
license: apache-2.0
tags:
- uncensored
- qwen3.6
- moe
- gguf
- vision
- multimodal
- genesis
language:
- en
- zh
- multilingual
pipeline_tag: image-text-to-text
base_model:
- HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive
---

# 🌟 Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive -> Genesis

> ⚡ [https://web.tribute.tg/d/KIH](https://web.tribute.tg/d/KIH) ⚡ If you like this Genesis LLM release you can [**donate**](https://web.tribute.tg/d/KIH) to me via [@Tribute](https://t.me/tribute) bot in Telegram messenger or [Hipolink](https://hipolink.net/luffythefox) and support future Genesis LLM development.

> ⚡ Also for donations I accept cryptocurrency `GRAM` via TON network from Telegram messenger. Here my wallet: `UQD3LAmWwEh8D3yMFjycgDQzAw_xgskifioMdlhE9LxGNUrq`

> ⚡ **Why Genesis project exists?** During training, **ALL** models don't just learn knowledge - they also accumulate random noise in their tensors. This noise builds up and creates something I call the **Noise Gate** - a fundamental barrier that stops LLM models from learning further and makes them unstable, verbose, and prone to hallucinations. My approach reduces this noise. It repairs the signal in tensors without touching the learned knowledge and gradient using [Marchenko–Pastur distribution](https://en.wikipedia.org/wiki/Marchenko%E2%80%93Pastur_distribution) as a core criteria. The result is a model that consistent in performance, context clarity and following instructions, because it's no longer fighting its own internal chaos.

> **What is Genesis?** Genesis is post training data regeneration and calibrarion algorythm for neural networks (LLM) in GGUF format that I made with AI help during almost half a year of development. It's optimized, architecture independent, works with any model in GGUF format and based on mathematical statistics. I don't train or finetune models, I repair **purity of signal** in them instead on Google Collab Free on Tesla T4 GPU via Python based on how models learns information. On first stage I scan ssm_conv1d tensors in model, they handle long context memory. I repair balance between heads in them. On second stage, I scan blocks in model via chunks via 3 parameters and pick best one that fits to weight distribution in tensor. Best picked chunk replaces zero chunks in broken tensor without touching learned structure in model. On third stage I scan model and detect noise in tensors via custom SVD. During scanning I exclude token_embd.weight, output.weight, 1D tensors, bias and norms. Then I reduce training noise in tensors via custom SVD based on [Marchenko–Pastur law](https://en.wikipedia.org/wiki/Marchenko%E2%80%93Pastur_distribution) with preserved training data, 99% of siginal and learned gradient.

## Any questions?

> Contact: luffythefox@mail.ru, azakharchenko92@gmail.com

> My Telegram: @LuffyTheFox

Model is based on [HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive) base. **0/465 refusals.**

Thanks to [HauhauCS](https://huggingface.co/HauhauCS) 

Tensor repair by me. Method: **Genesis**

> **[Join the Discord](https://discord.gg/SZ5vacTXYf)** for updates, roadmaps, projects, or just to chat.

**Links:**
- [Original uncensored model](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)
- [Quantization Script with Unsloth profiles support](https://pastebin.com/hXhcMJn9)

---

</details>

LLM models often have:

- **Saturated weights**: the model's activations are stuck, gradients vanish, outputs degrade.
- **Scale mismatches**: one layer's weights are 10× larger than its peers for no good reason.
- **Mean drift**: weight distributions shifted positive or negative, breaking symmetry assumptions.
- **Zero blocks**: zero blocks corrupt the signal, turning training into noise amplification.
- **Training Noise:** training noise increase randomness and ruins model output quality.

My approach fixes all of that without retraining - pure numerical surgery on the raw bytes of the file.

**Quantization script available here: https://pastebin.com/hXhcMJn9**

Feel free to do your own quants if you want.

## Recommended Settings for best perfomance on APEX quant

Chat template: [chat_template.jinja](https://huggingface.co/LuffyTheFox/Qwen3.6-35B-A3B-Uncensored-Genesis-Hermes-V7-GGUF/raw/main/chat_template.jinja) thanks to [froggeric](https://huggingface.co/froggeric) and [qweefchief](https://huggingface.co/qweefchief)

Set K Cache Quantization Type and V Cache Quantization Type to F16. 

Set Number of layers for which to force MoE weights onto CPU to 40.

Set GPU offload to maximum. Set number of active experts to 8.

For best model stability and first experience I recommend starting from this string in your System Prompt with enabled thinking and nothing else: 

`You are Qwen, a large language model developed by Alibaba Group's Tongyi Lab. You are a helpful assistant.`

If you want to bring more creativity to model use this System Prompt [System_Prompt_Creative.txt](https://huggingface.co/LuffyTheFox/Qwen3.6-35B-A3B-Uncensored-Genesis-Hermes-V5-GGUF/raw/main/System_Prompt_Creative.txt)

**Thinking mode (coding):**
- Coding/precise tasks: `temperature=0.6, top_p=0.95, top_k=20, min_p=0.0, seed=42, presence_penalty=disabled, repeat_penalty=disabled`
- General: `temperature=0.95, top_p=0.95, top_k=20, min_p=0.0, seed=42, presence_penalty=disabled, repeat_penalty=disabled`

**Non Thinking mode (creative):**
- General: `temperature=0.7, top_p=0.8, top_k=20, min_p=0.0, seed=42, presence_penalty=disabled, repeat_penalty=disabled`
- General: `temperature=0.95, top_p=disabled, top_k=20, min_p=disabled, seed=42, presence_penalty=disabled, repeat_penalty=disabled`

## Usage

**Ready to use.** Recommended quant: **APEX**

For 8 and 12 GB GPUs I highly recommend to use **APEX Compact** quant.

Recommended LM Studio runtime: [link to discussion](https://huggingface.co/LuffyTheFox/Qwen3.6-35B-A3B-Uncensored-Genesis-Hermes-V5-GGUF/discussions/12)

**Important:**
- Keep at least 128K context to preserve thinking capabilities
- Use `--jinja` flag with llama.cpp for proper chat template handling
- Vision support requires the `mmproj` file alongside the main GGUF

---

## Specs

- 35B total parameters, ~3B active per forward pass (MoE)
- 256 experts, 8 routed + 1 shared per token
- Hybrid architecture: Gated DeltaNet linear attention + full softmax attention (3:1 ratio)
- 40 layers, pattern: 10 × (3 × DeltaNet-MoE + 1 × Attention-MoE)
- 262K native context (extendable to 1M with YaRN)
- Natively multimodal (text, image, video)
- 248K vocabulary, 201 languages
- Base model. [HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive](https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive)

---

## Compatibility

Works with llama.cpp, LM Studio, koboldcpp, and other GGUF-compatible runtimes.