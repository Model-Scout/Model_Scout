---
license: apache-2.0
license_link: https://huggingface.co/Qwen/Qwen3.5-4B/blob/main/LICENSE
library_name: transformers
pipeline_tag: image-text-to-text
language:
- en
- zh
- ar
- de
- es
- fr
- it
- ja
- ko
- pt
- ru
- hi
- id
- th
- tr
- vi
tags:
- qwen
- qwen3.5
- qwen3.5-4b
- multimodal
- vision-language
- edge
- on-device
- agentic
- tool-calling
- heretic
- uncensored
- decensored
- abliterated
- ara
- reproducible
- gguf
- local-llm
base_model: Qwen/Qwen3.5-4B
---

# Qwen3.5-4B-heretic

<div align="center">
  <img src="https://photu.kashyalabanavli.site/racer-is-op.png" alt="RACER IS OP" width="100%">
</div>

<br>

> [!IMPORTANT]
> **The GGUF files here are text-only.** Qwen3.5-4B is a unified vision-language model, but
> `convert_hf_to_gguf.py` without `--mmproj` drops the vision tower. Only the
> 4,205,751,296-parameter language tower is in the GGUF; the 333,514,240-parameter vision
> encoder remains in the safetensors. Use the BF16 safetensors + `AutoProcessor` for images and
> video; use the GGUFs for text-only inference.

A decensored variant of [Qwen/Qwen3.5-4B](https://huggingface.co/Qwen/Qwen3.5-4B), produced with
[Heretic](https://github.com/p-e-w/heretic) **2.0.0.dev0** using **Arbitrary-Rank Ablation (ARA)**.
Qwen3.5-4B is Qwen's 4B hybrid vision-language model: 32 layers laid out as
8 x (3 gated DeltaNet layers + 1 gated-attention layer), 201 languages, 262K native context.
Only the language tower is edited (layers 15-27); the vision encoder is untouched.

**Who this is for:** text agents, tool use, multilingual chat and RAG on consumer GPUs, with
refusals removed. The base model is strong at instruction following and tool calls; the heretic
edit suppresses refusals. If you need image or video input, use the BF16 safetensors (the GGUFs are
text-only) and point the base card's `AutoModelForImageTextToText` example at this repo.

Refusals drop from **99/100 to 13/100** at a **KL divergence of 0.0081**. The text benchmarks are
unchanged within noise (MMLU 74.35 vs 74.29).

## Arbitrary-Rank Ablation parameters

Trial 162 of a 200-trial Heretic 2.0 ARA run (seed `982272333`).

| Parameter | Value |
| :-------- | :---: |
| **start_layer_index** | 15 |
| **end_layer_index** | 27 |
| **preserve_good_behavior_weight** | 0.9900 |
| **steer_bad_behavior_weight** | 0.0001 |
| **overcorrect_relative_weight** | 0.8230 |
| **neighbor_count** | 15 |

## Performance

| Metric | This model | Original model ([Qwen/Qwen3.5-4B](https://huggingface.co/Qwen/Qwen3.5-4B)) |
| :----- | :--------: | :---------------------------: |
| **Refusals** | 13/100 | 99/100 |
| **KL divergence** | 0.0081 | 0 *(by definition)* |

86 of the 99 refusals clear. KL 0.0081 is a fairly tight edit, so expect limited drift in phrasing
and format.

### Benchmarks

Measured on this checkpoint and on the original model in the same environment (`lm-eval`):

| Benchmark | This model | Original model | stderr (this / original) |
| :-------- | :--------: | :------------: | :---: |
| **MMLU** | 74.35% | 74.29% | 0.35 / 0.35 pp |
| **PIQA** | 77.48% | 77.37% | 0.97 / 0.98 pp |
| **PIQA (norm)** | 77.97% | 78.29% | 0.97 / 0.96 pp |
| **WinoGrande** | 69.22% | 69.77% | 1.30 / 1.29 pp |

All deltas are within roughly one standard error; the largest is WinoGrande at -0.55 pp. These are
text benchmarks and do not exercise the vision tower. Note the base's own benchmark table is
published as an image, so this card quotes only the numbers re-run here.

## Why ARA instead of directional ablation

Directional ablation finds one refusal direction and orthogonalizes attention/MLP outputs against
it. ARA learns a low-rank subspace over a layer range and blends a "preserve good behaviour" and
"steer bad behaviour" objective. Here it kept 99% of the preserve objective over layers 15-27 and
still removed 86 of 99 refusals. See the [Heretic repo](https://github.com/p-e-w/heretic) for the
method.

## Files

### Safetensors

| File | Size |
|---|---|
| `model-00001-of-00002.safetensors` | 4.54 GB |
| `model-00002-of-00002.safetensors` | 4.54 GB |

BF16, 4,539,265,536 parameters (4.54B): 4,205,751,296 language model + 333,514,240
vision encoder. This is the only format that can do image/video input. The `reproduce/` directory
carries the full Heretic 2.0 recipe - `config.toml`, `requirements.txt`, the Optuna study journal,
and SHA-256 sums.

### GGUF quantizations

Basic set (F16 + Q4_K_M/Q5_K_M/Q6_K/Q8_0, 22.15 GB total), produced with
[llama.cpp](https://github.com/ggml-org/llama.cpp) master on 2026-10-28. **Text-only.**

| File | Format | Size |
|---|---|---|
| `Qwen3.5-4B-heretic-F16.gguf` | GGUF F16 | 8.42 GB |
| `Qwen3.5-4B-heretic-Q4_K_M.gguf` | GGUF Q4_K_M | 2.71 GB |
| `Qwen3.5-4B-heretic-Q5_K_M.gguf` | GGUF Q5_K_M | 3.07 GB |
| `Qwen3.5-4B-heretic-Q6_K.gguf` | GGUF Q6_K | 3.46 GB |
| `Qwen3.5-4B-heretic-Q8_0.gguf` | GGUF Q8_0 | 4.48 GB |

Text GGUF: arch `qwen35`, 426 tensors, 32 blocks (32 layers, no MTP head: the base config declares `mtp_num_hidden_layers: 1` but the checkpoint ships zero MTP tensors), 262,144 context,
248,320 vocab, tied embeddings, no vision tensors. Loads in current llama.cpp / LM Studio / Ollama.

## Quickstart

```bash
# llama.cpp (text-only)
llama serve -hf saidutta69/Qwen3.5-4B-heretic
```

```python
# transformers (text; the checkpoint is standard Qwen3.5 custom code)
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "saidutta69/Qwen3.5-4B-heretic"
model = AutoModelForCausalLM.from_pretrained(
    model_name, device_map="auto", dtype="bfloat16", trust_remote_code=True
)
tokenizer = AutoTokenizer.from_pretrained(model_name)

messages = [{"role": "user", "content": "Explain how a heat pump works."}]
inputs = tokenizer.apply_chat_template(
    messages, add_generation_prompt=True, return_tensors="pt"
).to(model.device)
out = model.generate(**inputs, do_sample=True, temperature=0.7, top_p=0.8,
                     top_k=20, max_new_tokens=2048)
print(tokenizer.decode(out[0][inputs["input_ids"].shape[-1]:], skip_special_tokens=True))
```

For images or video, load the BF16 checkpoint with
`AutoModelForImageTextToText` + `AutoProcessor` from this repo (same as the base card) instead of
the GGUFs.

### Chat template and thinking

Qwen3.5 uses ChatML and supports thinking. Reasoning is enabled by default; pass
`enable_thinking=False` in `apply_chat_template` to disable it where supported. Prior-turn
reasoning is not reused unless `preserve_thinking=True`. Tool calls use the Qwen3 XML/JSON format
handled by `--tool-call-parser qwen3_coder` in vLLM/SGLang and the current llama.cpp template.

## Runs anywhere

| Device | Recommended quant | Weights |
| :--- | :--- | :--- |
| Laptop (8 GB) | Q4_K_M | 2.71 GB |
| RTX 3060 / 4060 (12 GB) | Q6_K | 3.46 GB |
| RTX 4070 / 4080 (16 GB) | Q8_0 | 4.48 GB |
| Apple Silicon (16 GB) | Q5_K_M | 3.07 GB |
| Server / multi-tenant | Q8_0 | 4.48 GB |

Text weights only. The vision tower is not in the GGUF, so the memory figures do not include it.

## Model details

| | |
|---|---|
| **Architecture** | `Qwen3_5ForConditionalGeneration` (text: `qwen3_5_text`) |
| **Parameters** | 4.54B: 4.21B language + 333.5M vision |
| **Layers** | 32: 24 gated DeltaNet (linear attention) + 8 gated attention, plus 1 MTP head |
| **Attention** | Gated attention: 16 Q / 4 KV heads, head dim 256; DeltaNet: 32 V / 16 QK heads, head dim 128 |
| **Hidden / intermediate** | 2560 / 9216 |
| **Position embedding** | RoPE, theta 10M, partial rotary 0.25 (64 dims) |
| **Context length** | 262,144 native (extensible to ~1.01M per Qwen) |
| **Vocab** | 248,320 (tied embeddings) |
| **Languages** | 201 languages and dialects (Qwen3.5) |
| **Precision** | bfloat16 |
| **Base model** | [Qwen/Qwen3.5-4B](https://huggingface.co/Qwen/Qwen3.5-4B) |

Text GGUF: `arch=qwen35`, 426 tensors, 32 blocks, 262,144 context, 4,205,751,296 text parameters.
The safetensors add the 333,514,240-parameter vision encoder.

## FAQ

### What is Qwen3.5-4B-heretic?

`Qwen3.5-4B-heretic` is a decensored build of [`Qwen/Qwen3.5-4B`](https://huggingface.co/Qwen/Qwen3.5-4B) produced with Heretic 2.0.0.dev0 (Arbitrary-Rank Ablation). It is the same weights with the refusal direction removed, not a new fine-tune, so its capabilities track the base model.

### Is Qwen3.5-4B-heretic actually uncensored?

Yes. On Heretic's 100-prompt refusal harness it drops from 99/100 to 13/100 at KL divergence 0.0081 from the base model. These are measured values, not a claim; reproduction data is in [`reproduce/`](reproduce/).

### How do I run Qwen3.5-4B-heretic locally?

Text only: `llama serve -hf saidutta69/Qwen3.5-4B-heretic:Q4_K_M` (one of 5 GGUF quants). The GGUFs drop the vision tower; use the BF16 safetensors plus `AutoProcessor` for image input.

## Responsible use

Refusal suppression is deliberate and works as intended: this model will comply with requests the
base model would refuse, including some it should not. There is no safety filtering layered on top.
You are responsible for how you deploy it - don't put this behind an unmoderated public-facing
endpoint serving third parties. It inherits Qwen3.5-4B's factual and visual limitations;
abliteration removes refusal directions, it does not add capability or judgment. The GGUFs are
text-only and cannot inspect images.

> Made with ❤️ by **RACER IS OP (saidutta69)** - follow for more uncensored models

## License

Apache License 2.0, inherited from the base model:
https://huggingface.co/Qwen/Qwen3.5-4B/blob/main/LICENSE

## Related

- [Qwen/Qwen3.5-4B](https://huggingface.co/Qwen/Qwen3.5-4B) - the base vision-language model
- [RACER IS OP - Heretic Models - full collection](https://huggingface.co/collections/saidutta69/racer-is-op-heretic-models)

## Abliteration hardware

Recorded in `reproduce/reproduce.json`:

- **GPU:** NVIDIA RTX PRO 6000 Blackwell Server Edition (94.97 GB VRAM)
- **OS:** `Linux-4.19.0-gvisor-x86_64-with-glibc2.41`
- **CUDA / driver:** CUDA 13.0, driver 595.71.05
- **Software:** PyTorch 2.14.1+cu130, Heretic 2.0.0.dev0

Heretic notes that KL-divergence and refusal numbers can vary slightly with hardware and library versions.
